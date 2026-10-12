from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent.parent/'renderer'))
from common_renderer import draw
if __name__=='__main__':
    draw(ROOT/'scene.json', sys.argv[1] if len(sys.argv)>1 else ROOT/'redrawn.png')
