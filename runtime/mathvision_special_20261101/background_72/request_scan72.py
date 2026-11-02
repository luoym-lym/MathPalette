from tools72 import *
import base64

targets={sha(p):str(p) for q in ('Plane335','Plane355') for p in (HERE/q).glob('*/candidate.png')}
checked=[];matches=[];errors=[]
for parent,dirs,files in os.walk(BASE):
    directory=Path(parent)
    if directory==HERE:dirs[:]=[];continue
    rel=directory.relative_to(BASE).parts
    if rel and rel[0].startswith('background_') and rel[0][11:].isdigit() and int(rel[0][11:])>=67:
        dirs[:]=[];continue
    for leaf in files:
        if 'request' not in leaf.lower() or not leaf.endswith('.json'):continue
        p=directory/leaf
        try:
            obj=read(p);found=[]
            def visit(value):
                if isinstance(value,dict):
                    for v in value.values():visit(v)
                elif isinstance(value,list):
                    for v in value:visit(v)
                elif isinstance(value,str) and value.startswith('data:image/png;base64,'):
                    raw=base64.b64decode(value.split(',',1)[1]);h=hashlib.sha256(raw).hexdigest();del raw
                    found.append(h)
            visit(obj)
            checked.append({'path':str(p),'sha256':sha(p),'embedded_png_sha256':found})
            for h in found:
                if h in targets:matches.append({'request':str(p),'candidate':targets[h],'png_sha256':h})
            del obj,found;gc.collect()
        except (ValueError,UnicodeError) as err:
            errors.append({'path':str(p),'type':type(err).__name__,'error':str(err),'unrelated_old_file_preserved':True})
write(HERE/'historic_exact_PNG_request_scan.json',{'finished_at':now(),'target_new_images':targets,'scanned_requests':checked,'exact_matches':matches,'parse_errors':errors,'own_new_requests_excluded':True,'concurrent_replacement_units_67_and_above_excluded':True,'no_global_zero_call_claim_for_any_other_image':True,'streamed_one_file_at_a_time_released_base64':True})
assert not matches,matches
print('historic request files',len(checked),'embedded PNGs',sum(len(r['embedded_png_sha256']) for r in checked),'new PNG exact historic matches',len(matches),'unrelated parse errors',len(errors),flush=True)
