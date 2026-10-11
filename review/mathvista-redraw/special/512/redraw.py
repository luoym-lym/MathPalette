import sys,json
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent))
from build_analytic import draw_scene
if __name__=='__main__': draw_scene(json.loads((P/'scene.json').read_text()),P/'redraw.png')
