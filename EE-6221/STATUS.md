# EE-6221 note status

## Note files

- `notes/beginner-notes.tex` - detailed, self-contained teaching note for the supplied manipulator-kinematics material; compiled PDF is stored beside it.
- `notes/notes.tex` - concise manipulator-kinematics review note; compiled PDF is stored beside it.
- `notes/week-01-beginner-notes.tex` - preserved Week 1-only teaching supplement; it is not the canonical full-scope beginner note.

## Source coverage

| Source | Pages/slides | `notes/beginner-notes.tex` coverage | `notes/notes.tex` coverage | Qualification |
|---|---:|---|---|---|
| `resources/course-outline-part-01.pdf` | p. 1 | Opening scope and course map | Course map and basic language | Supplied outline page covered for sequence and reference context. |
| `resources/lecture-01-manipulator-kinematics.pdf` | pp. 1-22 | Sections 1-2 | Course map and basic language | Robotics overview, architectures, DoF, workspace, and specifications covered; source examples remain selective. |
| same | pp. 23-52 | Sections 3-4 | Frames, rotations, and homogeneous transformations | Coordinate representations, rotations, composition order, and homogeneous transforms developed at beginner/review depth. |
| same | pp. 53-86 | Section 5 | Direct kinematics and D-H arm equation | D-H construction, arm-transform product, tool orientation vectors, and planar 2R example covered; long manipulator calculations are summarized. |
| same | pp. 87-117 | Section 6 | Inverse kinematics | Feasibility, multiplicity, analytic/numerical approaches, and quadrant handling covered; detailed source robot derivations remain selective. |
| same | pp. 118-132 | Section 7 | Trajectory planning | Pick/place framing, path-versus-trajectory distinction, and cubic interpolation covered. |
| same | pp. 133-156 | Section 8 | Differential motion, Jacobians, and singularities | Velocity mapping, pseudoinverse, rank loss, and singularity interpretation covered; implementation details remain selective. |
| `resources/week-01-transcript.txt` | Full transcript | Sections 1-4 | Sections 1-2 | Supports introductory teaching sequence; the handout controls notation and formal claims. |
| `resources/week-02-transcript.txt` | Full transcript | Section 5 | Direct kinematics and D-H arm equation | Supports D-H frame assignment, joint-variable identification, transform multiplication, and tool-axis interpretation; transcript errors are not adopted. |
| `resources/public-archive-2026-08-24/lecture-slides/` | 9 PDFs; all pages | not yet covered | not yet covered | Public exact-code slides/reference files spanning kinematics, control, mobile robots, and intelligent sensors. |
| `resources/public-archive-2026-08-24/past-exam-solutions-2015-2018/` | 3 PDFs; all pages | not yet covered | not yet covered | Publicly posted solution compilations; not verified as official marking schemes. |
| `resources/public-archive-2026-08-24/past-exam-2024-2025/` | Paper and student solution; all pages | not yet covered | not yet covered | Exact-code recent paper plus an unofficial solution that explicitly omits Problem 3(a). |
| `resources/public-archive-2026-08-24/assignments-2020/` | 2 PDFs; all pages | not yet covered | not yet covered | Assignment brief and submitted student work; not a current assignment or official solution. |

## Pending and unresolved

- Robot control, mobile-robot kinematics, and intelligent-sensor material remain pending in both notes. Course-specific public slides are now archived, but they have not yet been reviewed or synthesised.
- The public exams and assignment files are validated and indexed in the archive `README.md`; their calculations remain unchecked.
- No exact-code public quiz file was found. Commercial solution sites were excluded even when search snippets exposed exam wording.
- Expand the detailed source robot examples only after choosing which manipulator convention/problem set the learner wants to practise.

## File-organization record

- `Outline for Part I.pdf -> resources/course-outline-part-01.pdf`
- `kinematics(3).pdf -> resources/lecture-01-manipulator-kinematics.pdf`
- `6221-week1.txt -> resources/week-01-transcript.txt`
- `6221-week2.txt -> resources/week-02-transcript.txt`
- `notes.tex -> notes/notes.tex`; `notes.pdf -> notes/notes.pdf`
- `week1-beginner-notes.tex -> notes/week-01-beginner-notes.tex`; `week1-beginner-notes.pdf -> notes/week-01-beginner-notes.pdf`
- 2026-08-24: added `resources/public-archive-2026-08-24/` with 16 valid PDFs, source metadata, and a provenance README. Generic robotics resources, unrelated codes, and commercial solution sites were excluded.

## Update record

- 2026-08-24: brought the course into the updated canonical layout, repaired note citations, preserved the Week 1-only supplement under an honest scoped filename, and created the canonical full manipulator-kinematics beginner note. Archived later-course material remains explicitly separate from reviewed note coverage.
- 2026-08-24: compiled all three note outputs twice (`notes/beginner-notes.pdf`: 5 pages; `notes/notes.pdf`: 6 pages; `notes/week-01-beginner-notes.pdf`: 3 pages). Rendered and visually checked every page; no clipping, overlap, broken equations, or unreadable text was found.
