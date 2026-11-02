from tools28 import *
from partial_style import object_paths
from PIL import Image,ImageDraw
import numpy as np
from make28 import project

for qid in ASSIGNED:
    scene=AD.scene(qid)
    try:
        scene.fig.canvas.draw();targetpaths={}
        for obj in scene.objects:
            if obj.get('styleable'):
                ps=object_paths(scene,obj['id'])
                targetpaths[obj['id']]=[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[s['control'].tolist() for s in p['segments']]} for p in ps]
        if not (TASK/qid/'native_vector_paths_audit.json').exists():write(TASK/qid/'native_vector_paths_audit.json',{'question_id':qid,'checked_at':now(),'source_inputs_sha256':AD.frozen_inputs(qid)['files'],'paths':targetpaths,'source_inputs_equal_to_start':AD.frozen_inputs(qid)['files']==read(TASK/qid/'frozen_inputs.json')['files'],'path_extraction':'Unchanged partial_style.object_paths on fresh dedicated bridge. Source snapshot, stable object IDs and per-marker geometry were frozen before calls. This supplemental actual vector path extraction was performed during checkpoint audit; no tested evidence is edited.'})
    finally:scene.close()
    for p in sorted((TASK/qid).glob('r28_*/design.json')):
        folder=p.parent
        if (folder/'pixel_and_native_path_audit.json').exists():continue
        plugin=read(folder/'plugin.json');context=read(folder/'context.json');tf=np.asarray(context['canvas']['data_to_pixel'])
        mask=Image.new('L',(768,768));draw=ImageDraw.Draw(mask)
        def px(xy):return tuple((tf@np.array([*xy,1]))[:2])
        roles=read(p)['each_marker_proof'];objmap={o['id']:o for o in AD.scenes[qid]['objects']}
        path_bindings=[]
        for a in plugin['params']['actions']:
            if a['type']=='add_point':
                x,y=px(a['xy']);draw.ellipse((x-9,y-9,x+9,y+9),fill=255)
            elif a['type']=='add_line':draw.line([px(xy) for xy in a['endpoints']],fill=255,width=12)
            else:
                obj=objmap[a['target']];aa,bb=obj['points'];start,end=(0,1)
                if 'interval' in a:
                    it=a['interval'];start,end=it['start'],it['end']
                    actual=next(v for v in targetpaths[a['target']] if v['id']==it['path_id']);assert actual['sha256']==it['path_sha256']
                ends=[[aa[i]+t*(bb[i]-aa[i]) for i in range(3)] for t in [start,end]]
                pix=[px(project(qid,v)) for v in ends];draw.line(pix,fill=255,width=12)
                for x,y in pix:draw.ellipse((x-6,y-6,x+6,y+6),fill=255)
                path_bindings.append({'target':a['target'],'native_vector_paths':targetpaths[a['target']],'interval':a.get('interval'),'original_geometry_sha256':canonical_hash(obj)})
        baseline=np.array(Image.open(TASK/qid/'original.png').convert('RGBA'));candidate=np.array(Image.open(folder/'candidate.png').convert('RGBA'))
        changed=np.any(baseline!=candidate,axis=2);maskarr=np.array(mask)>0;outside=int(np.sum(changed&~maskarr))
        aa_diagnostic=None
        if outside:
            fullmask=mask.copy();fd=ImageDraw.Draw(fullmask)
            for a in plugin['params']['actions']:
                if a['type']=='set_object_style':
                    pix=[px(project(qid,v)) for v in objmap[a['target']]['points']]
                    fd.line(pix,fill=255,width=12)
                    for x,y in pix:fd.ellipse((x-6,y-6,x+6,y+6),fill=255)
            off=changed&~maskarr
            actualout=int(np.sum(changed&~(np.asarray(fullmask)>0)))
            grays=bool(np.all(candidate[off,0]==candidate[off,1]) and np.all(candidate[off,1]==candidate[off,2]) and np.all(baseline[off,0]==baseline[off,1]) and np.all(baseline[off,1]==baseline[off,2]))
            delta=int(np.max(np.abs(candidate.astype(int)-baseline.astype(int))[off]))
            yy,xx=np.where(off)
            aa_diagnostic={'pixels_outside_selected_interval_neighborhood':outside,'pixels_outside_whole_original_target_paths':actualout,'all_extra_changes_grayscale_only':grays,'maximum_channel_delta':delta,'extra_change_bbox':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())],'explanation':'Unchanged partial_style splits and re-renders the original full target paths; gray antialias differences can occur on the unselected portion. This is disclosed rather than classified as source geometry corruption. No tested image or raw request was changed.'}
            assert actualout==0 and grays,aa_diagnostic
            print('Partial-style grayscale audit',json.dumps(aa_diagnostic),flush=True)
        assert np.array_equal(candidate[:,:,3],np.full((768,768),255,dtype=np.uint8))
        write(folder/'pixel_and_native_path_audit.json',{'question_id':qid,'variant_id':folder.name,'checked_at':now(),'candidate_sha256':file_hash(folder/'candidate.png'),'formal_original_sha256':file_hash(AD.original_paths[qid]),'pixel_change_count':int(np.sum(changed)),'changed_pixels_outside_selected_mark_neighborhoods':outside,'source_labels_fills_geometry_outside_full_original_target_strokes_pixel_identical':True,'partial_style_grayscale_diagnostic':aa_diagnostic,'localization_tolerance':'Conservative6px radius for existing styles,9px for legal50pt2points, including caps/AA; this is a support audit, not a claim that strokes cover zero pixels of neighboring faces.','native_vector_path_bindings':path_bindings,'frozen_geometry_projection_visibility_hashes_equal_to_start':AD.frozen_inputs(qid)['files']==read(TASK/qid/'frozen_inputs.json')['files'],'no_general_automatic_visibility_claim':True,'primary_only':True})
        print(qid,folder.name,'changed',int(changed.sum()),'outside',outside,flush=True)

# Find all same-question tests and prior independent reports without modifying old snapshots.
oldtests=[]
for p in SHARED.rglob('binding.json'):
    if p.is_relative_to(TASK):continue
    b=read(p)
    if b.get('question_id') not in ASSIGNED:continue
    qid=b['question_id'];oldtests.append({'question_id':qid,'binding':str(p),'sha256':file_hash(p),'image_sha256':b.get('image_sha256'),'is_original_control':b.get('image_sha256')==file_hash(AD.original_paths[qid]),'preset':b.get('expected_wrong_answer')})
reviews=[]
for p in (SHARED/'independent_review').rglob('*.json'):
    content=p.read_text(encoding='utf-8-sig')
    if any(('"'+q+'"') in content or q in p.parts for q in ASSIGNED):reviews.append({'path':str(p),'sha256':file_hash(p)})
write(TASK/'global_same_question_history_search.json',{'checked_at':now(),'same_question_old_tests':oldtests,'original_controls_found':[x for x in oldtests if x['is_original_control']],'independent_reports_found':reviews,'test_count_outside_own_unit':len(oldtests),'other_active_scope_never_written':True})
