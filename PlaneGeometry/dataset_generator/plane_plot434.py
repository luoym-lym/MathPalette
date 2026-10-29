"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane434:

    def __init__(self):
        self.__dict__.update({'id': 'Plane434', 'source_dataset': 'MathVision', 'question': 'Two identical rectangles with sides of length $3 \\mathrm{~cm}$ and $9 \\mathrm{~cm}$ are overlapping as in the diagram. What is the area of the overlap of the two rectangles?\nChoices:\nA:$12 \\mathrm{~cm}^{2}$\nB:$13.5 \\mathrm{~cm}^{2}$\nC:$14 \\mathrm{~cm}^{2}$\nD:$15 \\mathrm{~cm}^{2}$\nE:$16 \\mathrm{~cm}^{2}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$12 \\mathrm{~cm}^{2}$', 'B': '$13.5 \\mathrm{~cm}^{2}$', 'C': '$14 \\mathrm{~cm}^{2}$', 'D': '$15 \\mathrm{~cm}^{2}$', 'E': '$16 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:1953', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane434.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane434.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane434', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane434.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane434().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
