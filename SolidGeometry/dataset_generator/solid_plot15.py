"""Frozen MathVerse question Solid15; source key s3589."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid15:
    def __init__(self):
        self.id = 'Solid15'
        self.source_dataset = 'MathVerse'
        self.query = 'Consider the two similar spheres shown.\n\n\nFind the volume of Sphere A, in simplest exact form.'
        self.answer = '\\[36\\pi \\mathrm{cm}^3\\]'
        self.answer_type = 'expression'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid15.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid15().draw()
    print(result["image_path"])
