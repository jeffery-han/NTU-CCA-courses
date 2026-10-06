import sys, zipfile, re, xml.etree.ElementTree as ET
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def read(path):
    z = zipfile.ZipFile(path)
    ss = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', NS):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t' % NS['m'])))
    rows = []
    for r in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).iter('{%s}row' % NS['m']):
        row = {}
        for c in r.findall('m:c', NS):
            col = re.match(r'[A-Z]+', c.get('r')).group()
            v = c.find('m:v', NS)
            if v is None:
                isv = c.find('m:is', NS)
                row[col] = ''.join(t.text or '' for t in isv.iter('{%s}t' % NS['m'])) if isv is not None else None
            elif c.get('t') == 's':
                row[col] = ss[int(v.text)]
            else:
                row[col] = float(v.text) if c.get('t') not in ('str', 'b') else v.text
        rows.append((int(r.get('r')), row))
    return rows

if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('==', p)
        for n, row in read(p):
            print(n, [row.get(c) for c in 'ABCDE'])
