"""Unified protocol workbench adapter."""
from pathlib import Path
import sys
_PROJECT=Path(__file__).resolve().parents[2]
if str(_PROJECT) not in sys.path: sys.path.insert(0,str(_PROJECT))
from dataset_tools.unified_workbench import RENDER_LOCK, Scene, RendererAdapter, scene_png
