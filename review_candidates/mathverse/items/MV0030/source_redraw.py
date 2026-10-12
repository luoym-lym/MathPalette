from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'renderer'))
from common_renderer import draw
if __name__=='__main__':
    p=Path(__file__).with_name('scene.json')
    draw(p)
