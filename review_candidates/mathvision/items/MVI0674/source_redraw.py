from pathlib import Path
import renderer_semantic as r
if __name__=="__main__":
 p=Path(__file__).resolve().parent
 r.draw(p/"scene.json",p/"image.png")
 r.draw(p/"scene.json",p/"image.svg")
