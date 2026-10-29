"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane447:

    def __init__(self):
        self.__dict__.update({'id': 'Plane447', 'source_dataset': 'MathVision', 'question': 'A rectangular piece of paper $6$ inches wide is folded as in the diagram so that one corner touches the opposite side. The length in inches of the crease $L$ in terms of angle $\\theta$ is\nChoices:\nA:$3\\sec ^2\\theta\\csc\\theta$\nB:$6\\sin\\theta\\sec\\theta$\nC:$3\\sec\\theta\\csc\\theta$\nD:$6\\sec\\theta\\csc ^2\\theta$\nE:$\\text{None of these}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$3\\sec ^2\\theta\\csc\\theta$', 'B': '$6\\sin\\theta\\sec\\theta$', 'C': '$3\\sec\\theta\\csc\\theta$', 'D': '$6\\sec\\theta\\csc ^2\\theta$', 'E': '$\\text{None of these}$'}, 'source_key': 'test:2302', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane447.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane447.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane447', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane447.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane447().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
