from pathlib import Path
import sys
p=Path(__file__).resolve()
sys.path.insert(0,str(p.parents[4]/'SolidGeometry/dataset_generator'))
sys.path.insert(0,str(p.parent))
from renderer import draw
if __name__=='__main__': draw(p.with_name('scene.json'),p.with_name('image.png'))
