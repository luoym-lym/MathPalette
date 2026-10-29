"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane394:

    def __init__(self):
        self.__dict__.update({'id': 'Plane394', 'source_dataset': 'MathVision', 'question': 'A $3 \\mathrm{~cm}$ wide strip is grey on one side and white on the other. The strip is folded so that it fits inside a rectangle of length $27 \\mathrm{~cm}$, as shown. The grey trapeziums are identical. What is the length of the original strip?\nChoices:\nA:$36 \\mathrm{~cm}$\nB:$48 \\mathrm{~cm}$\nC:$54 \\mathrm{~cm}$\nD:$57 \\mathrm{~cm}$\nE:$81 \\mathrm{~cm}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$36 \\mathrm{~cm}$', 'B': '$48 \\mathrm{~cm}$', 'C': '$54 \\mathrm{~cm}$', 'D': '$57 \\mathrm{~cm}$', 'E': '$81 \\mathrm{~cm}$'}, 'source_key': 'test:1632', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane394.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane394.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane394', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane394.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane394().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
