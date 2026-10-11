"""Approved frozen SOLIDGEO question Solid22."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid22:
    def __init__(self):
        self.id = 'Solid22'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'A rectangular container has length and width 2 units each and height 8 units. It is partially filled with water to a height of 5 units, as shown in Figure (1). The container is then tilted without spilling any water, and its front view is shown in Figure (2). Find the length of $CD$.\n\nChoices:\nA: $2 \\sqrt{5}$\nB: $3 \\sqrt{5}$\nC: $3 \\sqrt{10}$\nD: $2 \\sqrt{10}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.subject = 'SolidGeometry'
        self.choices = {'A': '$2 \\sqrt{5}$', 'B': '$3 \\sqrt{5}$', 'C': '$3 \\sqrt{10}$', 'D': '$2 \\sqrt{10}$'}
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid22.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid22().draw()['image_path'])
