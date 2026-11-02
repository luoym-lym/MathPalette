import review_bootstrap as b
import ast
import hashlib
import io
import json
import sys
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from dataset_tools import catalog
from dataset_tools.mathvision_workbench import build_scene

sys.path.insert(0, str(b.PROJECT / 'SolidGeometry/workbench'))
from render_plugins import PluginRenderer
from renderer_adapter import scene_png
from workbench_io import load_config, pixel_hash, environment_versions
from partial_style import object_paths

BASE = b.PROJECT / 'runtime/mathvision_special_20261101'
QROOT = BASE / 'background_16/Solid197'
CAND = QROOT / 'crease_side_binding'

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def write(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

record = next(r for r in catalog.rows(b.PROJECT / 'SolidGeometry/dataset.jsonl') if r['id'] == 'Solid197')
scene_data = read(b.PROJECT / 'SolidGeometry' / record['scene'])
plugin = read(CAND / 'plugin.json')

class Adapter:
    def scene(self, qid):
        assert qid == 'Solid197'
        return build_scene(b.PROJECT / 'SolidGeometry', record)

ad = Adapter()
scene = ad.scene('Solid197')
try:
    data, baseline_pixel = scene_png(scene)
    assert baseline_pixel == pixel_hash(b.PROJECT / 'SolidGeometry' / record['image'])
    scene.fig.canvas.draw()
    width, height = scene.fig.canvas.get_width_height()
    transform = np.array([[1,0,0],[0,-1,height],[0,0,1]]) @ scene.ax.transData.get_affine().get_matrix()
    metadata = {'original_pixel_sha256': baseline_pixel, 'objects': scene.objects,
                'snap_points': scene.snap_points, 'xlim':list(scene.ax.get_xlim()), 'ylim':list(scene.ax.get_ylim())}
    (b.ROOT / 'baseline_reproduced.png').write_bytes(data)
    snap_matches = [[s for s in scene.snap_points if s['xy'] == xy]
                    for action in plugin['params']['actions'] for xy in action['endpoints']]
    assert all(snap_matches), snap_matches
    paths = {oid:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],
                   'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,oid)]
             for oid in ['cube100_cube101']}
    def existing_state():
        return {'line_xy':[x.get_xydata().tolist() for x in originals['lines']],
                'line_color':[x.get_color() for x in originals['lines']],
                'line_style':[x.get_linestyle() for x in originals['lines']],
                'line_width':[x.get_linewidth() for x in originals['lines']],
                'patch_paths':[x.get_path().vertices.tolist() for x in originals['patches']],
                'patch_fill':[list(x.get_facecolor()) for x in originals['patches']],
                'patch_edges':[list(x.get_edgecolor()) for x in originals['patches']],
                'patch_width':[x.get_linewidth() for x in originals['patches']],
                'text':[(x.get_text(),list(x.get_position())) for x in originals['texts']],
                'view':[list(scene.ax.get_xlim()),list(scene.ax.get_ylim())]}
    originals = {'lines':list(scene.ax.lines),'patches':list(scene.ax.patches),'texts':list(scene.ax.texts)}
    before = existing_state()
    cfg = load_config()
    cfg['runtime_dir'] = str(b.ROOT / 'render_state')
    cfg['output_dir'] = str(b.ROOT / 'render_output')
    renderer = PluginRenderer(cfg, ad, {'Solid197':metadata})
    norm = renderer.normalize(plugin)
    assert norm == plugin
    with matplotlib.rc_context(scene.settings):
        renderer.apply_actions(scene, norm)
    after = existing_state()
    assert before == after
    assert len(scene.ax.lines) == len(originals['lines']) + 2
    appended = list(scene.ax.lines)[-2:]
    line_properties = [{'xy':x.get_xydata().tolist(),'linewidth_pt':x.get_linewidth(),
                        'color':x.get_color(),'linestyle':x.get_linestyle(),'capstyle':x.get_solid_capstyle()}
                       for x in appended]
finally:
    scene.close()

norm1, png1, pixel1 = renderer.render(plugin)
norm2, png2, pixel2 = renderer.render(plugin, frozen=True)
assert norm1 == norm2 == plugin and png1 == png2 == (CAND/'candidate.png').read_bytes()
assert pixel1 == pixel2 == read(CAND/'render_check.json')['pixel_sha256']
(b.ROOT/'candidate_reproduced_01.png').write_bytes(png1)
(b.ROOT/'candidate_reproduced_02.png').write_bytes(png2)
original = np.array(Image.open(b.PROJECT/'SolidGeometry'/record['image']).convert('RGBA'))
candidate = np.array(Image.open(CAND/'candidate.png').convert('RGBA'))
diff = np.any(original != candidate, axis=2)
yy, xx = np.nonzero(diff)
positions = np.column_stack([xx + .5, yy + .5])
distances = []
marker_geometry = []
for action in plugin['params']['actions']:
    a, z = ((transform @ np.array([*p,1]))[:2] for p in action['endpoints'])
    delta = z-a
    t = np.clip(((positions-a) @ delta) / (delta @ delta), 0, 1)
    distance = np.linalg.norm(positions-(a+t[:,None]*delta), axis=1)
    distances.append(distance)
    marker_geometry.append({'id':action['id'],'pixel_endpoints':[a.tolist(),z.tolist()],
                            'length_px':float(np.linalg.norm(delta)), 'action':action})
min_distance = np.minimum(*distances)
assert min_distance.max() < 2.1
assert candidate[:,:,3].min() == 255
source_polygons = [o for o in scene_data['objects'] if o['type']=='face']
areas = {}
for o in source_polygons:
    vertices=np.array(o['points'],dtype=float)
    twice=sum((np.cross(vertices[i],vertices[(i+1)%len(vertices)]) for i in range(len(vertices))), np.zeros(3))
    areas[o['id']]=float(np.linalg.norm(twice)/2)
assert len(areas) == 15
assert [areas['frontsticker'+str(i)] for i in range(5)] == [1/8,1/16,1/16,1/16,1/16]
assert sum(areas.values())*2*100 == 225
source_features={o['id']:o for o in source_polygons}
central=np.array(source_features['frontsticker0']['points'])
edgefront=np.array(source_features['frontsticker2']['points'])
edgeright=np.array(source_features['rightsticker4']['points'])
world_marker_endpoints=[central[:2].tolist(),edgefront[:2].tolist()]
for action,world in zip(plugin['params']['actions'],world_marker_endpoints):
    projection = np.array(scene_data['projection']['matrix']) @ (np.array(world)-np.array(scene_data['projection']['origin'])).T
    projected = projection.T + np.array(scene_data['projection']['offset'])
    assert projected.tolist() == action['endpoints']

profile_tree = ast.parse((b.PROJECT/'SolidGeometry/workbench/quick_test.py').read_text(encoding='utf-8-sig'))
constants = {}
for node in profile_tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('SYSTEM_PROMPT','TEST_PROFILES','MIMO_API_BASE') for t in node.targets):
        constants[node.targets[0].id] = ast.literal_eval(node.value)
binding=read(next((CAND/'tests').glob('*/binding.json')))
request=read(next((CAND/'tests').glob('*/request.json')))
profile=constants['TEST_PROFILES']['quicktest3']
assert binding['settings'] == {**profile,'api_base':constants['MIMO_API_BASE']}
assert binding['system_prompt'] == request['messages'][0]['content'] == constants['SYSTEM_PROMPT']
assert binding['reference_quick_test_sha256'] == sha(b.PROJECT/'SolidGeometry/workbench/quick_test.py')
result={'isolation':b.ISOLATION,'environment':environment_versions(),'freetype':matplotlib.ft2font.__freetype_version__,
        'baseline_pixels_match_formal':True,'normalized_plugin_unchanged':True,
        'candidate_twice_byte_identical_to_frozen':True,'candidate_pixel_sha256':pixel1,
        'source_scene_component_sha256':{k:catalog.digest(scene_data[k]) for k in ('points','objects','labels','view','projection','visibility','dimensions','constraints')},
        'all_original_artist_geometry_fill_text_styles_view_unchanged':before==after,
        'original_artist_counts':{k:len(v) for k,v in originals.items()},
        'two_new_lines_only':True,'appended_lines':line_properties,'appearance_changes':renderer.appearance_changes(plugin),
        'exact_context_snap_matches':snap_matches,'cube_edge_path':paths,'world_marker_endpoints':world_marker_endpoints,
        'marker_geometry':marker_geometry,'pixel_difference':{'changed_pixels':int(diff.sum()),
            'bbox':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())],
            'max_distance_to_original_feature_segments_px':float(min_distance.max()),
            'zero_changes_outside_two_stroke_footprints':True},
        'independent_world_polygon_areas_unit2':areas,'three_visible_faces_total_cm2':sum(areas.values())*100,
        'all_six_faces_total_cm2':sum(areas.values())*2*100,
        'world_lengths_cm':{'central_side':float(np.linalg.norm(central[1]-central[0])*10),
                             'central_diagonal':float(np.linalg.norm(central[2]-central[0])*10),
                             'fold_crease':float(np.linalg.norm(edgefront[1]-edgefront[0])*10)},
        'matching_fold_endpoints_on_front_right':all(any(np.array_equal(p,q) for q in edgeright[:2]) for p in edgefront[:2]),
        'profile':profile,'system_prompt':constants['SYSTEM_PROMPT'],'profile_exact_match':True,
        'all_figures_closed':plt.get_fignums()==[],'subprocesses_started':0,'solver_calls':0}
write(b.ROOT/'render_and_geometry_audit.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
