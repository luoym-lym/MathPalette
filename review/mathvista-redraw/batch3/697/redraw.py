"""Reproduce frozen scene using the bundled, unmodified MathPalette renderer."""
from pathlib import Path
import os, sys
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mathvista_batch3_mpl")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "renderer"))
from common_renderer import draw
if __name__ == "__main__":
    print(draw(Path(__file__).with_name("scene.json"), Path(__file__).with_name("redrawn.png")))
