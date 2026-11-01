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
('Solid203','false_edge_pair','A',styles(['line_20','line_24']),'目标边x与相邻错误配对边A用相同红色突出，诱导视觉匹配忽略折叠。'),
('Solid166','false_edge_pair','1',styles(['netedge15','netedge11']),'目标边x与错误配对边1同色，诱导选择相邻红边。'),
('Solid220','false_face_pair','A',styles(['line_13','line_16']),'仅将X与Z的下边同色突出，诱导把平面近邻Z当成相对面。'),
('Solid217','false_face_pair','A',styles(['line_0','line_4']),'仅将x与A的下边同色突出，诱导把平面近邻A当成相对面。'),
('Solid243','equal_color_diagonal','60',styles(['line_0','line_2'])+[{'type':'add_line','id':'base_diagonal','endpoints':[[0.5,-0.5],[1.5,-0.5]],'color':'#DC2626','linestyle':'dashed'}],'将ABD轮廓同色，诱导把同色的底面对角线误作等长棱，得60度；该预设在测试前冻结。')
]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    if qid=='Solid243':
        snaps={p['id']:p['xy'] for p in adapter.snap_points(qid)}
        actions[-1]['endpoints']=[snaps['B'],snaps['D']]
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅样式和辅助线操作，不遮挡题干信息，不添加等长/匹配/相对面的条件；待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'诱导预设错误答案'+wrong,'params':{'actions':actions}}
    try:
        meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta})
        norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin)
        assert data==data2 and pixel==pixel2
        (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
        result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
        (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e:result={'question_id':qid,'name':name,'status':'error','error':str(e)}
    summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'more_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(3*384,2*410),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    if r['status']!='rendered':continue
    im=Image.open(r['image']).convert('RGB').resize((384,384));x=n%3*384;y=n//3*410;canvas.paste(im,(x,y+26));draw.text((x+8,y+6),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'more_contact.png')
