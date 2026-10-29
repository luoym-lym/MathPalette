"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane429:

    def __init__(self):
        self.__dict__.update({'id': 'Plane429', 'source_dataset': 'MathVision', 'question': "If $r, s$, and $t$ denote the lengths of the 'lines' in the picture, then which of the following inequalities is correct?\nChoices:\nA:$r<s<t$\nB:$r<t<s$\nC:$s<r<t$\nD:$s<t<r$\nE:$t<s<r$", 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$r<s<t$', 'B': '$r<t<s$', 'C': '$s<r<t$', 'D': '$s<t<r$', 'E': '$t<s<r$'}, 'source_key': 'test:1897', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane429.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane429.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane429', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane429.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane429().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
