"""Reproduce the frozen, unapproved MathVerse source problem 695."""
from pathlib import Path
from common_renderer import draw
ROOT = Path(__file__).resolve().parents[1]
def redraw(output_path=None):
    return draw(ROOT / "scenes/MathVerse695.json", output_path or ROOT / "images/MathVerse695.png")
if __name__ == "__main__":
    import sys
    print(redraw(sys.argv[1] if len(sys.argv)>1 else None))
