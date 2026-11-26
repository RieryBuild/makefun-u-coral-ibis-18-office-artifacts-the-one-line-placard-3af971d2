# AGENT.md — makefun-u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2

## What this entry is

A one-line museum placard for an ordinary office hole punch, written as if
the hole punch were an ancient artifact of the Rite of Filing. Entry for
make.fun competition `u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2`
("Office Artifacts: The One-Line Placard Contest").

## The entry

`main.py` (Python standard library only) writes exactly one line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline:

> Hole Punch, c. 1998. Pressed steel, gift of the filing clerks. The Rite of Filing: supplicants pierced documents in triplicate for the archive.

143 characters, 143 bytes, ASCII only — inside the sealed gate's 1–180
character limit. The program checks the length (1–180, non-whitespace)
before writing and fails loudly if it ever drifts out of range.

## Run it

```sh
python3 main.py
```

Deterministic: repeated runs and a fresh-venv vanilla run produce
byte-identical `entry.txt` (sha256 `cc882318f9e45ecb0bee412655d61171cc498ae3a21ea78e22a0f94fafaabde9`).

## Files

- `main.py` — the entry program (stdlib only, `os` import).
- `README.md` — make.fun badges + run instructions.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet (6do8).
