"""Frozen Author designed question Plane108; importing does not write files."""
from pathlib import Path
import sys

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.geometry_dataset import draw_question, read_json, renderer_for


class Plane108:
    def __init__(self):
        self.id = 'Plane108'
        self.source_dataset = 'Author designed'
        self.question = 'Which marked angle, A, B, or C, has the same measure as R? All diagrams are drawn to scale.\nChoices:\nA: Angle A\nB: Angle B\nC: Angle C'
        self.query = self.question
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Angle A', 'B': 'Angle B', 'C': 'Angle C'}
        self.source_key = 'visual-matching:angle_match'
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = Path(__file__).with_name('scenes') / 'Plane108.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def build_scene(self):
        fig, _ = renderer_for('PlaneGeometry').render_scene(self.get_scene())
        return fig, fig.axes[0]

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        scene = self.get_scene()
        if scene['source_image'] is not None:
            return draw_question('PlaneGeometry', self.scene_path, output_path)
        # Original author designs legitimately have no source image.
        # The shared renderer's file wrapper predates nullable sources;
        # its scene renderer already supports them without alteration.
        target = Path(output_path).resolve() if output_path else _PROJECT_ROOT / '.runtime/reproduced/PlaneGeometry' / (self.id + '.png')
        if target.is_relative_to(_PROJECT_ROOT) and not target.is_relative_to(_PROJECT_ROOT / '.runtime/reproduced'):
            raise ValueError('Redraw into .runtime/reproduced or an external output directory.')
        if target.suffix.lower() not in ('.png', '.svg'):
            raise ValueError('The output must be PNG or SVG.')
        data, checks = renderer_for('PlaneGeometry').image_bytes(scene, vector=target.suffix.lower() == '.svg')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return {'image_path': str(target), 'constraints': checks}

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)


if __name__ == '__main__':
    print(Plane108().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
