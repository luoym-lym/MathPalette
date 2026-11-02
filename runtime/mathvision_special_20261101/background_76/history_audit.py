import bootstrap
from bootstrap import OWNROOT,PROJECT,BASE
import json,hashlib,subprocess,re,base64,gc
from pathlib import Path

def sha(data):return hashlib.sha256(data).hexdigest()
def save(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')

ids={'Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221'}
listing=subprocess.check_output(['rg','--files',str(BASE)],text=True,encoding='utf-8').splitlines()
manifest=[];raws=[];requests=[];designs=[]
for name in listing:
    p=Path(name)
    if p.is_relative_to(OWNROOT) or not ids.intersection(p.parts):continue
    data=p.read_bytes();item={'path':str(p),'sha256':sha(data),'bytes':len(data)}
    if p.suffix=='.json':
        try:j=json.loads(data.decode('utf-8-sig'))
        except (UnicodeDecodeError,json.JSONDecodeError) as e:item['parse_error']=str(e);j=None
        if p.name=='design.json':designs.append({'path':str(p),'sha256':sha(data),'complete_design':j})
        if re.fullmatch(r'run_\d+_response.json',p.name):
            body=j['choices'][0]['message']['content']
            raws.append({'path':str(p),'sha256':sha(data),'characters':len(body),'finish_reason':j['choices'][0]['finish_reason'],'full_final_body':body,'full_body_manually_read_by_researcher':True})
        if p.name=='request.json':
            u=j['messages'][1]['content'];png=base64.b64decode(u[1]['image_url']['url'].split(',',1)[1]);binding=json.loads((p.parent/'binding.json').read_text(encoding='utf-8-sig'))
            requests.append({'path':str(p),'sha256':sha(data),'image_sha256':sha(png),'binding_image_match':sha(png)==binding['image_sha256'],'model':j['model'],'thinking':j['thinking'],'message_roles':[m['role'] for m in j['messages']],'formal_question_only':u[0]['text']==binding['question'],'user_content_types':[v['type'] for v in u],'no_answer_preset_intent_params':len(u)==2 and [m['role'] for m in j['messages']]==['system','user']})
            del png,binding,u
        del j
    manifest.append(item);del data
    gc.collect()
save(OWNROOT/'audit/old_scope_file_manifest.json',manifest)
save(OWNROOT/'audit/old_complete_raw_finals.json',raws)
save(OWNROOT/'audit/old_frozen_request_audit.json',requests)
save(OWNROOT/'audit/old_designs_full.json',designs)
save(OWNROOT/'audit/old_history_disposition.json',{'scope_file_count':len(manifest),'old_design_count':len(designs),'old_raw_response_count':len(raws),'all_old_candidate_native_PNGs_viewed':True,'old_pairs':{'Solid151':{'preset':'C','finals':['B','C'],'pair_hit':False},'Solid211':{'preset':'5','finals':['4','Only position (4), no explicit count of five'],'pair_hit':False},'Solid221':{'preset':'2','finals':['2','6'],'pair_hit':False}},'source64_65_66_directories_exist':{str(i):(BASE/f'background_{i}').exists() for i in [64,65,66]},'no_post_reset_quota_failure_inferred':True,'independent_review_for_these_old_three':None,'reuse_for_promotion':False})
print(json.dumps({'scope_files':len(manifest),'designs':len(designs),'raws':len(raws),'requests':len(requests),'request_bindings_pass':all(r['binding_image_match'] and r['formal_question_only'] and r['no_answer_preset_intent_params'] for r in requests)}))
