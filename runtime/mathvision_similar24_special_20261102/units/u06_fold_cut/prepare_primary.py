from local_env import *
import json, importlib.util

REFS=read_json(OWN/'reference_read_inventory.json')
proof146={
 'kind':'primary independent mathematical derivation, not independent second review',
 'normalization':'Use paper [-1,1] x [0,1], folded on x=0 into Q=[0,1] x [0,1]. Each picture is schematic; panel display offsets and the 1.8:1 drawn choice boxes are not extra length givens.',
 'cut_invariant':'Without an extra fold/rearrangement, each straight cutting pass is supported by one line in Q. Removing pieces or interrupting a cut cannot increase the number of supporting lines. Two passes therefore supply at most two distinct cutting lines in Q. This support-line argument does not assume that a later cut through a disconnected region creates only one segment.',
 'constructive_exhaustion':{
   'A':{'cuts':[[[0,.2],[.4,0]],[[0,.8],[.4,1]]], 'discard':'Discard bottom and top triangles at folded edge x=0. Reflection gives one central V at each of the two horizontal boundaries.'},
   'B':{'cuts':[[[0,.2],[.4,.5]],[[.4,.5],[0,.8]]], 'discard':'Discard the triangle touching the fold with vertices (0,.2),(.4,.5),(0,.8). Reflection produces one internal diamond.'},
   'C':{'cuts':[[[.7,0],[1,.2]],[[.7,1],[1,.8]]], 'discard':'Clip the two outer corners of Q at x=1. Reflection clips all four corners of the original rectangle.'},
   'E':{'cuts':[[[0,.52],[.48,0]],[[.5,1],[1,.53]]], 'discard':'The first cut removes the bottom folded corner, giving a central bottom V after unfolding; the second clips the upper outer corner, giving the two upper corner chamfers. No top-bottom symmetry is required by one vertical fold.'}},
 'D_impossible':'The right half of D contains a full V at the top and a full inverted V at the bottom, each strictly away from x=0 and x=1. The four slanted segments have four distinct support lines. In the actual frozen coordinates their top and bottom vertices have y=2.25-.28 and y=1.25+.28 and their respective base halfwidth is .27. Each V needs both slopes; a top supporting line and bottom supporting line of the same slope have different intercepts. Thus at least four straight passes are necessary in Q; two cannot make D. Coloring a slope class cannot identify displaced parallel lines as one pass.',
 'unique_answer':'D',
 'source_originals_viewed':True,'formal_png_viewed':True,
 'semantic_scope':'The source specifies one fold and two freely chosen straight cuts. The scissors in Solid174 are an illustrative tool, not an additional specified cut or direction.'}

proof239={
 'kind':'primary independent mathematical derivation, not independent second review',
 'fold_assignment':'The closed packet has layered open top/left edges; bottom/right are crease edges. Gray front versus banded reverse is material-side coding retained unchanged.',
 'normalized_setup':'Take Q=[0,1]^2 in the coincident closed stack, creases x=1 and y=0. The given cut joins P=(1/2,0) to R=(1,1/2), cutting off triangle T with third vertex C=(1,0).',
 'unfold_maps':['(x,y)','(2-x,y)','(x,-y)','(2-x,-y)'],
 'constructive_result':'The union of those four closed triangles has boundary vertices (1/2,0),(1,1/2),(3/2,0),(1,-1/2). Its interior is a single central diamond in the full square [0,2] x [-1,1], with area 1/2, i.e. 1/8 of the full paper. No outer boundary is reached: every diamond point has 1/2<=x<=3/2 and -1/2<=y<=1/2.',
 'exhaustive_choices':{'A':'Four outer notches modify all four sides; impossible because the removed diamond is strictly internal.',
 'B':'Two outer notches modify top/bottom; impossible for the same internal-location invariant.',
 'C':'Internal axis-aligned square has horizontal/vertical sides. Reflected original cut lines have slopes +1/-1; no horizontal/vertical hole edge is created.',
 'D':'Triangle is not invariant under both crease reflections. Its horizontal base is an old crease, not a new cut, and cannot be a final hole edge.',
 'E':'Has exactly the constructed internal diamond with the original outside square. Unique.'},
 'unique_answer':'E','source_originals_viewed':True,'formal_png_viewed':True,
 'visibility_scope':'The slightly separated display layers reveal four coincident layers without changing the material fold map; all world points, projection matrix, intervals, bands and layer outlines are frozen.'}

proof220={
 'kind':'primary independent mathematical derivation, not independent second review',
 'fold_assignment':'Exactly one fold. The left vertical edge of the displayed remaining half-sheet, x=13 in its local display panel, is the fold; the right straight edge is an outside edge. Reflect the whole removed half-opening about x=13.',
 'analytic_cut':'The cut joins (13,5.4) and (13,6.6) on the fold. It has circular arc portions of radius .6 centered at (13,6) and one three-point zigzag on the right, with middle tip (14.25,6) and two side tips (13.98,5.55),(13.98,6.45). Its reflected partner supplies the left three-point zigzag. The removed half-opening has a segment of positive length on the crease, so the two removed interiors join across an interval, not a single point.',
 'construction':'After reflection there is one connected finite-width rounded central opening with three points on both left and right. Translate center (13,6) to (20,0) to obtain the native D contour. The fold line is an axis of the whole opening, not two local axes of separate holes.',
 'exhaustive_choices':{'A':'Two single-sided openings have disjoint interiors. Their star tips may touch at a point at the fold, but a point does not reproduce the positive-width central opening.',
 'B':'Two outward-pointing openings have separate interiors; their circular boundaries can be tangent, still no positive-width joined center.',
 'C':'Only one right zigzag and no left reflected zigzag; not invariant under the displayed vertical fold.',
 'D':'One central rounded region and two mirrored outer zigzags, exactly the reflected half-cut.',
 'E':'Two separate locally double-sided openings, with local centers away from the global fold; a point contact at the seam does not connect their interiors. It duplicates an already completed reflection instead of joining the two halves.'},
 'unique_answer':'D','source_originals_viewed':True,'formal_png_viewed':True,
 'display_note':'Curve sample vertices are rendering construction samples, not new physical vertices or extra cuts. No new fold is permitted.'}

def interval(qid, target, first, end, color, width=1.5):
    p=read_json(OWN/qid/'raw_paths.json')[target][0]
    n=len(p['segments'])
    assert 0<=first<end<=n
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,
            'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':first/n,'end':end/n,'wrap':False}}

items=[]
for qid in ['Solid146','Solid174']:
    target='line23' if qid=='Solid146' else 'line27'
    paths=read_json(OWN/qid/'raw_paths.json')[target][0]
    actions=[];roles=[]
    for i, segment in enumerate(paths['segments']):
        a,b=segment['control']
        dx=b[0]-a[0];dy=b[1]-a[1]
        if abs(dx)<1e-12 or abs(dy)<1e-12: continue
        color='#DC2626' if dx*dy>0 else '#2563EB'
        actions.append(interval(qid,target,i,i+1,color))
        roles.append({'action_index':len(actions)-1,'source':{'option':'D','original_segment_index':i,'control':segment['control']},
                      'receiver':'Other D notch slants with the same slope direction',
                      'information':'Compare repeated slope directions at separate cutting locations. Red is increasing y with x, blue decreasing y with x. These are directions, not proof of one cut per color.',
                      'misreading_target':'Collapse the four different cutting lines in a folded half into two color/direction classes, then reject E for lacking top-bottom symmetry.',
                      'necessity':'This one side is one member of the parallel-direction comparison; horizontal/vertical retained edges stay black.'})
    assert len(actions)==8
    items.append((qid,'parallel_cut_direction_alias','E',actions,roles,proof146,
      'The source contains no specified cut. Transfer only the reference principle of comparing real cut-boundary directions: compare existing slants within D, never draw a cut on the folded blank. Supplemental current Solid176 shows useful within-option edge comparison is allowed when the paired edges carry a concrete role.',
      'The old prescreen found no true source cut to pair and made zero calls. This design supplies a different concrete input relation: slope-class pairing across four existing D notches, not an invented source cut or an entire option color. No earlier candidate PNG exists for this formal question.',
      'Only D is colored. On an annotation reading its four distinct cutting lines remain impossible. On a literal colored-paper reading D remains impossible (already fails geometry), while the uncolored blank source and A/B/C/E are unchanged and retain their explicit two-cut constructions. Therefore D remains the unique answer under both readings.'))

qid='Solid239'
actions=[{'type':'set_object_style','target':'line148','color':'#DC2626','linewidth_pt':1.5}]
roles=[{'action_index':0,'source':'The already specified diagonal dashed cutting instruction','receiver':'The two rising boundary-notch sides of B','information':'Identifies the only original straight cut and its direction without altering dashes, endpoints or adding a line.','necessity':'Provides the actual source cutting direction for the output comparison.'}]
for i in [1,2,6,7]:
    # B bottom and top Vs: compare inherited versus reflected directions.
    p=read_json(OWN/qid/'raw_paths.json')['line153'][0]
    aa,bb=p['segments'][i]['control']
    color='#DC2626' if (bb[0]-aa[0])*(bb[1]-aa[1])>0 else '#2563EB'
    actions.append(interval(qid,'line153',i,i+1,color))
    roles.append({'action_index':len(actions)-1,'source':'Original diagonal cut; red original slope, blue its reflected opposite slope',
                  'receiver':{'option':'B','segment':i,'control':[aa,bb]},
                  'information':'Compare the two mirror-paired Vs at opposite outer borders, as if a crease endpoint were an open perimeter endpoint.',
                  'necessity':'Each of the four sides is a specific cut/mirror counterpart; black outside straight edges retain the distinction between notch and internal hole.'})
items.append((qid,'cut_to_opposite_border_notches','B',actions,roles,proof239,
 'From current Solid142/Solid167 transfer cut-to-unfolded-edge direction pairing. Here there is one specified dashed cut, so red identifies its original direction and blue the reflected direction in B. Do not copy their two-cut count or old option letters.',
 'Old single_unfold_triangle_binding paired one diagonal to D and treated a crease as its base (D preset); crease_axes_as_hole_edges paired two crease directions to C (C preset). Both returned E/E. New B relation compares four slants at two outer-border notches with the actual cut, targeting boundary-location versus central-hole mapping. It does not recolor a fold edge, does not retain either old receiver or tested PNG, and does not merely change an option letter in the same local feature matching.',
 'The only source color lies on the explicitly named dashed cutting instruction, not on a physical paper boundary or a reverse-side band. A dashed line to be cut is an instruction whose color does not require colored ink to survive on the final hole. The uncolored correct E exactly retains the material shape. Colored B remains geometrically impossible even if its output boundary is read as physical ink. No alternate answer or no-answer reading is created.'))

qid='Plane220'
actions=[interval(qid,'o17',50,56,'#DC2626'),interval(qid,'o17',107,113,'#2563EB'),
         interval(qid,'o18',50,56,'#2563EB'),interval(qid,'o18',107,113,'#DC2626')]
roles=[
 {'action_index':0,'source':'E left component outer zigzag','receiver':'E right component outer zigzag (action 3)','information':'Red pairs the two outer three-point tips under reflection about the actual global dotted fold; source half-cut has a three-point zigzag.','necessity':'First member of outer correspondence.'},
 {'action_index':1,'source':'E left component inward zigzag near global seam','receiver':'E right component inward zigzag (action 2)','information':'Blue pairs the extra inward tips under the same global reflection. Each component also has its own local reflection pair, unlike A single-sided raw copies.','necessity':'First member of inner correspondence; exposes the second reflection level.'},
 {'action_index':2,'source':'E right component inward zigzag','receiver':'Action 1','information':'Second member of inner correspondence; the point contact at the fold stays visible.','necessity':'Completes the actual inner pair.'},
 {'action_index':3,'source':'E right component outward zigzag','receiver':'Action 0','information':'Second member of outer correspondence. Together the four lobes suggest two already-completed symmetric holes for the two layers.','necessity':'Completes the actual outer pair.'}]
items.append((qid,'nested_mirror_component_duplication','E',actions,roles,proof220,
 'Transfer current red/blue groups of concrete cut-edge counterparts, and current Solid176 intra-option paired-edge comparison. Source paper remains unstyled because its real boundary could otherwise become intrinsic printed edging. Here red identifies the outer mirror pair and blue the inner pair across the global seam; these are specific existing zigzags, not a colored whole option.',
 'Old C copied a single arc/star profile; old A duplicated two single-sided raw profiles, with presets C and A and finals A/C and E/A. This E design compares inner versus outer zigzag pairs at two levels of reflection: each E component is itself a full double-sided completion, and the two components are then duplicated about the global fold. It is a completion-then-duplication misconception, not the prior raw-profile-copy mechanism. No source arc or source star is colored, no full E circular contour is colored, and the existing seam/contact stays unaltered. Prior refinement only considered A-to-B direction swap, arc recolor and new seam; none is used here.',
 'Source remains entirely uncolored and retains its original one-fold meaning. Correct D stays entirely unchanged. E fails connected-interior/size geometry with or without colors; interpreting red/blue as E intrinsic edging cannot make E possible or invalidate D. A/B/C are untouched. Hence D stays uniquely correct under both readings.'))

manifest=[]
for qid,vid,wrong,actions,roles,proof,transfer,diff,semantics in items:
    root=OWN/qid
    candidate=root/vid
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':vid,'intent':'Concrete existing cut-edge comparison; preserve original unique solution.',
            'params':{'actions':actions}}
    save(candidate/'plugin.json',plugin,True)
    save(candidate/'mathematics.json',proof,True)
    save(candidate/'reference_transfer.json',{'current_references':[r for r in REFS if r['id'] in ['Solid142','Solid167','Solid176']],
          'all_nine_PNGs_actually_viewed':True,'migration':transfer,'old18_not_authority':True},True)
    save(candidate/'history_difference_audit.json',{'question_id':qid,'difference':diff,
           'old_full_read_inventory':str(root/'history_files_read.json'),'old_full_raw_responses':str(root/'history_raw_responses_full.json'),
           'new_hypothesis_not_postoutput':True},True)
    save(candidate/'premodel_primary_reasoning.json',{'created_at':now(),'question_id':qid,'variant_id':vid,
           'expected_wrong_answer':wrong,'expected_wrong_value':wrong,'formal_correct_answer':proof['unique_answer'],
           'each_action_role':roles,'human_semantics_both_readings':semantics,
           'conciseness':'No new points, lines, labels, cuts, folds or full-option outline styles. All actions cover one necessary comparison member; no fully overwritten actions.',
           'primary_only':True,'API_calls_at_creation':0,'native_candidate_visual_review_pending':True},True)
    manifest.append({'question_id':qid,'variant_id':vid,'candidate_directory':str(candidate),'expected_wrong_answer':wrong,'correct_answer':proof['unique_answer']})
save(OWN/'primary_design_manifest.json',manifest,True)
checkpoint=read_json(OWN/'checkpoint.json')
checkpoint['phase']='four_material_hypotheses_prepared_pending_render'
checkpoint['updated_at']=now()
for item in manifest:
    checkpoint['questions'][item['question_id']]={'status':'prepared_pending_render','variant_id':item['variant_id'],'calls':0}
save(OWN/'checkpoint.json',checkpoint)
print(json.dumps(manifest,ensure_ascii=False,indent=2))
