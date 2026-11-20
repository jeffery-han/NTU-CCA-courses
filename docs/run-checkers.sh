#!/bin/sh
# Run every answer-key checker in one course (or in all courses with no argument).
# Usage, from the repository root:  sh docs/run-checkers.sh EE-6407
# Exit status is non-zero if any checker fails.
cd "$(dirname "$0")/.." || exit 2
fail=0
for f in ${1:-EE-*}/quizzes/*-check.py ${1:-EE-*}/quizzes/*/*-check.py ${1:-EE-*}/notes/*-check.py ${1:-EE-*}/quizzes/*-check.mjs ${1:-EE-*}/quizzes/*/*-check.mjs; do
  [ -e "$f" ] || continue
  case "$f" in
    *.py)  run="python3" ;;
    *.mjs) run="$(command -v node || echo /opt/homebrew/bin/node)" ;;
  esac
  if (cd "$(dirname "$f")" && "$run" "$(basename "$f")" >/dev/null 2>&1); then
    echo "ok    $f"
  else
    echo "FAIL  $f"; fail=1
  fi
done
exit $fail
