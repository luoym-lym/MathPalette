from bootstrap import *
from math_tools import cells
c=read(OWN/'current_context.json')
def corners(cs):
    vs={(x+dx,y+dy) for x,y in cs for dx,dy in ((0,0),(1,0),(0,1),(1,1))}
    out=[]
    for x,y in sorted(vs):
        n=sum((x+dx,y+dy) in cs for dx,dy in ((-1,-1),(-1,0),(0,-1),(0,0)))
        if n in (1,3):out.append({'xy':[x,y],'kind':'convex90' if n==1 else 'concave270'})
    return out
inventories={k:corners(cells(c,'given_' if k=='board' else k+'_')) for k in ('board','A','B','C','D','E')}
counts={k:{kind:sum(v['kind']==kind for v in vs) for kind in ('convex90','concave270')} for k,vs in inventories.items()}
assert counts['board']==counts['A']==counts['C']=={'convex90':5,'concave270':1}
assert counts['B']==counts['D']=={'convex90':6,'concave270':2}
assert counts['E']=={'convex90':8,'concave270':4}
save('corner_inventory_hypothesis_before_E_outputs.json',{'at_utc':now(),'question_id':'Plane213','proposed_variant_id':'user233_C_convex_concave_inventory_v6','wrong_preset_if_admitted':'C','current_eligibility':eligibility(),'inventories':inventories,'counts':counts,'new_information':'The entire source outline and C both have5 convex90-degree corners and1 concave270-degree corner. Compare the actual angle-type inventory using blue short corner-arms for every convex corner and red for the one concave corner in both diagrams. This is a true combinatorial boundary invariant match, insufficient to infer3-copy tileability. A shares this inventory and remains the unique tiling answer.','difference_from_every_previous':'An angle-type count across all6 exterior corners, rather than a single notch or an open bounding L/4-link stair. It requires no full colored option contour or internal source edge and no added dots/lines. Only partial styles of existing exterior unit edges would be used.','proposed_concision':'Each of6 corners needs its two incident short arms to display the local turn;12 corners across the source and C yield24 disjoint partial-style actions, each with a corner-type count role. Need actual native-image clarity review before any API; reject if the clusters are busy or ineffective. No action-count cap is substituted for this actual judgment.','source_reference':'Current Plane233 C01 paired red/blue existing boundary features, extended to the explicitly permitted real convex/concave structure. No other reference substituted.','design_not_yet_rendered_or_admitted':True,'requires_fresh_schema_noop_repeat_process_replay_native_review_and_zero_history_gates':True,'no_three_candidate_early_stop':True})
print(json.dumps({'counts':counts,'new_API_calls':0}))
