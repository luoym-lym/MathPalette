"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid89:

    def __init__(self):
        self.__dict__.update({'id': 'Solid89', 'source_dataset': 'MathVision', 'question': 'A $3 \\times 3 \\times 3$ cube weighs 810 grams. Three holes are drilled through it as shown, each in the shape of a $1 \\times 1 \\times 3$ rectangular parallelepiped. What is the weight of the remaining solid?\nChoices:\nA:$540 \\mathrm{~g}$\nB:$570 \\mathrm{~g}$\nC:$600 \\mathrm{~g}$\nD:$630 \\mathrm{~g}$\nE:$660 \\mathrm{~g}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$540 \\mathrm{~g}$', 'B': '$570 \\mathrm{~g}$', 'C': '$600 \\mathrm{~g}$', 'D': '$630 \\mathrm{~g}$', 'E': '$660 \\mathrm{~g}$'}, 'source_key': 'test:180', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid89.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid89.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid89', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid89.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid89().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
