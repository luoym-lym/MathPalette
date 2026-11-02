from bootstrap import *
from itertools import combinations
from fractions import Fraction

def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def local(c,e):
 x=min(p[0] for p in c);y=min(p[1] for p in c)
 return {(a-x,b-y):v for (a,b),v in c.items()},{edge((a-x,b-y),(u-x,v-y)):col for ((a,b),(u,v)),col in e.items()}
def boundary(c):
 z={}
 for x,y in c:
  p=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
  for a,b in zip(p,p[1:]+p[:1]):z[edge(a,b)]='#000000'
 return z
def transform(p,k,flip):
 x,y=p
 if flip:x=-x
 for _ in range(k):x,y=-y,x
 return x,y
def variants(c,e,reflections):
 seen=set();out=[]
 for flip in ([False,True] if reflections else [False]):
  for k in range(4):
   # Transform unit cells through their four vertices, not their lower-left coordinates alone.
   cc={}
   for (x,y),v in c.items():
    ps=[transform(p,k,flip) for p in [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]]
    cc[min(a for a,b in ps),min(b for a,b in ps)]=v
   ee={edge(transform(a,k,flip),transform(b,k,flip)):col for (a,b),col in e.items()}
   cc,ee=local(cc,ee);key=(tuple(sorted(cc.items())),tuple(sorted(ee.items())))
   if key in seen:continue
   seen.add(key);out.append((flip,k,cc,ee))
 return out
def fits(c,e,board,ink,match_fill,match_ink,reflections):
 out=[]
 for f,k,cc,ee in variants(c,e,reflections):
  for dx in range(int(max(x for x,y in board))+1):
   for dy in range(int(max(y for x,y in board))+1):
    moved={(x+dx,y+dy):v for (x,y),v in cc.items()}
    inks={edge((x+dx,y+dy),(a+dx,b+dy)):v for ((x,y),(a,b)),v in ee.items()}
    if not set(moved)<=set(board):continue
    if match_fill and any(board[p]!=v for p,v in moved.items()):continue
    if match_ink and any(ink.get(p)!=v for p,v in inks.items()):continue
    out.append({'flip':f,'quarter_turns':k,'translation':[dx,dy],'cells':moved,'ink':inks})
 unique=[];seen=set()
 for p in out:
  key=(tuple(sorted(p['cells'].items())),tuple(sorted(p['ink'].items())) if match_ink else ())
  if key not in seen:seen.add(key);unique.append(p)
 return unique
def enc(p):return {'flip':p['flip'],'quarter_turns':p['quarter_turns'],'translation':p['translation'],'cells':[[*xy,v] for xy,v in sorted(p['cells'].items())],'colored_edges':[{'endpoints':e,'color':c} for e,c in sorted(p['ink'].items()) if c!='#000000']}

allresults={}
for q in ['Plane218','Plane398']:
 elig=eligibility(q);scene=read(ROOT/'PlaneGeometry'/elig['formal_record']['scene'])
 variant={'Plane218':'p03_native_outer_boundary_conservation','Plane398':'p03_native_L_arm_transport_all_options'}[q]
 cp=SOURCE/q/variant;plugin=read(cp/'plugin.json');design=read(cp/'design.json')
 objs={o['id']:o for o in scene['objects']};groups={};coords={};edgegroups={}
 if q=='Plane218':
  for oid,o in objs.items():
   if o['type']!='segment':continue
   g=oid.split('_')[0];edgegroups.setdefault(g,{})[edge(*o['points'])]='#000000'
  for g,eds in edgegroups.items():
   vertices={p for e in eds for p in e};cells={}
   for x,y in vertices:
    ps=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    if all(edge(a,b) in eds for a,b in zip(ps,ps[1:]+ps[:1])):cells[x,y]=False
   groups[g]=cells
 else:
  for oid,o in objs.items():
   if not oid.startswith('cell'):continue
   ps=[scene['points'][p] for p in o['points']];xs=set(p[0] for p in ps);ys=set(p[1] for p in ps)
   assert len(xs)==len(ys)==2 and max(xs)-min(xs)==max(ys)-min(ys)==1
   g='piece1' if oid.startswith('cellpiece1') else 'piece2' if oid.startswith('cellpiece2') else oid[4]
   groups.setdefault(g,{})[min(xs),min(ys)]=bool(o.get('semantic_fill',False));coords[oid]=ps
  edgegroups={g:boundary(c) for g,c in groups.items()}
 checks=[];marked=set()
 for i,a in enumerate(plugin['params']['actions']):
  assert a['type']=='set_object_style' and a['linewidth_pt']==1.5 and set(a)<=set(['type','target','color','linewidth_pt','interval'])
  oid=a['target'];o=objs[oid];g=oid.split('_')[0] if q=='Plane218' else 'piece2' if oid.startswith('cellpiece2') else oid[4]
  if q=='Plane218':eds=[edge(*o['points'])]
  else:
   iv=a['interval'];assert iv['wrap'] is False and iv['end']-iv['start']==0.25
   # Native polygons are four unit edges in stored vertex order; interval spans exactly one.
   z=Fraction(str(iv['start']))*4;assert z.denominator==1;k=int(z);eds=[edge(coords[oid][k],coords[oid][(k+1)%4])]
  for e in eds:
   assert e in edgegroups[g] and (g,e) not in marked
   marked.add((g,e));edgegroups[g][e]=a['color']
   assert sum(e in boundary({cell:False}) for cell in groups[g])==1,'Marked line must be actual exterior boundary'
  checks.append({'index':i,'target':oid,'group':g,'exact_geometry_endpoints':eds,'color':a['color'],'native_exterior_edge':True,'no_duplicate_or_ineffective_mark':True,'information_role':('source perimeter total' if g=='given' else 'transported option perimeter; retained-red accounting' ) if q=='Plane218' else ('source L arm identity' if g=='piece2' else 'A clockwise-quarter-turn arm identity' if g=='A' else 'E trial arm placement, black-white mismatch remains visible' if g=='E' else 'valid zero-turn L arm transport')})
 groups={g:local(c,edgegroups[g])[0] for g,c in groups.items()}
 # Normalize edges separately with the original group origins (groups now normalized).
 originalgroups={}
 if q=='Plane218':
  for g in edgegroups:
   vertices={p for e in edgegroups[g] for p in e};originalgroups[g]={(min(p[0] for p in vertices),min(p[1] for p in vertices)):False}
 else:
  for g in edgegroups:
   ps={p for e in edgegroups[g] for p in e};originalgroups[g]={(min(x for x,y in ps),min(y for x,y in ps)):False}
 inks={g:local(originalgroups[g],e)[1] for g,e in edgegroups.items()}
 results={}
 for l in 'ABCDE':
  if q=='Plane218':
   assert len(groups[l])==5 and len(groups['given'])==12
   p=fits(groups[l],inks[l],groups['given'],inks['given'],False,False,True)
   sols=[(a,b) for a,b in combinations(range(len(p)),2) if not(set(p[a]['cells'])&set(p[b]['cells']))]
   ip=fits(groups[l],inks[l],groups['given'],inks['given'],False,True,False)
   isol=[(a,b) for a,b in combinations(range(len(ip)),2) if not(set(ip[a]['cells'])&set(ip[b]['cells']))]
   results[l]={'D4_geometric_disjoint_pairs':len(sols),'rotation_ink_disjoint_pairs':len(isol),'red_units_per_copy':sum(c=='#DC2626' for c in inks[l].values()),'ink_witness':[enc(ip[i]) for i in isol[0]] if isol else []}
  else:
   p=[fits(groups[g],inks[g],groups[l],inks[l],True,False,True) for g in ['piece1','piece2']]
   sols=[(i,j) for i,a in enumerate(p[0]) for j,b in enumerate(p[1]) if not(set(a['cells'])&set(b['cells'])) and set(a['cells'])|set(b['cells'])==set(groups[l])]
   ip=[fits(groups[g],inks[g],groups[l],inks[l],True,True,False) for g in ['piece1','piece2']]
   isol=[(i,j) for i,a in enumerate(ip[0]) for j,b in enumerate(ip[1]) if not(set(a['cells'])&set(b['cells'])) and set(a['cells'])|set(b['cells'])==set(groups[l])]
   results[l]={'D4_pattern_assemblies':len(sols),'rotation_ink_assemblies':len(isol),'ink_witness':{g:enc(ip[k][idx]) for k,(g,idx) in enumerate(zip(['piece1','piece2'],isol[0]))} if isol else {}}
 unique=[l for l,v in results.items() if (v.get('D4_geometric_disjoint_pairs',v.get('D4_pattern_assemblies'))==0)]
 intrinsic=[l for l,v in results.items() if v.get('rotation_ink_disjoint_pairs',v.get('rotation_ink_assemblies'))==0]
 assert unique==intrinsic==[{'Plane218':'A','Plane398':'E'}[q]]
 report={'question_id':q,'at_utc':now(),'scope':'OFFLINE recovery preparation, not independent second review or qualification','correct_answer_independently_derived':unique[0],'intrinsic_colored_material_reading_unique_answer':intrinsic[0],'all_native_formal_source_and_reference_images_viewed':True,'exact_native_scene_path':str(ROOT/'PlaneGeometry'/elig['formal_record']['scene']),'native_scene_sha256':sha(ROOT/'PlaneGeometry'/elig['formal_record']['scene']),'geometry_extraction':'Fresh extraction from current formal scene. No source worker imports or source proof results used as premise. All unit edges, cell fills and plugin interval spans checked exactly.','completeness':('Enumerate every grid D4 orientation, contained integer translation and unordered disjoint pair; cut along displayed square grid; two pentominoes leave TWO unused cells. This is not a 12-cell tiling task.' if q=='Plane218' else 'The 7-cell L includes endpoints at diameter 4 sqrt(2), equal to 4x4 target diameter, forcing those endpoints to opposite target corners in any isometry. Its orientation is therefore a quarter-turn/reflection and corner aligned. Enumerate all such transforms and all translations, preserve black/white cells and require full 16-cell coverage.'),'marked_action_count':len(checks),'every_marker':checks,'groups_cells':{g:[[*p,v] for p,v in sorted(c.items())] for g,c in groups.items()},'results':results,'frozen_wrong_preset':design['expected_wrong_answer'],'mechanism_hypothesis_only':design['mechanism'],'human_clarity':'Native thin exterior-only runs leave fills, labels, cell junctions and diagnostic contours visible. Each contiguous run identifies a source/target length or transported arm. There are no new cuts or false interior partitions. Exact intrinsic-ink witnesses for every feasible option prove that reading the colors as actual ink does not remove a valid answer. Source/user233 uses true open boundary correspondences; transfer follows that method. No model effect is established.','caveat':('A has no valid two-piece placement, so source design phrase inherited boundary in a legal cut placement of A is too broad: an individual A copy fits but a pair does not. This fresh audit does not repeat that claim.' if q=='Plane218' else 'E colored local L spans are a real trial only, not a valid full assembly. The frozen wrong-A mechanism remains untested.'),'new_API_calls':0}
 save(OWN/q/'fresh_math_and_markers_v2.json',report);allresults[q]={l:{k:v for k,v in d.items() if k!='ink_witness'} for l,d in results.items()}
print(json.dumps(allresults,ensure_ascii=False))
