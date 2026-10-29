"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid247:

    def __init__(self):
        self.__dict__.update({'id': 'Solid247', 'source_dataset': 'MathVision', 'question': 'A solid right prism $ABCDEF$ has a height of $16$ and equilateral triangle bases with side length $12,$ as shown. $ABCDEF$ is sliced with a straight cut through points $M,$ $N,$ $P,$ and $Q$ on edges $DE,$ $DF,$ $CB,$ and $CA,$ respectively. If $DM=4,$ $DN=2,$ and $CQ=8,$ determine the volume of the solid $QPCDMN.$', 'answer': '\\frac{224\\sqrt{3}}{3}', 'answer_type': 'number', 'subject': 'SolidGeometry', 'source_key': 'test:3011', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid247.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid247.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid247', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid247.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid247().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
