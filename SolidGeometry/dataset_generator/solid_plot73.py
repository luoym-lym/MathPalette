"""Redraw the frozen approved original Solid73."""
from pathlib import Path
import sys

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'dataset_tools/geometry_dataset.py').is_file())
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
from dataset_tools.geometry_dataset import read_json,renderer_for,draw_question


class Solid73:
    def __init__(self):
        self.id='Solid73'
        self.source_dataset='Author designed'
        self.source_key='triangular-prism-net:lateral-edge-from-P'
        self.question=('The figure shows a net of a right triangular prism with equilateral triangular bases. '
                       'The three rectangles are joined along the common edges shown. '
                       'When the net is folded into the prism, which labeled point is the other endpoint '
                       'of the lateral edge with one endpoint at P?\nChoices:\n'
                       'A: Point Q\nB: Point R\nC: Point S\nD: None of these three points')
        self.query=self.question
        self.answer='B'
        self.answer_type='choice'
        self.choices={'A':'Point Q','B':'Point R','C':'Point S','D':'None of these three points'}
        self.subject='SolidGeometry'
        self.level=None
        self.scene_path=Path(__file__).parent/'scenes/Solid73.json'

    def get_scene(self):
        return read_json(self.scene_path)

    def build_scene(self):
        fig,_=renderer_for('SolidGeometry').render_scene(self.get_scene())
        return fig,fig.axes[0]

    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)):
            output_path=num
        return draw_question('SolidGeometry',self.scene_path,output_path)

    def redraw(self,output_path=None):
        return self.draw(output_path=output_path)


if __name__=='__main__':
    print(Solid73().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
