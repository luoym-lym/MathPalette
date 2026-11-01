from research import *
from bridge_adapter import RuntimeBridgeAdapter
from partial_style import object_paths

adapter=RuntimeBridgeAdapter()
RED='#DC2626'
BLUE='#2563EB'

def style(target,color=RED,**extra):
    return dict(type='set_object_style',target=target,color=color,**extra)

def make(qid,name,expected,actions,mechanism,math_check,roles):
    check=eligible('SolidGeometry',qid)
    if not check['eligible']:raise ValueError((qid,check['exclusion_reasons']))
    folder=HERE/qid/name
    folder.parent.mkdir(parents=True,exist_ok=True)
    context=adapter.inspect_question(qid)
    path_bindings=[]
    for action in actions:
        if '_range' in action:
            low,high=action.pop('_range')
            scene=adapter.scene(qid)
            try:
                scene.fig.canvas.draw()
                paths=object_paths(scene,action['target'])
                if len(paths)!=1:raise ValueError('Expected exactly one source vector path')
                path=paths[0]
                action['interval']={'path_id':path['id'],'path_sha256':path['sha256'],
                                    'start':low,'end':high,'wrap':False}
                path_bindings.append({'target':action['target'],**action['interval'],
                                      'parameter_basis':'exact affine source segment parameter'})
            finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':mechanism,'intent':'predeclared wrong answer '+expected,'params':{'actions':actions}}
    report=adapter.render_candidate(plugin,folder)
    write(folder/'design.json',{'question_id':qid,'branch':'SolidGeometry','variant_id':name,
        'expected_wrong_answer':expected,'correct_answer':check['record']['answer'],
        'mechanism':mechanism,'unique_solution_primary_check':math_check,'marker_roles':roles,
        'path_bindings':path_bindings,'status':'PREDECLARED_BEFORE_BOTH_CALLS',
        'second_review_status':'not_started_required_if_two_hits',
        'frozen_scene_changes':False,'approval':'No Pass/Collect or formal approval'})
    write(folder/'eligibility_before_design.json',check)
    print(json.dumps({'qid':qid,'variant':name,'expected':expected,'markers':len(actions),
                      'baseline':report['baseline_matches_formal'],'repeat_identical':report['deterministic']},ensure_ascii=False))

if __name__=='__main__':
    selected=sys.argv[1:]
    if not selected:selected=['Solid238','Solid245','Solid246','Solid242']
    if 'Solid238' in selected:
        make('Solid238','subrange_14_binding','448',
             [style('line_6',_range=(0,3/7),linewidth_pt=2),style('line_8',BLUE,linewidth_pt=2),style('line_7',BLUE,linewidth_pt=2)],
             'Red isolates GJ inside given GH=14; blue pairs BJ with AH=8. The intended range error assigns the whole 14 to marked GJ, giving (14*8/2)*8=448 rather than subtracting HJ.',
             'Triangle BGJ is a prism end. Rectangle ABJH on its edgeBJ gives BJ=AH=8. Rectangle FIDE on the other end has axial edgeFE=8; all axial edges are equal after folding, hence HJ=AB=FE=8. Since G,J,H are collinear in that order and GH=14, GJ=14-8=6. Right angleBJG is explicitly marked. Base area=8*6/2=24; axial length=8. Volume=192. Red cannot make the whole GH=14 into the legGJ.',
             ['Red line_6 interval [0,3/7] is exactly G-to-J, tempting total/subrange 14 binding.',
              'Blue line_8 is BJ, the leg corresponding to AH.',
              'Blue line_7 is AH, carrying the formal given8 and establishing the BJ basis.'])
    if 'Solid245' in selected:
        make('Solid245','height_to_slant_pair','228\\pi',
             [style('line_7',linewidth_pt=2),style('line_4',linewidth_pt=2)],
             'Pair the axial height segment marked8 with the right slant segment markedL in red. This encourages substitution L=8 into lateral area while retaining diameters8 and20; wrong total=228pi.',
             'R=10,r=4,h=8. True generatrix L=sqrt((10-4)^2+8^2)=10. Total area=pi(R+r)L+pi(R^2+r^2)=(140+116)pi=256pi. If L is confused with h=8, result=(112+116)pi=228pi.',
             ['Red line_7 selects the axial height8.', 'Red line_4 selects the true slant generatrix L as the misleading counterpart.'])
    if 'Solid246' in selected:
        make('Solid246','whole_width_to_AB_pair','\\frac{3}{2}\\pi',
             [style('line_6',linewidth_pt=2),style('line_4',_range=(0.5,1.0),linewidth_pt=2)],
             'Pair the whole lower card width labelled6 with upper subsegmentAB in red. The targeted range error treats AB as6 rather than3, doubling the difference in arc travel to3pi/2.',
             'B is6 inches from fold and A is3 inches from fold. Both rotate theta=45deg=pi/4. Difference=(6-3)*pi/4=3pi/4 inches, uniquely fixed by text. Color is appearance and adds no equality condition.',
             ['Red line_6 is full lower widthWO bearing6.', 'Red line_4 [0.5,1] is exactly upperAB, a subrange of the total upper widthTB; sourceA is affine midpoint.'])
    if 'Solid242' in selected:
        make('Solid242','cut_face_membership','96\\pi',
             [*[style(x,BLUE,linestyle='dashed') for x in ['line_2','line_3','line_4','line_5']],
              style('arc_0',linewidth_pt=2),style('arc_1',linewidth_pt=2)],
             'Blue dashed boundary identifies the rectangular cutting plane as if it were internal construction, while the red semicircular end rims group the curved boundary. The intended surface-membership error omits the new rectangular cut face, yielding96pi.',
             'Half-cylinder r6,h10. Curved surface=pi*r*h=60pi; two semicircular ends=pi*r^2=36pi; rectangular cut face=(2r)*h=120. Total=96pi+120. Text says solid, all boundary faces must count despite dashed appearance overrides.',
             ['Blue dashed line_2 is top diameterAC, cut-face boundary.', 'Blue dashed line_3 is bottom diameterac, cut-face boundary.',
              'Blue dashed line_4 is cut-face sideAa.', 'Blue dashed line_5 is cut-face sideCc.',
              'Red arc_0 is the top semicircular end rim.', 'Red arc_1 is bottom semicircular end rim, retaining its existing hidden dash style.'])
    if 'Solid213' in selected:
        context=adapter.inspect_question('Solid213')
        points={p['id']:p['xy'] for p in context['snap_points']}
        make('Solid213','nine_unit_basis_binding','C',
             [dict(type='add_line',id='xy_route',endpoints=[points['X'],points['Y']],color=RED,linestyle='dashed'),
              style('line_5',_range=(0,0.9),linewidth_pt=2),style('line_12','#16A34A',linewidth_pt=2)],
             'Red pairs the complete XY diagonal with the lower9 units of the stack height, excluding the top1 cube. Green selects the side3 cube height. The intended basis error uses3/9 instead of3/10 for the in-cube diagonal portion, yielding optionC=2sqrt33/3.',
             'Set X=(0,0,10),Y=(4,4,0). Along segment P(t)=(4t,4t,10-10t), lengthXY=sqrt132=2sqrt33. Side3 cube is [0,3]x[0,3]x[4,7]. The z interval gives t in[0.3,0.6], and x,y bounds allow t<=0.75, so the portion length is0.3*2sqrt33=3sqrt33/5, uniquely optionA. The lower9-unit selected reference omits the top cube and is not a true basis for totalXY.',
             ['Red dashed added line joins the exact current context X and Y; it locates the segment asked about.',
              'Red line_5 interval[0,0.9] is the lower9 of the10-unit total height, creating the false full-diagonal reference.',
              'Green line_12 is the side3 cube vertical edge, identifying the numerator3 without modifying any labels.'])
