from review_bootstrap import *
import json
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
reports = {
    '295': BASE/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
    '342': BASE/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json',
    '233': BASE/'independent_review/Plane233_two_U_partial_partition_binding/independent_review.json',
    '192': BASE/'independent_review/Plane192_v03/independent_review.json',
}
mode=sys.argv[1]
if mode=='keys':
    for key,p in reports.items(): print(key, json.dumps(list(read(p)),ensure_ascii=False))
elif mode=='old':
    for i in (1,2,3):
        d=BASE/f'plane_explore/Plane192/v{i:02d}'
        print('OLD DESIGN',i)
        for name in ['design.json','plugin.json']:
            print(name, json.dumps(read(d/name),ensure_ascii=False))
        for p in sorted(d.glob('tests/*/run_??_response.json')):
            print(str(p.relative_to(BASE)), read(p)['choices'][0]['message']['content'])
elif mode in reports:
    p=reports[mode]; v=read(p)
    keys=sys.argv[2:]
    print(str(p));print(json.dumps({k:v[k] for k in keys if k in v},ensure_ascii=False,indent=2))
