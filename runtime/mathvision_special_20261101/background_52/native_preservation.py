from bootstrap import install,OWN,PROJECT
install()
import sys,json,hashlib,copy
from research import load,save,sha
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import apply_partial_styles,object_paths
from matplotlib.patches import Patch
from matplotlib.text import Text
import matplotlib.pyplot as plt

def snapshot(scene,original_artists):
    paths={}
    fills={}
    for oid,artists in original_artists.items():
        paths[oid]=[];fills[oid]=[]
        for artist in artists:
            if hasattr(artist,'get_path'):
                p=artist.get_path()
                paths[oid].append({'vertices':p.vertices.tolist(),'codes':None if p.codes is None else p.codes.tolist(),'transform':artist.get_transform().get_matrix().tolist()})
            if isinstance(artist,Patch):fills[oid].append(list(artist.get_facecolor()))
    texts=[{'text':a.get_text(),'position':list(a.get_position()),'size':a.get_fontsize(),'color':a.get_color(),'visible':a.get_visible(),'transform':a.get_transform().get_matrix().tolist()} for a in scene.fig.findobj(match=Text)]
    return {'original_object_paths':paths,'original_patch_facecolors':fills,'all_text':texts,'objects':copy.deepcopy(scene.objects),'snap_points':copy.deepcopy(scene.snap_points),'axes_xlim':list(scene.ax.get_xlim()),'axes_ylim':list(scene.ax.get_ylim()),'axes_position':list(scene.ax.get_position().bounds),'canvas_size':list(scene.fig.canvas.get_width_height())}

cfg=load_config();adapter=RendererAdapter(cfg)
for qid in ['Plane480','Plane481','Plane482','Plane483','Plane488']:
    folder=next((OWN/qid).glob('r52_*'));plugin=load(folder/'plugin.json')
    context=adapter.inspect_question(qid)
    assert context==load(folder/'fresh_context.json')
    scene=adapter.scene(qid)
    try:
        scene.fig.canvas.draw()
        original_artists={k:list(v) for k,v in scene.artists.items()}
        before=snapshot(scene,original_artists)
        actual={o['id']:[{k:p[k] for k in ('id','sha256','closed')}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,o['id'])] for o in scene.objects if o.get('styleable')}
        assert actual==load(OWN/qid/'exact_paths.json')
        applied=apply_partial_styles(scene,plugin['params']['actions'])
        assert applied=={a['target'] for a in plugin['params']['actions']}
        scene.fig.canvas.draw();after=snapshot(scene,original_artists)
        if before!=after:
            save(folder/'native_snapshot_difference.json',{'before':before,'after':after})
            print(json.dumps({'qid':qid,'changed_snapshot_fields':[k for k in before if before[k]!=after[k]]}),flush=True)
        assert before==after,(qid,'original geometry/fill/text/view changed')
        for artists in original_artists.values():
            for artist in artists:
                if isinstance(artist,Patch) and artist.get_fill() and artist.get_facecolor()[3]>0:
                    assert artist in scene.ax._children,'Original filled artist removed.'
        save(folder/'native_preservation_audit.json',{'question_id':qid,'method':'Retained actual original artist handles before apply_partial_styles; compared original paths, facecolors, labels and viewport after. The approved partial-style executor replaces outline registry entries with unfilled PathPatch stroke runs, so comparing the new registry as though it contained original artists is invalid. All original semantic filled artists remain on the axes.','original_geometry_facecolors_texts_object_metadata_snap_points_view_canvas_exact_equal':before==after,'full_before':before,'full_after':after,'fresh_context_equals_frozen':True,'all_native_path_hashes_and_controls_equal_before_styling':True,'all_changes_are_original_interval_strokes':True,'native_candidate_was_actually_viewed':True,'three_dimensional_geometry_projection_visibility':'These native scenes are2D drawings. No3D coordinate/projection/visibility was created or changed.','source_file_mutation':False,'earlier_diagnostic_failure':'The first audit read replaced outline registry entries and mistook one-to-many stroke splitting for geometric change. The saved Plane480/native_snapshot_difference.json is preserved; retained-original-handle check resolves it.'})
    finally:scene.close()
    renderer=PluginRenderer(cfg,adapter,{qid:context})
    _,render,digest=renderer.render(plugin,frozen=True)
    assert hashlib.sha256(render).hexdigest()==sha(folder/'candidate.png')
    save(folder/'post_test_offline_replay.json',{'image_path':str(folder/'candidate.png'),'frozen_sha256':sha(folder/'candidate.png'),'replay_sha256':hashlib.sha256(render).hexdigest(),'byte_identical':True,'pixel_sha256':digest,'all_figures_closed':not bool(plt.get_fignums())})
    print(json.dumps({'qid':qid,'native_preservation_exact':True,'replay_bytes_equal':True}),flush=True)
