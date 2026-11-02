import tools_local as t
def part(q,oid,i,j,color='#DC2626',width=2):
    p=t.json.loads((t.HERE/q/'paths_public.json').read_text())[oid][0];n=len(p['controls'])
    return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':i/n,'end':j/n,'wrap':False}}
def style(oid,color='#DC2626',width=2):return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width}
def objects(q):return t.json.loads((t.HERE/q/'context.json').read_text())['objects']
def face_edge_line(q,oid,i,ident):
    meta=t.json.loads((t.HERE/q/'context.json').read_text());o=next(o for o in meta['objects'] if o['id']==oid);p=o['geometry']['points']
    xy=[]
    for point in [p[i],p[(i+1)%len(p)]]:
        xy.append(next(s['xy'] for s in meta['snap_points'] if s.get('world_xyz')==point))
    return {'type':'add_line','id':ident,'endpoints':xy,'color':'#DC2626','linestyle':'solid','linewidth_pt':1}
if t.BRANCH=='PlaneGeometry':
    q='Plane443'
    t.render(q,'opposite_long_edge_binding',[part(q,'o0',1/3,1),part(q,'o0',2+1/3,3),style('o3','#2563EB',1.5)],'A',
        'Pair the two opposite long boundary portions incident to the fold endpoints in red and retain the actual dashed fold in blue. Test mistaken equal-half folding rather than the oblique reflected overlap.',
        ['Red bottom boundary is the existing two-thirds length from the lower fold point toward the right corner.','Red top boundary is the existing two-thirds length from the upper fold point toward the left corner; paired long edges can induce a half-area symmetry shortcut.','Blue is the original dashed oblique fold, unchanged endpoints and dash semantics.'],
        'Set width=1,length=sqrt(3). Fold joins (L/3,0) to (2L/3,1). Reflection and polygon union give B/A=2/3, choice C. Colored intervals create no new dividing line or area; the original thirds and fold remain legible. Need independent numerical polygon-union verification in primary proof.')
    q='Plane278'
    t.render(q,'convex_neck_substitution',[part(q,'piece1',2,3),part(q,'piece3',2,3),part(q,'piece1',1,2,'#2563EB'),part(q,'piece4',1,2,'#2563EB')],'D',
        'Pair the same convex top feature on B and D in red and the concave right feature on B and E in blue. This partial feature substitution can wrongly make D seem redundant while keeping B.',
        ['B top convex arc is paired with D top convex arc; these are actual congruent source features.','D top convex arc is the second member of the red feature match, not an isolated answer contour.','B right concave arc is paired with E right concave arc.','E right concave arc is the second member of the blue match. The two roles together tempt a false B-for-D substitution, ignoring B extra concavity.'],
        'Curved-edge counts (convex,concave): A=(0,2),B=(1,1),C=(2,0),D=(1,0),E=(0,1). Straight square boundary requires curved edges paired convex to concave. Only omitting B balances three with three; A,C,D,E can form a square by pairing C two convex with A two concave and D convex with E concave. B is uniquely excluded. Open arc recolorings add no piece or cut and preserve all tangents/endpoints.')
else:
    q='Solid157'
    t.render(q,'missing_foot_branch_swap',[style('maine14'),style('Ae7'),style('maine18','#2563EB'),style('Ae15','#2563EB')],'A',
        'Pair a front cavity ledge with the A foot ledge in red and a receding source top edge with A elevated branch in blue. This swaps a planar T arm for the bent branch of A during depth completion.',
        ['maine14 is the existing upper horizontal border of the missing front cell.','Ae7 is A lower horizontal step ledge; the red pair binds actual unit-width ledges.','maine18 is the source existing receding top seam above the cavity, retained as a seam rather than a new cut.','Ae15 is A elevated receding branch edge, encoding the specific mistaken depth continuation.'],
        'The missing positions are {(0,1,0),(1,0,0),(1,1,0),(2,1,0)}: planar T tetromino. Its cube adjacency graph has one degree-3 cube. Only C has the same rigid cube set; A/B/D/E differ. Independently enumerate 24 proper cube rotations plus translation in primary proof. Every original texture and visible/hidden interval is unchanged; no filled face is edited.')
    q='Solid197'
    t.render(q,'crease_side_binding',[face_edge_line(q,'frontsticker0',0,'central_side'),face_edge_line(q,'frontsticker2',0,'fold_crease')],'450',
        'Bind a central square sticker side to the existing crease diagonal of the edge sticker using red open boundary intervals. Test reading the half-face crease length as a whole sticker side.',
        ['frontsticker0 first edge is an actual side of the central diamond-shaped sticker.','frontsticker2 first edge is the existing fold crease spanning the two sticker contact corners on the cube edge. The equal-color correspondence tempts diagonal/side substitution; no explicit equality symbol or dimension is added.'],
        'There are 6 face-center plus 12 edge stickers, all congruent squares. Each sticker has diagonal 5 cm, so area=5^2/2=12.5 and total18*12.5=225. The crease is the sticker diagonal, not its side. Both marked intervals are on already-existing material boundaries; original grey fills and remaining boundaries stay clear. Square-side inference 5 would yield predeclared wrong450.')
    q='Solid178'
    obs=objects(q);gray=next(o for o in obs if o['id']=='graycell');pts=gray['geometry']['points']
    # Bind the gray cell horizontal axis to the corresponding front-boundary edge
    # at the same x coordinate, ignoring its true two-row depth offset.
    a,b=pts[0],pts[1]
    segs=[o for o in obs if o.get('kind')=='segment' and isinstance(o['geometry'].get('points',[None])[0],list)]
    def edge(points):
        return next(o['id'] for o in segs if {tuple(p) for p in o['geometry']['points']}=={tuple(p) for p in points})
    front=[[a[0],0,a[2]],[b[0],0,b[2]]]
    t.render(q,'top_to_front_boundary_binding',[style(edge([a,b])),style(edge(front))],'13',
        'Pair the gray top cell x-directed edge with the same x-span at the front boundary in red. Test flattening the depth offset and treating a face-interior start as an edge start.',
        ['Gray top cell first edge identifies its actual x-span without adding a point or recoloring the fill.','The matched existing front-boundary x-edge has that same x-span but a different y coordinate. Confusing the depth mapping would place the start on a second boundary and give13 instead17.'],
        'The 4x4x4 grid has a single initial gray cube in the top-face interior. After two days exactly cubes within Manhattan distance<=2 are gray. Enumerate all64 lattice positions from the frozen gray cell lower corner; the count is17. For the paired but false front-edge coordinate the count is13. Original gray location remains unambiguous; no cell is moved and only two existing open edges change color.')
