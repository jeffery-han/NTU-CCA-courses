---
description: Search RedNote for NTU course reviews and fold them into ntu-eee-course-reviews-rednote.md
argument-hint: "[search query, default: NTU EEE 选课评价]"
---

Refresh the crowd-sourced course-review file from RedNote (小红书).

**Search query:** ${ARGUMENTS:-NTU EEE 选课评价}

## Steps

1. **Search.** Use the `mcp__vb-rednote-mcp__search_notes` tool with the query
   above (`limit` 15–20). If that MCP server is not connected, fall back to the
   `rednote` skill (browser-driven) — same goal, slower.
   - Run 2–3 phrasings if the first is thin: swap in `测评` / `攻略` / `避雷` /
     `锐评`, or narrow to a course code (`NTU EE6204 期末`).
2. **Go deeper only where it pays.** For the few notes with real per-course exam
   intel (assessment structure, quiz reforms, "fails people", scope-drawing),
   pull `get_note_content` and `get_note_comments` — corrections live in comments.
   Skip notes that are pure vibes.
3. **Update `ntu-eee-course-reviews-rednote.md`** at the Courses root (it already
   exists — merge, don't clobber):
   - Keep the structure: source key table → **master table, one row per course**
     (Course | Name | Verdict | Speed-run? | Assessment shape | Key warnings |
     Sources) → per-course detail blocks → post links.
   - Add new courses as new rows; enrich existing rows; add a new `S##` source
     row + link for every note you actually read. Note the semester/year a claim
     is about when the poster gives it.
   - Update the "compiled ... (date)" line at the top.
4. **Label everything as unofficial.** These are second-hand student
   recollections; lecturers and formats change yearly. Never harden a date,
   grade weight, or policy into asserted fact.
5. **Commit & push** per CLAUDE.md (local-first `main`):
   `git pull --ff-only origin main` → stage the file → commit
   `EE-XXXX / course-reviews: refresh RedNote course reviews` (or a program-wide
   message) → `git push origin main`.

Report: how many notes read, which courses gained/changed rows, compile result
(none needed — it's Markdown), push result.
