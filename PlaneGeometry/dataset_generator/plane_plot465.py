"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane465:

    def __init__(self):
        self.__dict__.update({'id': 'Plane465', 'source_dataset': 'MathVision', 'question': 'A portion of a corner of a tiled floor is shown.  If the entire floor is tiled in this way and each of the four corners  looks like this one, then what fraction of the tiled floor is made of darker tiles?\n\nChoices:\nA:$\\frac{1}{3}$\nB:$\\frac{4}{9}$\nC:$\\frac{1}{2}$\nD:$\\frac{5}{9}$\nE:$\\frac{5}{8}$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{1}{3}$', 'B': '$\\frac{4}{9}$', 'C': '$\\frac{1}{2}$', 'D': '$\\frac{5}{9}$', 'E': '$\\frac{5}{8}$'}, 'source_key': 'test:2643', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane465.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane465.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane465', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane465.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane465().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
