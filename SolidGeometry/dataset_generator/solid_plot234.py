"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid234:

    def __init__(self):
        self.__dict__.update({'id': 'Solid234', 'source_dataset': 'MathVision', 'question': 'A wedge is cut from a $6$-cm cylinder as shown by the dashed curve. Which answer choice is closest to the volume of the wedge in cubic centimeters?\nChoices:\nA:48\nB:75\nC:151\nD:192\nE:603', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '48', 'B': '75', 'C': '151', 'D': '192', 'E': '603'}, 'source_key': 'test:2693', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid234.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid234.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid234', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid234.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid234().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
