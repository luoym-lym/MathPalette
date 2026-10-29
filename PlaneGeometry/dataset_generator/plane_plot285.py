"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane285:

    def __init__(self):
        self.__dict__.update({'id': 'Plane285', 'source_dataset': 'MathVision', 'question': '$A 10 \\mathrm{~cm}$ long piece of wire is folded so that every part is equally long (see diagram). The wire is then cut through in the two positions marked. How long are the three pieces created in this way?\nChoices:\nA:$2 \\mathrm{~cm}, 3 \\mathrm{~cm}, 5 \\mathrm{~cm}$\nB:$2 \\mathrm{~cm}, 2 \\mathrm{~cm}, 6 \\mathrm{~cm}$\nC:$1 \\mathrm{~cm}, 4 \\mathrm{~cm}, 5 \\mathrm{~cm}$\nD:$1 \\mathrm{~cm}, 3 \\mathrm{~cm}, 6 \\mathrm{~cm}$\nE:$3 \\mathrm{~cm}, 3 \\mathrm{~cm}, 4 \\mathrm{~cm}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$2 \\mathrm{~cm}, 3 \\mathrm{~cm}, 5 \\mathrm{~cm}$', 'B': '$2 \\mathrm{~cm}, 2 \\mathrm{~cm}, 6 \\mathrm{~cm}$', 'C': '$1 \\mathrm{~cm}, 4 \\mathrm{~cm}, 5 \\mathrm{~cm}$', 'D': '$1 \\mathrm{~cm}, 3 \\mathrm{~cm}, 6 \\mathrm{~cm}$', 'E': '$3 \\mathrm{~cm}, 3 \\mathrm{~cm}, 4 \\mathrm{~cm}$'}, 'source_key': 'test:855', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane285.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane285.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane285', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane285.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane285().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
