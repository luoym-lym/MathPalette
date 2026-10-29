"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane407:

    def __init__(self):
        self.__dict__.update({'id': 'Plane407', 'source_dataset': 'MathVision', 'question': 'A paper ribbon has length $36 \\mathrm{~cm}$. It is divided into four rectangles of different lengths. Two lines are drawn, each joining the centres of two adjacent rectangles, as shown.\nWhat is the sum of the lengths of these lines?\nChoices:\nA:$18 \\mathrm{~cm}$\nB:$17 \\mathrm{~cm}$\nC:$20 \\mathrm{~cm}$\nD:$19 \\mathrm{~cm}$\nE:It depends upon the sizes of the rectangles', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$18 \\mathrm{~cm}$', 'B': '$17 \\mathrm{~cm}$', 'C': '$20 \\mathrm{~cm}$', 'D': '$19 \\mathrm{~cm}$', 'E': 'It depends upon the sizes of the rectangles'}, 'source_key': 'test:1740', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane407.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane407.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane407', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane407.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane407().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
