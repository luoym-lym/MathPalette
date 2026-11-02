from tools20 import *

R='#DC2626';B='#2563EB'

def make(qid,vid,preset,actions,hypothesis,proof,roles):
    out=HERE/qid/vid
    assert eligibility(qid)['eligible']
    cfg,ad=adapter();before=inputs(ad,qid);ctx=ad.inspect_question(qid)
    write(out/'fresh_context.json',ctx);write(out/'eligibility_design.json',eligibility(qid));write(out/'source_inputs.json',before)
    p={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:ctx});normalized,data,digest=pr.render(p)
    n2,data2,digest2=pr.render(normalized,frozen=True)
    assert normalized==n2 and data==data2 and digest==digest2 and before==inputs(ad,qid)
    (out/'candidate.png').write_bytes(data);(out/'repeat.png').write_bytes(data2);write(out/'plugin.json',normalized)
    targets={x['id']:x for x in ctx['canvas']['targets']}
    write(out/'marker_bindings.json',[{'action_index':i,'action':a,'role':roles[i],'original_target':targets.get(a.get('target'))} for i,a in enumerate(normalized['params']['actions'])])
    design={'question_id':qid,'candidate_id':qid+'/'+vid,'created_at':now(),'expected_wrong_answer':preset,'correct_answer':ad.records[qid]['answer'],'hypothesis':hypothesis,'primary_math_proof':proof,'per_marker_roles':roles,'mathematics_and_count_targets_preserved':True,'pretest_immutable':True,'source_inputs_sha256':file_hash(out/'source_inputs.json'),'plugin_sha256':file_hash(out/'plugin.json'),'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':digest,'baseline_pixel_equality':True,'twice_byte_identical':True,'approval_status':'PRIMARY ONLY; parent must launch NEW independent second review'}
    write(out/'design.json',design)
    print(json.dumps({'candidate':design['candidate_id'],'preset':preset,'actions':len(actions),'image_sha256':design['image_sha256']}),flush=True)

def edge(qid,oid,start,end,color):
    ctx=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
    target=next(t for t in ctx['canvas']['targets'] if t['id']==oid)
    path=target['partial_paths'][0]
    return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}}

if __name__=='__main__':
    q='Plane393'
    actions=[edge(q,'o1',0,1/3,R),edge(q,'o168',0,1/3,R),edge(q,'o2',0,1/3,B),edge(q,'o169',0,1/3,B)]
    roles=[
      'Original dark triangle left outer side, from (8,10) to (8,8), binds its retained left-side placement after just the first downward flip to the red A side.',
      'A dark triangle left outer side, from (0,2.5) to (0,0), is the matching first-flip location. It stays left, contrary to the required second rightward flip.',
      'Original light-grey triangle bottom outer side, from (8,8) to (10,8), binds the source bottom to A top under a single downward reflection.',
      'A light-grey triangle top outer side, from (0,2.5) to (2.5,2.5), completes the first-reflection feature pair. No whole answer contour is highlighted.'
    ]
    make(q,'first_flip_outer_feature_binding','A',actions,
      'Pair the dark outer side and light-grey outer side between source and A, encoding the result after the first lower-edge flip and encouraging omission of the second right-edge flip.',
      'Normalize the source square to (u,v) in [0,1]^2. A lower-edge flip gives (u,1-v) relative to the next square; the right-edge flip then gives (1-u,1-v). The composition is a half-turn. The source dark triangle at the left therefore ends at the right; its light-grey bottom triangle ends at the top; its white upper-right half ends at lower-left. Only B has dark right / grey top / white lower-left. A is exactly the intermediate first-flip view and fails the second reflection. C has dark top rather than right; D has grey bottom; E has dark bottom. Four open outer-side annotations leave both diagonal boundaries, distinct fills, question mark and two arrows unchanged. Colors are workbench annotations, not new card sectors or mathematical givens.',roles)
    q='Plane416'
    actions=[{'type':'set_object_style','target':'o7','color':R,'linewidth_pt':2},edge(q,'o23',0,1/8,R),edge(q,'o6',0,1/3,B),edge(q,'o23',7/8,1,B)]
    roles=[
      'Original horizontal dashed cutting line, still dashed, identifies the actual cut direction in the last folded wedge.',
      'E hole top horizontal edge is paired to the actual horizontal cut. This is one short hole side, not a whole-hole border.',
      'Original final wedge diagonal fold boundary from (13.5,6) to (12.439339828220179,7.060660171779821) is the second input feature. Mistaking this fold boundary for a surviving cut edge would create bevels.',
      'E upper-right diagonal hole bevel is paired to the source diagonal fold boundary. The targeted error incorrectly propagates a fold as an additional cut and produces an octagonal hole.'
    ]
    make(q,'cut_and_fold_bevel_binding','E',actions,
      'Pair the true horizontal cut with E horizontal hole side and the existing diagonal fold boundary with E bevel; predicted error treats a fold edge as an extra cut, inferring an octagonal hole.',
      'Translate the last triangle apex to (0,0): its folded wedge is bounded by x=0 and y=-x, with y>=0 and -y<=x<=0. The cut is y=a for positive a (a=0.75 in frozen display coordinates). Reflection about the diagonal boundary y=-x sends the cut to x=-a. Reflection about the previous horizontal and vertical folds generates only x=+-a and y=+-a. Their removed center is the axis-aligned square [-a,a]^2. No diagonal cut is made, and unfolding does not turn the fold boundary itself into a cut. C alone has an axis-aligned square hole. A has a tilted square, B and E octagonal holes, D a star with extra concave corners. All original grey material, white holes, dashed fold/cut lines, right-angle sign and scissors remain. Only existing open edge portions receive color, so no new cut or region is drawn.',roles)
    q='Plane431'
    actions=[edge(q,'o142',0,1/8,R),edge(q,'o142',1/8,2/8,B),{'type':'set_object_style','target':'o143','color':R,'linewidth_pt':2},{'type':'set_object_style','target':'o144','color':B,'linewidth_pt':2}]
    roles=[
      'B copy of the given track: its first rising face is red, identifying the surface that constrains the wheel center while that face is in contact.',
      'B copy of the given track: its first falling face is blue, identifying the next surface after the crest.',
      'B first rising proposed locus segment is red, pairing it with the actual rising track face. This segment is parallel to the face at a radius offset.',
      'B first falling proposed locus segment is blue, pairing it with the actual falling face; their sharp meeting incorrectly carries the track corner into the midpoint locus.'
    ]
    make(q,'crest_face_to_sharp_locus_binding','B',actions,
      'Pair the two physical faces at the first crest with the two straight midpoint-locus portions in B, encouraging the false assumption that constant normal offsets meet in a sharp crest rather than a circular arc.',
      'While the wheel contacts a straight face, its midpoint is on a parallel line at perpendicular distance r. At a convex crest, contact stays at the crest while the center travels on a radius-r circular arc connecting the offset face lines. At a concave valley, simultaneous contact with both faces switches at the intersection of the offset lines, giving a sharp valley. Thus the locus has rounded crests and sharp valleys: E alone. A rounds both, B has sharp crests and rounded valleys, C plateaus, D has both sharp. The four marks cover one existing crest/its candidate local counterpart only; they do not add paths, remove rounding, change wheel radius, add contact points or alter the grey track.',roles)
