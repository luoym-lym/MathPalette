from env41 import *
tracked={}
def track(p):
    if p.is_file():tracked[str(p.relative_to(ROOT))]=file_hash(p)
for q in ASSIGNED:
    previous=[]
    for group in ('background_20','background_21','plane_explore'):
        d=BASE/group/q
        if d.exists():
            for p in sorted(d.rglob('*')):
                if p.is_file():track(p)
                if p.name in ('assessment.json','primary_prescreen.json','source_primary_audit.json','design.json','plugin.json'):
                    previous.append({'path':str(p.relative_to(ROOT)),'content':read(p)})
    bindings=[]
    for p in BASE.rglob('binding.json'):
        if HERE in p.parents:continue
        b=read(p)
        if b.get('question_id')==q:
            bindings.append({'path':str(p.relative_to(ROOT)),'content':b})
            for f in p.parent.iterdir():track(f)
    relevant_checkpoint=[]
    def find(v,path):
        if isinstance(v,dict):
            if v.get('question_id')==q or v.get('id')==q:return [{'location':path,'content':v}]
            return sum((find(x,path+'/'+k) for k,x in v.items()),[])
        if isinstance(v,list):return sum((find(x,path+'/'+str(i)) for i,x in enumerate(v)),[])
        return []
    for p in [BASE/'plane_explore/checkpoint.json',BASE/'plane_explore/designs.json',BASE/'exploration_report.json',BASE/'background_20/checkpoint.json',BASE/'background_21/checkpoint.json']:
        if p.exists():relevant_checkpoint+=find(read(p),str(p.relative_to(ROOT)))
    hist={'question_id':q,'prior_files':previous,'all_found_bindings':bindings,'checkpoint_and_summary_matches':relevant_checkpoint,'rule':'All old evidence read-only; answer tails are not grades.'}
    write(HERE/q/'prior_history_inventory.json',hist)
    print(json.dumps({'qid':q,'prior_assessments':[{ 'path':v['path'],'status':v['content'].get('status'),'source_math_observation':v['content'].get('source_math_observation'),'prescreen_reason':v['content'].get('prescreen_reason',v['content'].get('reason'))} for v in previous if 'assessment' in v['path'] or 'prescreen' in v['path']],'binding_paths':[v['path'] for v in bindings]},ensure_ascii=False))
    e=read(HERE/q/'eligibility_start.json')
    for p in e['frozen_content']['files']:
        track((ROOT/'PlaneGeometry'/p).resolve())
    for p in read(HERE/q/'adapter_input_hashes.json'):track(ROOT/p)
    m=read(HERE/q/'context.json');s=read(HERE/q/'source_scene_snapshot.json')
    print(json.dumps({'qid':q,'scene':s,'object_ids':[v['id'] for v in m['objects']]},ensure_ascii=False))
for p in [ROOT/'provenance/approvals.json',ROOT/'PlaneGeometry/dataset.jsonl',ROOT/'PlaneGeometry/special_variant/accepted_index.jsonl',ROOT/'PlaneGeometry/special_variant/collected_index.jsonl',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py',BASE/'background_41_brief.txt',BASE/'background_41_assignment.json',BASE/'annotation_semantics_lesson_plane242_r24_20261102.json',BASE/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json']:track(p)
write(HERE/'source_hashes_before.json',tracked)
