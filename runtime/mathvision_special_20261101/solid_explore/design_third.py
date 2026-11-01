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
def styles(ids):return [{'type':'set_object_style','target':x,'color':'#DC2626','linewidth_pt':2} for x in ids]
plans=[
('Solid148','false_roll_pair','A',styles(['grid0','grid19']),'仅把位置1与7的下边同色，诱导错误同面配对1/7。'),
('Solid175','false_roll_pair','A',styles(['grid0','grid19']),'仅把位置1与7的下边同色，诱导错误同面配对1/7。'),
('Solid229','false_face_pair','D',styles(['line_0','line_16']),'仅将R与W下边同色强调，诱导把R误作W的相对面，预设选D。'),
('Solid240','adjacent_face_capture','6',styles(['line_13','line_16']),'同色标出展开图Q和6的共同边与Q外侧边，诱导把展开图邻面6误作立体Q右侧面。')]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅颜色线宽覆盖，不增加几何条件，不盖字，不改变线型或3D/投影。待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    try:
        meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta})
        norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
        (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
        result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
        (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e:result={'question_id':qid,'name':name,'status':'error','error':str(e)}
    summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'third_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(2*500,2*526),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    if r['status']!='rendered':continue
    im=Image.open(r['image']).convert('RGB').resize((500,500));x=n%2*500;y=n//2*526;canvas.paste(im,(x,y+26));draw.text((x+8,y+6),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'third_contact.png')
