"""Frozen MathVerse question Plane09; source key s1649."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane09:
    def __init__(self):
        self.id = 'Plane09'
        self.source_dataset = 'MathVerse'
        self.query = 'A rally car starts at point P and races to point Q. Here the car turns west and races to point R. At point R the car must turn to head directly back to point P.\n\nWhat is the compass bearing of R from P? Give your answer to one decimal place.'
        self.answer = '\\[S 23.5 ^\\circ W\\]'
        self.answer_type = 'text'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane09.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane09().draw()
    print(result["image_path"])
