from tools import *
from partial_style import object_paths
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
PATHS={}
def paths(qid):
    if qid not in PATHS:
        if (TASK/qid/'path_context.json').exists():
            PATHS[qid]=read(TASK/qid/'path_context.json');return PATHS[qid]
        s=AD.scene(qid)
        try:
            s.fig.canvas.draw();result={}
            for obj in s.objects:
                oid=obj['id']
                if not obj.get('styleable') or not s.artists.get(oid):continue
                result[oid]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[v['control'].tolist() for v in p['segments']]} for p in object_paths(s,oid)]
            PATHS[qid]=result
            write(TASK/qid/'path_context.json',result)
        finally:s.close()
    return PATHS[qid]
def style(oid,color,width=2):return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width}
def part(qid,oid,start,end,color,width=2):
    p=paths(qid)[oid][0]
    return style(oid,color,width)|{'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
def make(qid,name,wrong,actions,mechanism,proof,roles):
    assert len(actions)==len(roles)
    if (TASK/qid/name/'design.json').exists():
        print(qid,name,'already created; unchanged');return
    candidate(qid,name,wrong,actions,mechanism,proof,[{'action_index':i+1,'role':r} for i,r in enumerate(roles)])
if BRANCH=='PlaneGeometry':
    q='Plane402'
    make(q,'exposed_strip_extent_binding','26/3',[
        part(q,'o0',0,.25,RED),part(q,'o1',0,.25,RED),style('o4',RED)],
        'Bind the original 13-unit long edge to the exposed straight lengths of P and Q in red, inviting the missing-overlap error x+q=13 and x=26/3. The 4-unit fold elbow, 45-degree line, all dashed dimensions and P/Q labels remain intact.',
        'Let q be the exposed height of Q. The 45-degree fold consumes a 4 by 4 elbow of strip length 4, so x+4+q=13. Since P=4x and Q=4q with P=2Q, x=2q and 3q=9: q=3,x=6 uniquely. Color is an annotation, not an equality or an extra constraint.',
        ['Original bottom edge: full length 13 to be wrongly matched to only the two exposed straight spans.','P bottom edge: first constituent x of the misleading exposed-length sum.','Q right side: second constituent q of that sum; it is perpendicular after folding and not a second independent source length.'])
    q='Plane409';a=[part(q,'trapezium0',0,.25,RED),part(q,'trapezium0',.5,.75,BLUE)];roles=['Original long base b: red source for the false short-base correspondence.','Original short base a: blue source for the false long-base correspondence.']
    for i in range(3):
        a += [part(q,f'joinedtrapezium{i}',.5,.75,RED),part(q,f'joinedtrapezium{i}',0,.25,BLUE)]
        roles += [f'Assembled trapezium {i+1} short base a: falsely paired to source b by red.',f'Assembled trapezium {i+1} long base b: falsely paired to source a by blue.']
    make(q,'assembled_base_identity_swap','C',a,
        'Swap the color correspondence of the labeled short and long source bases with their three rotated assembled counterparts. This targets a/b identity during rotation and invites 3(2b-a), choice C; it adds no equality marks or cut lines.',
        'Write t for either equal leg. The 60-degree assembly makes the horizontal excess of the long base b over the short base a equal t, so t=b-a. Each side of the equilateral hole is a-t=2a-b. Its perimeter is 6a-3b, uniquely E. Frozen display a=4,b=5,t=1 gives hole side3 and confirms this. Colors do not rename a/b, impose equal lengths, or alter the black semantic hole fill.',roles)
    q='Plane476';s=read(TASK/q/'source_scene_snapshot.json')['points']
    make(q,'ratio_whole_side_denominator','A',[
        part(q,'upper4',.25,.5,BLUE),
        {'type':'add_point','id':'numerator_X','xy':s['X'],'color':RED},
        {'type':'add_point','id':'numerator_Q','xy':s['Q'],'color':RED}],
        'The two red endpoint markers identify numerator XQ while the blue entire XY side suggests a denominator span XY in place of QY, inviting XQ/XY=2/5, choice A. All named original points remain readable; no region boundary or counting target is added.',
        'Let h be Q height above the base, with unit grid coordinates P=(0,0),X=(5,2),Y=(5,1). The lower portion comprises the rightmost unit square plus the triangle of base5 and height h. Thus 1+5h/2=10/2 gives h=8/5. XQ=2/5 and QY=3/5, so the required ratio is2/3, uniquely D. Endpoint markers coincide with existing marked points and do not add area or alter any edge.',
        ['Whole original XY edge: denominator substitution cue, length1.','Existing X point: first endpoint of the numerator XQ.','Existing Q point: second endpoint of the numerator XQ.'])
    q='Plane378';a=[];roles=[]
    for i in [0,1,2]:
        a.append(part(q,f'rectangle{i}',.5,.75,RED));roles.append(f'Top-row rectangle {i+1} long top edge: one of three congruent long units across DC.')
    for i in [3,4]:
        a.append(part(q,f'rectangle{i}',.75,1,RED));roles.append(f'Left column rectangle {i} long vertical edge: one of two long units below the omitted top strip.')
    make(q,'long_unit_top_strip_omission','D',a,
        'Match three horizontal long edges across DC with two vertical long edges in the left column, inviting AD/DC=2/3 by omitting the uncolored top short-width strip. Each mark identifies an actual congruent-rectangle long side; D remains at the full upper-left corner.',
        'Let a and b be small rectangle long and short sides. The common lower height equals2a in the left column and3b in the center, so2a=3b. Full AD=2a+b=4b while DC=3a=9b/2. Therefore AD/DC=8/9 uniquely A. The top short strip is present, visible and still part of AD.',roles)
else:
    q='Solid134';a=[];roles=[]
    colors=[RED,GREEN,BLUE];heights=[.52,.65,.39]
    for i in range(3):
        a.append(part(q,f'front{i}edge3',1-heights[i],1,colors[i]));roles.append(f'Front vase {i+1} left side below the original water surface: actual water-height span, not a new level.')
    for option_vase,source_vase in [(0,2),(1,1),(2,0)]:
        a.append(style(f'option1vase{option_vase}edge1',colors[source_vase]));roles.append(f'B top view vase {option_vase+1} depth edge: color-paired to source vase {source_vase+1}, swapping I/III while keeping II.')
    make(q,'water_height_identity_swap','B',a,
        'Use three colored actual water-height spans and the corresponding top-view depth edges in B, swapping the identities of I and III. This invites the otherwise correct inverse-height reasoning to assign the greater depth to I instead of III. Roman numerals and gray water fill stay unchanged.',
        'All three front widths are equal. A rectangular vase volume is front width times depth times water height. Water heights satisfy hII>hI>hIII. Because VI=VIII=4, depthIII>depthI. Also VII=3<4 and hII>hI, so depthII<depthI. Hence depthIII>depthI>depthII. Only A has that depth ordering. B reverses I and III; C,D,E fail the necessary ordering. Relative pixel heights are not treated as exact givens.',roles)
    q='Solid140'
    make(q,'rotation_axis_dimension_swap','B',[
        style('leftedge1',RED),style('rightedge7',RED),style('leftedge7',BLUE),style('rightedge0',BLUE)],
        'Pair the old 1m height with the new 2m depth in red, and the old 2m depth with the new 1m width in blue. This wrong axis transport targets a factor2 rise (50cm, B) in place of the actual factor4. All dimension text, water fill and edge visibility remain frozen.',
        'Original water volume is4*2*.25=2 cubic meters. After the shown rotation the base is1*2=2 square meters, hence height=1m uniquely D. Pair colors have no measurement semantics and cannot override the explicit 4m/2m/1m labels; the original water surface already depicts the correct conserved volume.',
        ['Original 1m vertical edge: red first member of the erroneous old-height/new-depth pair.','New 2m base-depth edge: red second member.','Original 2m base-depth edge: blue first member of the erroneous old-depth/new-width pair.','New 1m base-width edge: blue second member.'])
    q='Solid153';a=[];roles=[]
    for side in ['left','right']:
        a.append(part(q,'A'+side,0,.35,RED));roles.append(f'A {side} lower wall: narrow lower portion whose cumulative capacity controls a high half-volume level.')
        a.append(part(q,'E'+side,.35,.65,RED));roles.append(f'E {side} middle waist: paired local narrow feature invites local-neck reasoning rather than cumulative volume.')
    make(q,'local_neck_cumulative_volume_confusion','E',a,
        'Pair the narrow lower walls of A with the narrow middle waist of E using four partial original side-contour styles. This targets the misconception that the narrowest local neck creates the highest half-volume level, favoring E. No waterline, new contour, dimension or fill is added.',
        'A widens upwards, so its lower half contains less than half its full volume and the half-volume water level is above midheight. B has constant cross-section and reaches midheight. C and E have top/bottom symmetric profiles and reach midheight. D widens downwards, so half volume is below midheight. Thus A is uniquely highest. This is a qualitative profile argument; no exact pixel-derived volume is assumed.',roles)
