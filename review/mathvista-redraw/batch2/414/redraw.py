from pathlib import Path
import sys
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p.parent/'vendor'))
from common_renderer import draw
if __name__=='__main__': print(draw(p/'scene.json'))
