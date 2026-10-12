"""Native deterministic redraw of staged MathVerse problem 279. Importing does not write files."""
from pathlib import Path
import argparse
import json
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/"renderer"))
from common_renderer import draw

class MathVerse279:
    def __init__(self):
        record=json.loads((ROOT/"candidate.json").read_text(encoding="utf-8"))
        self.id=record["id"]
        self.source_dataset=record["source_dataset"]
        self.query=record["question"]
        self.answer=record["answer"]
        self.answer_type=record["answer_type"]
        self.choices=record.get("choices")
        self.subject="PlaneGeometry"
        self.level=None
    def redraw(self,output_path=None):
        return draw(ROOT/"scene.json",output_path or ROOT/"redrawn.png")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_path",nargs="?",default=None,help="Optional PNG or SVG destination; defaults to this candidate's redrawn.png")
    args=parser.parse_args()
    MathVerse279().redraw(args.output_path)
