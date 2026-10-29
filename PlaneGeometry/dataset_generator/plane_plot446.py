"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane446:

    def __init__(self):
        self.__dict__.update({'id': 'Plane446', 'source_dataset': 'MathVision', 'question': 'The figure below shows line $\\ell$ with a regular, infinite, recurring pattern of squares and line segments.\nHow many of the following four kinds of rigid motion transformations of the plane in which this figure is drawn, other than the identity transformation, will transform this figure into itself?\n\nsome rotation around a point of line $\\ell$\nsome translation in the direction parallel to line $\\ell$\nthe reflection across line $\\ell$\nsome reflection across a line perpendicular to line $\\ell$', 'answer': '2', 'answer_type': 'number', 'subject': 'PlaneGeometry', 'source_key': 'test:2222', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane446.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane446.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane446', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane446.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane446().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
