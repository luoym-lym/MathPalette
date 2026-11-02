from local_env import *
import json, hashlib, base64, gc, argparse

ap=argparse.ArgumentParser()
ap.add_argument('mode',choices=['refs','history'])
ap.add_argument('--qid')
args=ap.parse_args()
if args.mode=='refs':
    records=[]
    manifest=read_json(TASK/'reference_manifest.json')
    for qid, m in manifest.items():
        root=TASK/m['directory']
        ref=read_json(root/'reference.json')
        plugin=read_json(root/'C01.json')
        recipes=read_json(root/'recipes.json')
        checks={'png_match':sha(root/'C01.png')==m['png_sha256'],'plugin_match':sha(root/'C01.json')==m['plugin_sha256'],
                'recipe_params_equal':recipes[0]['params']==plugin['params'],'reference_recipe_equal':ref['recipes']==recipes,
                'accepted_recipe_equal':ref['accepted_entries']==recipes}
        for rel, expected in ref['frozen_source_files_sha256'].items():
            assert sha(PROJECT/rel)==expected, rel
        for leaf, entry in ref['copied_files'].items():
            assert sha(root/leaf)==entry['sha256']
        assert all(checks.values()), checks
        entry={'id':qid,'all_files':[{'path':str(f),'sha256':sha(f)} for f in root.iterdir() if f.is_file()],
               'checks':checks,'formal_record':ref['formal_record'],'approval':ref['approval'],
               'plugin':plugin,'recipe_metadata':{k:v for k,v in recipes[0].items() if k not in plugin},
               'collection':ref['collection'],'collected_entries':ref['collected_entries']}
        records.append(entry)
        if qid not in ['Solid142','Solid167']:
            print(json.dumps(entry,ensure_ascii=False,indent=2))
    save(OWN/'reference_read_inventory.json',records,True)
else:
    h=read_json(TASK/'history_index.json')
    q=next(x for x in h['questions'] if x['question_id']==args.qid)
    root=OWN/args.qid
    save(root/'history_index_excerpt.json',q)
    paths=set(q['other_scoped_history_file_references']+q['additional_math_manual_history_references'])
    for x in q['independent_review_references']:
        if isinstance(x,str): paths.add(x)
        elif isinstance(x,dict) and 'path' in x: paths.add(x['path'])
    for d in q['designs']:
        paths.add(d['design_path'])
        for f in (PROJECT/d['directory']).rglob('*'):
            if f.is_file(): paths.add(f.relative_to(PROJECT).as_posix())
    inventory=[]; semantic=[]; responses=[]
    for rel in sorted(paths):
        f=PROJECT/rel
        info={'path':rel,'sha256':sha(f),'size':f.stat().st_size}
        if f.suffix=='.json':
            data=read_json(f)
            if f.name=='request.json':
                for message in data['messages']:
                    if isinstance(message['content'],list):
                        for item in message['content']:
                            if item['type']=='image_url':
                                raw=base64.b64decode(item['image_url']['url'].split(',',1)[1])
                                info['embedded_image_sha256']=hashlib.sha256(raw).hexdigest()
                                del raw
                                item['image_url']['url']='[decoded SHA recorded; original request retained read-only]'
                info['request_without_base64']=data
            elif f.name.endswith('_response.json'):
                responses.append({'path':rel,'sha256':info['sha256'],'complete_raw_response':data})
            elif f.name in ['design.json','primary_prescreen.json','assessment.json','primary_review.json','source_audit.json','refinement_assessment.json','design_difference_audit.json'] or 'manual' in f.name or 'independent_review' in rel:
                semantic.append({'path':rel,'content':data})
            info['fully_parsed']=True
            del data
        inventory.append(info)
        gc.collect()
    save(root/'history_files_read.json',inventory)
    save(root/'history_semantic_full.json',semantic)
    save(root/'history_raw_responses_full.json',responses)
    print(json.dumps({'question_id':args.qid,'files':len(inventory),'designs':len(q['designs']),
                      'transport_groups':len(q['all_saved_transport_groups_for_question']),
                      'semantic':semantic,'responses':responses},ensure_ascii=False,indent=2))
