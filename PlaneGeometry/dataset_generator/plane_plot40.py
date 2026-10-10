"""Frozen MathVerse question Plane40; source key s3884."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane40:
    def __init__(self):
        self.id = 'Plane40'
        self.source_dataset = 'MathVerse'
        self.query = 'In the figure above. What is the value of z?\nChoices:\nA.80\nB.60\nC.50\nD.40\nE.10'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane40.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane40().draw()
    print(result["image_path"])
