import task_env
from task_env import OWN, PROJECT, BASE
from inspect_sources import read,save,sha,eligibility
import sys, json, hashlib, io
from datetime import datetime, timezone
import numpy as np
from PIL import Image
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config,pixel_hash,environment_versions,canonical_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.mathvision_workbench import png_bytes

def stamp():return datetime.now(timezone.utc).isoformat()
def h(data):return hashlib.sha256(data).hexdigest()
config=load_config();config['runtime_dir']=str(OWN/'adapter_runtime');config['output_dir']=str(OWN/'adapter_output')
adapter=RendererAdapter(config)

def native_scene(qid):
    row=adapter.records[qid]
    p=PROJECT/'PlaneGeometry'/next(x for x in row['runtime_dependencies'] if x.endswith('/scene.json'))
    s=read(p)
    return {o['id']:{**o,'xy':[s['points'][v] if isinstance(v,str) else v for v in o.get('points',[])]} for o in s['objects']}

def prepare(qid,variant,preset,mechanism,difference,build,semantics):
    folder=OWN/qid/variant
    if (folder/'design.json').exists():
        print(qid,variant,'already frozen; unchanged; not rerendered',flush=True)
        return
    folder.mkdir(exist_ok=False)
    e=eligibility(qid);assert e['eligible'];save(folder/'eligibility_before_design.json',e)
    context=adapter.inspect_question(qid);save(folder/'context.json',context)
    renderer=PluginRenderer(config,adapter,{qid:context})
    scene=adapter.scene(qid)
    try:
        scene.fig.canvas.draw()
        full_paths={}
        for o in context['objects']:
            if o.get('styleable'):
                full_paths[o['id']]=[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],
                    'controls':[s['control'].tolist() for s in p['segments']],
                    'styles':[s['style'] for s in p['segments']]} for p in object_paths(scene,o['id'])]
        actions,roles=build(full_paths,native_scene(qid))
        noop=png_bytes(scene)
        axes={'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'position':list(scene.ax.get_position().bounds),'aspect':scene.ax.get_aspect()}
        texts=[{'text':t.get_text(),'position':list(t.get_position()),'size':t.get_fontsize(),'color':t.get_color()} for t in scene.ax.texts]
        fills=[{'facecolor':list(p.get_facecolor()),'fill':p.get_fill(),'zorder':p.get_zorder()}for p in scene.ax.patches]
    finally:scene.close()
    assert pixel_hash(noop)==pixel_hash(adapter.original_paths[qid])
    save(folder/'path_fingerprints.json',full_paths)
    save(folder/'frozen_source_identity.json',{'question_content':e['content'],'original_approval':e['approval'],'objects':context['objects'],'snap_points':context['snap_points'],'native_axes':axes,'native_texts':texts,'native_patch_fills':fills,'coordinate_and_geometry_edits':False,'3D_projection_visibility':'N/A planar; no geometry/projection/visibility changes'})
    audit={'question_id':qid,'variant_id':variant,'saved_at_utc':stamp(),'all_old_question_files_and_raw_responses_read':True,
           'old_history_audit_path':str(OWN/qid/'old_history_audit.json'),'old_history_audit_sha256':sha(OWN/qid/'old_history_audit.json'),
           'material_difference':difference,'new_information_mechanism':mechanism,'predeclared_wrong_answer':preset,
           'not_recolor_width_crop_rename_of_old_image':True,'not_posthoc_relabel':True,'old_evidence_untouched':True,
           'primary_math_proof':str(OWN/qid/'primary_math_audit.json'),'mark_roles_before_calls':roles,'human_semantics_before_calls':semantics,
           'status':'PRIMARY_RESEARCH_ONLY; NEW independent parent review required if two hits'}
    save(folder/'design_difference_audit.json',audit)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':variant,
            'intent':mechanism,'params':{'actions':actions}}
    plugin=renderer.normalize(plugin)
    plugin,data,digest=renderer.render(plugin,frozen=True)
    plugin2,data2,digest2=renderer.render(plugin,frozen=True)
    assert data==data2 and digest==digest2 and plugin==plugin2
    save(folder/'plugin.json',plugin)
    (folder/'candidate.png').write_bytes(data);(folder/'redraw_2.png').write_bytes(data2)
    with Image.open(io.BytesIO(data)) as im:
        im.load();assert im.size==(768,768) and im.convert('RGBA').getextrema()[3]==(255,255)
    design={'question_id':qid,'variant_id':variant,'created_at_utc':stamp(),'expected_wrong_answer':preset,
            'mechanism':mechanism,'material_difference_audit':str(folder/'design_difference_audit.json'),
            'primary_math_audit':str(OWN/qid/'primary_math_audit.json'),'marker_roles':roles,
            'human_semantics':semantics,'png_sha256':h(data),'pixel_sha256':digest,'plugin_sha256':sha(folder/'plugin.json'),
            'status':'FROZEN_BEFORE_CALLS; native primary review still required'}
    save(folder/'design.json',design)
    save(folder/'render_check.json',{'created_at_utc':stamp(),'adapter':'PlaneGeometry/workbench/mathvision_adapter.py RendererAdapter','renderer':'PlaneGeometry/workbench/mathvision_plugins.py PluginRenderer',
         'actual_schema_validated':True,'defaults_normalized':True,'frozen_normalization_equal':True,'baseline_noop_pixel_equal':True,
         'formal_pixel_sha256':pixel_hash(adapter.original_paths[qid]),'noop_pixel_sha256':pixel_hash(noop),
         'two_draws_byte_identical':True,'candidate_png_sha256':h(data),'second_png_sha256':h(data2),'pixel_sha256':digest,
         'normalized_action_count':len(plugin['params']['actions']),'geometry_text_fill_view_unchanged_by_declared_operations':True,
         'opaque_768_square':True,'environment':environment_versions(),'strict_own_write_guard':True})
    print(qid,variant,'preset',preset,'actions',len(actions),'PNG',h(data),flush=True)

RED='#DC2626';BLUE='#2563EB'
def partial(paths,target,start,end,color=RED,width=2):
    p=paths[target][0];n=len(p['controls'])
    if start<0:start+=n
    if end<0:end+=n
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,
            'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start/n,'end':end/n,'wrap':False}}

def build415(paths,obs):
    p=paths['leftbigupper'][0]
    assert np.allclose(p['controls'][-1],[[0,3],[0,1]],atol=1e-13)
    assert np.allclose(paths['rightbigleft'][0]['controls'][0],[[7,1],[7,3]],atol=1e-13)
    actions=[partial(paths,'leftbigupper',-1,len(p['controls'])),partial(paths,'rightbigleft',0,1)]
    roles=[{'action_index':0,'feature':'left large-quarter exposed vertical radius, (0,3) to (0,1), display length2=10cm',
            'information_role':'Source member: true10cm radial material edge that contributes to the left perimeter.'},
           {'action_index':1,'feature':'right central vertical large-quarter radius, (7,1) to (7,3), display length2=10cm',
            'information_role':'Receiving member: congruent same-piece radius after translation; now shared with the other large quarter and internal. The intended error includes this10cm seam in the right perimeter, giving left30 minus right(10+10)=10.'}]
    return actions,roles

prepare('Plane415','r44_exposed_radius_to_contact_seam','10',
        'A true10cm material radius is red in both arrangements, external on the left and a shared internal seam on the right. Test carrying its perimeter contribution through the actual piece correspondence: wrongly P_right=15pi+20 gives difference10.',
        {'old':'arc_inventory_perimeter_alias marks8 complete curved arcs by radius family; preset0; full finals15 and20, both misses.',
         'new':'Exactly2 straight radii, no curved marks. The new variable is external-versus-internal ownership of the SAME10cm material edge. Wrong10 comes from one falsely retained seam contribution, not old arc cancellation or observed15.'},
        build415,
        'Actual numerical perimeter question. The two red segments are congruent radii under an actual rigid piece correspondence, with exposed/contact status visibly different. All curves, seams and rectangle boundaries remain, with no added line, cut, fill, relation symbol or text. Even a literal printed-edge reading changes no geometric perimeter and cannot remove the unique numerical answer20.')

def build421(paths,obs):
    actions=[];roles=[]
    for target in ['hex1','hex2']:
        vs=obs[target]['xy']; center=((np.array(vs[0])+np.array(vs[3]))/2).tolist()
        for i,v in enumerate(vs):
            actions.append({'type':'add_line','id':f'r44_{target}_spoke{i}','endpoints':[center,v],'color':BLUE,'linestyle':'solid'})
            roles.append({'action_index':len(actions)-1,'feature':f'{target} center-to-vertex{i} radius','source_center_derivation':'midpoint of opposite frozen vertices0 and3; no center point symbol added',
                          'information_role':'One spoke of the complete6-triangle source-unit fan; adjacent source triangles each have area t=sqrt3/4. All6 spokes are needed for the visible6-cell count.'})
    for target,root,inds in [('lowGrey',0,[2,3]),('upGrey',1,[3,4])]:
        vs=obs[target]['xy']
        for i in inds:
            actions.append({'type':'add_line','id':f'r44_{target}_diag{i}','endpoints':[vs[root],vs[i]],'color':BLUE,'linestyle':'solid'})
            roles.append({'action_index':len(actions)-1,'feature':f'{target} existing vertex{root} to existing vertex{i}',
                          'information_role':'Receiver partition edge: the two diagonals create3 actual gray triangles of areas3t,t,2t. Counting the3 visible pieces as source-unit triangles yields gray6/(white12+gray6)=1/3, despite their unequal areas.'})
    return actions,roles

prepare('Plane421','r44_unequal_triangle_count_transfer','C',
        'Partition both regular hexagons into6 equal unit triangles and each actual gray pentagon into3 unequal triangles, using the same blue1pt auxiliary style. Test transferring the source triangle-as-area-unit to every visible receiving triangle by count:6gray/(12white+6gray)=1/3, choiceC.',
        {'old':'v01 uniformly styles both full white hexagon contours; v02 styles full white contours plus outer frame. Both presetC; finals0/C and1/5/C, so neither has2 hits.',
         'new':'16 NEW interior triangulation lines, zero old whole-outline styling. The explicit count correspondence is6 unit triangles per hexagon versus3 unequal triangles per gray pentagon, with receiver areas3t,t,2t. The wrong preset remainsC for a new geometry-count mechanism frozen before calls.'},
        build421,
        'The question asks a numerical shaded-area fraction of static geometric regions. Blue solids are ordinary auxiliary decomposition lines, not cut/fold instructions or equality marks. Gray/white membership and all original borders remain. Literal blue ink also cannot change the areas bounded by the original gray/white fills. A careful human uses the visibly unequal triangle areas and gets1/2. No colors-preserved-picture choice is requested.')

def build441(paths,obs):
    # outer polygon edges: bottom, right, top, left. Highlight the actual8-unit left side.
    actions=[{'type':'add_line','id':'r44_original_height_overlay','endpoints':[obs['outer']['xy'][3],obs['outer']['xy'][0]],'color':RED,'linestyle':'solid'},
             {'type':'set_object_style','target':'cut1','color':RED,'linewidth_pt':2},
             {'type':'set_object_style','target':'cut3','color':RED,'linewidth_pt':2},
             {'type':'set_object_style','target':'cut2','color':RED,'linewidth_pt':2}]
    roles=[{'action_index':0,'feature':'original left exterior sideAD, length8','information_role':'Known whole-height source.'},
           {'action_index':1,'feature':'upper existing vertical return, length4','information_role':'First actual half-height member; pairs with the lower return to span the source height8.'},
           {'action_index':2,'feature':'lower existing vertical return, length4','information_role':'Second actual half-height member; completes total vertical rise8 without a new construction.'},
           {'action_index':3,'feature':'existing horizontal y-run, true length6','information_role':'Receiving run of the same stepped interface. Proposed mistake transfers total vertical rise4+4=8 into this single horizontal run after informal piece turning, yielding y8.'}]
    return actions,roles

prepare('Plane441','r44_total_rise_to_horizontal_run_overlay','8',
        'Bind the true8-unit outer height and the two4-unit vertical returns to the horizontal y-run of the existing step. Test confusing total vertical rise4+4 with the one horizontal run when reasoning about repositioning the congruent hexagons, yielding y8.',
        {'old':'Only prescreen existed: no saved design or solver call; concern that arbitrary step/exterior interchange could imply unsupported equality or require adding a target square.',
         'new':'No target square is invented. Four existing open line portions expose the exact source decomposition8=4+4 and the receiving horizontal run. The source AD is an allowed1pt line coincident with the real side; the3 returns use original-object styles. No equality ticks, new contact, new geometric boundary, cut or piece is added. This is a primary new hypothesis, not a proven useful mechanism; independent targeting review remains necessary.',
         'offline_implementation_correction':'The earlier untested r44_total_rise_to_horizontal_run draft failed with object_changed on outer partial path because before/after canvas-draw path fingerprints differ. Its bytes are preserved; no PNG/design or API invocation existed. The coincident original-edge overlay avoids that unsupported interval without modifying the adapter. Same one hypothesis, not an additional tested design.'},
        build441,
        'Static numerical y question with the original8x18 statement, letters, step and y label unchanged. A shared hue is an appearance cue, not a conventional length-equality symbol; the drawn perpendicular runs remain visibly distinct. The correct area-and-assembly argument still fixes y6. A physical printed-edge reading also leaves that numerical value unchanged. No output picture is selected, so there is no missing color-preserving choice. Primary information-targeting caveat: the false aggregate-to-run transfer is a hypothesis and must receive NEW independent assessment if the pair hits.')

# Copy the existing real-call harness; alter ONLY filesystem isolation/bootstrap.
source=BASE/'harness/quicktest3_isolated.py'
code=source.read_text(encoding='utf-8')
assert code.count('PROJECT = Path(__file__).resolve().parents[3]')==1
code=code.replace('PROJECT = Path(__file__).resolve().parents[3]', 'PROJECT = Path(__file__).resolve().parents[4]')
code=code.replace('RUNTIME = (PROJECT / "runtime").resolve()', 'RUNTIME = Path(__file__).resolve().parents[1]')
needle='from __future__ import annotations\n'
code=code.replace(needle,needle+'\nimport sys as _sys\nfrom pathlib import Path as _Path\n_sys.path.insert(0,str(_Path(__file__).resolve().parents[1]))\nimport task_env\n',1)
harness=OWN/'harness';harness.mkdir(exist_ok=True)
(harness/'quicktest3_isolated.py').write_text(code,encoding='utf-8')
save(OWN/'harness_isolation_audit.json',{'source_path':str(source),'source_sha256':sha(source),'own_harness_sha256':sha(harness/'quicktest3_isolated.py'),'changes':['Import task_env strict own write guard before project imports','PROJECT parents4 because one extra directory','RUNTIME restricted to own background_44 directory'],'model_thinking_system_prompt_payload_timeout_token_limit_and_no_retry_code_unchanged':True,'no_real_calls_in_preparation':True})
