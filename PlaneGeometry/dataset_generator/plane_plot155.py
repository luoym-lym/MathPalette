"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane155:

    def __init__(self):
        self.__dict__.update({'id': 'Plane155', 'source_dataset': 'MathVision', 'question': 'The pattern shown is made from sticks, each $5 \\mathrm{~cm}$ long and $1 \\mathrm{~cm}$ wide. What is the length of the pattern?\nChoices:\nA:$20 \\mathrm{~cm}$\nB:$21 \\mathrm{~cm}$\nC:$22 \\mathrm{~cm}$\nD:$23 \\mathrm{~cm}$\nE:$25 \\mathrm{~cm}$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$20 \\mathrm{~cm}$', 'B': '$21 \\mathrm{~cm}$', 'C': '$22 \\mathrm{~cm}$', 'D': '$23 \\mathrm{~cm}$', 'E': '$25 \\mathrm{~cm}$'}, 'source_key': 'test:83', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane155.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane155.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane155', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane155.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane155().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
