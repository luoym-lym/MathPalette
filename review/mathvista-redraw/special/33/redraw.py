import sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'vendor/SolidGeometry/dataset_generator'))
from common_renderer import draw
if __name__=='__main__': draw(P/'scene.json',P/'redraw.png')
