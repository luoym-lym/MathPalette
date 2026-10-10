"""Frozen MathVerse question Plane21; source key s1644."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane21:
    def __init__(self):
        self.id = 'Plane21'
        self.source_dataset = 'MathVerse'
        self.query = 'In remote locations, photographers must keep track of their position from their base. One morning a photographer sets out from base, represented by point B, to the edge of an ice shelf at point S. She then walked to point P.\n\nIf the photographer were to walk back to her base from point P, what is the total distance she would have travelled? Round your answer to one decimal place.'
        self.answer = '2191.7 metres'
        self.answer_type = 'numeric'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane21.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane21().draw()
    print(result["image_path"])
