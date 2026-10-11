"""Portable strict-protocol MathPalette frozen-scene reproduction."""
import os,sys,tempfile
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'mathvista_batch4_mpl'))
os.environ.setdefault('XDG_CACHE_HOME',str(Path(tempfile.gettempdir())/'mathvista_batch4_cache'))
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'vendor'))
import common_renderer as cr
image_bytes=cr.image_bytes
draw=cr.draw
