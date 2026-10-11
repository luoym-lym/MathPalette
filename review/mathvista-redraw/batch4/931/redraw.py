from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from redraw_runtime import draw
if __name__=='__main__':
 print(draw(HERE/'scene.json', HERE/'redrawn.png'))
