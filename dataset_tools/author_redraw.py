"""Compatibility CLI; all originals use the unified question class."""
from pathlib import Path
import sys
if str(Path(__file__).resolve().parents[1]) not in sys.path:
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from dataset_tools.draw_question import draw_question

def main():
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question_id');parser.add_argument('output',type=Path)
    args=parser.parse_args()
    branch='PlaneGeometry' if args.question_id.startswith('Plane') else 'SolidGeometry' if args.question_id.startswith('Solid') else None
    if branch is None:parser.error('Expected Plane or Solid ID')
    print(json.dumps(draw_question(branch,args.question_id,args.output)))

if __name__=='__main__':main()
