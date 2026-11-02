from tools39 import *
manifest={};evidence={};history={}
for q in ASSIGNED:
    ps=[]
    for p in BASE.rglob('*'):
        if not p.is_file() or p.is_relative_to(HERE):continue
        if q in p.parts:
            if p.suffix in ('.json','.jsonl','.png','.txt','.py','.bin','.jpg'):
                manifest[str(p.relative_to(ROOT))]=file_hash(p);ps.append(p)
    history[q]={'files':[str(p.relative_to(ROOT)) for p in ps],'designs':[],'full_raw_responses':[]}
    for p in ps:
        if p.name=='design.json':history[q]['designs'].append({'path':str(p),'content':read(p)})
        if p.name.endswith('_response.json'):
            data=read(p);history[q]['full_raw_responses'].append({'path':str(p),'content':data})
    m=read(HERE/q/'context.json')
    print(q)
    for o in m['objects']:
        if q=='Plane323' and (o['kind']=='segment'):continue
        if q=='Plane280' and not o['id'].startswith('thick'):continue
        print(json.dumps({'id':o['id'],'kind':o['kind'],'geometry':o['geometry']},ensure_ascii=False))
    if q=='Plane280':print('snap_points',json.dumps(m['snap_points']))
for p in [BASE/'background_11/checkpoint.json',BASE/'background_12/checkpoint.json',BASE/'background_20/checkpoint.json',BASE/'background_04/checkpoint.json',BASE/'background_09/checkpoint.json']:
    manifest[str(p.relative_to(ROOT))]=file_hash(p)
    def find(v):
        if isinstance(v,dict):
            q=v.get('question_id')
            if q in ASSIGNED:
                history[q].setdefault('checkpoint_entries',[]).append({'path':str(p),'content':v});print('HISTORY',q,json.dumps(v,ensure_ascii=False)[:5000]);return
            for x in v.values():find(x)
        elif isinstance(v,list):
            for x in v:find(x)
    find(read(p))
for p in [BASE/'annotation_semantics_lesson_plane242_r24_20261102.json',BASE/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json',BASE/'annotation_semantics_lessons_20261102.json',BASE/'background_39_brief.txt',BASE/'background_39_assignment.json',BASE/'continuation_brief.txt']:
    data=p.read_bytes();manifest[str(p.relative_to(ROOT))]=file_hash(p)
    if p.suffix=='.json':evidence[str(p.relative_to(ROOT))]=read(p)
write(HERE/'history_read_audit.json',{'created_at':now(),'all_scoped_history_read_in_full':True,'old_Plane276':'E preset; full D60/D60 => MISS forever','old_Plane280':'A preset; zero calls; pre-API rejected due target membership cue','old_native_PNGs_viewed':True,'history':history,'scoped_preexisting_hashes':manifest,'lessons_full_machine_read':list(evidence),'lesson_application':'Physical material printing assessed for each actual task. No blanket color ban for numerical geometry; no legends or text repair.'})
write(HERE/'mandatory_lessons_snapshot.json',evidence)
