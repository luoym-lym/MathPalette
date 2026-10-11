from pathlib import Path
import sys
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p.parent))
from redraw_runtime import draw
if __name__=="__main__":
 print(draw(p/"scene.json", p/"redrawn.png"))
