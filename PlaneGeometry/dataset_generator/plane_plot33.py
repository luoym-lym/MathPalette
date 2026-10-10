"""Frozen MathVerse question Plane33; source key s2059."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Plane33:
    def __init__(self):
        self.id = 'Plane33'
        self.source_dataset = 'MathVerse'
        self.query = 'This is part of a piece of jewellery. It is made out of a metal plate base, and gold plated wire (of negligible thickness) runs around the outside.\n\nWhat is the area covered by the metal plate base?\n\nGive your answer correct to two decimal places.'
        self.answer = 'Area $=70.69 \\mathrm{~mm}^{2}$'
        self.answer_type = 'area'
        self.subject = 'PlaneGeometry'
        self.level = 'high_school'
        self.scene_path = Path(__file__).with_name("scenes") / "Plane33.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('PlaneGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Plane33().draw()
    print(result["image_path"])
