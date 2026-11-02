from tools45 import *
import numpy as np
q='Solid81';ctx=read(TASK/q/'context.json');sc=read(TASK/q/'source_scene_snapshot.json');p=sc['projection']
objects={o['id']:o for o in ctx['objects']}
def endpoint(target,i):
    v=objects[target]['geometry']['points'][i]
    return (np.array(p['matrix'])@(np.array(v)-p['origin'])+p['offset']).tolist()
actions=[];roles=[]
for i,(source,target,color) in enumerate([('given1e1','Ae2',RED),('given2e1','Ae6',BLUE)]):
    # Native left endpoint of source glue seam -> right endpoint of receiving seam.
    ends=[endpoint(source,0),endpoint(target,1)]
    actions.append({'type':'add_line','id':'external_pair_'+str(i),'endpoints':ends,'color':color,'linestyle':'dashed'})
    roles.append({'action_index':i,'source_object':source,'source_endpoint_index':0,'receiver_object':target,'receiver_endpoint_index':1,'exact_endpoint_calculation':'Native full-precision3D endpoint passed through the frozen projection. No pixel estimate, geometry edit, midpoint or new point object.','role':('Link source first domino glue seam to A lower vertical-column seam.' if i==0 else 'Link source second domino glue seam to A upper vertical-column seam. These two apparent domino memberships overlap in A middle cube. Mistaking this indicated local correspondence for the only possible placement leads to wrongA; a legal A matching instead rotates one domino into the base/foot pair.')})
render(q,'r45_external_overlapping_domino_side_seams',actions,'A',
       'Two external dashed source-to-receiver links map the two given glue seams to overlapping vertical adjacent pairs in A. Mistaking this local placement for an exhaustive assembly forces a leftover foot and the wrong impossibility A; the unique actual impossibility is B.',
       read(TASK/'independent_primary_math_audit.json')[q],roles,
       'Old unit05 saved no design because outlining nonadjacent pairs might impose a false partition. This design uses two obviously external cross-panel dashed links, each joining an actual source glue-seam endpoint to an actual A side-seam endpoint. No original edge is recolored, no original seam is restyled and no new cube boundary or fixed cut is drawn. The links leave the source immediately into whitespace and approach A from outside. Physical block-print interpretation cannot require cross-panel links to move with cubes. The new targeted misconception is overlap of two locally valid domino placements and failure to consider the horizontal base pairing; it is not generic option salience or claiming B constructible. Own earlier front-seam draft was rejected by geometric preflight because the links crossed A side edges before reaching the intended front seam; ZERO API requests/starts/bindings existed. This is an offline endpoint-placement correction of that same untested mechanism, not a second tested hypothesis or a cosmetic retry of a solver failure. Original draft evidence remains intact.')
