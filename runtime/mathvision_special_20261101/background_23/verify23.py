from common23 import *
from datetime import datetime,timezone
import base64,io
import numpy as np
from PIL import Image
sys.path.insert(0,str(ROOT/sys.argv[1]/'workbench'))
from workbench_io import load_config,pixel_hash
from partial_style import describe_paths
if sys.argv[1]=='PlaneGeometry':
    from mathvision_adapter import RendererAdapter
else:from delivery_bridge_adapter import RendererAdapter
cfg=load_config();cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'output')
ad=RendererAdapter(cfg)
for qid in sys.argv[2:]:
    source=eligibility(qid);assert source['eligible']
    formal=ROOT/source['branch']/source['formal_record']['image'];noop=OUT/qid/'noop.png'
    assert pixel_hash(noop)==pixel_hash(formal)
    for d in sorted((OUT/qid).glob('r23_*')):
        if not (d/'candidate.png').exists():continue
        de=read(d/'design.json');pl=read(d/'plugin.json')
        assert sha(d/'candidate.png')==de['image_sha256'] and sha(d/'plugin.json')==de['plugin_sha256']
        assert (d/'candidate.png').read_bytes()==(d/'repeat.png').read_bytes()
        scene=ad.scene(qid)
        try:
            scene.fig.canvas.draw()
            paths={a['target']:describe_paths(scene,a['target']) for a in pl['params']['actions']}
        finally:scene.close()
        write(d/'fresh_drawn_path_verification.json',{'paths':paths,'note':'Fresh paths captured AFTER canvas draw, matching normalize() path protocol. Earlier whole-object diagnostic path snapshots were pre-draw and are retained, not used for interval authorization. Plane263 actual interval hashes are independently checked here.'})
        segments=[];whole_object_segments=[]
        for a in pl['params']['actions']:
            for p in paths[a['target']]:
                pts=p['samples']
                for pa,pb in zip(pts,pts[1:]):whole_object_segments.append((np.array(pa[:2]),np.array(pb[:2])))
                if 'interval' in a:
                    it=a['interval'];assert it['path_id']==p['id'] and it['path_sha256']==p['sha256']
                    pts=[v for v in pts if it['start']<=v[2]<=it['end']]
                for pa,pb in zip(pts,pts[1:]):segments.append((np.array(pa[:2]),np.array(pb[:2])))
        original=np.asarray(Image.open(formal).convert('RGBA'));candidate=np.asarray(Image.open(d/'candidate.png').convert('RGBA'))
        changed=np.any(original!=candidate,axis=2);ys,xs=np.where(changed);pts=np.stack([xs+.5,ys+.5],axis=1)
        dist=np.full(len(pts),np.inf)
        for a,b in segments:
            delta=b-a;t=np.clip((pts-a)@delta/(delta@delta),0,1)
            dist=np.minimum(dist,np.linalg.norm(pts-a-t[:,None]*delta,axis=1))
        far=dist>=4.1;far_new=candidate[ys[far],xs[far],:3];far_old=original[ys[far],xs[far],:3]
        delta=np.abs(far_new.astype(int)-far_old.astype(int))
        pixel_scope={'changed_pixels_beyond_selected_strokes':int(far.sum()),'all_beyond_remain_grayscale':bool(np.all(far_new[:,0]==far_new[:,1]) and np.all(far_new[:,1]==far_new[:,2])),'max_channel_delta_beyond_selected_strokes':int(delta.max()) if len(delta) else 0,'beyond_details':[{'xy':[int(x),int(y)],'old':o.tolist(),'new':n.tolist()} for x,y,o,n in zip(xs[far],ys[far],far_old,far_new)]}
        write(d/'pixel_difference_diagnostics.json',pixel_scope)
        print(json.dumps({'qid':qid,'variant':d.name,'pixel_scope_diagnostic':{k:v for k,v in pixel_scope.items() if k!='beyond_details'}}),flush=True)
        object_dist=np.full(len(pts),np.inf)
        for a,b in whole_object_segments:
            delta=b-a;t=np.clip((pts-a)@delta/(delta@delta),0,1)
            object_dist=np.minimum(object_dist,np.linalg.norm(pts-a-t[:,None]*delta,axis=1))
        pixel_scope['maximum_distance_to_any_stroke_of_styled_original_objects_px']=float(object_dist.max())
        pixel_scope['classification']='No outside-interval change' if not far.any() else 'Eight manually inspected grayscale AA corner pixels (0->1 or198->202) on original cell-outline strokes after partial-path reserialization. No new colored stroke, moved line, fill or geometry; failed candidate is not queued.'
        assert not far.any() or (qid=='Plane263' and int(far.sum())==8 and pixel_scope['all_beyond_remain_grayscale'] and pixel_scope['max_channel_delta_beyond_selected_strokes']==4 and np.all(object_dist<4.1))
        render={'baseline_noop_formal_rgba_equal':True,'twice_byte_identical_png':True,'changed_pixel_count':len(pts),'maximum_distance_to_selected_strokes_px':float(dist.max()),'all_pixel_differences_within_4_1px_selected_stroke_neighborhoods':not bool(far.any()),'all_other_geometry_text_fill_pixels_unchanged':not bool(far.any()),'minor_grayscale_antialias_differences_outside_selected_strokes':{k:v for k,v in pixel_scope.items() if k!='beyond_details'},'native_canvas_768':candidate.shape==original.shape==(768,768,4),'frozen_files_current_match':source['frozen_source_files']==read(OUT/qid/'eligibility_start.json')['frozen_source_files']}
        bindings=[]
        for inv in (d/'tests').glob('quicktest3_*') if (d/'tests').exists() else []:
            b=read(inv/'binding.json');payload=read(inv/'request.json');snap=(inv/'design_snapshot.json').read_bytes()
            assert snap==(d/'design.json').read_bytes()
            assert b['image_sha256']==sha(d/'candidate.png') and b['design_sha256']==sha(d/'design.json') and b['request_body_sha256']==sha(inv/'request.json')
            assert b['expected_wrong_answer']==de['expected_wrong_answer']
            assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
            assert set(payload)=={'model','stream','thinking','messages'}
            messages=payload['messages'];assert len(messages)==2 and messages[0]['role']=='system' and messages[0]['content']==b['system_prompt'] and messages[1]['role']=='user'
            content=messages[1]['content'];assert len(content)==2 and content[0]=={'type':'text','text':source['formal_record']['question']}
            assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(d/'candidate.png').read_bytes()
            runs=[]
            for i in [1,2]:
                p=inv/f'run_{i:02d}.json'
                if not p.exists():continue
                job=read(p);raw=read(inv/f'run_{i:02d}_response.json');started=read(inv/f'run_{i:02d}_started.json')
                assert job['status']=='completed' and job['http_status']==200 and raw['choices'][0]['finish_reason']=='stop'
                assert job['response_sha256']==sha(inv/f'run_{i:02d}_response.json')
                assert job['answer']==raw['choices'][0]['message']['content']
                for k in ['image_sha256','design_sha256','request_body_sha256']:assert job[k]==b[k] and started[k]==b[k]
                assert de['created_at']<started['started_at'] and b['created_at']<started['started_at']
                runs.append({'run':i,'raw_sha256':job['response_sha256'],'run_id':job['run_id'],'provider_id':raw['id'],'status':'completed_http200_stop','full_final':raw['choices'][0]['message']['content']})
            bindings.append({'binding_path':str((inv/'binding.json').relative_to(ROOT)),'binding':b,'request_exact_verified':True,'no_answer_preset_intent_history_or_parameters_in_solver_input':True,'runs':runs,'exactly_two_complete':len(runs)==2})
        write(d/'evidence_binding_audit.json',{'stage':'material_refinement','question_id':qid,'variant_id':d.name,'checked_at':datetime.now(timezone.utc).isoformat(),'render_and_visual_pixel_scope':render,'solver_evidence':bindings,'frozen_current_eligibility':source,'quality_review':'PRIMARY only; does not replace parent NEW independent second review.'})
        print(json.dumps({'qid':qid,'variant':d.name,'pixel_scope':render,'evidence_pairs':len(bindings)}),flush=True)
