from tools45 import *
math=read(TASK/'independent_primary_math_audit.json')
def style(target,color):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}

q='Solid97';vid='r45_complementary_adjacent_seam_handedness'
roles=[
 {'action_index':0,'target':'dicee6','role':'Source: actual vertical shared edge of visible1/front and3/left, showing the ordered neighboring value pair. Not a pip, extra face or invented hidden edge.'},
 {'action_index':1,'target':'dicee10','role':'Receiver: actual shared edge of6/top and4/front, the complements7-1 and7-3. Same red creates a local pair correspondence; the preset mistake carries the remaining2 to the right by an improper reflection, rather than the proper rotation that puts5 there.'}
]
render(q,vid,[style('dicee6',RED),style('dicee10',RED)],'B',
       'Compare the source1/3 seam to receiver6/4 seam: infer right-face2 by reversing die handedness when transferring the complementary adjacent pair. Correct proper rotation gives5.',
       math[q],roles,
       'No old candidate or API pair exists; old unit05 explicitly found no clean seam correspondence. This design supplies an exact two-edge source/receiver complement relation and a determinant-1 alternative proof giving precisely only2. It also explicitly resolves physical edge-color consistency: the two seams are distinct opposite cube edges, each hidden in the other view; a single identical red-edged die realizes both views and still uniquely gives5. This is not whole-option highlighting, pip recoloring or an absent-face outline.')

q='Solid108';vid='r45_planar_hinge_pair_state_transfer'
roles=[
 {'action_index':0,'target':'netedge1','role':'Red source departure hinge START->blank. First member of the actual local two-crossing route.'},
 {'action_index':1,'target':'netedge9','role':'Red receiver departure hinge C->D. Receives the source departure in the congruent planar two-hinge mapping; it does not bound an added tetrahedron marked face.'},
 {'action_index':2,'target':'netedge3','role':'Blue source next hinge blank->A. Fixes the direction/order of the source route pair and prevents red from being an isolated triangle salience mark.'},
 {'action_index':3,'target':'netedge11','role':'Blue receiver next hinge D->E. Completes the planar-120degree comparison pair. The improper shortcut is copying contact-face identity from START to C by board-plane rotation; actual rolls first return atE.'}
]
render(q,vid,[style('netedge1',RED),style('netedge9',RED),style('netedge3',BLUE),style('netedge11',BLUE)],'C',
       'Bind the first two real crossing hinges to the congruent later two-hinge pair. A planar pose correspondence sends START toC, encouraging copying the marked contact face at the fourth roll; actual tetrahedron state first returns atE, sixth roll.',
       math[q],roles,
       'Old unit07 saved no design and lacked a full rolling-state proof. New work proves all6 initial orientations, identifies the exact actual pairs START->blank->A and C->D->E, and distinguishes their planar-120degree isometry from 3D rolling. Four existing board edges receive open pair styles; no chosen whole triangle contour, arbitrary tetrahedron-to-board initial alignment, second marked face or shortcut is introduced. Neither new geometry nor a recolored old candidate is used.')
