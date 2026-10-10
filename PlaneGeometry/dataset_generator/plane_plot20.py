"""Frozen MathVerse question Plane20; source key s1379."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane20:
    def __init__(self):
        self.id = 'Plane20'
        self.source_dataset = 'MathVerse'
        self.query = '\\[Find m \\widehat C B.\nChoices:\nA:24\nB:33\nC:67\nD:134\\]'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane20.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane20().draw()
    print(result["image_path"])
