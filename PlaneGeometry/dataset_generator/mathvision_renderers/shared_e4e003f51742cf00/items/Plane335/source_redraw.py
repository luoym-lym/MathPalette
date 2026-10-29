from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'PlaneGeometry/dataset_generator'))
from common_renderer import draw
if __name__=='__main__':
 draw(HERE/'scene.json',HERE/'image.png')
