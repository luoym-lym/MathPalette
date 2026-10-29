"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid124:

    def __init__(self):
        self.__dict__.update({'id': 'Solid124', 'source_dataset': 'MathVision', 'question': 'A cube has side length $12 \\mathrm{~cm}$. Find the length of the route shown on its surface from point $M$ to point $N$.\nChoices:\nA:40 cm\nB:48 cm\nC:50 cm\nD:60 cm\nE:It is impossible to determine', 'answer': 'D', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '40 cm', 'B': '48 cm', 'C': '50 cm', 'D': '60 cm', 'E': 'It is impossible to determine'}, 'source_key': 'test:722', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid124.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid124.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid124', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid124.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid124().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
