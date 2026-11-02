from tools33 import *
from itertools import combinations
from math import gcd

def history():
    records={}
    for q in ASSIGNED:
        paths=[]
        for unit in BASE.glob('background_*'):
            if unit==HERE or not unit.is_dir(): continue
            folder=unit/q
            if folder.exists(): paths += [p for p in folder.rglob('*') if p.is_file()]
        paths += [p for p in (BASE/'plane_mid').glob(q+'*') if p.is_file()]
        paths += [p for p in (BASE/'root_explore'/q).rglob('*') if p.is_file()] if (BASE/'root_explore'/q).exists() else []
        content=[]
        for p in sorted(paths):
            if p.suffix=='.json':
                data=read(p)
                if p.name in ('assessment.json','primary_prescreen.json','source_primary_audit.json','primary_review.json','design.json','manual_final_review.json'):
                    clean={k:v for k,v in data.items() if k not in ('eligibility_recheck','source_files')}
                    content.append({'path':str(p.relative_to(ROOT)),'content':clean})
                    print(q,p.name,json.dumps(clean,ensure_ascii=False),flush=True)
        designs=[str(p.relative_to(ROOT)) for p in paths if p.name=='design.json']
        replies=[str(p.relative_to(ROOT)) for p in paths if p.name.endswith('_response.json')]
        checkpoint_extract=[]
        for unit in ['background_10','background_18','background_21']:
            for name in ['checkpoint.json','checkpoint_initial_snapshot.json','assessment_scope.json']:
                p=BASE/unit/name
                if not p.exists():continue
                d=read(p)
                def walk(v,path=''):
                    if isinstance(v,dict):
                        if v.get('question_id',v.get('id'))==q:
                            clean={k:x for k,x in v.items() if k not in ('eligibility_recheck','eligibility','authoritative_state_hashes','source_files','formal_record')}
                            checkpoint_extract.append({'path':str(p.relative_to(ROOT)),'json_path':path,'content':clean})
                        else:
                            for k,x in v.items(): walk(x,path+'/'+k)
                    elif isinstance(v,list):
                        for i,x in enumerate(v):walk(x,path+'/'+str(i))
                walk(d)
        records[q]={'read_previous_question_files':{str(p.relative_to(ROOT)):file_hash(p) for p in paths},'previous_primary_records':content,'same_question_design_paths':designs,'same_question_full_response_paths':replies,'checkpoint_entries':checkpoint_extract,
                    'no_old_two_hit_to_queue':not designs,'history_limit':'Old formal and PNG files were also compared against fresh current snapshots. Historical mutable progress hashes remain diagnostic.'}
        print(q,'old designs',designs,'replies',replies,'checkpoint entries',len(checkpoint_extract),flush=True)
    write(HERE/'previous_history_audit.json',records)

def features():
    for q in ASSIGNED:
        ctx=read(HERE/q/'context.json');sc=read(HERE/q/'source_scene_snapshot.json')
        print('\n',q,'points',json.dumps(sc.get('points'),ensure_ascii=False),flush=True)
        print('objects',json.dumps([{'id':o['id'],'kind':o.get('kind'),'styleable':o.get('styleable'),'geometry':o.get('geometry')} for o in ctx['objects']],ensure_ascii=False),flush=True)

def read_lessons():
    for q,v in [('Plane295','inner_ear_shoulder_correspondence'),('Plane342','quarterturn_wedge_edge_binding')]:
        p=BASE/'independent_review'/f'{q}_{v}'/'independent_review.json';d=read(p)
        # Read exact full report, and show all primary semantic/mathematical conclusions.
        excluded=['exact_raw_full_final_preset_profile_bindings','two_hit_evidence','current_authoritative_eligibility','reviewed_source_evidence_hashes','exact_frozen_hashes','controls_and_effect_limits']
        print(json.dumps({k:v for k,v in d.items() if k not in excluded},ensure_ascii=False,separators=(',',':')),flush=True)
    
if __name__=='__main__':
    {'history':history,'features':features,'lessons':read_lessons}[sys.argv[1]]()
