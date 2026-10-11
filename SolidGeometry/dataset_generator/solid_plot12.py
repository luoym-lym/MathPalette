"""Frozen MathVerse question Solid12; source key s3544."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid12:
    def __init__(self):
        self.id = 'Solid12'
        self.source_dataset = 'MathVerse'
        self.query = 'Find the surface area of the square pyramid.\n\nRound your answer to one decimal place.'
        self.answer = '\\[256.2 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid12.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid12().draw()
    print(result["image_path"])
