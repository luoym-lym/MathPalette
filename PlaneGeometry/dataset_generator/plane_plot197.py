"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane197:

    def __init__(self):
        self.__dict__.update({'id': 'Plane197', 'source_dataset': 'MathVision', 'question': 'A pathway consists of 10 paving stones, each $4 \\mathrm{dm}$ wide and 6 dm long. A black line connects the middle points of the paving stones as shown. What is the length of the black line?\nChoices:\nA:$24 \\mathrm{dm}$\nB:$40 \\mathrm{dm}$\nC:$46 \\mathrm{dm}$\nD:$50 \\mathrm{dm}$\nE:$56 \\mathrm{dm}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$24 \\mathrm{dm}$', 'B': '$40 \\mathrm{dm}$', 'C': '$46 \\mathrm{dm}$', 'D': '$50 \\mathrm{dm}$', 'E': '$56 \\mathrm{dm}$'}, 'source_key': 'test:460', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane197.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane197.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane197', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane197.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane197().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
