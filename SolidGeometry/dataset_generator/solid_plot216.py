"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid216:

    def __init__(self):
        self.__dict__.update({'id': 'Solid216', 'source_dataset': 'MathVision', 'question': 'In the adjoining figure of a rectangular solid, $\\angle DHG=45^\\circ$ and $\\angle FHB=60^\\circ$. Find the cosine of $\\angle BHD$.\n\nChoices:\nA:$\\frac{\\sqrt{3}}{6}$\nB:$\\frac{\\sqrt{2}}{6}$\nC:$\\frac{\\sqrt{6}}{3}$\nD:$\\frac{\\sqrt{6}}{4}$\nE:$\\frac{\\sqrt{6}-\\sqrt{2}}{4}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\frac{\\sqrt{3}}{6}$', 'B': '$\\frac{\\sqrt{2}}{6}$', 'C': '$\\frac{\\sqrt{6}}{3}$', 'D': '$\\frac{\\sqrt{6}}{4}$', 'E': '$\\frac{\\sqrt{6}-\\sqrt{2}}{4}$'}, 'source_key': 'test:2341', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid216.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid216.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid216', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid216.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid216().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
