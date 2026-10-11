from pathlib import Path
import sys,os
os.environ.setdefault('MPLCONFIGDIR','/tmp/mathvista-redraw-mpl')
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p.parent/'runtime'))
from common_renderer import draw
if __name__=='__main__':
    print(draw(p/'scene.json',p/'redrawn.png'))
