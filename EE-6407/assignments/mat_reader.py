"""Minimal stdlib reader for MATLAB v5 .mat files holding real numeric matrices.

read(path) -> {name: list of rows}. Handles zlib-compressed elements; no cells/structs/sparse.
"""
import struct, zlib

NUM = {1: 'b', 2: 'B', 3: 'h', 4: 'H', 5: 'i', 6: 'I', 7: 'f', 9: 'd', 12: 'q', 13: 'Q'}
MI_MATRIX, MI_COMPRESSED = 14, 15


def _elements(buf):
    i = 0
    while i + 8 <= len(buf):
        typ, n = struct.unpack_from('<II', buf, i)
        if typ >> 16:  # small data element: size in upper 16 bits, data in the next 4 bytes
            typ, n = typ & 0xFFFF, typ >> 16
            yield typ, buf[i + 4:i + 4 + n]
            i += 8
        else:
            yield typ, buf[i + 8:i + 8 + n]
            i += 8 + n + (-n % 8)


def _matrix(body):
    flags, dims, name, real = list(_elements(body))[:4]
    if flags[1][0] & 0xFF in (1, 2, 5):  # cell / struct / sparse
        raise ValueError('only numeric matrices are supported')
    rows, cols = struct.unpack('<ii', dims[1][:8])
    typ, data = real
    vals = struct.unpack(f'<{len(data) // struct.calcsize(NUM[typ])}{NUM[typ]}', data)
    # MATLAB stores column-major
    return name[1].decode(), [[float(vals[c * rows + r]) for c in range(cols)] for r in range(rows)]


def read(path):
    buf = open(path, 'rb').read()[128:]
    out = {}
    for typ, data in _elements(buf):
        if typ == MI_COMPRESSED:
            (typ, data), = list(_elements(zlib.decompress(data)))[:1]
        if typ == MI_MATRIX:
            k, v = _matrix(data)
            out[k] = v
    return out
