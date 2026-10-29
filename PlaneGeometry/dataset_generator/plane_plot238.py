"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane238:

    def __init__(self):
        self.__dict__.update({'id': 'Plane238', 'source_dataset': 'MathVision', 'question': 'A piece of paper numbered 1 to 36 is folded in half twice, as shown.\nA hole is then punched through all four layers at the position shown in the right-hand diagram. Which four numbers are pierced?\nChoices:\nA:$8,11,26,29$\nB:$14,16,21,23$\nC:$14,17,20,23$\nD:$15,16,21,22$\nE:$15,17,20,22$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$8,11,26,29$', 'B': '$14,16,21,23$', 'C': '$14,17,20,23$', 'D': '$15,16,21,22$', 'E': '$15,17,20,22$'}, 'source_key': 'test:670', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane238.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane238.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane238', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane238.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane238().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
