"""Strict reproducible staging candidate MV_F0617; not user approved."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from render import draw as _draw
class MV_F0617:
    def __init__(self):
        row=next(r for r in map(json.loads,(ROOT/'candidates.jsonl').read_text().splitlines()) if r['id']=='MV_F0617')
        self.__dict__.update(row)
        self.query=self.question
    def draw(self,num=0,output_path=None):
        return _draw(self.id,output_path)
if __name__=='__main__':
    print(MV_F0617().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
