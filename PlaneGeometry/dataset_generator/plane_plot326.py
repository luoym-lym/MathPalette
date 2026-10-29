"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane326:

    def __init__(self):
        self.__dict__.update({'id': 'Plane326', 'source_dataset': 'MathVision', 'question': 'In the picture there is a square tile with two fourths of a circle. The radius of every fourth is half the side of the tile and its length equals $5 \\mathrm{dm}$. A large square is formed from 16 such tiles. What is the maximum possible length of an unbroken continuous curve consisting of the fourths?\nChoices:\nA:$75 \\mathrm{dm}$\nB:$100 \\mathrm{dm}$\nC:$105 \\mathrm{dm}$\nD:$110 \\mathrm{dm}$\nE:$80 \\mathrm{dm}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$75 \\mathrm{dm}$', 'B': '$100 \\mathrm{dm}$', 'C': '$105 \\mathrm{dm}$', 'D': '$110 \\mathrm{dm}$', 'E': '$80 \\mathrm{dm}$'}, 'source_key': 'test:1038', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane326.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane326.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane326', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane326.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane326().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
