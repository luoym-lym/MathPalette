from tools55 import *
from math import sqrt
import numpy as np

def partial(qid,target,start,end,color,width=2):
    path=read(HERE/qid/'exact_paths.json')[target][0]
    return dict(type='set_object_style',target=target,color=color,linewidth_pt=width,interval=dict(path_id=path['id'],path_sha256=path['sha256'],start=start,end=end,wrap=False))

def spec(qid,name,wrong,mechanism,diff):
    return dict(question_id=qid,name=name,variant_id=name,branch=BRANCH,description=mechanism,
      expected_wrong_answer=wrong,correct_answer=eligibility(qid)['record']['answer'],mechanism=mechanism,
      primary_math_proof=read(HERE/qid/'primary_math.json'),difference_audit=diff,
      actions=[],marker_roles=[],limitations=['Primary designer assessment only; parent must commission NEW independent second review.',
      'Two responses cannot establish incremental effect, reliability or the precise causal mechanism; no controls repeated.'])

q='Solid195';s=read(PROJECT/BRANCH/eligibility(q)['record']['scene']);paths=read(HERE/q/'exact_paths.json')
d=spec(q,'r55_two_arc_procedure_unit_binding','3',
    'Bind the six actual quarter-arcs of a legal alternating right/left route into three two-arc color groups. Each group is one repeated two-arc procedure; the frozen wrong hypothesis counts procedure repetitions3 instead of quarter-arcs6. No new route segment, arrow, intersection or start label is added; every other hoop portion remains visible.',
    dict(old='All prior native prescreens saved no design or API calls; whole-hoop emphasis and false projected-join ideas were rejected.',
      new='A fully enumerated genuine six-step alternating route, grouped by the procedure unit rather than whole hoop or projected crossing.',
      substantive_difference='Two-arc program unit versus requested quarter-arc unit; true successive arcs on different hoops are matched in each group.',
      preset_rationale_before_calls='Exactly three two-arc cycles complete the first return. Counting cycle-groups gives3; ignoring direction by itself does NOT change the return time.',
      all_old_failed_images_excluded=True))
# Each entry is a genuine geometric quarter on a hoop, intersected with the original visible arc domains.
quarters=[(0,0,90,'#DC2626','+x to +y: first arc of procedure1'),(1,270,360,'#DC2626','+y to -z: second arc of procedure1, traversed decreasing angle'),
          (2,180,270,'#2563EB','-z to -x: first arc of procedure2, decreasing angle'),(0,180,270,'#2563EB','-x to -y: second arc of procedure2'),
          (1,90,180,'#16A34A','-y to +z: first arc of procedure3, decreasing angle'),(2,0,90,'#16A34A','+z to +x: second arc of procedure3, decreasing angle')]
for qi,(hoop,lo,hi,color,role) in enumerate(quarters):
 for obj in s['objects']:
  if not obj['id'].startswith('hoop'+str(hoop)+'arc'):continue
  a,b=obj['domain_deg'];start=max(a,lo);end=min(b,hi)
  if end<=start:continue
  path=paths[obj['id']][0];assert len(path['controls'])==obj['intervals'][0]['samples']-1
  action=partial(q,obj['id'],(start-a)/(b-a),(end-a)/(b-a),color,1.5)
  d['actions'].append(action)
  d['marker_roles'].append(dict(index=len(d['actions'])-1,quarter_index=qi,target=obj['id'],geometric_angle_range=[start,end],full_quarter=[lo,hi],role=role,
    why_needed='One original visible fragment of the named true quarter; omitted false-crossing occlusion gaps are not filled or bridged.',
    exact_domain=obj['domain_deg'],samples=obj['intervals'][0]['samples'],path_sha256=path['sha256']))
write(HERE/q/'spec_r55.json',d)

q='Solid206'
d=spec(q,'r55_equilateral_end_to_ridge_prism_binding','216*sqrt(6)',
    'Pair the two genuine congruent equilateral triangular end faces LAD and RCB in red, and identify the actual2s ridge connecting their apexes in blue. Test treating the nonparallel triangles as prism bases and the ridge2s as perpendicular prism length: sqrt(3)*s^2/4 times2s=216sqrt6, rather than integrating the wedge.',
    dict(old='Own previous prescreen had no design/calls; it rejected unspecified triangular-end salience without a definite prism-length hypothesis.',
      new='The six exact real end-face edges define the common area unit; the distinct blue ridge2s supplies a specific mistaken axial length. The wrong formula and exact output are fixed now.',
      substantive_difference='Face area to extrusion length role transfer across nonparallel end faces, rather than generic face highlighting or using an unnamed height.',
      preset_rationale_before_calls='Each real end triangle is equilateral side s, so area=sqrt3*s^2/4. Wrongly multiplying by actual ridge2s yields216sqrt6 at s=6sqrt2.',
      human_resolution='All s/2s text, short base connectors and original hidden dashes remain readable; a careful human sees the three connector lengths s,s,2s cannot form a prism.'))
for target,role in [('line_2','A-L source triangle side'),('line_6','A-D source triangle base; original hidden dashes retained'),('line_8','L-D source triangle side; original hidden dashes retained'),('line_3','B-R corresponding receiver triangle side'),('line_1','B-C corresponding receiver triangle base'),('line_4','C-R corresponding receiver triangle side')]:
 d['actions'].append(dict(type='set_object_style',target=target,color='#DC2626',linewidth_pt=1.5));d['marker_roles'].append(dict(index=len(d['actions'])-1,target=target,role=role,why_needed='One of three boundaries needed to identify the real equilateral end-face area and its congruent counterpart; no added section face.'))
d['actions'].append(dict(type='set_object_style',target='line_5',color='#2563EB',linewidth_pt=2));d['marker_roles'].append(dict(index=6,target='line_5',role='L-R true2s apex connector; intended misassigned perpendicular prism length.',why_needed='Binds the only length2s to the repeated triangle area; the other two connecting edges stay black and have length s.'))
write(HERE/q/'spec_r55.json',d)

q='Solid207'
d=spec(q,'r55_source_halfside_to_full_panel_scale','108',
    'Match the real half of the source square top side, from midpoint sm to corner s2 (length6), to one true full side of the upper A panel (length12). Test carrying the half-side unit into the full enclosing cube side: side6 gives half-cube volume108 instead of864. No fold, piece, hexagon edge, text or equality marker is added.',
    dict(old='Previous own prescreen had no design/calls; it considered wrong A/B closures that would change the visible six-piece net.',
      new='An open half-side source and a full existing A side form one local scale-level correspondence; the correct half-cube topology is kept.',
      substantive_difference='The enclosing cube scale is misbound by a factor2, not a different closure, omitted face, restored square or doubled volume.',
      preset_rationale_before_calls='The source half is6 because the source square is12. Treating that source half as the full A edge and hence cube side yields6^3/2=108.',
      human_resolution='The uncolored remaining source half and all A/B edges remain present; original cuts and the numerical12x12 statement independently fix actual full cube side12. Colored ink has no effect on the numerical volume asked.'))
d['actions']=[partial(q,'line_26',0,.5,'#DC2626'),dict(type='set_object_style',target='line_9',color='#DC2626',linewidth_pt=2)]
d['marker_roles']=[dict(index=0,target='line_26',range=[0,.5],role='Source s2 to sm half-edge length6; endpoint at the pre-existing cut midpoint.',why_needed='Selects the real half-side scale, not the full12 edge.'),dict(index=1,target='line_9',role='Receiving full A side f1_1 to f1_2 length12.',why_needed='Locates the full cube-edge role which would be incorrectly assigned the source half-side scale. No closed contour or extra partition.')] 
write(HERE/q/'spec_r55.json',d)
print('Three geometrically distinct preregistered hypotheses; no API calls.')
