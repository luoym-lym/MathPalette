"""Record a user's explicit approval of a named frozen question, in any branch."""
from pathlib import Path
import sys
import argparse
import json

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
from dataset_tools.geometry_review import approve,registration_for,read_registry,BRANCHES


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("branch",choices=sorted(BRANCHES))
    parser.add_argument("qid")
    parser.add_argument("--instruction",required=True)
    args=parser.parse_args()
    review=approve(args.branch,args.qid,args.instruction)
    print(json.dumps({k:review[k] for k in ["id","branch","approved_at_utc","content_sha256"]},indent=2))
