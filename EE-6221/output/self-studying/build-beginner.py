"""Rebuild the offline beginner companions from notes-bank.json. Run with Python 3.

beginner-notes.html = Quiz 1 (sections without a "quiz" tag); beginner-notes-quiz-2.html =
sections tagged "quiz": 2. Prints any slide pages the Quiz 2 pop-ups still need in quiz2-pages/.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bank = json.loads((ROOT / 'notes-bank.json').read_text())

def prose(text):
    """Render the bank's existing paragraphs and flat Markdown lists; preserve math."""
    blocks = []
    for block in text.split('\n\n'):
        lines = block.splitlines()
        if all(re.match(r'^(?:- |\d+\. )', line) for line in lines):
            ordered = not lines[0].startswith('- ')
            tag = 'ol' if ordered else 'ul'
            blocks.append(f'<{tag}>' + ''.join('<li>' + html.escape(re.sub(r'^(?:- |\d+\. )', '', line)) + '</li>' for line in lines) + f'</{tag}>')
        else:
            blocks.append('<p>' + html.escape(block) + '</p>')
    return '\n'.join(blocks)

short = ['Start here', 'Frames & rotations', 'Move between frames', 'D–H & forward kinematics', 'Inverse kinematics', 'Trajectory graphs']
sources = ['Local transcript and group-chat record; logistics not officially verified.',
           'Lecture handout pp. 25–35, 57–58.',
           'Lecture handout pp. 39–52.',
           'Lecture handout pp. 53–70. The planar arm and grasp coordinates are supplementary examples.',
           'Lecture handout pp. 87–117. The planar position-only construction is supplementary.',
           'Lecture handout pp. 130–132. Scalar joint example and graph values are supplementary.']
nav = ''.join(f'<a href="#module-{i}">{i+1:02d} {name}</a>' for i, name in enumerate(short))
sections = []
for i, s in enumerate(s for s in bank['sections'] if 'quiz' not in s):
    reference = prose(s['content'])
    for e in s['examples']:
        reference += '<details><summary>Worked reference example</summary>' + prose(e['text']) + '<p class="source">' + html.escape(e['source_locator']) + '</p></details>'
    for e in s['exercises']:
        # Existing exercise text sometimes combines prompts and full solutions.
        reference += '<details><summary>Further practice and worked feedback — try on paper first</summary>' + prose(e['text']) + '<p class="source">' + html.escape(e['source_locator']) + '</p></details>'
    lesson = s['visual_lesson_html']
    # End the module with its immediate-feedback check, after optional reference material.
    before, check = lesson.split('<fieldset', 1)
    sections.append(f'<section id="module-{i}"><p class="eyebrow">MODULE {i+1:02d} / 06</p><h2>{short[i]}</h2>' + before +
                    '<p class="source">' + sources[i] + ' <a href="../../resources/lecture-01-manipulator-kinematics.pdf">Open source handout</a></p>' +
                    '<details class="reference"><summary>Reference and further practice</summary>' + reference + '</details><fieldset' + check +
                    (f'<a class="next" href="#module-{i+1}">Continue to {short[i+1]} →</a>' if i < 5 else '<p>Ready to apply the ideas? <a href="../../quizzes/quiz-01-mock-01.html">Open the timed mock</a>.</p>') + '</section>')
page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EE6221 Quiz 1 — Visual beginner notes</title>
<link rel="stylesheet" href="self-study-assets/katex/katex.min.css">
<link rel="stylesheet" href="self-study-assets/visual-lessons.css">
<script defer src="self-study-assets/katex/katex.min.js"></script>
<script defer src="self-study-assets/katex/contrib/auto-render.min.js"></script>
<script defer src="self-study-assets/render-math.js"></script>
<script defer src="self-study-assets/visual-lessons.js"></script></head>
<body><a class="skip" href="#main">Skip to lessons</a>
<header><p class="eyebrow">EE6221 · QUIZ 1 STUDY COMPANION</p><h1>See the robot.<br>Build the mathematics.</h1><p>From coordinate frames to a moving arm, one step at a time.</p><p class="meta">6 modules · interactive diagrams · worked examples · offline</p></header>
<nav aria-label="Lesson navigation">''' + nav + '''</nav><main id="main">
<noscript><p class="notice">JavaScript is disabled. Worked explanations and expandable solutions remain available; enable JavaScript for diagrams, typeset mathematics, and feedback buttons.</p></noscript>''' + '\n'.join(sections) + '''</main>
<footer>Supplementary teaching companion; canonical PDFs remain in notes/. Built from notes-bank.json with build-beginner.py. Diagrams use simplified stated geometry, not official quiz predictions.</footer></body></html>'''
(ROOT / 'beginner-notes.html').write_text(page)
print('Built beginner-notes.html (6 modules)')

# ---------------------------------------------------------------- Quiz 2
PDF = {1: 'part-2-lecture-01-introduction-and-sensors', 2: 'part-2-lecture-02-vision-sensors-and-systems',
       3: 'part-2-lecture-03-structure-and-pose-estimation', 4: 'part-2-lecture-04-kalman-filter-sensor-integration'}
needed = set()

def cite(text):
    """Outside tags, turn 'Lec N p. A' / 'Lec N pp. A–B, C' into links that pop up the slide pages."""
    def link(m):
        n, out = int(m.group(1)), []
        for part in m.group(3).split(', '):
            a, _, b = part.partition('–')
            a, b = int(a), int(b or a)
            needed.update((n, p) for p in range(a, b + 1))
            label = (f'Lec {n} {m.group(2)} ' if not out else '') + part
            out.append(f'<a href="../../resources/part-2/{PDF[n]}.pdf#page={a}" data-pages="{PDF[n]}:{a}-{b}">{label}</a>')
        return ', '.join(out)
    pat = re.compile(r'Lec ([1-4]) (pp?\.) (\d+(?:–\d+)?(?:, \d+(?:–\d+)?)*)')
    return ''.join(c if c.startswith('<') else pat.sub(link, c) for c in re.split(r'(<[^>]+>)', text))

quiz2 = sorted((s for s in bank['sections'] if s.get('quiz') == 2), key=lambda s: s['order'])
n2 = len(quiz2)
side = ''.join(f'<a href="#q2-{i}"><span>{i+1:02d} {s["short"]}</span><span class="score" data-for="q2-{i}"></span></a>' for i, s in enumerate(quiz2))
mods = []
for i, s in enumerate(quiz2):
    reference = prose(s['content'])
    for e in s['examples']:
        reference += f'<details><summary>Worked example · {e["provenance"]}</summary>' + prose(e['text']) + '<p class="source">' + html.escape(e['source_locator']) + '</p></details>'
    for e in s['exercises']:
        reference += f'<details><summary>Practice, try on paper first · {e["provenance"]}</summary>' + prose(e['text']) + '<p class="source">' + html.escape(e['source_locator']) + '</p></details>'
    before, check = s['visual_lesson_html'].split('<fieldset', 1)
    nxt = (f'<a class="next" href="#q2-{i+1}">Continue to {quiz2[i+1]["short"]} →</a>' if i < n2 - 1 else
           '<p>Ready? <a href="../../quizzes/quiz-02-mock-01.html">Sit the timed Quiz 2 mock</a> (closed book, 60 min).</p>')
    mods.append(cite(f'<section id="q2-{i}"><p class="eyebrow">MODULE {i+1:02d} / {n2:02d}</p><h2>{s["short"]}</h2>' + before +
                     '<p class="source">Source: ' + html.escape(s['source_note']) + '</p>' +
                     '<details class="reference"><summary>Full teaching text, worked examples and practice</summary>' + reference + '</details><fieldset' + check + nxt + '</section>'))
page2 = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EE6221 Quiz 2 — Visual beginner notes</title>
<link rel="stylesheet" href="self-study-assets/katex/katex.min.css">
<link rel="stylesheet" href="self-study-assets/visual-lessons.css">
<link rel="stylesheet" href="self-study-assets/quiz2-lessons.css">
<script defer src="self-study-assets/katex/katex.min.js"></script>
<script defer src="self-study-assets/katex/contrib/auto-render.min.js"></script>
<script defer src="self-study-assets/render-math.js"></script>
<script defer src="self-study-assets/quiz2-lessons.js"></script></head>
<body><a class="skip" href="#main">Skip to lessons</a><div class="app">
<aside aria-label="Contents"><p class="eyebrow">EE6221 · QUIZ 2</p><p class="side-title">Sensors, vision, pose, Kalman fusion</p><nav>''' + side + '''</nav>
<p class="side-tools"><a href="review-page.html">Review page</a> · <a href="../../quizzes/quiz-02-mock-01.html">Timed mock</a> · <a href="beginner-notes.html">Quiz 1 notes</a></p></aside>
<div class="content"><header><p class="eyebrow">EE6221 · QUIZ 2 STUDY COMPANION</p><h1>From a sensor reading<br>to a fused estimate.</h1><p>Lec 1–4 of Part 2, one step at a time. Click any slide citation to see the slide itself.</p><p class="meta">''' + str(n2) + ''' modules · interactive diagrams · worked examples · offline</p></header>
<main id="main"><noscript><p class="notice">JavaScript is disabled. Worked explanations and expandable solutions remain available; enable JavaScript for diagrams, typeset mathematics, slide pop-ups and feedback buttons.</p></noscript>''' + '\n'.join(mods) + '''</main>
<footer>Supplementary teaching companion; canonical PDFs remain in notes/. Built from notes-bank.json with build-beginner.py. Generated examples are labelled; format predictions are unofficial.</footer></div></div>
<dialog class="page-view" aria-label="Cited slides"><div class="bar"><strong></strong><span><a target="_blank">Open PDF at this page</a> <button type="button">Close</button></span></div><div class="pages"></div></dialog></body></html>'''
(ROOT / 'beginner-notes-quiz-2.html').write_text(page2)
print(f'Built beginner-notes-quiz-2.html ({n2} modules)')
missing = sorted((PDF[n], p) for n, p in needed if not (ROOT / 'quiz2-pages' / f'{PDF[n]}-p{p:03d}.jpg').exists())
for stem, p in missing:
    print('MISSING', stem, p)
