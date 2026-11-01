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
snaps={p['id']:p['xy'] for p in adapter.snap_points('Solid208')}
triangle=[{'type':'add_line','id':'section_'+a+b,'endpoints':[snaps[a],snaps[b]],'color':'#DC2626','linestyle':'dashed'} for a,b in [('D','M'),('M','N'),('N','D')]]
plans=[('Solid208','triangle_section_capture','23',triangle,'仅用三条红虚线连接题设D/M/N，诱导将三角形误认完整截面并把较小部分当1/12体积，错误p+q=23；原三点坐标、完整平面及题干不改。'),('Solid219','quarter_cut_capture','C',styles(['line_22','line_26','line_24','line_28']),'用同色强化两组切痕，诱导把角部件误认三个方向各半的1/8，预设错误C；不新增切面或移动切痕。')]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅受限标记，不盖字、不移动冻结几何，不增加题设条件；待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    try:
        meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
        (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
        result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
        (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e:result={'question_id':qid,'name':name,'status':'error','error':str(e)}
    summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'fifth_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(1000,526),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    if r['status']!='rendered':continue
    im=Image.open(r['image']).convert('RGB').resize((500,500));x=n*500;canvas.paste(im,(x,26));draw.text((x+8,6),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'fifth_contact.png')
