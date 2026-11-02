from tools45 import *
from partial_style import object_paths
from renderer_adapter import scene_png
from PIL import Image
import io
import numpy as np

def art_state(scene):
    text=[{'text':a.get_text(),'position':list(a.get_position()),'transform':a.get_transform().get_matrix().tolist(),'size':a.get_fontsize(),'color':a.get_color()} for a in scene.ax.texts]
    fills=[{'class':type(a).__name__,'facecolor':np.array(a.get_facecolor()).tolist(),'transform':a.get_transform().get_matrix().tolist(),'path':a.get_path().vertices.tolist()} for a in scene.ax.patches]
    points={}
    for o in scene.objects:
        if o['kind']=='point' or o.get('geometry',{}).get('type')=='point':
            points[o['id']]=[{'path':a.get_path().vertices.tolist(),'transform':a.get_transform().get_matrix().tolist(),'color':a.get_color(),'markersize':a.get_markersize()} for a in scene.artists.get(o['id'],[])]
    return {'text':text,'fills':fills,'points':points,'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim())}

for q in ['Solid97','Solid108']:
    f=next((TASK/q).glob('r45_*/design.json')).parent
    plugin=read(f/'plugin.json');ctx=AD.inspect_question(q);renderer=PluginRenderer(CONFIG,AD,{q:ctx});assert renderer.normalize(plugin)==plugin
    scene=AD.scene(q)
    try:
        scene.fig.canvas.draw();before=art_state(scene)
        paths=[]
        for i,a in enumerate(plugin['params']['actions']):
            ob=next(x for x in ctx['objects'] if x['id']==a['target'])
            for p in object_paths(scene,a['target']):
                paths.append({'action_index':i,'target':a['target'],'object_canonical_sha256':canonical_hash(ob),'frozen_object':ob,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist()} for s in p['segments']]})
        noop,pix0=scene_png(scene);assert pix0==ctx['original_pixel_sha256']
        renderer.apply_actions(scene,plugin);scene.fig.canvas.draw();after=art_state(scene);direct,pix1=scene_png(scene)
        assert before==after,'text/fill/pip/view artist state changed'
        assert direct==(f/'candidate.png').read_bytes()
        with Image.open(io.BytesIO(noop)) as im:a=np.array(im.convert('RGBA'))
        with Image.open(io.BytesIO(direct)) as im:b=np.array(im.convert('RGBA'));assert im.size==(768,768) and b[:,:,3].min()==255
        # Original pips occupy point artist bounding boxes far from styled seams.
        pip_checks=[]
        for o in scene.objects:
            if o.get('geometry',{}).get('type')=='point':
                for artist in scene.artists.get(o['id'],[]):
                    px=artist.get_transform().transform(artist.get_path().vertices)
                    cx,cy=px.mean(axis=0);cy=768-cy
                    x0,x1=max(0,int(cx)-7),min(768,int(cx)+8);y0,y1=max(0,int(cy)-7),min(768,int(cy)+8)
                    pip_checks.append({'id':o['id'],'raster_box':[x0,y0,x1,y1],'pixels_equal':np.array_equal(a[y0:y1,x0:x1],b[y0:y1,x0:x1])})
        assert all(x['pixels_equal'] for x in pip_checks)
        check={'fresh_context_equals_saved':ctx==read(f/'context.json'),'normalized_plugin_unchanged':True,'actual_schema_sha256':file_hash(ROOT/'SolidGeometry/workbench/plugin.schema.json'),'no_op_matches_formal_pixels':True,'two_offline_byte_identical':read(f/'render_check.json')['twice_byte_identical'],'direct_apply_byte_equal_candidate':True,'filled_paths_text_point_artists_and_view_identical':True,'path_bindings':paths,'pip_raster_preservation':pip_checks,'new_points_lines_faces_or_relations':False,'native_view_notes':('Viewed exact768x768 PNG. Two red seams are visible; all16pips remain black and separated, question arrow and? unobstructed. Both marked edges are actual source seams.' if q=='Solid97' else 'Viewed exact768x768 PNG. Four open board hinges form two red/blue ordered comparisons. START and A-E remain readable; gray tetrahedron face and hidden dashed edge unchanged. No complete extra triangle is colored.'),'semantic_review':read(f/'design.json')['pretest_math_proof'].get('red_edge_color_preserving_reading',read(f/'design.json')['pretest_math_proof'].get('semantics')),'primary_only':True,'checked_at':now()}
        assert check['fresh_context_equals_saved']
        write(f/'pretest_visual_review.json',check)
        write(f/'pretest_freeze.json',{'created_at':now(),'all_pretest_gates_pass':True,'question_id':q,'expected_wrong_answer':read(f/'design.json')['expected_wrong_answer'],'files':{n:file_hash(f/n) for n in ['design.json','design_difference_audit.json','plugin.json','candidate.png','context.json','pretest_visual_review.json','render_check.json']},'requires_new_parent_independent_review':True})
        print(q,'pretest_pass',len(paths),'paths',len(pip_checks),'pip regions')
    finally:scene.close()
