"""Exact arithmetic support for the written PRIMARY proofs, not a second review."""
import research as r
from fractions import Fraction as F

# (a,b) means a+b*sqrt(3). Every operation is exact rational arithmetic.
def q(a=0,b=0): return F(a),F(b)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def mul(x,y): return x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def rotate(p,c,s): return add(mul(c,p[0]),neg(mul(s,p[1]))),add(mul(s,p[0]),mul(c,p[1]))
def edge(a,b): return frozenset((a,b))

points={'A':(q(),q()),'B':(q(-1),q()),'C':(q(F(-1,2)),q(0,F(-1,2))),
        'D':(q(F(1,2)),q(0,F(-1,2)))}
rotations={60:(q(F(1,2)),q(0,F(1,2))),120:(q(F(-1,2)),q(0,F(1,2))),
           180:(q(-1),q()),240:(q(F(-1,2)),q(0,F(-1,2))),300:(q(F(1,2)),q(0,F(-1,2)))}
target={points[k] for k in 'ABC'}
table={str(angle):{k:next((name for name,v in points.items() if v==rotate(points[k],*matrix)),None) for k in 'ACD'}
       for angle,matrix in rotations.items()}
matches={str(angle):{rotate(points[k],*matrix) for k in 'ACD'}==target for angle,matrix in rotations.items()}
assert [k for k,v in matches.items() if v]==['300']
source_colors=[('A','C','blue'),('A','D','blue'),('C','D','red')]
target_colors={edge(points[a],points[b]):color for a,b,color in [('A','B','blue'),('A','C','blue'),('B','C','red')]}
color321=all(target_colors[edge(rotate(points[a],*rotations[300]),rotate(points[b],*rotations[300]))]==color for a,b,color in source_colors)
assert color321
r.save(r.OWN/'Plane321/exact_mathematical_checks.json',{'role':'PRIMARY exact support, not independent second review',
    'arithmetic':'Exact Fraction pairs in Q(sqrt(3)); no floating point tolerance',
    'option_vertex_matches':table,'whole_triangle_matches':matches,
    'colored_edge_sets_match_under300':color321,
    'continuous_angle_exclusion':'The written proof exhausts both possible permutations of the nonfixed vertices. This finite option check supplements that proof; it does not replace continuous uniqueness.'},new=True)

proof=r.read(r.OWN/'Plane490/primary_math_proof.json')
light=list(map(tuple,proof['light_vertices'])); dark=list(map(tuple,proof['dark_vertices']))
negp=lambda p:tuple(-x for x in p)
assert [negp(p) for p in dark]==light
means={name:[sum(v[i] for v in vertices)/len(vertices) for i in (0,1)] for name,vertices in [('light',light),('dark',dark)]}
assert means=={'light':[2.0,1.0],'dark':[-2.0,-1.0]}
corners={name:[(vertices[(i+1)%7][0]-p[0])*(vertices[(i-1)%7][1]-p[1])-(vertices[(i+1)%7][1]-p[1])*(vertices[(i-1)%7][0]-p[0]) for i,p in enumerate(vertices)] for name,vertices in [('light',light),('dark',dark)]}
assert all(all(c!=0 for c in values) for values in corners.values())
common_colors={edge((F(-4),F(0)),(F(4),F(0))):'blue',edge((F(-4),F(0)),(F(-4),F(2))):'red',edge((F(4),F(-2)),(F(4),F(0))):'red'}
assert all(common_colors[edge(*[negp(p) for p in e])]==color for e,color in common_colors.items())
strips={}
for name,vertices in [('light',light),('dark',dark)]:
    strips[name]={}
    for i,color in [(2,'red'),(3,'blue')]:
        a,b=vertices[i],vertices[(i+1)%7]
        ends=[tuple(F(a[k])+(F(b[k])-a[k])*t for k in (0,1)) for t in (F(1,4),F(3,4))]
        strips[name][edge(*ends)]=color
assert all(strips['light'][edge(*[negp(p) for p in e])]==color for e,color in strips['dark'].items())
r.save(r.OWN/'Plane490/exact_mathematical_checks.json',{'role':'PRIMARY exact support, not independent second review',
    'corner_integer_determinants':corners,'all7_are_genuine_corners':True,
    'exact_vertex_sums':{'light':[14,7],'dark':[-14,-7]},'all_corresponding_vertices_negate':True,
    'mean_nonzero_forces_unique_angle_mod360':'180','existence_verified_by_all_vertices':True,
    'A01_colored_sharedZ_invariant_under180':True,'A02_colored_middle_half_flank_strips_correspond_under180':True,
    'arithmetic':'Integer polygon coordinates and exact Fraction strip endpoints; no tolerance used.'},new=True)

copies={}
for qid in ('Plane321','Plane490'):
    row=r.eligibility(qid)['record']; branch=r.PROJECT/'PlaneGeometry'
    for field,out in [('image','formal.png'),('original_image','source.jpg'),('scene','formal_scene.json')]:
        source=branch/row[field]; target=r.OWN/qid/out
        target.write_bytes(source.read_bytes())
        assert r.sha(source)==r.sha(target)
        copies[str(target.relative_to(r.OWN))]={'source':str(source),'sha256':r.sha(source),'copy_bytes_equal':True}
r.save(r.OWN/'native_sources_preserved.json',{'created_at':r.now(),'copies':copies,'no_original_modified':True},new=True)
observations={
 'Plane217':'Four original holes paired diagonally red/blue; optionA existing crossing dotted lines red down/right and blue up/right.',
 'Plane233':'Original and optionC open L boundaries: four-cell vertical left red and two-cell lower horizontal blue. No source internal partitions.',
 'Plane308':'Original odd1/3/5 red and even2/4/6 blue; optionA two actual triangles paired red/blue. Not old consecutive groups.',
 'Plane427':'ST/TV real equal legs red, dottedSV blue, both original angle arcs retained. Not old reversed colors.',
 'Solid126':'Removed/top boundaries red and depth edges blue; removed2 overwritten blue is final visible action, so old covered red has no separate information.',
 'Solid142':'Left cut red and top cut blue, optionA vertical diamond hole pairs red horizontal positions and blue vertical positions.',
 'Solid167':'Two actual cuts red/blue and optionA vertical diamond pairs; not old optionD horizontal-diamond mapping.',
 'Solid176':'Four actual triangle-flap sides in optionD red; dashed folds retained, compares closing flaps rather than full option emphasis.',
 'Solid203':'Original x edge and labelC edge red, other outline/labels/octahedron retained; not oldA target.'}
r.save(r.OWN/'reference_primary_observations.json',{'created_at':r.now(),'all9_current_C01_PNG_individually_viewed':True,
    'all_C01_plugins_recipes_reference_JSON_fully_parsed':True,'observations':observations,
    'source_preservation':'initial_read_manifest.json; full JSON contents in reference_full_read.json',
    'repeated_recipe_and_accepted_content_checked_equal':True,'role':'Primary reference transfer research only'},new=True)
print('Exact mathematics, compatible color mappings, native copies and nine current-reference observations saved.')
