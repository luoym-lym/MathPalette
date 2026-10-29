"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid214:

    def __init__(self):
        self.__dict__.update({'id': 'Solid214', 'source_dataset': 'MathVision', 'question': 'The centers of the faces of the right rectangular prism shown below are joined to create an octahedron. What is the volume of the octahedron?\n\nChoices:\nA:$\\frac{75}{12}$\nB:$10$\nC:$12$\nD:$10\\sqrt{2}$\nE:$15$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\frac{75}{12}$', 'B': '$10$', 'C': '$12$', 'D': '$10\\sqrt{2}$', 'E': '$15$'}, 'source_key': 'test:2206', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid214.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid214.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid214', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid214.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid214().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
