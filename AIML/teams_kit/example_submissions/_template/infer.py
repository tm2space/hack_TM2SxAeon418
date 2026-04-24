"""
Demo entry point.

Replace this stub with whatever your project does. The only contract
is: a judge running `python infer.py` (or some clearly-documented variant)
should see your model produce an output on a sample input within ~10 min
on a Colab GPU.

If your project is notebook-based, point to the notebook from your README
and delete this file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(input_path: Path, output_path: Path) -> int:
    """Replace this with your inference pipeline."""
    print(f"[stub] would load TerraMind, process {input_path}, write {output_path}")
    print("[stub] replace this file with your real inference code")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="<your project> inference demo")
    parser.add_argument("--input",  type=Path, required=True, help="path to input tile")
    parser.add_argument("--output", type=Path, required=True, help="where to write output")
    args = parser.parse_args()
    sys.exit(main(args.input, args.output))
