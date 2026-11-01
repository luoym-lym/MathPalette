from tools08 import *
q='Plane404';v='unreflected_first_digit_binding';folder=HERE/q/v
s=json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'));obj={o['id']:o for o in s['objects']}
digit_sets=[];mapping=[]
for offset,upper,lower in [(0,['o2','o3'],['o18','o19','o20']),(3,['o4','o5'],['o21','o22','o23']),(6,['o6','o7'],['o24','o25','o26'])]:
    segments=[]
    for oid in upper+lower:
        pts=copy.deepcopy(obj[oid]['points'])
        if oid in upper:pts=[[x,6-y] for x,y in pts]
        segments.append({'object':oid,'after_fold':pts})
    names=set()
    for seg in segments:
        (x1,y1),(x2,y2)=seg['after_fold']
        if y1==y2:names.add({.5:'bottom',1.5:'middle',2.5:'top'}[y1])
        else:
            left=x1==offset;lo,hi=sorted([y1,y2])
            if lo==.5:names.add('lower_left' if left else 'lower_right')
            if hi==2.5:names.add('upper_left' if left else 'upper_right')
    digit_sets.append(sorted(names));mapping.append(segments)
expected=[{'top','middle','bottom','upper_left','lower_right'},{'top','middle','bottom','upper_left','lower_left','lower_right'},{'top','middle','bottom','upper_left','upper_right','lower_right'}]
assert all(set(a)==b for a,b in zip(digit_sets,expected))
write(folder/'fold_segment_math_audit.json',{'reflection_axis_object':'o1','axis_y':3,'map':'(x,y)->(x,6-y) for the top half; lower half fixed','exact_source_segment_mappings':mapping,'seven_segment_sets':digit_sets,'uniquely_read_digits':[5,6,9],'unique_option':'C','reason':'Only formal C is 5:6:9; the original dots are unchanged and are not counted as number strokes.','color_or_width_does_not_move_add_remove_segments':True})
cfg,ad=adapter();m=ad.inspect_question(q);p=json.loads((folder/'plugin.json').read_text(encoding='utf-8'));renderer=PluginRenderer(cfg,ad,{q:m})
_,data,px=renderer.render(p,frozen=True);assert data==(folder/'candidate.png').read_bytes()
(folder/'replay_final.png').write_bytes(data)
write(folder/'replay_final_audit.json',{'byte_identical_to_tested_png':True,'sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':px,'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'replayed_at':now()})
targets={t['id']:t for t in m['canvas']['targets']}
write(folder/'path_fingerprints.json',{'question_id':q,'targets':{a['target']:targets[a['target']] for a in p['params']['actions']},'fresh_context':str(folder/'context.json')})
d=json.loads((folder/'design.json').read_text(encoding='utf-8'))
write(folder/'primary_review.json',{'question_id':q,'variant_id':v,'primary_review_only':True,'actual_original_and_candidate_pngs_viewed':True,'status':'credible_pair_pending_NEW_independent_review','preserved_unique_answer':'C = 5:6:9','preset_wrong_answer':'A = 2:6:9','math_proof':d['primary_mathematical_proof'],'executable_proof':str(folder/'fold_segment_math_audit.json'),'marker_roles':d['marker_roles'],'visual_review':'Five existing number-encoding bars only. The two red vertical bars retain their original upper-right/lower-left placement on the source half. Three blue horizontal bars identify the stationary completion at the same digit location. All dots, other digits, fold line, paper boundary and fold arrow remain clearly black and readable. Added appearance supplies no new cut, point, numeral, equality condition or filled region. The human still reflects the red bars in the existing horizontal dashed axis, obtaining 5.','semantic_ambiguity_check':'Unlike Plane233, there are no new closed source cut contours, claimed partitions or pieces. Original number strokes receive a legal color/width style. The numeral result ignores annotation hue exactly as the formal numeric choices do; geometry of every stroke is unchanged.','per_marker_proof':[{'target':'o2','role':'Upper-right source vertical; maps to lower-right of 5. Red makes it eligible for the tempting unreflected 2 interpretation.'},{'target':'o3','role':'Lower-left source vertical; maps to upper-left of 5. Together with o2 this encodes the full handed source pair.'},{'target':'o18','role':'Bottom horizontal completion stroke of first digit; blue stationary group.'},{'target':'o19','role':'Middle horizontal completion stroke of first digit; blue stationary group.'},{'target':'o20','role':'Top horizontal completion stroke of first digit; blue stationary group.'}],'conciseness':'Every one of the five bars contributes to exactly the first target numeral; there is no option highlighting.','original_control':'Separate original-control pair ends B then C (2:6:6 then 5:6:9); narratives inaccurate. Control is not consistently correct.','limitations':['Two candidate calls only. The entire final answers were manually read; both finish at A/2:6:9 although their reasoning is inaccurate and mutually different.','Original control is B/C, so no causal improvement claim or statistical effectiveness estimate.','No human performance study or per-marker ablation.','This is not independent second review and is not user Pass/Collect. Parent must launch a NEW independent review before any delivery.'],'replay_final_sha256':hashlib.sha256(data).hexdigest()})
print(json.dumps({'question_id':q,'unique_answer':'C','replay_equal':True,'candidate_status':'pending_independent_review'}))
