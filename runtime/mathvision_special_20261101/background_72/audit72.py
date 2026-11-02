from tools72 import *
import shutil

def snapshots():
    paths = [PROJECT/'AGENTS.md', PROJECT/'MATHPALETTE_PROTOCOL.md']
    paths += [PROJECT/BRANCH/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/README.md','workbench/agent_prompt.md','workbench/plugin.schema.json']]
    paths += [BASE/p for p in ['background_72_brief.txt','background_72_assignment.json','background_60_brief.txt','background_60_assignment.json','continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','selection60_61_parent_eligibility.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']]
    paths += list((BASE/'background_60/readin_snapshots').glob('*'))
    manifest=[]
    for p in paths:
        if not p.is_file():
            manifest.append({'source':str(p),'exists':False});continue
        h=sha(p); dest=HERE/'snapshots'/(p.name+'.'+h+'.snapshot')
        dest.parent.mkdir(exist_ok=True)
        if not dest.exists():shutil.copyfile(p,dest)
        assert sha(dest)==h
        manifest.append({'source':str(p),'sha256':h,'bytes':p.stat().st_size,'snapshot':str(dest)})
    write(HERE/'initial_snapshot_manifest.json',manifest)
    a=read(BASE/'background_60_assignment.json');b=read(BASE/'background_72_assignment.json')
    result={q['question_id']:next(x for x in a['questions'] if x['question_id']==q['question_id'])==q['source_assignment_question'] for q in b['questions']}
    write(HERE/'source_assignment_binding.json',{'source_full_json_parsed':True,'selected_entries_equal_complete_read_72_embedding':result,'source_scope_overridden':IDS})
    assert all(result.values())
    print('snapshots',len(manifest),'source entries exact',result,flush=True)

def old_inventory():
    selected=[]
    for parent,dirs,files in os.walk(BASE):
        d=Path(parent)
        if d==HERE:dirs[:]=[];continue
        rel=d.relative_to(BASE).parts
        if rel and rel[0].startswith('background_') and rel[0][11:].isdigit() and int(rel[0][11:])>=67:
            dirs[:]=[];continue
        if any(q in d.parts for q in IDS+RELATED):
            selected += [d/f for f in files]
    selected += [BASE/'background_19/sliding_bar_proof.json']
    selected += [BASE/'independent_review'/p/'independent_review.json' for p in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']]
    result=[]
    for p in sorted(set(selected)):
        if not p.is_file():continue
        row={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
        if p.suffix=='.json':
            obj=read(p)
            row['full_json_parse']=True
            row['keys']=list(obj) if isinstance(obj,dict) else ['list']
            if p.name.endswith('_response.json'):
                row['raw_response']=True
                row['finish_reasons']=[c.get('finish_reason') for c in obj.get('choices',[])]
                dest=HERE/'old_raw'/p.relative_to(BASE)
                write(dest,obj)
            del obj;gc.collect()
        result.append(row)
    write(HERE/'old_history_inventory.json',result)
    print('old files',len(result),'raw response files',sum(bool(r.get('raw_response')) for r in result),flush=True)
    for q in IDS+RELATED:
        rowsq=[r for r in result if q in Path(r['path']).parts]
        print(q, len(rowsq), 'raw',sum(bool(r.get('raw_response')) for r in rowsq),flush=True)

if __name__=='__main__':
    if sys.argv[1]=='snapshots':snapshots()
    elif sys.argv[1]=='old':old_inventory()
