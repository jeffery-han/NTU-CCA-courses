# EE6407 public study-resource archive

Downloaded on 2026-08-24 from publicly accessible sources found through an Exa web search. The files are for private study and are not verified as current official NTU teaching material, question papers, solutions, or marking schemes.

## Contents

| Directory | Contents | Files | Qualification |
|---|---|---:|---|
| `past-exam-walkthroughs-2020-2024/` | Question-by-question personal solutions labelled from 2020 S2 through 2024 S1 | 25 PDFs | The source author calls these personal solutions. They are not official papers or marking schemes and may contain errors. |
| `past-paper-images-undated/` | Photographed handwritten past-paper solution pages | 8 JPEGs plus the source README | The upstream filenames do not identify the year or semester, so no date has been inferred locally. These are student workings, not clean question papers. |
| `legacy-ee6227/quiz/` | A publicly posted quiz under the older EE6227 course code | 1 PDF | The title and published topic outline closely match EE6407, but no official renumbering record was found; keep this separate from exact-code EE6407 assessments. |
| `legacy-ee6227/assignments/` | Two assignment briefs and student submissions | 5 PDFs, 1 DOCX, and 2 small source READMEs | Older-code coursework; useful for practice, but not evidence of the current EE6407 assessment format. |
| `worked-slide-examples/` | Worked examples for genetic algorithms and machine-learning topics | 48 PDFs | Supplementary student explanations corresponding to slide examples; independently check notation and arithmetic. |
| `topic-explainers/` | Exam review, GA, complexity, search, clustering, and optimisation explainers | 11 PDFs plus 1 XLSX | Mostly Chinese-language student material; supplementary rather than authoritative. |
| `student-note/` | Combined EE6227/EE6407 review note | 1 PDF (39 pages) | The author explicitly warns that written material was not checked and may contain errors. |
| `coursework-2024/` | Genetic-algorithm and machine-learning coursework | 1 PDF, 1 MLX, 1 Python file, and 2 images | Student work from a repository whose author studied during 2024. The two upstream `.png` files contain valid JPEG data; their original names are preserved for traceability. |
| `legacy-ee6227/slides/` | Consolidated Week 1-10 notes/slides | 5 PDFs | Publicly posted under EE6227. Course-code and teaching-run differences may matter. |
| `course-outline/` | Publicly posted EE6407 outline | 1 PDF | Useful for topic mapping; check the current official course site for live policy or assessment details. |
| `exam-summary/` | Chinese-language exam-question summary | 1 DOCX | Unofficial compilation; do not treat it as an official paper or disclosure of the current exam. |
| `source-metadata/` | Source READMEs and licences | 7 files | Preserves provenance, scope statements, and upstream cautions. |

The downloaded payload contains 123 source files, including 98 PDFs, and occupies about 78 MB. This README is the archive's additional local index.

## Sources and pinned revisions

- [freshman2233/EE6407-Genetic-Algorithms-And-Machine-Learning](https://github.com/freshman2233/EE6407-Genetic-Algorithms-And-Machine-Learning), commit `f8b5a910022849c880834aec14e0dc59cde4c2a6` - personal exam walkthroughs, slide examples, topic explainers, outline, and exam summary.
- [KuRRe8/eeemsc-coursework](https://github.com/KuRRe8/eeemsc-coursework), commit `d678815e75222577586439c408c1336245e69ff6` - EE6407 student note, coursework, and undated past-paper images.
- [NTU-CCA/EE6227](https://github.com/NTU-CCA/EE6227), commit `a05fd7222d12cdbd77ed5731dcac308dfc4e1e7f` - older-code quiz, assignments, and consolidated slides for a course with a matching title and topic outline.
- [chesha1/NTU_SP_Courses](https://github.com/chesha1/NTU_SP_Courses) - contextual student advice about the older EE6227 course; linked only, because it does not contain additional assessment payloads.
- [NTU EEE/IEM past-year-paper page](https://ntueeeclub.github.io/) - points students to NTU Library for recent official papers, but its public page does not expose a course-specific EE6407 download.

## Search result and exclusions

Exa was used to review 78 candidates across exact-code, public-repository, assessment, note/resource, older-code, and 2024-2026 gap searches. The results converged on the three downloadable course-specific repositories above.

No publicly accessible exact-code EE6407 quiz collection or 2025-2026 exam paper was found. The only quiz retained is clearly separated under the older EE6227 code. The NTU EEE Club page and general past-paper portals were not presented as EE6407 sources when they did not expose a matching public file.

The newer repository's `4.Resource/3.REFERENCES/` directory was deliberately excluded because it bundles commercial textbook scans, including files labelled as Z-Library copies. Generic evolutionary-computing courses, unrelated NTU modules, and a Taiwan NTU course page were also excluded because they are not course-specific EE6407 archives.

## Validation

- All 98 PDFs opened successfully with `pdfinfo`.
- All 4 ZIP-based Office/MATLAB containers (`.docx`, `.xlsx`, `.mlx`) passed `unzip -t` integrity checks.
- No downloaded file is zero bytes.
- The 8 `.jpg` past-paper images are valid JPEG files. The two upstream coursework files named `.png` are valid JPEG-encoded images and are documented above rather than silently renamed.

## Study-use caution

Attempt a question before opening a walkthrough or submission. Public student work can be incomplete or wrong and may not match the notation, scope, permitted aids, or marking expectations of the current course run. Check NTULearn and current instructor announcements before using old material for assessment preparation.
