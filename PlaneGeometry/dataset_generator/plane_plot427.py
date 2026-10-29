"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane427:

    def __init__(self):
        self.__dict__.update({'id': 'Plane427', 'source_dataset': 'MathVision', 'question': 'The diagram shows an equilateral triangle RST and also the triangle $T U V$ obtained by rotating triangle $R S T$ about the point $T$. Angle $R T V=70^{\\circ}$. What is angle $R S V$?\nChoices:\nA:$20^{\\circ}$\nB:$25^{\\circ}$\nC:$30^{\\circ}$\nD:$35^{\\circ}$\nE:$40^{\\circ}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$20^{\\circ}$', 'B': '$25^{\\circ}$', 'C': '$30^{\\circ}$', 'D': '$35^{\\circ}$', 'E': '$40^{\\circ}$'}, 'source_key': 'test:1890', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane427.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane427.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane427', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane427.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane427().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
