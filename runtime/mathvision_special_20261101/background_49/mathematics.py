import research_env as env
import json,itertools,math
import numpy as np
from inspect_sources import save,sha,QIDS

def native(q):
 return json.loads((env.PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/q/'scene.json').read_text(encoding='utf-8-sig'))
def main():
 proofs={}
 proofs['Solid80']={'unique_answer':10,'proof':'The cut removes exactly one original vertex p101 and intersects its three incident edges in U,V,W. The other seven old corners persist. All three cut intersections are distinct new vertices; 8-1+3=10. Phantom dashed old-corner stubs are construction, not current solid edges. No invisible old edge needs to be added.','count_target':'actual vertices of the remaining block, not colored points or dashed construction junctions'}
 allcells=set(itertools.product(range(3),repeat=3))
 holes=[{p for p in allcells if all(p[j]==1 for j in range(3) if j!=a)} for a in range(3)]
 union=set.union(*holes)
 proofs['Solid89']={'unique_answer':'C','weight_grams':(27-len(union))*30,'unit_cube_mass':810/27,
  'holes':list(map(sorted,holes)),'removed_union':sorted(union),'union_size':len(union),
  'proof':'The three centered axial 1x1x3 bores consist of three cells each. Every pair and the triple intersect exactly in (1,1,1). Inclusion-exclusion gives 9-3+1=7 removed; 20 remain at30g =>600g(C). Distinct apertures are not disjoint volumes.',
  'prospective_error':{'rule':'add the three bore volumes without correcting the central overlap','removed_multiplicity':9,'result_grams':540,'choice':'A'}}
 proofs['Solid90']={'unique_answer':10,'squared_edge_lengths':{'x':45,'y':19,'z':36},
  'equations':['x+y=64 from XY','x+z=81 from YZ','y+z=55 from XZ'],
  'proof':'Three independent face-diagonal equations have the unique positive solution x=45,y=19,z=36. Adding gives 2(x+y+z)=200; requested body diagonal XA=sqrt(100)=10. A face diagonal is not an orthogonal edge.',
  'prospective_error':{'rule':'sum the three face-diagonal squares as if they were three independent orthogonal components','result_exact':'10*sqrt(2)','result_squared':200}}
 pairs=[]
 for x,y in itertools.product(range(1,20),repeat=2):
  triples=[(7,2,x),(3,4,x),(7,3,y),(2,4,y)]
  if all(2*max(t)<sum(t) for t in triples):pairs.append([x,y])
 assert pairs==[[6,5]]
 s=native('Solid107'); pts={k:np.array(v,float) for k,v in s['points'].items()}
 volume=abs(np.linalg.det(np.array([pts[k]-pts['A'] for k in ['B','C','D']])))/6
 proofs['Solid107']={'unique_answer':11,'all_integer_pairs_DB_AC':pairs,'proof':'x=DB lies strictly between5 and9 from ADB and between1 and7 from DCB; integer intersection is {6}. y=AC lies between4 and10 from ADC and2 and6 from ABC; integer intersection is {5}. Sum11. The source realization has positive tetrahedral volume, so these necessary face bounds are attainable.',
  'native_tetrahedron_volume':volume,'actual_face_incidence':{'DB':[['AD=7','AB=2'],['DC=3','CB=4']], 'AC':[['AD=7','DC=3'],['AB=2','CB=4']]},
  'prospective_error':{'rule':'rebind the two AC face-bounds to opposite-edge pairs (7,4) and (2,3), leaving DB=6','false_AC_bounds':['3<y<11','1<y<5'],'false_AC_integer':4,'wrong_total':10,'difference_from_old':'computes4 from intersecting wrongly grouped triangle bounds; does not copy CB length4 onto AC'}}
 for q in ['Solid159','Solid172']:
  s=native(q); faces=[['T','L','F'],['T','F','R'],['T','R','L'],['B','L','F'],['B','F','R'],['B','R','L']]
  order=['L','F','R','T','B']; fm=np.array([[int(v in f) for v in order] for f in faces])
  matrix=np.vstack([fm[1:]-fm[0],np.eye(5)[0],np.eye(5)[3]])
  rhs=np.array([0]*5+[5,1]); sol=np.linalg.lstsq(matrix,rhs,rcond=None)[0]
  assert np.allclose(sol,[5,5,5,1,1]) and np.linalg.matrix_rank(matrix)==5
  proofs[q]={'unique_answer':17,'native_points':s['points'],'native_labels':s['labels'],
   'six_actual_faces':faces,'incidence_degrees':dict(zip(order,fm.sum(axis=0).tolist())),
   'equal_sum_constraint_rank_with_givens':5,'unique_vertex_values':dict(zip(order,[5,5,5,1,1])),
   'proof':'Equal totals on TLF,TFR,TRL imply L=F=R=5. Comparing TLF and BLF gives T=B=1. All five values are therefore forced; sum3*5+2*1=17. The hidden LR is a true equatorial edge; the TF/LR screen crossing is not a new vertex.',
   'semantics':'The problem assigns numbers to graph vertices. Colored edge stubs are comparisons of incidences; neither edge length nor color is a new number equality condition. No material paper/color transport is requested.'}
 proofs['Solid159']['prospective_error']={'rule':'transfer equatorial degree4 to both degree3 apices and divide all six equal face sums by4','face_sum':11,'six_face_total':66,'wrong_total':16.5,'correct_incidence_identity':'66=4*(5+5+5)+3*(1+1)','old_error_different':'Old swaps the three-member and two-member value groups and predicts13; new retains vertex values but uses wrong incidence divisor.'}
 proofs['Solid172']['prospective_error']={'rule':'treat the two visible three-arm stars at horizontal extremes L,R as the apex pair; propagate5 twice and1 to the remaining triple','wrong_total':13,'actual_diagnostic':'L and R each have degree4 including the preserved hidden LR; T and B are the actual degree3 apex pair.'}
 poly=native('Solid171')['polyhedra'][0]
 edges={tuple(sorted((a,b))) for f in poly['faces'] for a,b in zip(f,f[1:]+f[:1])}
 triangular=[f for f in poly['faces'] if len(f)==3]
 new={tuple(sorted((a,b))) for f in triangular for a,b in zip(f,f[1:]+f[:1])}
 assert len(edges)==36 and len(new)==24 and len(triangular)==8
 proofs['Solid171']={'unique_answer':36,'vertices':len(poly['vertices']),'face_count':len(poly['faces']),
  'exact_edges':sorted(edges),'triangle_faces':triangular,'new_triangle_edges':sorted(new),'remaining_original_edges':sorted(edges-new),
  'proof':'All8 cube corners are separately truncated. Each of12 original edges survives as one remnant. Each of8 new triangular faces contributes3 edges, none shared with another triangular face, so12+8*3=36. Independently face incidence gives (6*8+8*3)/2=36, and Euler24-36+14=2.',
  'prospective_error':{'rule':'transfer one-edge counting unit from an original remnant to an entire three-edge triangular cut-face boundary','wrong_total':12+8,'missing_edges':16}}
 n=native('Solid163'); a=n['two_view_verification']; vis=set(map(tuple,a['visible_cells_each']))
 bs=[set(map(tuple,a[k])) for k in ['first_visible_black','second_visible_black']]
 ws=[vis-b for b in bs]; cases=[]
 rotations=[]
 for perm in itertools.permutations(range(3)):
  for signs in itertools.product([-1,1],repeat=3):
   m=np.zeros((3,3),int)
   for i,j in enumerate(perm):m[i,j]=signs[i]
   if round(np.linalg.det(m))==1:rotations.append(m)
 for m in rotations:
  rot=lambda ss:{tuple((m@(np.array(p)-1)+1).tolist()) for p in ss}
  b,w=rot(bs[1]),rot(ws[1]); conflicts=(bs[0]&w)|(ws[0]&b)
  white=ws[0]|w; black=bs[0]|b; free=allcells-white-black
  cases.append({'matrix':m.tolist(),'conflict_cells':sorted(conflicts),'consistent':not conflicts,
   'white_union':sorted(white),'forced_black':sorted(black),'free_cells':sorted(free),
   'maximum_black':27-len(white),'double_counted_white':sorted(ws[0]&w)})
 good=[c for c in cases if c['consistent']]; assert len(good)==1 and good[0]['maximum_black']==9
 proofs['Solid163']={'unique_maximum':9,'first_visible_black':sorted(bs[0]),'second_visible_black':sorted(bs[1]),
  'first_visible_white':sorted(ws[0]),'second_visible_white':sorted(ws[1]),'proper_rotations_enumerated':24,
  'cases':cases,'compatible_cases':good,'proof':'Each small cube is uniformly either white or black. Read each visible face cell, identify repeated face appearances of the same boundary cube, and compare the two views over all24 proper cube rotations. Exactly one orientation is compatible with both colors. Its forced white union has18 distinct cubes; the remaining9 can all be black, including every free unseen cell. Thus upper bound9 is attained.',
  'source_semantic_warning':'Outlining an entire white cell is not allowed to fill it or add a third kind. Adding any dark dot at a grid corner can be read as another vertex; not an acceptable counting mark.'}
 for q,p in proofs.items():save(env.ROOT/q/'primary_math_proof.json',p)
 print(json.dumps({'unique_answers':{q:p.get('unique_answer',p.get('unique_maximum')) for q,p in proofs.items()},'Solid163_consistent':good},ensure_ascii=False))
if __name__=='__main__':main()
