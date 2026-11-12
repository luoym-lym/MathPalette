"""Draw a formal question through its single Python class and shared protocol."""
from pathlib import Path
import argparse
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[1]
BRANCHES=('Analytics','PlaneGeometry','SolidGeometry')


def load_question(branch,qid):
    if branch not in BRANCHES:
        raise ValueError('Unknown branch')
    rows=[json.loads(line) for line in (ROOT/branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    row=next((r for r in rows if r['id']==qid),None)
    if row is None:
        raise ValueError('Unknown formal question')
    path=(ROOT/branch/row['script']).resolve()
    if not path.is_relative_to(ROOT/branch):
        raise ValueError('Invalid question class path')
    spec=importlib.util.spec_from_file_location('_draw_'+qid,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return getattr(module,qid)()


def draw_question(branch,qid,output_path=None,variant=None):
    from dataset_tools.catalog import assert_formal_dataset
    assert_formal_dataset(ROOT/branch/'dataset.jsonl')
    question=load_question(branch,qid)
    image=question.draw(output_path,variant=variant)
    return {'question_id':qid,'branch':branch,'image_path':str(image),'protocol_version':'2.0.0'}


if __name__=='__main__':
    import sys
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('branch',choices=BRANCHES);parser.add_argument('question_id')
    parser.add_argument('--output',type=Path);parser.add_argument('--variant')
    args=parser.parse_args()
    print(json.dumps(draw_question(args.branch,args.question_id,args.output,args.variant),ensure_ascii=False))
