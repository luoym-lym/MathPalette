"""Frozen MathVerse question Solid21; source key s3639."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid21:
    def __init__(self):
        self.id = 'Solid21'
        self.source_dataset = 'MathVerse'
        self.query = 'Each side length of the cube is equal. Find the volume of the cube shown.'
        self.answer = '$144cm^3$'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid21.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid21().draw()
    print(result["image_path"])
