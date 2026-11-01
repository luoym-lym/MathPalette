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
def styles(ids,color='#DC2626'):
    return [{'type':'set_object_style','target':x,'color':color,'linewidth_pt':2} for x in ids]
def overlay_existing(qid,ids):
    scene=adapter.scenes[qid];objs={o['id']:o for o in scene['objects']};actions=[]
    for n,oid in enumerate(ids):
        endpoints=[adapter.renderer.project(scene,adapter.renderer.point(scene,r)).tolist() for r in objs[oid]['points']]
        actions.append({'type':'add_line','id':f'color_pair_{n}','endpoints':endpoints,'color':'#DC2626','linestyle':'solid'})
    return actions
plans=[
('Solid176','false_flap_pair','D',styles(['flap310b','flap311b','flap300b','flap301b']),'仅将D的四条三角瓣斜边同色，诱导错误判断D折后碰撞而非C。'),
('Solid228','false_net_edge_pair','A',styles(['line_3','line_17']),'将A阶梯展开图两端的原外边同色，诱导错配封口边并错误判A无法成盒。'),
('Solid84','symbol_similarity_capture','A',styles(['targetline4','targetline5','option0line4','option0line5']),'以同色强调目标大菱形与错误选项A小菱形的上半部，诱导模型按形似配对而忽略要求相对面。'),
('Solid237','false_projected_face_pair','E',overlay_existing('Solid237',['0line_0','0line_1','2line_0','2line_1']),'用四条与原边精确重合的红辅助线配对R/P两个前面上下边，诱导把P误认A的相对色。标签、面与原线不改。'),
('Solid180','bounding_dimension_capture','1820',styles(['netedge0','netedge3','netedge5']),'突出与26、10、7显示范围平行的三条原线，诱导直接将三个总范围相乘1820，忽略展开图尺寸分解。'),
('Solid210','height_slant_pair','D',styles(['line_1','line_26']),'将扇形半径与错误D圆锥的轴线同色，诱导把扇形半径10配成圆锥高10而非斜高10。'),
('Solid218','cut_pyramid_capture','B',styles(['line_0','line_3','line_13']),'仅突出等边三角面G，诱导把单位立方体削去体积误算1/3，选择2/3。'),
('Solid221','invalid_position_capture','2',styles(['line_19','line_29']),'仅突出C/G两个不能构成无盖盒的候选外边，诱导把两个不能折的位置数误答成所求能折数量。')]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅原边颜色/白名单线宽或与原边重合的辅助线；不盖字、不移位、不新增折叠或等长条件。待用户审核。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    try:
        meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
        (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
        result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
        (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e:result={'question_id':qid,'name':name,'status':'error','error':str(e)}
    summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'net_batch_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(4*400,2*425),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    if r['status']!='rendered':continue
    im=Image.open(r['image']).convert('RGB').resize((400,400));x=n%4*400;y=n//4*425;canvas.paste(im,(x,y+25));draw.text((x+8,y+5),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'net_batch_contact.png')
