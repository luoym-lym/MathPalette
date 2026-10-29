"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane254:

    def __init__(self):
        self.__dict__.update({'id': 'Plane254', 'source_dataset': 'MathVision', 'question': 'A paper ribbon $27 \\mathrm{~cm}$ long is divided into four rectangles of different sizes. Two segments each connect the centres of two adjacent rectangles, as shown. Find the sum of the lengths of these two segments.\nChoices:\nA:$12 \\mathrm{~cm}$\nB:$13.5 \\mathrm{~cm}$\nC:$14 \\mathrm{~cm}$\nD:$14.5 \\mathrm{~cm}$\nE:The number depends on the division', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$12 \\mathrm{~cm}$', 'B': '$13.5 \\mathrm{~cm}$', 'C': '$14 \\mathrm{~cm}$', 'D': '$14.5 \\mathrm{~cm}$', 'E': 'The number depends on the division'}, 'source_key': 'test:747', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane254.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane254.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane254', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane254.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane254().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
