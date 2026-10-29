"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane276:

    def __init__(self):
        self.__dict__.update({'id': 'Plane276', 'source_dataset': 'MathVision', 'question': 'A square with perimeter $48 \\mathrm{~cm}$ is cut into two equally big pieces with one cut. They are fitted together to make a rectangle as shown in the diagram. How big is the perimeter of that rectangle?\nChoices:\nA:$24 \\mathrm{~cm}$\nB:$30 \\mathrm{~cm}$\nC:$48 \\mathrm{~cm}$\nD:$60 \\mathrm{~cm}$\nE:$72 \\mathrm{~cm}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$24 \\mathrm{~cm}$', 'B': '$30 \\mathrm{~cm}$', 'C': '$48 \\mathrm{~cm}$', 'D': '$60 \\mathrm{~cm}$', 'E': '$72 \\mathrm{~cm}$'}, 'source_key': 'test:832', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane276.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane276.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane276', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane276.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane276().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
