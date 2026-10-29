"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane380:

    def __init__(self):
        self.__dict__.update({'id': 'Plane380', 'source_dataset': 'MathVision', 'question': 'The big rectangle shown is divided into 30 equally big squares. The perimeter of the area shaded in grey is $240 \\mathrm{~cm}$. How big is the area of the big rectangle?\nChoices:\nA:$480 \\mathrm{~cm}^{2}$\nB:$750 \\mathrm{~cm}^{2}$\nC:$1080 \\mathrm{~cm}^{2}$\nD:$1920 \\mathrm{~cm}^{2}$\nE:$2430 \\mathrm{~cm}^{2}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$480 \\mathrm{~cm}^{2}$', 'B': '$750 \\mathrm{~cm}^{2}$', 'C': '$1080 \\mathrm{~cm}^{2}$', 'D': '$1920 \\mathrm{~cm}^{2}$', 'E': '$2430 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:1486', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane380.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane380.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane380', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane380.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane380().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
