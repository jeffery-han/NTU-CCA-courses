"""Rebuild the offline beginner companion from notes-bank.json. Run with Python 3."""
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
for i, s in enumerate(bank['sections']):
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
