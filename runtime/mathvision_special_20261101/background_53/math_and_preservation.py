from research import *
import math
import numpy as np
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config
from freeze import VARIANTS

def audit():
    s241=read(BRANCH/'dataset_generator/scenes/Solid241.json')
    p={k:np.array(v,dtype=float) for k,v in s241['points'].items()}
    def cosine(a,b):return float(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b))
    s243=read(BRANCH/'dataset_generator/scenes/Solid243.json')
    q={k:np.array(v,dtype=float) for k,v in s243['points'].items()}
    mathcheck={'241':{'BAF_deg':math.degrees(math.acos(cosine(p['B']-p['A'],p['F']-p['A']))),'DAH_deg':math.degrees(math.acos(cosine(p['D']-p['A'],p['H']-p['A']))),'cos_CEG':cosine(p['C']-p['E'],p['G']-p['E']),'expected_sqrt130_over13':math.sqrt(130)/13,'cos_FAH':cosine(p['F']-p['A'],p['H']-p['A']),'wrong_cos30':math.sqrt(3)/2},'243':{'ABC_deg':math.degrees(math.acos(cosine(q['A']-q['B'],q['C']-q['B']))),'CBD_deg':math.degrees(math.acos(cosine(q['C']-q['B'],q['D']-q['B']))),'ABD_deg':math.degrees(math.acos(cosine(q['A']-q['B'],q['D']-q['B']))),'rays_at_B_scalar_triple':float(np.linalg.det(np.array([q['A']-q['B'],q['C']-q['B'],q['D']-q['B']]))),'wrong_planar_difference':15},'238':{'actual_prism_volume':8*6*8/2,'wrong_hypotenuse_transfer_volume':8*math.sqrt(14**2-8**2)*8/2,'wrong_exact':'64sqrt33','actual_leg_deduced_from14_minus8':6},'242':{'curved_60pi':60,'ends_36pi':36,'cut_rectangle':120,'wrong_transfer_pi_coefficient':60+36+60}}
    assert abs(mathcheck['241']['cos_CEG']-math.sqrt(130)/13)<1e-12
    assert abs(mathcheck['243']['ABD_deg']-45)<1e-10
    assert abs(mathcheck['243']['rays_at_B_scalar_triple'])>0.7
    dump(OWN/'math_calculation_audit.json',{'at':now(),'checks':mathcheck,'role':'Independent calculations corroborate text/3D proofs, never page measurements or reverse engineering from stored answer.'})
    config=load_config();config['runtime_dir']=str(OWN/'state');config['output_dir']=str(OWN/'output')
    adapter=RendererAdapter(config)
    audits=[]
    for qid,var in VARIANTS.items():
        folder=OWN/qid/var
        metadata=adapter.inspect_question(qid)
        renderer=PluginRenderer(config,adapter,{qid:metadata})
        plugin=read(folder/'plugin.json')
        scene=adapter.scene(qid)
        try:
            def original_state():
                texts=[{'text':t.get_text(),'xy':list(t.get_position()),'fontsize':t.get_fontsize(),'color':t.get_color(),'transform':t.get_transform().get_matrix().tolist()} for t in scene.ax.texts]
                geometry={}
                for key,artists in scene.artists.items():
                    geometry[key]=[]
                    for a in artists:
                        row={'class':type(a).__name__,'transform':a.get_transform().get_matrix().tolist()}
                        if hasattr(a,'get_path'):
                            row['path']=a.get_path().vertices.tolist()
                            row['codes']=a.get_path().codes.tolist() if a.get_path().codes is not None else None
                        if hasattr(a,'get_facecolor'):row['facecolors']=np.asarray(a.get_facecolor()).tolist()
                        if hasattr(a,'get_offsets'):row['offsets']=np.asarray(a.get_offsets()).tolist()
                        geometry[key].append(row)
                return {'text':texts,'geometry':geometry,'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'aspect':scene.ax.get_aspect()}
            before=original_state()
            renderer.apply_actions(scene,plugin)
            after=original_state()
            assert before==after
            audits.append({'question_id':qid,'original_artist_geometry_text_facecolors_point_offsets_view_unchanged':True,'original_artist_count':sum(len(a) for a in scene.artists.values()),'text_count':len(scene.ax.texts),'new_line_count':sum(a['type']=='add_line' for a in plugin['params']['actions']),'new_point_count':sum(a['type']=='add_point' for a in plugin['params']['actions']),'original_state_sha256':hashlib.sha256(json.dumps(before,sort_keys=True).encode()).hexdigest(),'appearance_changes':renderer.appearance_changes(plugin),'limits':'Stroke styling changes edge raster pixels. This preserves original artist geometry/text/fill and fixed3D inputs, not identical visible pixels on styled outlines. Added auxiliary lines are explicitly enumerated; original artists remain unchanged.'})
        finally:scene.close()
    dump(OWN/'original_artist_preservation_audit.json',{'at':now(),'audits':audits})
    print('math and4 original-artist preservation audits pass')

if __name__=='__main__':audit()
