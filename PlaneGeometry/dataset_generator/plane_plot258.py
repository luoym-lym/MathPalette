"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane258:

    def __init__(self):
        self.__dict__.update({'id': 'Plane258', 'source_dataset': 'MathVision', 'question': 'The diagram shows squares of different sizes. The side length of the smallest square is $20 \\mathrm{~cm}$. How long is the black line?\nChoices:\nA:$380 \\mathrm{~cm}$\nB:$400 \\mathrm{~cm}$\nC:$420 \\mathrm{~cm}$\nD:$440 \\mathrm{~cm}$\nE:$1680 \\mathrm{~cm}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$380 \\mathrm{~cm}$', 'B': '$400 \\mathrm{~cm}$', 'C': '$420 \\mathrm{~cm}$', 'D': '$440 \\mathrm{~cm}$', 'E': '$1680 \\mathrm{~cm}$'}, 'source_key': 'test:771', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane258.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane258.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane258', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane258.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane258().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
