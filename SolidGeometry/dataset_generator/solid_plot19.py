"""Frozen MathVerse question Solid19; source key s3599."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid19:
    def __init__(self):
        self.id = 'Solid19'
        self.source_dataset = 'MathVerse'
        self.query = 'Two similar cylinders as shown in the figure, find the fully simplified ratio of the volume of the larger cylinder to the volume of the smaller cylinder.'
        self.answer = '100'
        self.answer_type = 'ratio'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid19.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid19().draw()
    print(result["image_path"])
