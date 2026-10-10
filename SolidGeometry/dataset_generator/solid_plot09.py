"""Frozen MathVerse question Solid09; source key s3484."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid09:
    def __init__(self):
        self.id = 'Solid09'
        self.source_dataset = 'MathVerse'
        self.query = 'Find the volume of the figure shown.\n\nRound your answer to two decimal places.'
        self.answer = 'Volume $=874.93 \\mathrm{~cm}^{3}$'
        self.answer_type = 'number'
        self.subject = 'SolidGeometry'
        self.level = 'medium'
        self.scene_path = Path(__file__).with_name("scenes") / "Solid09.json"

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == "__main__":
    result = Solid09().draw()
    print(result["image_path"])
