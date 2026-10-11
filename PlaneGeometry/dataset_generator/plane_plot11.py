"""Frozen MathVerse question Plane11; source key s1859."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane11:
    def __init__(self):
        self.id = 'Plane11'
        self.source_dataset = 'MathVerse'
        self.query = '\\[Consider the adjacent figure:\n\nSolve for the unknown \\theta . Leave your answer in degrees.\\]'
        self.answer = '\\[60^\\circ \\]'
        self.answer_type = 'number'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane11.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane11().draw()
    print(result["image_path"])
