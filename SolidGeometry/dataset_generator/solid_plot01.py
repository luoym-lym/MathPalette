"""Frozen MathVerse question Solid01; source key s3184."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid01:
    def __init__(self):
        self.id = 'Solid01'
        self.source_dataset = 'MathVerse'
        self.query = 'We want to find $y$, the length of the diagonal $DF$.\n\nCalculate $y$ to two decimal places.'
        self.answer = '$y=21.61$'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid01.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid01().draw()
    print(result["image_path"])
