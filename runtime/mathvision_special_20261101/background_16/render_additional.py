import tools_local as t
RED='#DC2626';BLUE='#2563EB'
def meta(q):return t.json.loads((t.HERE/q/'context.json').read_text())
def part(q,oid,s,e,col=RED):
    p=t.json.loads((t.HERE/q/'paths_public.json').read_text())[oid][0]
    return {'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':s,'end':e,'wrap':False}}
def style(oid,col=RED):return {'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2}
def edge(q,a,b,col=RED):
    scene=t.json.loads((t.ROOT/('PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry')/t.json.loads((t.HERE/q/'formal_record.json').read_text())['scene']).read_text(encoding='utf-8-sig'))
    import numpy as np
    a=np.array(a);b=np.array(b)
    for o in meta(q)['objects']:
        if o.get('kind')!='segment' or not o.get('styleable'):continue
        p=o['geometry']['points'];p=[scene['points'][x] if isinstance(x,str) else x for x in p];c,d=map(np.array,p)
        v=d-c;den=v@v
        if den==0:continue
        s=float((a-c)@v/den);e=float((b-c)@v/den)
        if np.linalg.norm(c+s*v-a)<1e-10 and np.linalg.norm(c+e*v-b)<1e-10 and min(s,e)>-1e-10 and max(s,e)<1+1e-10:
            return part(q,o['id'],max(0,min(s,e)),min(1,max(s,e)),col)
    raise ValueError((q,a.tolist(),b.tolist()))
if t.BRANCH=='SolidGeometry':
    q='Solid151';actions=[];roles=[]
    for oid,col in [('gridh023',RED),('gridh123',RED),('gridh020',BLUE),('gridh120',BLUE)]:
        for s,e in [(0,1/3),(2/3,1)]:
            actions.append(part(q,oid,s,e,col));roles.append(oid+' existing '+('left' if s==0 else 'right')+' corner-cell boundary span; matched by color to the corresponding corner of the given checkerboard or option C, without marking the distinguishing center cell.')
    t.render(q,'checkerboard_corner_binding',actions,'C',
        'Match the four actual black corner features of the given checkerboard face to option C using top red and bottom blue partial grid-edge spans; test copying the familiar corner pattern and overlooking the global15-black constraint.',roles,
        'Count black corner incidences across the five given faces:15; candidate A/E add3 and hence give6 black corner cubes, B/C add4 and D adds2, impossible multiples of3. The five-face edge-mid incidence sum is8; A/E add2, yielding5 black edge cubes. Given black face centers=4; A center is white, E center black. A yields15 exterior black cubes and an internal white cube, E would force16 exterior black cubes. Therefore A uniquely fits15 black total. Colors affect only existing grid-edge intervals; no fill or face count is changed.')
    q='Solid189'
    t.render(q,'plan_center_height_swap',[style('planedge34'),style('planedge35'),style('towere10'),style('towere12')],'18',
        'Pair the central light plan-cell corner with a visible two-high light tower-column top corner. Test misassigning the central column height2 instead of4 while matching the8 outer light columns correctly.',
        ['planedge34 is the right boundary of the central light plan cell.','planedge35 is the top boundary of that same central light plan cell; the two source edges form an open corner rather than a new region.','towere10 is the visible front top edge of the light column at (-2,0), height2.','towere12 is the adjacent receding top edge of that same two-high column. The paired open corners encode a specific wrong plan/height correspondence.'],
        'Columns at Manhattan distance d from the center have height4-d, d=0..3. Plan light columns are d=0 and d=2. There is one center column height4 and8 distance2 columns each height2, so4+8*2=20 light blocks. The marked two-high column is not the center: its actual location and all black/white fills remain visible. Incorrect centerheight2 produces18.')
    q='Solid222'
    actions=[edge(q,[2,0,3],[3,0,3]),edge(q,[2,0,2],[2,0,3]),edge(q,[3,0,2],[3,1,2]),edge(q,[3,1,1],[3,1,2])]
    t.render(q,'staggered_face_cell_overlap',actions,'18',
        'Pair open corners of the front upper-right black square and the right front-middle black square. Test incorrectly identifying staggered face cells as one edge cube and duplicating this subtraction on the opposite pair.',
        ['Front upper-right black cell top edge, a real painted-corner cube feature.','Front upper-right black cell left edge gives the same open-corner feature without enclosing a new region.','Right front-middle black cell top edge is at a different height but paired in red.','Right front-middle black cell far edge completes the second open corner; false coincidence would subtract two nonexistent overlaps.'],
        'Front/back fourcorners andcenter shade8 corner cubes+2 facecenters. Right/left alternating edgemiddle pattern shades8 distinct edgemiddle cubes. Top/bottom each shade1 center. These three sets are disjoint, so total8+2+8+2=20. Opposite faces same patterns is retained verbatim; no unshown face, cell or paint is added. The red corners are on two different cubes separated by a grid step.')
else:
    q='Plane206';obs=meta(q)['objects']
    actions=[edge(q,[9,7],[10,7]),edge(q,[10,7],[11,7]),edge(q,[11,7],[12,7])]
    # Third option has a four-unit exposed left-to-right profile; match its
    # actual vertical support rail against the source's three-unit long leg.
    candidates=[o for o in obs if o['id'].startswith('option2_')]
    # Select the long vertical rail on the right-facing stem, x=13 in the
    # frozen picture. Exact coordinates come from the current object context.
    byx={}
    for o in candidates:
        a,b=o['geometry']['points']
        if a[0]==b[0]:byx.setdefault(a[0],[]).append((min(a[1],b[1]),max(a[1],b[1]),o['id']))
    # The rail at the third pattern's main stem is the longest consecutive run.
    def longest(items):
        best=[]
        for a in items:
            run=[b for b in items if b[0]>=a[0]];run=sorted(run);cur=[];end=a[0]
            for b in run:
                if b[0]>end:break
                cur.append(b);end=max(end,b[1])
            if len(cur)>len(best):best=cur
        return best
    rail=max((longest(v) for v in byx.values()),key=len)
    actions +=[style(oid) for a,b,oid in rail]
    t.render(q,'long_leg_whole_profile_binding',actions,'3',
        'Match the source L three-cell horizontal long leg to the third composite pattern longest vertical rail. Test mistaking the combined outline span for the required long leg of one piece and rejecting that pattern.',
        ['Three consecutive existing source lower edges encode its actual3-unit long leg.']+['Third pattern existing rail edge '+oid+'; together these encode its4-unit composite span, whose false identification with one L leg can exclude this otherwise tileable pattern.' for a,b,oid in rail],
        'All four8-cell target patterns admit exact coverings by two congruent L tetrominoes, allowing rotations as implicit in rearrangement. Independent cell-set exact-cover search will save a witness for every pattern. The red rail stays on existing unit-grid edges, adds no segmentation and does not prescribe an internal cut. Correct count remains4.')
    q='Plane489'
    actions=[];roles=[]
    for oid in ['c00','c04','c40','c44']:
        actions.append(part(q,oid,0,.5));roles.append(oid+' two original adjacent corner-square edges; identifies a painted face-corner feature whose unit cube is shared by three faces.')
    for oid in ['c11','c13','c31','c33']:
        actions.append(part(q,oid,0,.5));roles.append(oid+' two original adjacent internal painted-square edges; matches the corner-cell feature without a new cut, tempting the same one-face count for shared and unshared cells.')
    t.render(q,'corner_face_incidence_binding',actions,'53/125',
        'Pair open corners of four painted face-corner cells and four internal painted cells in red. Test treating all12 painted squares per face as distinct unit cubes across all6 faces, ignoring corner sharing.',roles,
        'The shown face has8 painted cells in the central3x3 ring plus4 corners. Across six faces the48 noncorner painted cubes are distinct; the24 corner-face incidences represent8 corner cubes. Thus56 cubes are painted and125-56=69 have no paint:69/125. Open boundary recolorings preserve every semanticgray/whitefill and every25-cell boundary; wrong independent-face counting yields125-6*12=53.')
