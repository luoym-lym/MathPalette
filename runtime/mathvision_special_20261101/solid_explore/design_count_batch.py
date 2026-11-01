from pathlib import Path
import os,sys,json
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
for key,name in {'MPLCONFIGDIR':'mpl_cache','TEMP':'temp','TMP':'temp','XDG_CACHE_HOME':'cache'}.items():
    target=OUT/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(OUT/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config,file_hash
from renderer_adapter import RendererAdapter
from render_plugins import PluginRenderer
from PIL import Image,ImageDraw
cfg=load_config();cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'outputs');adapter=RendererAdapter(cfg)
def xy(qid,ref):
    scene=adapter.scenes[qid]
    return adapter.renderer.project(scene,adapter.renderer.point(scene,ref)).tolist()
def line(qid,ident,a,b,color='#2563EB'):
    return {'type':'add_line','id':ident,'endpoints':[xy(qid,a),xy(qid,b)],'color':color,'linestyle':'solid'}
plans=[]
for qid in ['Solid155','Solid183']:
    labels={l['text']:l['anchor'] for l in adapter.scenes[qid]['labels'] if l.get('text') in ['P','Q']}
    actions=[line(qid,'requested_diagonal',labels['P'],labels['Q'])]
    plans.append((qid,'projected_diagonal_count','11',actions,'仅画出题干所指P-Q空间对角线。准确投影在平面网格中穿过11个可见区间，诱导按2D区间计数11；真实3D通行数为3+4+5-2=10，端点、网格及尺寸不变。'))
plans.append(('Solid95','pillar_height_capture','80',[line('Solid95','pillar_left_height',[0,0,0],[0,0,5],'#DC2626'),line('Solid95','pillar_right_height',[4,0,0],[4,0,5],'#DC2626')],'两条红线精确重合于两根前排柱的完整5格高原棱，提供柱高分组线索，诱导只数9根5格柱而遗漏共同底板，125-45=80。底板与每个方格完整保留。'))
snaps={p['id']:p['xy'] for p in adapter.snap_points('Solid80')}
plans.append(('Solid80','removed_vertex_marker','11',[{'type':'add_point','id':'removed_vertex_cue','xy':snaps['p101'],'color':'#DC2626'}],'仅标出三条原有切除辅助虚线交汇的旧顶点，诱导把已切旧顶点继续计入得11。题干明确切去一角，新实体仍有8-1+3=10个顶点；不新增边或遮住切面。'))
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'标记明确对应所问对角线/已有柱棱/已切旧顶点，不更改几何、投影、题干、文字、原格线或基座；二次视觉复核后再交付。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
    (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
    result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
    (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'count_batch_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(2*600,2*625),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    im=Image.open(r['image']).convert('RGB').resize((600,600));x=n%2*600;y=n//2*625;canvas.paste(im,(x,y+25));draw.text((x+8,y+5),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'count_batch_contact.png')
