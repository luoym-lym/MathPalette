"""Finish already-investigated bridge candidates; never launch an API call."""
from pathlib import Path
import json
from bridge_adapter import RuntimeBridgeAdapter

OUT=Path(__file__).resolve().parent
adapter=RuntimeBridgeAdapter()
plans=[
('Solid166','bridge_terminal_edge_pair','1',['netedge15','netedge11'],'八面体展开图中的目标边x与错误边1同色，两条均为实际原边、分处上下两个三角瓣，编码错误的封边对应。正式应为边5；无新增几何或文字。'),
('Solid203','bridge_terminal_edge_pair','A',['line_20','line_24'],'八面体展开图目标边x与错误选项边A同色，编码错误封边对应；两条为不同原边，正式应为E。无新线、点或文字。'),
('Solid240','bridge_false_hinge_mapping','6',['line_13','line_20'],'将平面展开图Q/6的公共折边与立体图Q/?的公共边同色，建立错误的展开边到空间边映射，诱导?=6；正式应为1。原折叠、显隐和字形不改。')]
predeclared=[{'question_id':qid,'name':name,'expected_wrong_answer':wrong,'targets':targets,'mechanism':reason} for qid,name,wrong,targets,reason in plans]
(OUT/'bridge_predeclared_designs.json').write_text(json.dumps(predeclared,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary=[]
for qid,name,wrong,targets,reason in plans:
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':'预设错误'+wrong,'params':{'actions':[{'type':'set_object_style','target':t,'color':'#DC2626','linewidth_pt':2} for t in targets]}}
    target=OUT/qid/name
    report=adapter.render_candidate(plugin,target)
    design={'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'status':'PREPARED_NOT_TESTED','second_review_status':'pending','human_solvability':'只改两条原边的颜色/线宽，原实虚线保持，不改几何、投影、可见性、标签或题干；尚未通过双测或独立二次复核。'}
    (target/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary.append({'question_id':qid,'name':name,'path':str(target),'expected_wrong_answer':wrong,'baseline_matches_formal':report['baseline_matches_formal'],'deterministic':report['deterministic'],'status':'PREPARED_NOT_TESTED'})
    print(json.dumps(summary[-1],ensure_ascii=False),flush=True)
(OUT/'bridge_prepared_candidates.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
