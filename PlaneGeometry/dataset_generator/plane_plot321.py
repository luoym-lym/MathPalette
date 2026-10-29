"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane321:

    def __init__(self):
        self.__dict__.update({'id': 'Plane321', 'source_dataset': 'MathVision', 'question': 'An equilateral triangle $A C D$ is rotated counterclockwise about point $A$. Through what angle has it rotated when it first covers equilateral triangle $A B C$?\nChoices:\nA:$60^{\\circ}$\nB:$120^{\\circ}$\nC:$180^{\\circ}$\nD:$240^{\\circ}$\nE:$300^{\\circ}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$60^{\\circ}$', 'B': '$120^{\\circ}$', 'C': '$180^{\\circ}$', 'D': '$240^{\\circ}$', 'E': '$300^{\\circ}$'}, 'source_key': 'test:1009', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane321.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane321.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane321', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane321.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane321().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
