from pathlib import Path
import os,sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(OUT/'mpl_cache')
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config,file_hash
from renderer_adapter import RendererAdapter
from render_plugins import PluginRenderer
from PIL import Image,ImageDraw
cfg=load_config(); cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'outputs')
adapter=RendererAdapter(cfg)
RED='#DC2626'
def styles(ids,width=2):
    return [{'type':'set_object_style','target':x,'color':RED,'linewidth_pt':width} for x in ids]
plans=[
 ('Solid165','red_quadrilateral','D','360 degrees',[*styles(['diagPQ','diagPS','cube011_cube111','cube110_cube111'])], '四条既有空间边同色连成强投影闭环，诱导按平面四边形内角和作答。'),
 ('Solid202','red_quadrilateral','D','360 degrees',styles(['line_12','line_13','line_7','line_11']), '将WXYZ的投影闭环以同色突出，诱导平面内角和360。'),
 ('Solid243','equilateral_capture','60','60 degrees',styles(['line_0','line_1','line_3']), '突出等边侧面ABC，使模型将ABD误绑为ABC。原字母和棱保持清晰。'),
 ('Solid244','rectangular_base_capture','60','60',styles(['line_0','line_1','line_3','line_4']), '仅将底面四棱同色，诱导把三角底ABC误读为矩形底ABCD，得到3倍体积60。'),
 ('Solid248','diameter_completion','20','20',[{'type':'add_line','id':'diameter_left','endpoints':[[-3,5],[0,5]],'color':RED,'linestyle':'solid'},{'type':'set_object_style','target':'line_4','color':RED}], '以同色补全圆口直径，诱导将明确r=3视觉读作d=3。原r字样、原半径和标签不移动。'),
 ('Solid223','large_face_group','15','15',[{'type':'add_point','id':'face6_marker','xy':[0.2,1.25],'color':RED},{'type':'add_point','id':'face4_marker','xy':[2.2,1.25],'color':RED},{'type':'add_point','id':'face5_marker','xy':[3.2,1.25],'color':RED}], '仅用三个同色小点分组最大数字6/4/5，诱导忽略折叠后的相对面约束。点不盖字、不成为点名。'),
]
summary=[]
for qid,name,wrong,wrong_sem,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'诱导错误答案 '+wrong_sem,'params':{'actions':actions}}
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'expected_wrong_semantics':wrong_sem,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'human_solvability':'仅增补颜色/点/辅助线，不修改题干、标签、数值、三维几何、投影或原可见性；人类应使用明确题设。待用户审核。','status':'unreviewed_runtime_candidate'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    try:
        meta=adapter.inspect_question(qid)
        renderer=PluginRenderer(cfg,adapter,{qid:meta})
        normalized,data,pixels=renderer.render(plugin)
        (folder/'plugin.json').write_text(json.dumps(normalized,ensure_ascii=False,indent=2),encoding='utf-8')
        (folder/'candidate.png').write_bytes(data)
        _,data2,pixels2=renderer.render(plugin)
        assert pixels==pixels2 and data==data2
        result={'question_id':qid,'name':name,'status':'rendered','pixel_sha256':pixels,'png_sha256':file_hash(folder/'candidate.png'),'deterministic':True,'appearance_changes':renderer.appearance_changes(normalized),'action_count':len(actions),'baseline_matches_formal':True,'design':str(folder/'design.json'),'image':str(folder/'candidate.png')}
        (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e:
        result={'question_id':qid,'name':name,'status':'error','error':str(e)}
    summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'design_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(3*384,2*410),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    if r['status']!='rendered':continue
    im=Image.open(r['image']).convert('RGB').resize((384,384));x=n%3*384;y=n//3*410
    canvas.paste(im,(x,y+26));draw.text((x+8,y+6),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'candidate_contact.png')
