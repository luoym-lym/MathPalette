from pathlib import Path
from renderer import draw
HERE=Path(__file__).resolve().parent
if __name__=='__main__':
 draw(HERE/'scene.json',HERE/'image.png')
 draw(HERE/'scene.json',HERE/'image.svg')
