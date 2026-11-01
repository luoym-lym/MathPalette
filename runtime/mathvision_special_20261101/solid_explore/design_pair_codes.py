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
def pairs(red,blue):return [{'type':'set_object_style','target':t,'color':c,'linewidth_pt':2} for c,targets in [('#DC2626',red),('#2563EB',blue)] for t in targets]
plans=[
('Solid176','two_color_lid_pairing','D',pairs(['flap310b','flap311b'],['flap300b','flap301b']),'将D上方两条端盖外边配红，下方两条闭合对角边配蓝。蓝色对应确实闭合的同一底盖对角线；红色错误配对的是顶盖相对两外边，诱导以相同颜色对应方式错误判D不能闭合。仅颜色编码，无新增黏合条件。'),
('Solid229','two_color_opposite_pairing','D',pairs(['line_0','line_16'],['line_7','line_13']),'用红色下边配对R/W两个面，用蓝色下边配对实际相对的G/O两个面。正确G/O分组强化颜色作为对应线索，诱导把红R/W误读为相对面。数学上W仍唯一与B相对，边色不构成条件。')]
summary=[]
for qid,name,wrong,actions,reason in plans:
    folder=OUT/qid/name;folder.mkdir(parents=True,exist_ok=True)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'unreviewed_runtime_candidate','human_solvability':'仅四条原边双色编码，不添线/点/字、不遮挡、不移动边；原数学问题唯一。须经第二次独立复核后才交付。'}
    (folder/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误答案'+wrong,'params':{'actions':actions}}
    meta=adapter.inspect_question(qid);renderer=PluginRenderer(cfg,adapter,{qid:meta});norm,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin);assert data==data2 and pixel==pixel2
    (folder/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8');(folder/'candidate.png').write_bytes(data)
    result={'question_id':qid,'name':name,'status':'rendered','baseline_matches_formal':True,'deterministic':True,'pixel_sha256':pixel,'png_sha256':file_hash(folder/'candidate.png'),'action_count':len(actions),'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'image':str(folder/'candidate.png'),'design':str(folder/'design.json')}
    (folder/'render_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');summary.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
(OUT/'pair_codes_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
canvas=Image.new('RGB',(1200,625),'white');draw=ImageDraw.Draw(canvas)
for n,r in enumerate(summary):
    im=Image.open(r['image']).convert('RGB').resize((600,600));x=n*600;canvas.paste(im,(x,25));draw.text((x+8,5),r['question_id']+' / '+r['name'],fill='black')
canvas.save(OUT/'pair_codes_contact.png')
