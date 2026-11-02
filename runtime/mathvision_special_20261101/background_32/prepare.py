from audit import *
import base64
import copy
from fractions import Fraction
import numpy as np
from PIL import Image
from matplotlib.patches import Patch
from partial_style import apply_partial_styles
from dataset_tools.mathvision_workbench import png_bytes

write_new = save
def save(path, value):
    # Resume preparation after a local serialization issue without replacing any
    # already-written design, hypothesis, timestamp, or evidence.
    if not Path(path).exists(): write_new(path,value)

PLANS = [
    {'qid':'Plane295','variant':'r32_ear_content_preserving_comparison','wrong':'C','targets':[('giveninner-1','red',1/3,2/3),('giveninner1','blue',1/3,2/3),('Binner-1','red',1/3,2/3),('Binner1','blue',1/3,2/3),('Cinner-1','red',1/3,2/3),('Cinner1','blue',1/3,2/3)],'width':1,
     'difference':'Concretely resolves the rejected original-ink reading by carrying BOTH source shoulder colors onto the anatomically exact B shoulders, while retaining the purposeful comparison with the flatter C shoulders. B now preserves every preexisting colored feature. The old design colored only given/C and had no ink-preserving completion. The smaller 1 pt stroke is a supporting readability measure, not the substantive difference.',
     'hypothesis':'A red-left/blue-right shoulder correspondence between the given, true B and flatter C may induce a coarse matched-ear classification that overlooks the 0.19-unit loss of white-ear height in C. C is frozen before any new response; the new study does not presume the old color-only narrative will persist.',
     'roles':['Given left shoulder, actual preexisting source feature.','Given right shoulder, distinguishes the other handed feature.','B left shoulder, exact transport of existing red ink; resolves prior no-valid-completion objection.','B right shoulder, exact transport of existing blue ink; resolves the same objection for the right ear.','C left shoulder, actual lower/flatter counterpart tested for false feature preservation.','C right shoulder, second actual changed counterpart, keeps left/right bindings distinct.']},
    {'qid':'Plane342','variant':'r32_wedge_print_preserved_halfturn_alternative','wrong':'D','targets':[('o2','red',1/3,1),('o208','red',1/3,1),('o216','red',1/3,1)],'width':2,
     'difference':'The required right-side red V is now physically present in B as the exact half-turn of the source red V. The old given/D design had no valid color-preserving printed result. B remains valid whether colors are intrinsic print or comparison highlights; D remains the actual but incorrect quarter-turn comparison. This changes the available color-preserving completion, not merely palette, stroke width, crop, name or preset.',
     'hypothesis':'Shared red source-wedge and bottom-wedge edges may sustain the quarter-turn misconception D even when the correctly transported right red V is honestly available in B. Both perpendicular flips, plain reverse, black fill and full diagonals remain untouched.',
     'roles':['Source two sloping printed wedge edges, orientation reference.','B two sloping printed wedge edges, exact physical transport after the two flips and the concrete semantic repair.','D two sloping printed wedge edges, wrong quarter-turn correspondence to the same source feature.']},
    {'qid':'Plane295','variant':'r32_nose_extent_preserved_comparison','wrong':'A','targets':[('givennose','red',1/3,1),('Bnose','red',1/3,1),('Anose','red',1/3,1)],'width':1,
     'difference':'Changes the information target from white-ear shoulder orientation to the preexisting downward-nose extent and position. The true B carries the exact source red V. A has a higher base and deeper apex, so its similar downward V is the explicit wrong geometric hypothesis. This new A preset is based on those frozen nose coordinates before testing, not a relabel of any old output.',
     'hypothesis':'Match the direction and red V contour of the small downward source nose to the enlarged downward A nose, overlooking that adding eyes cannot move its base upward by 0.2 or tip downward by 0.06. B retains both the correct nose geometry and its red ink; uncolored C also differs in ear geometry.',
     'roles':['Given nose sloping sides, actual orientation/extent reference.','B nose sloping sides, exact geometry-and-ink-preserving completion.','A taller nose sloping sides, false same-downward-triangle correspondence despite changed extent and position.']},
    {'qid':'Plane342','variant':'r32_diagonal_print_preserved_singleflip','wrong':'A','targets':[('o3','red',0,1),('o209','red',0,1),('o205','red',0,1)],'width':2,
     'difference':'Targets the existing FULL printed diagonal rather than the two wedge legs. The source NW-SE diagonal is transported correctly to NW-SE in B. Rising A is the actual single-downward-reflection diagonal while its wedge remains left. A therefore represents stopping after one reflection and forgetting both the plain back and second flip; this is a different predeclared geometric error from old D quarter-turn wedge matching.',
     'hypothesis':'A source-to-A full-diagonal reflection correspondence may induce a single-flip answer A while neglecting the blank reverse and the required second perpendicular flip. B is explicitly color-preserving and mathematically correct. No new diagonal or arrow is drawn.',
     'roles':['Source full NW-SE printed diagonal, entire orientation reference.','B full NW-SE diagonal, exact print-preserving half-turn counterpart.','A full rising diagonal, genuine single-downward-reflection counterpart and targeted stopping-too-early error.']}
]

def plain(x):
    return json.loads(json.dumps(x,default=lambda v:v.tolist() if hasattr(v,'tolist') else str(v)))

def local(obj, center):
    obj=copy.deepcopy(obj)
    obj.pop('id',None)
    if 'center' in obj: obj['center']=[round(float(v)-center[i],12) for i,v in enumerate(obj['center'])]
    if 'points' in obj: obj['points']=[[round(float(v)-center[i],12) for i,v in enumerate(p)] for p in obj['points']]
    return obj

def math295():
    scene=read(ROOT/'Plane295/formal_scene_snapshot.json')
    obs={o['id']:o for o in scene['objects']}
    features=['head','ear-1','ear1','inner-1','inner1','nose']
    given_center=obs['givenhead']['center']
    given={f:local(obs['given'+f],given_center) for f in features}
    choices={}
    for letter in 'ABCDE':
        center=obs[letter+'head']['center']
        fs={f:local(obs[letter+f],center) for f in features}
        choices[letter]={'features':fs,'matches_each':{f:fs[f]==given[f] for f in features},'all_match':fs==given}
    matching=[k for k,v in choices.items() if v['all_match']]
    assert matching==['B']
    return {'question_id':'Plane295','derived_unique_answer':'B','method':'Independently compare every preexisting object after translating actual frozen head centers. Six features, all five options; no stored answer used to derive the survivor. Actual source JPG and formal native PNG were viewed.',
            'given_features':given,'all_choices':choices,'survivors':matching,
            'elimination':{'A':'Downward nose base y=0.2 vs 0; tip -0.4 vs -0.34.','B':'All six preexisting features preserved exactly in local vector coordinates.','C':'White-ear upper vertices (+/-0.8,0.99) vs (+/-0.82,1.18).','D':'Upward/shifted triangular nose.','E':'Circular nose instead of triangle.'},
            'source_wording_caveat':'The source and formal given lack mouths while every source/formal choice includes the same two mouth arcs. Literal ONLY-eyes raster extension would reject all original choices. Unique B applies to the natural finished-drawing reading preserving existing anatomy while allowing the common added mouth. This inherited caveat is not repaired, hidden, or used to eliminate an option.',
            'no_3d_projection_or_visibility_change':True}

def math342():
    scene=read(ROOT/'Plane342/formal_scene_snapshot.json')
    obs={o['id']:o for o in scene['objects']}
    def norm(points,frame):
        pts=[[Fraction(str(v)).limit_denominator(100000) for v in p] for p in obs[frame]['points']]
        lo=[min(p[i] for p in pts) for i in (0,1)]
        hi=[max(p[i] for p in pts) for i in (0,1)]
        assert hi[0]-lo[0]==hi[1]-lo[1]
        return [[(Fraction(str(v)).limit_denominator(100000)-lo[i])/(hi[i]-lo[i]) for i,v in enumerate(p)] for p in points]
    def fmt(points): return [[str(v) for v in p] for p in points]
    source=norm(obs['o2']['points'],'o1')
    diag=norm(obs['o3']['points'],'o1')
    wanted=[[1-x,1-y] for x,y in source]
    wanted_diag=[[1-x,1-y] for x,y in diag]
    choices={}
    for L,idx in zip('ABCDE',[204,208,212,216,220]):
        w=norm(obs[f'o{idx}']['points'],f'o{idx-1}')
        d=norm(obs[f'o{idx+1}']['points'],f'o{idx-1}')
        choices[L]={'wedge':fmt(w),'diagonal':fmt(d),'wedge_matches':sorted(w)==sorted(wanted),'diagonal_matches':sorted(d)==sorted(wanted_diag)}
    survivors=[L for L,v in choices.items() if v['wedge_matches'] and v['diagonal_matches']]
    assert survivors==['B']
    return {'question_id':'Plane342','derived_unique_answer':'B','method':'Independent physical-flip derivation from actual source and formal PNG, followed by exact rational normalization of actual formal vectors to the printed unit square. Not a stored-answer premise.',
            'source_wedge':fmt(source),'source_full_diagonal':fmt(diag),'down_flip':'(x,y)->(x,1-y), printed front faces away; intermediate visible reverse is plain white.','right_flip':'(x,y)->(1-x,y), printed front faces viewer again.','composition':'(x,y)->(1-x,1-y), half-turn.','required_wedge':fmt(wanted),'required_diagonal':fmt(wanted_diag),'all_choices':choices,'survivors':survivors,
            'single_downward_reflection_comparison':'Ignoring face visibility and second flip gives a left wedge plus rising diagonal, the geometry of A. Correct physical intermediate is still plain white; A is only the targeted misconception.','quarter_turn_comparison':'A planar counterclockwise quarter-turn moves the source left wedge to bottom and its NW-SE full diagonal to rising: D. This is not two perpendicular card flips.',
            'no_3d_projection_or_visibility_change':'This is a 2D depiction of a physical process; no frozen scene geometry, layer, arrow, blank reverse, diagonal, text or black fill is modified.'}

def study():
    history=[]
    for qid in IDS:
        oldroot=BASE/'background_19'/qid
        paths=list(oldroot.rglob('*.json'))
        paths+=list((BASE/'independent_review'/f'{qid}_{OLD[qid]}').rglob('*.json'))
        entries=[]
        for p in paths:
            value=read(p)
            entries.append({'path':str(p.relative_to(PROJECT)),'sha256':sha(p),'json_read_completely':True})
        inv=next((oldroot/OLD[qid]/'tests').iterdir())
        b=read(inv/'binding.json'); req=read(inv/'request.json')
        assert base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(oldroot/OLD[qid]/'candidate.png').read_bytes()
        assert b['image_sha256']==sha(oldroot/OLD[qid]/'candidate.png')
        full=[]
        for i in [1,2]:
            p=inv/f'run_{i:02d}_response.json'; raw=read(p)
            full.append({'run':i,'complete_assistant_content':raw['choices'][0]['message']['content'],'raw_path':str(p),'raw_sha256':sha(p),'finish_reason':raw['choices'][0]['finish_reason']})
        review=read(BASE/'independent_review'/f'{qid}_{OLD[qid]}'/'independent_review.json')
        history.append({'question_id':qid,'old_variant_id':OLD[qid],'preset':b['expected_wrong_answer'],'actual_old_finals':['C','C'] if qid=='Plane295' else ['D','D'],'old_decision':review['decision'],'old_rejection':review.get('reason',review.get('summary')),'full_raw_finals':full,'all_previous_json_read':entries,'old_original_control_invocations':[],'unchanged_old_retest_or_promotion':False})
    refs=[]
    for manifest in sorted(BASE.glob('batch_0[1-9]/manifest.json')):
        value=read(manifest)
        for p in manifest.parent.rglob('*design*.json'):
            d=read(p)
            refs.append({'batch':manifest.parent.name,'path':str(p),'sha256':sha(p),'question_id':d.get('question_id'),'hypothesis':d.get('hypothesis',d.get('intent')),'marker_roles':d.get('marker_roles')})
    checkpoints=[]
    for p in [BASE/'background_18/checkpoint.json',BASE/'background_19/checkpoint.json',BASE/'background_19/second_review_queue.json']:
        value=read(p)
        checkpoints.append({'path':str(p),'sha256':sha(p),'read_full_json':True,'status':value.get('status') if isinstance(value,dict) else None,'contains_assigned_ids':{q:q in p.read_text(encoding='utf-8-sig') for q in IDS}})
    save(ROOT/'prior_history_and_reference_audit.json',{'created_at':now(),'history':history,'checkpoints':checkpoints,'delivered_reference_designs_read':refs,'original_and_old_candidate_images_actually_viewed':True,'control_policy':'No same-question original controls exist in the supplied prior evidence. None repeated. No incremental effect established.','old_evidence_unmodified':True})
    save(ROOT/'preparation_errors.json',[{'stage':'initial source snapshot','error':'TypeError serializing ndarray in object_paths','affected_file':'Plane295/frozen_paths.json (partial JSON deliberately preserved)','resolution':'Complete exact path capture saved separately as frozen_paths_complete.json; only own preparation rerun; no API call/abort/retry.'}])

def prepare():
    study()
    proofs={'Plane295':math295(),'Plane342':math342()}
    for qid,proof in proofs.items(): save(ROOT/qid/'primary_original_math.json',proof)
    cfg,ad=make_adapter()
    for plan in PLANS:
        qid=plan['qid']; out=ROOT/qid/plan['variant']; e=eligibility(qid); assert e['eligible']
        save(out/'eligibility_before_design.json',e)
        save(out/'design_difference_audit.json',{'created_at':now(),'stage':'material_refinement','question_id':qid,'variant_id':plan['variant'],'old_design_path':str(BASE/'background_19'/qid/OLD[qid]/'design.json'),'old_design_sha256':sha(BASE/'background_19'/qid/OLD[qid]/'design.json'),'old_independent_decision':'reject','material_difference':plan['difference'],'new_preset_rationale':plan['hypothesis'],'not_cosmetic_or_unchanged_repeat':True,'content_reading_repair':'Source styled path(s) have exact correctly transported counterparts in B; B is valid even if hue is intrinsic drawing/print. Ignoring color also gives B. No assertion of hue exemption is needed.','immutable_old_evidence_preserved':True})
        meta=ad.inspect_question(qid)
        save(out/'fresh_context.json',meta)
        renderer=PluginRenderer(cfg,ad,{qid:meta})
        scene=ad.scene(qid)
        try:
            actions=[]; grounding=[]
            for index,(target,color,start,end) in enumerate(plan['targets']):
                p=object_paths(scene,target)[0]
                action={'type':'set_object_style','target':target,'color':{'red':'#DC2626','blue':'#2563EB'}[color],'linewidth_pt':plan['width'],'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
                actions.append(action)
                selected=p['segments'][round(start*len(p['segments'])):round(end*len(p['segments']))]
                grounding.append({'index':index+1,'action':action,'role':plan['roles'][index],'exact_original_path_controls':[s['control'].tolist() for s in p['segments']],'selected_original_controls':[s['control'].tolist() for s in selected],'selected_endpoint_pixels_bottom_origin':[scene.ax.transData.transform(selected[0]['control'][0]).tolist(),scene.ax.transData.transform(selected[-1]['control'][-1]).tolist()],'path_sha256_actual':p['sha256'],'closed_original_path':p['closed'],'follows_existing_feature_only':True})
            no_op=png_bytes(scene); assert pixel_hash(no_op)==meta['original_pixel_sha256']
            (out/'no_op.png').write_bytes(no_op)
            texts_before=[(t.get_text(),t.get_position(),t.get_color(),str(t.get_transform())) for t in scene.ax.texts]
            original_fills=[a for a in scene.ax.patches if a.get_fill()]
            fills_before=[(a.get_path().vertices.tolist(),a.get_facecolor(),a.get_visible(),str(a.get_transform())) for a in original_fills]
            view_before=[scene.ax.get_xlim(),scene.ax.get_ylim(),scene.ax.get_aspect(),list(scene.ax.get_position().bounds)]
            apply_partial_styles(scene,actions)
            texts_after=[(t.get_text(),t.get_position(),t.get_color(),str(t.get_transform())) for t in scene.ax.texts]
            fills_after=[(a.get_path().vertices.tolist(),a.get_facecolor(),a.get_visible(),str(a.get_transform())) for a in original_fills]
            view_after=[scene.ax.get_xlim(),scene.ax.get_ylim(),scene.ax.get_aspect(),list(scene.ax.get_position().bounds)]
            assert texts_before==texts_after and fills_before==fills_after and view_before==view_after
        finally: scene.close()
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':plan['variant'],'intent':plan['hypothesis'],'params':{'actions':actions}}
        normalized=renderer.normalize(plugin)
        assert renderer.normalize(normalized)==normalized
        save(out/'plugin_submitted.json',plugin);save(out/'plugin.json',normalized)
        design={'question_id':qid,'variant_id':plan['variant'],'created_at':now(),'expected_wrong_answer':plan['wrong'],'correct_answer':'B','hypothesis':plan['hypothesis'],'marker_roles':plan['roles'],'material_difference':plan['difference'],'primary_original_math':str(ROOT/qid/'primary_original_math.json'),'semantic_repair':'B correctly carries all source colored ink, so intrinsic-content and annotation readings agree on B.','source_caveat':proofs[qid].get('source_wording_caveat'),'approval_status':'UNREVIEWED primary exploration only; NEW parent independent review required for any eventual delivery'}
        save(out/'design.json',design)
        save(out/'per_marker_grounding.json',grounding)
        _,data,pixels=renderer.render(normalized,frozen=True)
        _,repeat,repeat_pixels=renderer.render(normalized,frozen=True)
        assert data==repeat and pixels==repeat_pixels
        (out/'candidate.png').write_bytes(data);(out/'repeat.png').write_bytes(repeat)
        assert sha(out/'candidate.png')!=sha(BASE/'background_19'/qid/OLD[qid]/'candidate.png')
        save(out/'render_audit.json',{'created_at':now(),'schema_normalization_idempotent':True,'fresh_no_op_pixel_equal_formal':True,'candidate_and_repeat_byte_identical':True,'candidate_sha256':sha(out/'candidate.png'),'candidate_pixel_sha256':pixels,'plugin_sha256':sha(out/'plugin.json'),'design_sha256':sha(out/'design.json'),'unchanged_texts':True,'unchanged_original_filled_artist_geometry_facecolor_visibility_transforms':True,'unchanged_view_aspect':True,'all_marker_path_hashes_verified':True,'new_point_line_text_or_relation_glyph':False,'new_closed_region_or_cut':False,'expected_raster_limit':'Colored existing outlines change local border pixels; vector fill preservation is not literal raster fill identity. No new topology or additional piece.','no_threeD_projection_visibility_change':True,'source_manifest_matches_start':input_manifest(ad,qid)==read(ROOT/qid/'input_manifest_start.json')})
        assert input_manifest(ad,qid)==read(ROOT/qid/'input_manifest_start.json')
        print(json.dumps({'question':qid,'variant':plan['variant'],'preset':plan['wrong'],'markers':len(actions),'deterministic':True,'png_sha256':sha(out/'candidate.png')}),flush=True)
    save(ROOT/'prepared_designs.json',PLANS)

if __name__=='__main__': prepare()
