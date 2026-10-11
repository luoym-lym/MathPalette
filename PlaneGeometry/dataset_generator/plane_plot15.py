"""Frozen MathVerse question Plane15; source key s3834."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane15:
    def __init__(self):
        self.id = 'Plane15'
        self.source_dataset = 'MathVerse'
        self.query = 'In rectangle ABDF above, C and E are midpoints of sides BD and DF, respectively. What fraction of the area of the rectangle is shaded?'
        self.answer = '5/8'
        self.answer_type = 'number'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane15.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane15().draw()
    print(result["image_path"])
