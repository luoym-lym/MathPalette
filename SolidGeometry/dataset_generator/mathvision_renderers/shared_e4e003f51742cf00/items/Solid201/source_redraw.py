from pathlib import Path
import sys
p=Path(__file__).resolve()
sys.path.insert(0,str(p.parents[4]/'SolidGeometry/dataset_generator'))
sys.path.insert(0,str(p.parent.parent))
import upper_solid_face_text_renderer as F
F.install()
if __name__=='__main__':
 F.R.draw(p.with_name('scene.json'),p.with_name('image.png'))
