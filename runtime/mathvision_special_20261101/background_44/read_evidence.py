import task_env
from task_env import OWN, BASE, PROJECT
import json, sys
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def emit(tag,x): print(tag, json.dumps(x,ensure_ascii=False,separators=(',',':')))

mode=sys.argv[1] if len(sys.argv)>1 else ''
def compact_geometry(s):
    pts=s.get('points',{})
    out={k:v for k,v in s.items() if k not in ['points','objects']}
    obs=[]
    for ob in s.get('objects',[]):
        ob=dict(ob)
        if 'points' in ob:
            xy=[pts.get(p,p) if isinstance(p,str) else p for p in ob['points']]
            ob['points']=xy if len(xy)<20 else {'count':len(xy),'first3':xy[:3],'last3':xy[-3:]}
        obs.append(ob)
    out['objects']=obs
    return out

if mode=='review':
    r=read(BASE/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json')
    fields=sys.argv[2:] or ['independent_unique_answer_proof','actual_image_inspection','per_marker','marker_group_assessments','human_semantics']
    for k in fields:emit(k,r[k])
elif mode=='old':
    for qid in sys.argv[2:]:
        inventory=read(OWN/qid/'old_file_inventory.json')
        for item in inventory:
            p=Path(item['path'])
            if p.name in ['assessment.json','prescreen.json','prescreen_assessment.json','design.json','primary_review.json','primary_math_audit.json','primary_visual.json','manual_final_review.json','manual_finals_and_binding_audit.json']:
                print('FILE',p)
                try:emit('CONTENT',read(p))
                except Exception as e:print('MALFORMED',type(e).__name__,str(e),'BYTES',item['bytes'],'SHA',item['sha256'])
        for item in inventory:
            p=Path(item['path'])
            if p.name.endswith('_response.json'):
                print('FULLRAW',p,'SHA',item['sha256'])
                try:emit('CONTENT',read(p))
                except Exception as e:print('MALFORMED_PRESERVED',type(e).__name__,str(e),'BYTES',item['bytes'])
elif mode=='scene':
    for qid in sys.argv[2:]:
        row=read(OWN/qid/'formal_record.json')
        emit('QUESTION',row['question'])
        for p in [PROJECT/'PlaneGeometry'/row['scene'],PROJECT/'PlaneGeometry'/next(x for x in row['runtime_dependencies'] if x.endswith('/scene.json'))]:
            s=read(p)
            print('FILE',p)
            if len(s.get('points',{}))>100:
                s['points']={'count':len(s['points']),'note':'Dense samples fully read by script; source geometry reviewed separately.'}
            emit('SCENE',s)
        c=read(OWN/qid/'context.json')
        emit('OBJECTS',c['objects']);emit('SNAPS',c['snap_points'] if len(c['snap_points'])<50 else {'count':len(c['snap_points'])})
        for t in c['canvas'].get('targets',[]):
            emit('TARGET',{k:v for k,v in t.items() if k not in ['samples','partial_paths','paths']})
            for p in t.get('partial_paths',[]):
                emit('PATH',{k:v for k,v in p.items() if k!='samples'})
elif mode=='geometry':
    for qid in sys.argv[2:]:
        row=read(OWN/qid/'formal_record.json')
        emit(qid+' question',row['question'])
        p=PROJECT/'PlaneGeometry'/next(x for x in row['runtime_dependencies'] if x.endswith('/scene.json'))
        emit(qid+' frozen_native_scene',compact_geometry(read(p)))
        c=read(OWN/qid/'context.json')
        for t in c['canvas'].get('targets',[]):
            emit('TARGET',{k:t[k] for k in ['id','kind','color','linewidth_pt','linestyle'] if k in t})
            for p in t.get('partial_paths',[]):
                emit('PATH',{k:v for k,v in p.items() if k!='samples'})
