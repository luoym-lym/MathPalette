from pathlib import Path
import os,sys,json
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
for key,name in {'MPLCONFIGDIR':'mpl_cache','TEMP':'temp','TMP':'temp','XDG_CACHE_HOME':'cache'}.items():
    target=OUT/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(OUT/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config,file_hash
from renderer_adapter import RendererAdapter
from render_plugins import PluginRenderer
from PIL import Image,ImageDraw
cfg=load_config();cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'outputs');adapter=RendererAdapter(cfg)
qid='Solid220';scene=adapter.scenes[qid]
def xy(world):return adapter.renderer.project(scene,world).tolist()
plans=[
('separate_face_edge_pair',[{'type':'set_object_style','target':t,'color':'#DC2626','linewidth_pt':2} for t in ['line_15','line_17']],'将X左侧原边与Z右侧原边同色，二者分别属于X/Z且不共享，不围出单个Z。用错配的相对边编码X/Z对应，预设错误A。'),
('separate_face_dot_pair',[{'type':'add_point','id':ident,'xy':xy(world),'color':'#DC2626'} for ident,world in [('face_x_cue',[1.2,1.25,0]),('face_z_cue',[1.2,0.25,0])]],'在X/Z各自面内部相同相对位置放一个同色点，两个点都不压字、彼此分离，明确标记两个不同面形成错误相对面分组；预设错误A。')]
summary=[]
for name,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':'A','correct_answer':'E','mechanism':reason,'status':'unreviewed_runtime_candidate','revision_reason':'Original line13/line16 merely frame Z because line13 is shared; this is a new image, new plugin and independently tested candidate.','human_solvability':'原X/Y是唯一相对面。原题只问字母对应的折叠拓扑；边色/附加无名点不增加相对面条件，所有字母和折边完整保留。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误A/Z','params':{'actions':actions}}
    meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
    (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
    result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
    (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'solid220_revised_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(1200,625),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    im=Image.open(r['image']).convert('RGB').resize((600,600));x=n*600;canvas.paste(im,(x,25));draw.text((x+8,5),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'solid220_revised_contact.png')
