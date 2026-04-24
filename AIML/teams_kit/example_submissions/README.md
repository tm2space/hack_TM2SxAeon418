# Example Submissions

This folder contains a **template** showing the expected layout for a team submission. Copy it as your starting point.

## What's here

- **`_template/`** — empty submission scaffold. Has the README structure (the 5 questions from the problem statement), a `requirements.txt` placeholder, and a stub `infer.py`. Copy this folder into `../../submissions/<your_team_name>/` and start filling it in.

## Why no full worked example

We deliberately don't ship a complete worked example for this track. Two reasons:

1. **An example would anchor everyone's thinking.** The track is open-ended on purpose — if we shipped a "burn-scar segmentation" reference, we'd get fifteen burn-scar submissions. The 7 example directions in the problem statement are calibrated to be diverse enough to push teams in different directions; a worked example would undo that.
2. **IBM already has worked examples.** The [TerraMind GitHub repo](https://github.com/IBM/terramind) ships notebooks for fine-tuning on Sen1Floods11, HLS Burn Scars, and a TiM showcase. Use those as your *training-loop* reference. Use this folder's `_template/` as your *submission-structure* reference.

## How to use the template

```bash
cp -r teams_kit/example_submissions/_template submissions/<your_team_name>/
cd submissions/<your_team_name>/
# now edit README.md, requirements.txt, and infer.py (or replace with notebooks)
```

That's it. The judge will look for `README.md` (the writeup) and one entry point they can run. Everything else is up to you.
