# the-joke-the-reviewer-laughs-at-20261121-0329 entry (Python 3.13, standard
# library only): writes one original one-line joke about working beside AI
# coding agents to /output/entry.txt. The program runs twice with no network,
# and both runs must write the same bytes, so the text is fixed here.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "My agent's first pull request added 2,000 lines and deleted exactly "
    "one: my name from the authors file."
)

# The gate requires 1 to 280 Unicode code points and more than whitespace.
if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
    raise SystemExit("entry text fails the 1-280 character gate")

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
