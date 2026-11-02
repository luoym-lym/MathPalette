from review_env import *
import copy
import hashlib
import io
import json
import math
import numpy as np
from PIL import Image
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from workbench_io import load_config, pixel_hash, environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths, apply_partial_styles, evaluate
from dataset_tools.mathvision_workbench import png_bytes

QID = 'Plane242'
CAND = BASE / 'background_24/Plane242/r24_disconnected_gray_arc_assembly'
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(b): return hashlib.sha256(b).hexdigest()
def write(p,v):
    with (HERE/p).open('x',encoding='utf-8',newline='\n') as f:
        json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False); f.write('\n')

plugin = read(CAND/'plugin.json')
cfg = load_config()
cfg['runtime_dir'] = str(HERE/'state')
cfg['output_dir'] = str(HERE/'output')
adapter = RendererAdapter(cfg)
meta = adapter.inspect_question(QID)
frozen_context = read(CAND/'context.json')
checks = {'fresh_context_exactly_equals_frozen_context':meta == frozen_context}
renderer = PluginRenderer(cfg,adapter,{QID:meta})
normalized = renderer.normalize(plugin)
checks['plugin_normalizes_without_change'] = normalized == plugin

scene = adapter.scene(QID)
try:
    original = png_bytes(scene)
    (HERE/'independent_noop.png').write_bytes(original)
    checks['no_op_matches_formal_pixels'] = pixel_hash(original) == pixel_hash(adapter.original_paths[QID])
    def snapshot():
        fills = []
        for a in scene.ax.get_children():
            if isinstance(a,Patch) and a.get_fill() and a.get_facecolor()[3] != 0:
                p = a.get_path().transformed(a.get_transform())
                fills.append({'type':type(a).__name__,'vertices':p.vertices.tolist(),
                              'codes':p.codes.tolist() if p.codes is not None else None,
                              'facecolor':list(a.get_facecolor()),'zorder':a.get_zorder()})
        texts = [{'text':t.get_text(),'position':list(t.get_position()),'fontsize':t.get_fontsize(),
                  'color':t.get_color(),'transform':t.get_transform().get_matrix().tolist()}
                 for t in scene.ax.texts]
        return {'fills':fills,'texts':texts,'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),
                'axes_position':list(scene.ax.get_position().bounds),'figsize':scene.fig.get_size_inches().tolist(),
                'dpi':scene.fig.dpi,'aspect':scene.ax.get_aspect()}
    pre = snapshot()
    marker_geometry = []
    fps = read(CAND/'path_fingerprints.json')
    designs = read(CAND/'design.json')['marker_roles']
    for i,a in enumerate(plugin['params']['actions']):
        p = next(p for p in object_paths(scene,a['target']) if p['id'] == a['interval']['path_id'])
        n = len(p['segments'])
        lo,hi = a['interval']['start']*n,a['interval']['end']*n
        indices = [j for j in range(n) if lo <= j and j+1 <= hi]
        ctrls = [p['segments'][j]['control'].tolist() for j in indices]
        all_ctrls = [s['control'].tolist() for s in p['segments']]
        samples = np.vstack([np.array([evaluate(p['segments'][j]['control'],t)
                                      for t in np.linspace(0,1,65)]) for j in indices])
        pix = scene.ax.transData.transform(samples)
        pix[:,1] = 768 - pix[:,1]
        bbox = [int(math.floor(pix[:,0].min()-4)),int(math.floor(pix[:,1].min()-4)),
                int(math.ceil(pix[:,0].max()+4))+1,int(math.ceil(pix[:,1].max()+4))+1]
        expected = next(x for x in fps[a['target']] if x['id'] == p['id'])
        marker_geometry.append({'action_index':i,'action':a,'actual_path_sha256':p['sha256'],
            'path_binding_exact':p['sha256'] == a['interval']['path_sha256'] == expected['sha256'],
            'full_controls_equal_fingerprint':all_ctrls == expected['exact_controls'],
            'selected_controls_equal_design':ctrls == designs[i]['exact_controls'],
            'total_native_segments':n,'selected_native_segment_indices':indices,'selected_controls':ctrls,
            'selected_segments_are_only_cubic_arcs':all(len(x)==4 for x in ctrls),
            'original_styles':[p['segments'][j]['style'] for j in indices],
            'pixel_bounds_with_4px_margin_xyxy_exclusive':bbox,
            'native_arc_length_approx_px':float(np.linalg.norm(np.diff(pix,axis=0),axis=1).sum()),
            'stroke_width_px':a['linewidth_pt']*scene.fig.dpi/72})
    apply_partial_styles(scene, plugin['params']['actions'])
    post = snapshot()
    checks['all_original_filled_paths_facecolors_and_transforms_identical'] = pre['fills'] == post['fills']
    checks['all_original_text_artists_identical'] = pre['texts'] == post['texts']
    checks['frozen_view_aspect_canvas_identical'] = all(pre[k]==post[k] for k in pre if k not in ('fills','texts'))
    direct = png_bytes(scene)
    checks['direct_style_replay_byte_equal_candidate'] = direct == (CAND/'candidate.png').read_bytes()
    original_data = np.array(Image.open(io.BytesIO(original)).convert('RGBA'))
    candidate_data = np.array(Image.open(CAND/'candidate.png').convert('RGBA'))
    diff = np.any(original_data != candidate_data, axis=2)
    mask = np.zeros((768,768),bool)
    for m in marker_geometry:
        x0,y0,x1,y1 = m['pixel_bounds_with_4px_margin_xyxy_exclusive']
        mask[y0:y1,x0:x1] = True
        m['changed_pixels_inside_marker_box'] = int(diff[y0:y1,x0:x1].sum())
        color = m['action']['color']
        rgb = np.array([int(color[j:j+2],16) for j in (1,3,5)])
        m['exact_palette_pixels_inside_marker_box'] = int(np.all(candidate_data[y0:y1,x0:x1,:3] == rgb,axis=2).sum())
    checks['all_changed_pixels_within_six_actual_arc_neighborhoods'] = not bool((diff & ~mask).any())
    checks['all_six_marks_have_visible_exact_color_pixels'] = all(m['exact_palette_pixels_inside_marker_box']>0 for m in marker_geometry)
    checks['all_six_actual_path_fingerprints_match'] = all(m['path_binding_exact'] and m['full_controls_equal_fingerprint'] and m['selected_controls_equal_design'] for m in marker_geometry)
    y,x = np.where(diff)
    pixels = {'changed_pixels':int(diff.sum()), 'outside_marker_neighborhoods':int((diff & ~mask).sum()),
              'diff_bbox_xyxy_exclusive':[int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1)]}
    geometry = {'before':pre,'after':post,'native_radius_px':float(np.linalg.norm(scene.ax.transData.transform([1,0])-scene.ax.transData.transform([0,0])))}
finally:
    scene.close()

plugin2,data1,digest1 = renderer.render(plugin, frozen=True)
plugin3,data2,digest2 = renderer.render(plugin, frozen=True)
checks['two_full_renderer_replays_byte_equal_frozen_candidate'] = data1 == data2 == (CAND/'candidate.png').read_bytes()
checks['two_full_renderer_pixel_hashes_match_frozen'] = digest1 == digest2 == read(CAND/'render_check.json')['pixel_sha256']
(HERE/'independent_reproduced.png').write_bytes(data1)
plt.close('all')
checks['no_live_matplotlib_figures'] = not plt.get_fignums()
write('native_render_audit.json', {'question_id':QID,'isolation':ISOLATION,'pid':os.getpid(),
      'checks':checks,'environment':environment_versions(),'marker_geometry':marker_geometry,
      'pixel_comparison':pixels,'original_geometry_text_view':geometry,'new_solver_calls':0,
      'original_png_sha256':sha(adapter.original_paths[QID].read_bytes()),'candidate_png_sha256':sha(data1),
      'formal_pixel_sha256':pixel_hash(original),'candidate_pixel_sha256':digest1,
      'all_captured_scenes_closed':True})
print(json.dumps({'checks':checks,'pixel_comparison':pixels,
                  'radius_px':geometry['native_radius_px'],
                  'marks':[{'index':m['action_index'],'visible_color_pixels':m['exact_palette_pixels_inside_marker_box'],
                            'arc_length_px':m['native_arc_length_approx_px']} for m in marker_geometry]},ensure_ascii=False))
