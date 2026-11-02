from common38 import *
import base64,io,math
import numpy as np
from PIL import Image
from partial_style import portion
FINALS={'Plane188':['18','18'],'Plane224':['12','77'],'Plane229':['44','44'],'Plane250':['39','19'],'Plane254':['B','B'],'Plane256':['0','50'],'Plane258':['E','C']}
NOTES={'Plane224':['Final12 is wrong but not preset77/9.','Long answer revises54/57 and ultimately derives77; final77, not preset77/9.'], 'Plane258':['Body1600 then explicit terminal approximate1680 and E; presetB400 is MISS.','Body240 and hypothetical changed smallest-side35 lead420 then terminal C; presetB400 is MISS. No credit for incidental400 option mention.'], 'Plane256':['Final0 cannot be relabelled to old different-image preset0. New frozen preset25 remains MISS.','Final50 correct although narrative swaps which of75/100 is leftmost in T; new preset25 MISS.']}
reports=[]
for q in QIDS:
    candidates=list((TASK/q).glob('r38_*/design.json'));assert len(candidates)==1
    dp=candidates[0];f=dp.parent;d=read(dp);plugin=read(f/'plugin.json');context=read(f/'context.json');imagebytes=(f/'candidate.png').read_bytes()
    assert sha(f/'candidate.png')==d['candidate_png_sha256']
    assert (f/'repeat.png').read_bytes()==imagebytes
    currentpaths=paths(q,sorted({a['target'] for a in plugin['params']['actions'] if a['type']=='set_object_style'}))
    assert currentpaths==read(f/'marker_path_bindings.json')
    renderer=PluginRenderer(CONFIG,AD,{q:context});assert renderer.normalize(plugin)==plugin
    selected=[];s=AD.scene(q)
    try:
        s.fig.canvas.draw();mask=np.zeros((768,768),bool)
        arr=np.array(Image.open(io.BytesIO(imagebytes)).convert('RGB'))
        orig=np.array(Image.open(AD.original_paths[q]).convert('RGB'))
        for i,a in enumerate(plugin['params']['actions']):
            controls=[]
            if a['type']=='add_point':
                xy=np.asarray([a['xy']]);margin=8
                assert any(np.allclose(a['xy'],p['xy'],atol=1e-10,rtol=0) for p in context['snap_points'])
            else:
                ps=object_paths(s,a['target']);iv=a.get('interval')
                for p in ps:
                    if iv and p['id']!=iv['path_id']:continue
                    n=len(p['segments'])
                    if iv:assert p['sha256']==iv['path_sha256'] and not iv['wrap']
                    for j,seg in enumerate(p['segments']):
                        start=max(0,iv['start']*n-j) if iv else 0
                        end=min(1,iv['end']*n-j) if iv else 1
                        if end>start:controls.append(portion(seg['control'],start,end).tolist())
                xy=np.concatenate([np.asarray(c) for c in controls]);margin=4
            pix=s.ax.transData.transform(xy);pix[:,1]=768-pix[:,1]
            x0,y0=np.floor(pix.min(0)-margin).astype(int);x1,y1=np.ceil(pix.max(0)+margin).astype(int)
            x0=max(x0,0);y0=max(y0,0);x1=min(x1+1,768);y1=min(y1+1,768)
            mask[y0:y1,x0:x1]=True
            rgb=np.array(tuple(bytes.fromhex(a['color'][1:])),float);crop=arr[y0:y1,x0:x1].astype(float)
            exact=int(np.all(crop==rgb,axis=2).sum())
            hue=rgb-rgb.mean();v=crop-crop.mean(axis=2,keepdims=True);mag=np.linalg.norm(v,axis=2)
            cos=np.sum(v*hue,axis=2)/np.maximum(mag*np.linalg.norm(hue),1e-9)
            visible=int(((cos>.99)&(mag>15)).sum());assert visible>0,(q,i,a)
            selected.append(dict(action_index=i,action=a,selected_fullprecision_controls=controls if a['type']=='set_object_style' else [a['xy']],native_pixel_bounds=[int(x0),int(y0),int(x1),int(y1)],exact_color_pixels_in_marker_bounds=exact,chromatic_pixels_in_marker_bounds=visible,visibility_caveat='Original overlapping black stroke leaves only anti-aliased colored fringe; visible native-size hue, no exact palette pixels.' if exact==0 else None,role=d['marker_roles'][i]['role']))
        changed=np.any(orig!=arr,axis=2);outside=int((changed & ~mask).sum())
        ys,xs=np.where(changed & ~mask)
        extra=[dict(x=int(x),y=int(y),original=orig[y,x].tolist(),candidate=arr[y,x].tolist()) for y,x in zip(ys,xs)]
        assert all(len(set(p['original']))==1 and len(set(p['candidate']))==1 for p in extra),(q,extra)
    finally:s.close()
    write(f/'native_marker_audit_v3.json',dict(question_id=q,per_marker=selected,changed_pixels=int(changed.sum()),changes_outside_marker_neighborhoods=outside,unmarked_grayscale_antialias_differences=extra,original_paths_bound_exactly=True,all_marks_visible=True,original_black_path_stroke_unchanged=q=='Plane258' and all(a['type']=='add_point' for a in plugin['params']['actions']),note='Exact/hue pixel visibility supplements actual native PNG inspection. Partial-style polygon stroke replacement can make minor grayscale antialias differences at untouched edges; exact coordinates listed without hiding them or claiming all pixels outside markers equal. Frozen image unchanged; no API retry.'))
    bs=list(f.glob('tests/*/binding.json'));assert len(bs)==1
    bpath=bs[0];b=read(bpath);t=bpath.parent;request=read(t/'request.json')
    checks=dict(image=sha(f/'candidate.png')==b['image_sha256'],design=sha(dp)==b['design_sha256'],snapshot=(t/'design_snapshot.json').read_bytes()==dp.read_bytes(),request=sha(t/'request.json')==b['request_body_sha256'],record=canon(AD.records[q])==b['question_record_sha256'],formal_question=b['question']==AD.records[q]['question'],preset=b['expected_wrong_answer']==d['expected_wrong_answer'],model=request['model']=='mimo-v2.6-flash',thinking=request['thinking']=={'type':'disabled'},no_tokens_or_timeout=not any(k in request for k in ['max_tokens','max_completion_tokens','timeout']),png_embedded=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==imagebytes,only_question_png=list(request)==['model','stream','thinking','messages'] and request['messages']==[{'role':'system','content':b['system_prompt']},{'role':'user','content':[{'type':'text','text':AD.records[q]['question']},request['messages'][1]['content'][1]]}])
    assert all(checks.values()),(q,checks)
    manual=[]
    for i,path in enumerate(sorted(t.glob('run_??_response.json'))):
        raw=read(path);job=read(path.with_name(path.name.replace('_response','')))
        assert raw['choices'][0]['finish_reason']=='stop' and job['status']=='completed' and job['response_sha256']==sha(path)
        assert all(job[k]==b[k] for k in ['image_sha256','design_sha256','request_body_sha256'])
        if q in FINALS:
            final=FINALS[q][i]
            manual.append(dict(run_index=i+1,raw_response_path=str(path),raw_response_sha256=sha(path),full_final_text=raw['choices'][0]['message']['content'],entire_raw_response_manually_read=True,final_answer=final,matches_predeclared_wrong_answer=final==d['expected_wrong_answer'],specific_manual_note=NOTES.get(q,['Clear terminal answer; no preset hit.']*2)[i],finish_reason='stop',status='completed'))
    if q in FINALS:
        assert len(manual)==2
        if not (f/'manual_final_review.json').exists():write(f/'manual_final_review.json',dict(question_id=q,variant_id=d['variant_id'],expected_wrong_answer=d['expected_wrong_answer'],read_at=now(),runs=manual,two_target_hits=False,decision='MISS; preserve preset unchanged',original_controls='No original control binding found in existing scoped history; no new controls requested or repeated.',limits='No claim of annotation causality, incremental effect or per-marker necessity from these responses.'))
    write(f/'evidence_binding_audit_v3.json',dict(question_id=q,checked_at=now(),checks=checks,started_runs=len(list(t.glob('run_??_started.json'))),completed_responses=len(list(t.glob('run_??_response.json'))),design_timestamp_precedes_first_call=dp.stat().st_mtime_ns<(t/'run_01_started.json').stat().st_mtime_ns,all_artifacts_below_unit=all(p.resolve().is_relative_to(TASK) for p in f.rglob('*')),binding_path=str(bpath)))
    reports.append(dict(question_id=q,variant_id=d['variant_id'],preset=d['expected_wrong_answer'],manual_finals=FINALS.get(q),checks=checks,completed=len(list(t.glob('run_??_response.json')))))
write(TASK/'verification_snapshot.json',dict(checked_at=now(),candidates=reports,completed_manual_pairs=len(FINALS),pending=['Plane179']))
print(json.dumps(reports,ensure_ascii=False,indent=2))
