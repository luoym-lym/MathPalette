"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid140:

    def __init__(self):
        self.__dict__.update({'id': 'Solid140', 'source_dataset': 'MathVision', 'question': 'In a box-shaped water tank with dimensions $4 \\mathrm{~m} \\times 2 \\mathrm{~m} \\times 1 \\mathrm{~m}$, the height of the water is $25 \\mathrm{~cm}$. The tank is then turned on its side (see picture on the right). How high is the water in the tank now?\nChoices:\nA:$25 \\mathrm{~cm}$\nB:$50 \\mathrm{~cm}$\nC:$75 \\mathrm{~cm}$\nD:$1 \\mathrm{~m}$\nE:$1.25 \\mathrm{~m}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$25 \\mathrm{~cm}$', 'B': '$50 \\mathrm{~cm}$', 'C': '$75 \\mathrm{~cm}$', 'D': '$1 \\mathrm{~m}$', 'E': '$1.25 \\mathrm{~m}$'}, 'source_key': 'test:969', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid140.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid140.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid140', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid140.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid140().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
