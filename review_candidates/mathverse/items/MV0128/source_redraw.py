from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'solid_renderer'))
from common_renderer import draw
if __name__=='__main__': print(draw(Path(__file__).with_name('scene.json'),Path(__file__).with_name('redrawn.png')))
