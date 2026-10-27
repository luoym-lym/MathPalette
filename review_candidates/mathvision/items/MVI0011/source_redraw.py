from pathlib import Path
import sys,json
p=Path(__file__).resolve().parent
root=p.parents[3]
sys.path.insert(0,str(root/'SolidGeometry/dataset_generator'))
import common_renderer as r
if __name__=='__main__':
 r.draw(p/'scene.json',p/'image.png')
 r.draw(p/'scene.json',p/'image.svg')
