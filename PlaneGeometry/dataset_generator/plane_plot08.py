"""Frozen MathVerse question Plane08; source key s1189."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane08:
    def __init__(self):
        self.id = 'Plane08'
        self.source_dataset = 'MathVerse'
        self.query = '\\[Find x.\nChoices:\nA:4\nB:4 \\sqrt { 2 }\nC:4 \\sqrt { 3 }\nD:8\\]'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane08.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane08().draw()
    print(result["image_path"])
