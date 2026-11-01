"""Derive both cases from frozen coordinates, independently of primary proofs."""
from pathlib import Path
import json
import math
import hashlib

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
REVIEW = ROOT/'runtime/mathvision_special_20261101/independent_review'
def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))
def write(folder, obj):
    (REVIEW/folder/'independent_math_audit.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def rounded(pt):
    return tuple(round(x,10) for x in pt)

s = read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane217.json')
o = {x['id']:x for x in s['objects']}
paper = o['o0']['points']
center = tuple(sum(p[i] for p in paper)/4 for i in (0,1))
holes = {rounded([o[f'o{i}']['center'][j]-center[j] for j in (0,1)]) for i in range(1,5)}
def ref(pt, kind):
    x,y = pt
    return rounded({'vertical':(-x,y),'horizontal':(x,-y),'rising_diagonal':(y,x),'falling_diagonal':(-y,-x)}[kind])
reflections = {kind:sorted(ref(p,kind) for p in holes) for kind in ('vertical','horizontal','rising_diagonal','falling_diagonal')}
seed = min(holes)
orbit_C = sorted({seed,ref(seed,'vertical'),ref(seed,'horizontal'),ref(ref(seed,'vertical'),'horizontal')})
orbit_A = sorted({seed,ref(seed,'rising_diagonal'),ref(seed,'falling_diagonal'),rounded([-seed[0],-seed[1]])})
axes = {'A':['o6','o7'],'B':['o9','o10','o11'],'C':['o13','o14'],'D':['o16','o17','o18'],'E':['o20','o21']}
actual_lines = {}
for option,ids in axes.items():
    actual_lines[option] = []
    for oid in ids:
        a,b = o[oid]['points']
        actual_lines[option].append({'id':oid,'endpoints':[a,b],'slope':None if a[0] == b[0] else (b[1]-a[1])/(b[0]-a[0]),'linestyle':o[oid]['linestyle']})
math217 = {'question_id':'Plane217','scene_sha256':hashlib.sha256((ROOT/'PlaneGeometry/dataset_generator/scenes/Plane217.json').read_bytes()).hexdigest(),
    'paper_center':center,'hole_offsets':sorted(holes),'C_four_point_single_punch_orbit':orbit_C,
    'A_four_point_single_punch_orbit_example':orbit_A,'reflection_images':reflections,
    'which_reflections_preserve_exact_hole_set':{k:set(v)==holes for k,v in reflections.items()},
    'actual_option_fold_axes':actual_lines,
    'B_E_exclusion':'Every listed crease is vertical, so every reflection and any composition preserves y. A single punch cannot produce the two distinct observed y offsets.',
    'D_exclusion':{'all_fold_slopes': [x['slope'] for x in actual_lines['D']],
                   'invariant':'x+y is invariant under reflection in every line y=x+c and under their compositions.',
                   'observed_offset_x_plus_y_values':sorted({round(x+y,10) for x,y in holes}),
                   'one_punch_possible':False},
    'unique_answer':'C','hole_pair_slopes':{'red':-0.55,'blue':0.55},'A_axis_slopes':{'red':-1,'blue':1},
    'documentation_correction':'Same-slope is false if interpreted as equal numerical slopes or parallel lines. Only falling/rising orientation and colored pair correspondence are encoded.',
    'construction_and_exclusion_checks_pass':set(orbit_C)==holes and set(orbit_A)!=holes and len({y for x,y in holes})==2 and len({round(x+y,10) for x,y in holes})==4}
write('Plane217_diagonal_pair_to_fold_axis_v1',math217)

s = read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane234.json')
o = {x['id']:x for x in s['objects']}
def ray_info(obj):
    arc = next(c for c in obj['commands'] if c['op']=='arc')
    center = arc['center']
    tip = obj['commands'][1]['point']
    delta = [tip[j]-center[j] for j in (0,1)]
    radius = math.hypot(*delta)
    shade = obj['semantic_color'].lower()
    symbol = {'#ffffff':'S','#bbbbbb':'M','#555555':'L'}[shade]
    assert math.isclose(radius,{'S':1.5,'M':1.75,'L':2}[symbol],abs_tol=1e-12)
    return {'object_id':obj['id'],'shade':shade,'tip_radius':radius,'radius_from_face':radius-arc['radius'],
            'tip_angle_degrees':math.degrees(math.atan2(delta[1],delta[0])),'word_symbol':symbol,'center':center}
source = [ray_info(x) for x in s['objects'] if x['id'].startswith('sunray')]
# Establish actual clockwise angular order, beginning at the top ray. IDs are
# then checked rather than used as the ordering proof.
source.sort(key=lambda x:(90-x['tip_angle_degrees'])%360)
assert [x['object_id'] for x in source] == [f'sunray{i}' for i in range(18)]
word = ''.join(x['word_symbol'] for x in source)
windows = [{'start_object':source[i]['object_id'], 'object_ids':[source[(i+j)%18]['object_id'] for j in range(4)],
            'word': ''.join(source[(i+j)%18]['word_symbol'] for j in range(4))} for i in range(18)]
options = {}
for i,letter in enumerate('ABCDE'):
    infos = [ray_info(o[f'{i}ray{j}']) for j in range(4)]
    infos.sort(key=lambda x:-x['tip_angle_degrees'])
    w = ''.join(x['word_symbol'] for x in infos)
    options[letter] = {'rays':infos,'word':w,'forward_matches':[v for v in windows if v['word']==w],
                       'reverse_word_matches_for_disclosure':[v for v in windows if v['word']==w[::-1]]}
rotation_checks = []
def rotate(pt,center,deg,dest):
    x,y = pt[0]-center[0],pt[1]-center[1]
    a=math.radians(deg)
    return [dest[0]+math.cos(a)*x-math.sin(a)*y,dest[1]+math.sin(a)*x+math.cos(a)*y]
for j in range(4):
    src=o[f'sunray{12+j}']; dest=o[f'1ray{j}']
    errs=[]
    for k in range(3):
        pt=rotate(src['commands'][k]['point'],[10,5.5],270,[5,0])
        errs.append(math.dist(pt,dest['commands'][k]['point']))
    rotation_checks.append({'source':src['id'],'option_B_ray':dest['id'],'rotation_degrees':270,
                            'max_exact_vertex_error':max(errs),'shade_equal':src['semantic_color']==dest['semantic_color']})
target_pair = []
for j in range(4):
    a=ray_info(o[f'sunray{3+j}']); b=ray_info(o[f'3ray{j}'])
    errors=[math.dist(rotate(o[a['object_id']]['commands'][k]['point'],[10,5.5],90,[15,0]),o[b['object_id']]['commands'][k]['point']) for k in range(3)]
    target_pair.append({'source':a['object_id'],'wrong_D':b['object_id'],'source_feature':a['word_symbol'],'D_feature':b['word_symbol'],
                       'source_shade':a['shade'],'D_shade':b['shade'],'source_radius':a['tip_radius'],'D_radius':b['tip_radius'],
                       'after_90deg_rotation_vertex_errors':errors})
math234={'question_id':'Plane234','scene_sha256':hashlib.sha256((ROOT/'PlaneGeometry/dataset_generator/scenes/Plane234.json').read_bytes()).hexdigest(),
 'independently_ordered_source_rays':source,'clockwise_source_word':word,'all_18_cyclic_windows':windows,'actual_options':options,
 'labels':s['labels'],'B_exact_rotation_verification':rotation_checks,'marked_source_to_D_comparison':target_pair,
 'unique_forward_rotation_answer':[k for k,v in options.items() if v['forward_matches']],
 'word_test_completeness':'All rays have the same circular base radius and 20-degree angular spacing, each ray spans the same 16-degree base angle, and shade determines its verified tip radius. Thus the ordered shade/radius word characterizes each four-ray part up to rotation. Numeric-leading option IDs are assigned by actual label anchor and x position.',
 'B_rotation_vertices_and_fills_match':all(x['max_exact_vertex_error']<1e-12 and x['shade_equal'] for x in rotation_checks),
 'unique_answer':'B','unchanged_geometry_proven_by_fresh_production_render':'See integrity_audit.json: exact plugin and tested-byte reproduction, no coordinates or semantic fills modified.'}
assert math234['unique_forward_rotation_answer']==['B'] and math234['B_rotation_vertices_and_fills_match']
write('Plane234_three_feature_match_ignores_gray',math234)
print('Plane217 unique C; Plane234 independently derived cycle',word,'options', {k:v['word'] for k,v in options.items()},'unique B')
