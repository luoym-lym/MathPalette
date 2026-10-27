from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from upper_comb_renderer_v2 import draw
if __name__=='__main__':
 draw(HERE/'scene.json',HERE/'image.png')
