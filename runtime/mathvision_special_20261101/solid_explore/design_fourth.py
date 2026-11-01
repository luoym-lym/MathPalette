from pathlib import Path
import os,sys,json
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(OUT/'mpl_cache');sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config,file_hash
from renderer_adapter import RendererAdapter
from render_plugins import PluginRenderer
from PIL import Image,ImageDraw
cfg=load_config();cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'outputs');adapter=RendererAdapter(cfg)
plans=[('Solid148','paired_bars','A',['grid0','grid2','grid19','grid21'],'分别将1和7两个位置的上下边改为同色，诱导错误配对1/7。'),('Solid229','paired_bars','D',['line_0','line_2','line_10','line_16'],'分别将R和W两个面的上下边改为同色，诱导错误相对面R/W。')]
summary=[]
for qid,name,wrong,targets,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    actions=[{'type':'set_object_style','target':x,'color':'#DC2626','linewidth_pt':3} for x in targets]
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅原边颜色/白名单线宽，不盖字、不移动折边、不添加条件；待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
    (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
    result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
    (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'fourth_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(1000,526),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    im=Image.open(r['image']).convert('RGB').resize((500,500));x=n*500;canvas.paste(im,(x,26));draw.text((x+8,6),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'fourth_contact.png')
