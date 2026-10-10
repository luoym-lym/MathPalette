"""Frozen MathVerse question Plane18; source key s1149."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane18:
    def __init__(self):
        self.id = 'Plane18'
        self.source_dataset = 'MathVerse'
        self.query = '\\[Find m \\angle 2 if m \\widehat B C = 30 and m \\widehat A D = 20.\nChoices:\nA:20\nB:25\nC:30\nD:155\\]'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane18.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane18().draw()
    print(result["image_path"])
