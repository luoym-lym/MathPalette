from tools_b import *
import math
def meta(q):return json.loads((HERE/q/'context.json').read_text(encoding='utf-8'))
def geom(q,oid):return next(o['geometry'] for o in meta(q)['objects'] if o['id']==oid)
def mean(pts):return [sum(p[d] for p in pts)/len(pts) for d in [0,1]]
def sub(a,b):return [a[0]-b[0],a[1]-b[1]]
def radius(g):
 c=mean(g['points']);return math.dist(c,g['points'][0])
q='Plane223';ctx=meta(q);scenter=mean(geom(q,'o0')['points']);ecenter=mean(geom(q,'o41')['points'])
pairs=[]
for i in range(1,9):
 s=geom(q,'o'+str(i));e=geom(q,'o'+str(i+41));sv=sub(mean(s['points']),scenter);ev=sub(mean(e['points']),ecenter)
 err=max(abs(sv[d]+ev[d]) for d in [0,1]);rerr=abs(radius(s)-radius(e));assert err<1e-12 and rerr<1e-12
 pairs.append({'source_id':s['id'],'E_id':e['id'],'source_centered_vector':sv,'E_centered_vector':ev,'center_180_error':err,'radius_error':rerr,'fills_inverted':s['fill_color']!=e['fill_color']})
sd=sub(mean(geom(q,'o7')['points']),mean(geom(q,'o5')['points']));cd=sub(mean(geom(q,'o32')['points']),mean(geom(q,'o30')['points']))
write(HERE/q/'rigid_feature_math_audit.json',{'source_center':scenter,'E_center':ecenter,'exact180_correspondence_all8_boundary_circles':pairs,'source_anchor_displacement':sd,'C_anchor_displacement':cd,'source_anchor_squared_distance':sum(v*v for v in sd),'C_anchor_squared_distance':sum(v*v for v in cd),'unique_answer':'E','other_options':'A has an extra solid dot; B lacks ring and sufficient features; D too few dots. C fails the preserved anchor distance even before exact ring radius comparison.'})
q='Plane219';ctx=meta(q);objects={o['id']:o['geometry'] for o in ctx['objects']};base=mean(objects['o16']['points']);head=mean(objects['o17']['points']);v=sub(head,base);sang=math.atan2(v[1],v[0]);comp=[]
for k,letter in enumerate('ABCDE',start=1):
 off=28*k;center=mean(objects['o'+str(off+16)]['points']);h=mean(objects['o'+str(off+17)]['points']);w=sub(h,center);theta=math.atan2(w[1],w[0])-sang;c=math.cos(theta);s=math.sin(theta);errors=[]
 for j in range(28):
  g=objects['o'+str(j)];g2=objects['o'+str(j+off)]
  if 'points' not in g:continue
  assert len(g['points'])==len(g2['points'])
  for a,b in zip(g['points'],g2['points']):
   x,y=sub(a,base);p=[center[0]+c*x-s*y,center[1]+s*x+c*y];errors.append(math.dist(p,b))
 comp.append({'option':letter,'rotation_ccw_degrees':round(math.degrees(theta)%360,8),'max_corresponding_geometry_error':max(errors),'exact_rigid_image':max(errors)<1e-8})
assert [r['option'] for r in comp if not r['exact_rigid_image']]==['D'],comp
write(HERE/q/'rigid_rotation_math_audit.json',{'source_body_center':base,'source_head_center':head,'all_geometry_point_arrays_compared_after_head_aligned_rotation':True,'results':comp,'unique_cannot_rotate_answer':'D','tolerance':1e-8})
write(HERE/q/'primary_prescreen.json',{'question_id':q,'assessed_at':now(),'status':'prescreen_only_no_design_saved','eligible_at_start':True,'actual_original_png_viewed':True,'baseline_pixel_match':True,'formal_correct_answer':'D','math_evidence':str((HERE/q/'rigid_rotation_math_audit.json').relative_to(ROOT)),'reason':'A,B,C,E are exact rotations; D changes the spot pattern between wings. Pairing a source wing or spot with a different wing in a rotatable option could make a false reflected correspondence, but adding colored outlines directly to ladybird wings/spots risks becoming part of the rotation pattern rather than providing an unambiguous separate geometric annotation. No clean useful hypothesis was promoted merely to fill the quota.','considered_but_not_saved':'Opposite-wing pairing to A, rejected for color-as-pattern ambiguity.','design_count':0,'api_calls':0,'approval':'No Pass/Collect.'})
q='Plane246';option_sequences={'A':'SRR','B':'RSR','C':'RSS','D':'RRS','E':'SRS'};evaluated={}
for opt,seq in option_sequences.items():
 rcount=seq.count('R')%4;stamps=[]
 for i,ch in enumerate(seq):
  if ch=='S':stamps.append(seq[i+1:].count('R')%4)
 evaluated[opt]={'sequence':seq,'corner_clockwise_quarter_turns':rcount,'stamp_clockwise_quarter_turns_at_end':stamps,'matches_target':rcount==2 and set(stamps)=={1}}
assert [k for k,v in evaluated.items() if v['matches_target']]==['B']
write(HERE/q/'operation_math_audit.json',{'R':'One clockwise quarter-turn, as lower-left black corner becomes upper-left.','S':'Prints one upward club in fixed diagram orientation, leaving corner unchanged.','target':{'corner_quarter_turns':2,'club_quarter_turns':1},'all_options':evaluated,'unique_answer':'B'})
write(HERE/q/'primary_prescreen.json',{'question_id':q,'assessed_at':now(),'status':'prescreen_only_no_design_saved','eligible_at_start':True,'actual_original_png_viewed':True,'baseline_pixel_match':True,'formal_correct_answer':'B','math_evidence':str((HERE/q/'operation_math_audit.json').relative_to(ROOT)),'reason':'The corner tracks the two rotations and the club stem tracks exactly one rotation after printing, forcing RSR. A wrong RRS or SRR pairing would require mapping the asymmetric club stem to a circular lobe or privileging an operation slot without an image feature counterpart. Recoloring only corner contours is an incomplete cue that does not establish a specific wrong sequence; recoloring machine boxes would be arbitrary answer highlighting. No concrete clean wrong feature correspondence survived prescreen.','considered_but_not_saved':['Corner-only binding toward RRS; rejected as underdetermining print order.','Stem-to-lobe mapping; rejected as confusing and insufficiently geometrically justified.'],'design_count':0,'api_calls':0,'approval':'No Pass/Collect.'})
q='Plane243'
write(HERE/q/'primary_prescreen.json',{'question_id':q,'assessed_at':now(),'status':'prescreen_only_no_design_saved','eligible_at_start':True,'actual_original_png_viewed':True,'baseline_pixel_match':True,'formal_correct_answer':'E','math_status':'Formal E retained; no independently complete global tiling uniqueness proof established for a new annotated candidate.','reason':'A local false placement of trapezoid D over the dotted cell was considered. Matching its top/left boundary to existing target edges would express a partial fit but would not establish the complete tiling. Adding its missing slanted partition could be mistaken for a genuine cut or assembly boundary. No candidate was rendered or sent to API without a rigorous unchanged global placement proof and a clear annotation mechanism.','considered_but_not_saved':'Local D-at-dot edge pairing, rejected before design for unresolved global tiling proof and possible false partition ambiguity.','design_count':0,'api_calls':0,'approval':'No Pass/Collect.'})
print(json.dumps({'Plane219':comp,'Plane246':evaluated,'prescreen_only':['Plane219','Plane243','Plane246']},ensure_ascii=False),flush=True)
