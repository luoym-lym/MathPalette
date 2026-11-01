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
def styles(ids):return [{'type':'set_object_style','target':x,'color':'#DC2626','linewidth_pt':2} for x in ids]
def overlay_existing(qid,ids):
    scene=adapter.scenes[qid];objs={o['id']:o for o in scene['objects']}
    return [{'type':'add_line','id':f'pair_edge_{n}','endpoints':[adapter.renderer.project(scene,adapter.renderer.point(scene,r)).tolist() for r in objs[oid]['points']],'color':'#DC2626','linestyle':'solid'} for n,oid in enumerate(ids)]
plans=[
('Solid176','minimal_top_pair','D',styles(['flap310b','flap311b']),'将已探索的四边方案简化，仅D上方两个三角瓣竖直短边同色，诱导错误的同向重叠判断，预设D。'),
('Solid84','false_cross_pair','E',styles(['cube1rightline0','cube1rightline1','option4line4','option4line5']),'源立方体的X面与错误选项E的X图案同色，诱导优先配对X图案而忽略实际所问相对面。此版明确改变着色对象，预设E。'),
('Solid228','stair_end_pair','A',styles(['line_0','line_2','line_16','line_18']),'将A阶梯展开图首尾两个面的上下边同色，诱导认为两端折后重复而错判A。'),
('Solid237','green_face_capture','C',overlay_existing('Solid237',['0line_4','0line_5','2line_4','2line_5']),'用与原边重合的四条红线突出两个视图的G面上下边，诱导把反复出现的绿色误绑为Aqua的相对色，预设C。')]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅原边样式或精确重合的辅助线；不盖字、不移动几何、不新增条件。待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
    (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
    result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
    (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'net_refinements_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(2*600,2*625),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    im=Image.open(r['image']).convert('RGB').resize((600,600));x=n%2*600;y=n//2*625;canvas.paste(im,(x,y+25));draw.text((x+8,y+5),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'net_refinements_contact.png')
