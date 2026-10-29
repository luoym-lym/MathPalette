"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane182:

    def __init__(self):
        self.__dict__.update({'id': 'Plane182', 'source_dataset': 'MathVision', 'question': 'An equilateral triangle is being rolled around a unit square as shown. How long is the path that the point shown covers, if the point and the triangle are both back at the start for the first time?\nChoices:\nA:$4 \\pi$\nB:$\\frac{28}{3} \\pi$\nC:$8 \\pi$\nD:$\\frac{14}{3} \\pi$\nE:$\\frac{21}{2} \\pi$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$4 \\pi$', 'B': '$\\frac{28}{3} \\pi$', 'C': '$8 \\pi$', 'D': '$\\frac{14}{3} \\pi$', 'E': '$\\frac{21}{2} \\pi$'}, 'source_key': 'test:254', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane182.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane182.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane182', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane182.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane182().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
