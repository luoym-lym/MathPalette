from tools13 import *
R='#DC2626';B='#2563EB';G='#16A34A';O='#EA580C'
def style(target,color,role,width=2):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width},role
def save(qid,vid,wrong,items,intent,proof):
    check=eligibility(qid);assert check['eligible'],check
    actions=[a for a,r in items]
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':vid,'intent':intent,'params':{'actions':actions}}
    folder=TASK/qid/vid
    report=AD.render_candidate(plugin,folder)
    ctx=json.loads((folder/'context.json').read_text(encoding='utf-8'))
    objects={o['id']:o for o in ctx['objects']}
    roles=[{'action_index':i,'action':a,'role':r,'fresh_context_object':objects.get(a.get('target'))} for i,(a,r) in enumerate(items)]
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':wrong,'frozen_before_tests_at':datetime.now(timezone.utc).isoformat(),'intended_misconception':intent,'marker_roles':roles,'primary_unique_mathematics':proof,'human_semantics':'Only existing source edges recolored. No geometry, fills, text, cuts, counts or given relations added. Colors are appearance cues, not stipulated equalities. Original information must remain readable.','image_sha256':report['png_sha256'],'pixel_sha256':report['pixel_sha256'],'correct_answer':AD.records[qid]['answer'],'approval_status':'Unreviewed primary exploration; requires NEW independent parent review before delivery.'})
    write(folder/'eligibility_at_render.json',check)
    print(qid,vid,wrong,report['png_sha256'],flush=True)
if __name__=='__main__':
    save('Solid162','white_terminal_face_swap','B',[
        style('maine20',R,'Back boundary of the visible top white unit face; identifies the upper terminal cube',3),
        style('maine12',R,'Left receding boundary of the same source white top face',3),
        style('maine33',B,'Bottom receding boundary of the white lower back-right unit face',3),
        style('maine35',B,'Back vertical boundary of that same source white side face',3),
        style('Be2',R,'Back top edge of the left terminal in the Z option, paired to source top terminal',3),
        style('Be3',R,'Adjacent receding edge of that terminal top face',3),
        style('Be20',B,'Outer side-depth edge of opposite terminal in B, paired to source lower side terminal',3),
        style('Be22',B,'Outer vertical edge of that same B terminal side face',3)],
        'Map the two actually visible white terminal face fragments to the two ends of planar zigzag B, mistaking projected separation for the hidden adjacency pattern.',
        'The gray material already occupies exactly four observed cells: (0,0,0),(0,0,1),(0,1,1),(1,0,0). Dark also fills four: (1,0,1),(2,0,0),(2,0,1),(2,1,1). The four remaining cells are (0,1,0),(1,1,0),(2,1,0),(1,1,1): a planar T with a degree-three central cube, congruent only to D. The source cube grid and gray/dark fills remain unchanged. B is a degree-two zigzag path, so the colored terminal correspondence is not a mathematical equivalence.')
    save('Solid198','upper_white_run_to_L','E',[
        style('maine20',R,'Back edge of left white top cell',3),style('maine12',R,'Left edge of left white top cell',3),
        style('maine29',B,'Back edge of right white top cell',3),style('maine30',B,'Right edge of right white top cell',3),
        style('Ee2',R,'Back edge of left end in E top row, bound to first source white top face',3),style('Ee3',R,'Left side of E left end top face',3),
        style('Ee12',B,'Back edge of E opposite top-row end, bound to second source white top face',3),style('Ee14',B,'Right side of same E terminal top face',3)],
        'Treat the visible adjacent white top squares as the separated endpoint faces of the L piece E, overlooking the hidden offset of the lower white pair.',
        'Each nonwhite color has all four cubes determined from the front/top/right visible material cells. The remaining white cells are (0,1,0),(1,1,0),(1,1,1),(2,1,1). This is a planar offset pair (zigzag S) congruent to C. E is planar L with a straight run of three cubes; white has longest straight run two. A and B are nonplanar and D is a 2x2 square. Thus C remains unique; colors on boundaries do not change material fills.')
    save('Solid96','circumference_volume_transfer','A',[
        style('small1toprim',R,'First small full circumference contributing one strip width'),
        style('small2toprim',B,'Second small full circumference contributing the other strip width'),
        style('largetoprim',R,'Resulting full circumference visually grouped with small first rim'),
        style('small1frontseam',G,'First strip vertical opening seam; common height reference'),
        style('small2frontseam',G,'Second opening seam; same vertical strip height'),
        style('largefrontseam',G,'Result assembly seam; same height unchanged')],
        'Transfer the additive two-strip lateral area/circumference correspondence directly to cylinder volume, predicting double rather than squared radius scaling.',
        'Unrolling each curved surface gives width 2*pi*r and height h. Joining side by side doubles circumference to 4*pi*r without changing height, so R=2r and Vnew/Vold=(2r)^2/r^2=4. D is unique. The original top/bottom ellipses and seam positions remain frozen; no equal-radius symbols are added.')
