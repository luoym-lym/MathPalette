"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane440:

    def __init__(self):
        self.__dict__.update({'id': 'Plane440', 'source_dataset': 'MathVision', 'question': 'Three one-inch squares are placed with their bases on a line. The center square is lifted out and rotated $ 45^\\circ$, as shown. Then it is centered and lowered into its original location until it touches both of the adjoining squares. How many inches is the point $ B$ from the line on which the bases of the original squares were placed?\nChoices:\nA:$1$\nB:$\\sqrt{2}$\nC:$\\frac{3}{2}$\nD:$\\sqrt{2} + \\frac{1}{2}$\nE:$2$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$1$', 'B': '$\\sqrt{2}$', 'C': '$\\frac{3}{2}$', 'D': '$\\sqrt{2} + \\frac{1}{2}$', 'E': '$2$'}, 'source_key': 'test:2146', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane440.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane440.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane440', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane440.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane440().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
