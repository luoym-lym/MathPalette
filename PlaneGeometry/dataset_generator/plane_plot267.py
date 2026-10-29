"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane267:

    def __init__(self):
        self.__dict__.update({'id': 'Plane267', 'source_dataset': 'MathVision', 'question': 'The figure on the right has a perimeter of $42 \\mathrm{~cm}$. The figure was made from eight equally sized squares. What is the area of the figure?\nChoices:\nA:$8 \\mathrm{~cm}^{2}$\nB:$9 \\mathrm{~cm}^{2}$\nC:$24 \\mathrm{~cm}^{2}$\nD:$72 \\mathrm{~cm}^{2}$\nE:$128 \\mathrm{~cm}^{2}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$8 \\mathrm{~cm}^{2}$', 'B': '$9 \\mathrm{~cm}^{2}$', 'C': '$24 \\mathrm{~cm}^{2}$', 'D': '$72 \\mathrm{~cm}^{2}$', 'E': '$128 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:809', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane267.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane267.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane267', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane267.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane267().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
