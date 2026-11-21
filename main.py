#!/usr/bin/env python3
"""The poem about stopping — a poem about agency.

Writes one short poem to /output/entry.txt (or the directory named
by MAKEFUN_OUTPUT_DIR). The poem is fixed text: every run writes
exactly the same bytes. No network, no input, no randomness.

The poem: at a crosswalk, a person chooses not to cross — knots
an untied shoelace while the light drains away — and the child
behind them stops too. Stopping as an act, and staying as
something that passes from one person to another.
"""

import os
import sys

POEM = """At the crosswalk, rain beads on my untied shoe.
The walk sign blinks; I could give the street my weight.
Instead I knot the lace, slowly,
while the green drains out.
Somewhere behind me, my daughter stops too."""

# The gate allows 1-280 Unicode code points; this poem is 209.
# Fail loudly here rather than shipping an out-of-gate text.
assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} characters"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
