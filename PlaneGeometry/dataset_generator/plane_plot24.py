"""Frozen MathVerse question Plane24; source key s1754."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane24:
    def __init__(self):
        self.id = 'Plane24'
        self.source_dataset = 'MathVerse'
        self.query = 'A man stands at point A looking at the top of two poles. The man wishes to find the distance between the two poles.\nHence find BC, the distance between the two poles in metres.\n\nRound your answer to one decimal place.'
        self.answer = '4.4 m'
        self.answer_type = 'length'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane24.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane24().draw()
    print(result["image_path"])
