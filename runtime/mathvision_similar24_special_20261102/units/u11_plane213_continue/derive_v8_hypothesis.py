from bootstrap import *
from math_tools import cells,is_exterior
c=read(OWN/'current_context.json');table={}
for k in ('board','A','B','C','D','E'):
    prefix='given_' if k=='board' else k+'_';cs=cells(c,prefix)
    groups={}
    for o in c['objects']:
        if not o['id'].startswith(prefix) or not is_exterior(o['geometry']['points'],cs):continue
        a,b=o['geometry']['points']
        orientation='V' if a[0]==b[0] else 'H';fixed=a[0] if orientation=='V' else a[1]
        start=min(a[1],b[1]) if orientation=='V' else min(a[0],b[0])
        groups.setdefault((orientation,fixed),set()).add(start)
    maximum=0
    for starts in groups.values():
        for start in starts:
            if start-1 in starts:continue
            length=1
            while start+length in starts:length+=1
            maximum=max(maximum,length)
    vertices={(x+dx,y+dy) for x,y in cs for dx,dy in ((0,0),(1,0),(0,1),(1,1))}
    concave=sorted((x,y) for x,y in vertices if sum((x+dx,y+dy) in cs for dx,dy in ((-1,-1),(-1,0),(0,-1),(0,0)))==3)
    table[k]={'maximum_straight_exterior_run':maximum,'complete_concave_corner_count':len(concave),'all_concave_vertices':concave}
assert [(table[k]['maximum_straight_exterior_run'],table[k]['complete_concave_corner_count']) for k in ('board','A','B','C','D','E')]==[(4,1),(3,1),(3,2),(4,1),(4,2),(1,4)]
save('hypothesis_v8_complete_invariant_table.json',{'at_utc':now(),'question_id':'Plane213','variant_id':'user233_C_max_run_unique_concavity_v8','wrong_preset':'C','fully_edge_derived_invariant_table':table,'new_information':'Among the choices, C alone shares the WHOLE BOARD pair(maximal straight exterior run=4, complete concave-corner inventory=1). The geometric tiling answer remains A; matching invariants of the whole object to a single component is an invalid sufficiency criterion.','source_red':['given_0','given_2','given_4','given_6'],'C_red':['C_0','C_2','C_4','C_6'],'source_blue':['given_27','given_29'],'C_blue':['C_11','C_12'],'specific_information_roles':'Red encodes one complete maximal run; blue marks ALL existing concave corners on each of the two compared outlines, one each. This is a complete two-invariant comparison, not just the presence of one sampled D concavity.','difference':'OldC5-convex/1-concave inventory was shared by A; it did not mark or compare maximal run length. OldD4-run+one sampled concavity did not compare complete corner inventory because D actually has2. OriginalC01 compared a convex2-unit foot at the source bottom, not the sole concave corner. All source blue positions and C blue targets here differ from that failed C01 transfer.','two_groups_not_one_rigid_map_claim':True,'no_same_PNG_retest_or_old_final_relabel':True,'requires_native_validity_and_all_fresh_render_history_gates':True,'reference':'Current user Plane233 true paired red/blue boundary comparisons and permitted real concave structure.','current_eligibility':eligibility()})
print(json.dumps({'invariant_table':table,'candidate_with_equal_full_pair':'C','new_API_calls':0}))
