"""Approved frozen SOLIDGEO question Solid23."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json

class Solid23:
    def __init__(self):
        self.id = 'Solid23'
        self.source_dataset = 'SOLIDGEO'
        self.query = 'The front, left, and top views of a cone and the relevant measurements are shown in the figure. Find the lateral surface area of the cone.\n\nChoices:\nA: $12 \\pi \\mathrm{cm}^{2}$\nB: $15 \\pi \\mathrm{cm}^{2}$\nC: $24 \\pi \\mathrm{cm}^{2}$\nD: $10 \\pi \\mathrm{cm}^{2}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.subject = 'SolidGeometry'
        self.choices = {'A': '$12 \\pi \\mathrm{cm}^{2}$', 'B': '$15 \\pi \\mathrm{cm}^{2}$', 'C': '$24 \\pi \\mathrm{cm}^{2}$', 'D': '$10 \\pi \\mathrm{cm}^{2}$'}
        self.level = 'unspecified'
        self.scene_path = Path(__file__).with_name('scenes') / 'Solid23.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def draw(self, output_path=None):
        return draw_question('SolidGeometry', self.scene_path, output_path)

if __name__ == '__main__':
    print(Solid23().draw()['image_path'])
