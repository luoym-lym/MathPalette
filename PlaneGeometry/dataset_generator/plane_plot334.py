"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane334:

    def __init__(self):
        self.__dict__.update({'id': 'Plane334', 'source_dataset': 'MathVision', 'question': 'Each of the nine paths shown is $100 \\mathrm{~m}$ long. What is the length of the longest route from $A$ to $B$ that does not use any path twice?\nChoices:\nA:$900 \\mathrm{~m}$\nB:$800 \\mathrm{~m}$\nC:$700 \\mathrm{~m}$\nD:$500 \\mathrm{~m}$\nE:$400 \\mathrm{~m}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$900 \\mathrm{~m}$', 'B': '$800 \\mathrm{~m}$', 'C': '$700 \\mathrm{~m}$', 'D': '$500 \\mathrm{~m}$', 'E': '$400 \\mathrm{~m}$'}, 'source_key': 'test:1083', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane334.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane334.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane334', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane334.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane334().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
