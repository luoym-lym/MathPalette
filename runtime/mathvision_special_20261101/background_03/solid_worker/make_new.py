from pathlib import Path
import sys
source=Path(__file__).with_name('prepare.py').read_text(encoding='utf-8').split('\nfor qid in sys.argv[1:]')[0]
exec(compile(source,str(Path(__file__).with_name('prepare.py')),'exec'))
R='#DC2626';B='#2563EB'
def style(target,color):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
configs={
 'Solid120':{'name':'false_tick_correspondence','wrong':'50','actions':[style('tick0_6',R),style('tick1_7',R),style('tick2_6',R)],'mechanism':'Red existing tick6 and existing tick28 are grouped as a false one-revolution correspondence (22 units); the red target-column tick prompts extrapolation 6+2*22=50. Correct same-angle values6,27 differ21; true answer6+2*21=48. All original ticks and numbers remain. Each of the three ticks has a role: lower anchor, misbound next-turn anchor, requested extrapolation position.','solution':'The same azimuth gives6 and27 on successive turns, so one revolution advances21. The ? is two turns above6:6+2*21=48.'},
 'Solid138':{'name':'false_tick_correspondence','wrong':'72','actions':[style('tick0_6',R),style('tick1_7',R),style('tick3_6',R)],'mechanism':'Red existing tick6 and tick28 suggest a false22-unit revolution; red question-column tick is three turns higher than6, predicting6+3*22=72. The real same-angle increment is27-6=21. This targets azimuth/range binding without altering any tick, label or tape edge.','solution':'The same-azimuth values6 and27 fix a21-unit revolution. The ? is three turns above6 and two turns above27:6+3*21=69.'},
 'Solid227':{'name':'linear_radius_volume_pair','wrong':'A','actions':[style('line_4',R),style('line_9',R),style('line_2',B),style('line_7',B)],'mechanism':'Match the original given radius10 and A radius20 in red while matching their equal heights5 in blue. This encodes doubled radius with same height and targets the false linear-volume rule V∝r*h, predictingA instead of the true quadratic radius rule. Four markers establish two specific dimension correspondences; no full-option outline.','solution':'Given radius10,height5 gives500π. A radius20,height5 gives2000π=4V. B radius10,height10 gives1000π=2V uniquely. C radius5,height10 gives250π=V/2, D radius20,height10 gives4000π=8V.'}
}
for qid in sys.argv[1:]:
    c=configs[qid];dst=TASK/qid/c['name']
    check=eligibility(qid)
    if not check['eligible']:raise ValueError('Became ineligible '+qid)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':c['mechanism'],'intent':'Predeclared target '+c['wrong'],'params':{'actions':c['actions']}}
    adapter.render_candidate(plugin,dst)
    write(dst/'eligibility_before_design.json',check)
    write(dst/'design.json',{'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':c['wrong'],'correct_answer':adapter.records[qid]['answer'],'mechanism':c['mechanism'],'unique_solution':c['solution'],'second_review_status':'pending; no independent review performed','approval_status':'runtime research only; no Pass or Collect'})
    print(json.dumps({'question_id':qid,'name':c['name'],'preset':c['wrong'],'png_sha256':sha(dst/'candidate.png')}),flush=True)
