from tools08 import *
R='#DC2626';B='#2563EB'
def st(o,c,w=None):
    a={'type':'set_object_style','target':o,'color':c}
    if w:a['linewidth_pt']=w
    return a
def interval(q,o,start,end,c):
    m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'));t=next(t for t in m['canvas']['targets'] if t['id']==o);p=t['partial_paths'][0]
    return {'type':'set_object_style','target':o,'color':c,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
mode=sys.argv[1]
if mode=='362_reverse':
    actions=[st(o,R) for o in ['o1','o3','o92','o95']]+[st(o,B) for o in ['o23','o78']]
    # Rightmost 2 in C consists of o91..o95; its handed bars are o92 and o94.
    actions[3]=st('o94',R)
    render('Plane362','reverse_order_side_binding',actions,'C',
    'Bind source 2 handed side strokes to rightmost 2 in C, and source 8 center to leftmost 8 in C. Distinct from unchanged-order design: invites reversing digit order while keeping the source glyph handedness.',
    'The composed upside-down-plus-mirror transformation is (x,y)->(x,-y), retaining digit order and vertically flipping each glyph. It gives 5008, B. C is 8002, an order reversal with the 2 unchanged. All original bars remain at identical coordinates and original width; only two source/output feature pairs are recolored.',
    [{'actions':['o1','o3','o92','o94'],'role':'Bind source 2 side-stroke handedness to C rightmost 2; intentionally wrong reversal instead of the actual vertical flip.'},{'actions':['o23','o78'],'role':'Middle-bar pairing anchors the invariant 8 at the opposite end, creating an ordered two-feature reversal correspondence.'}])
elif mode=='404':
    render('Plane404','unreflected_first_digit_binding',[st(o,R,1.5) for o in ['o2','o3']]+[st(o,B,1.5) for o in ['o18','o19','o20']],'A',
    'Separate the first source digit into red handed vertical strokes and blue horizontal completion bars. Intended error: combine upper bars without reflecting their top/bottom positions, reading 2:6:9 instead of 5:6:9.',
    'Fold across y=3 maps y to 6-y. First source upper-right bar (x=1,y4.5..5.5) becomes lower-right y0.5..1.5; lower-left bar (x=0,y3.5..4.5) becomes upper-left y1.5..2.5. With three fixed bottom horizontal bars this is 5. The middle digit becomes 6 and right becomes 9, hence C uniquely. Dots separating digits and marking unused endpoints stay unchanged. Color/width do not add or remove any number-encoding segment.',
    [{'actions':['o2','o3'],'role':'The two input handed vertical features of the first numeral; their upper/lower order must reverse in the real fold.'},{'actions':['o18','o19','o20'],'role':'The three horizontal completion bars at exactly the first numeral position; blue groups the stationary half against the red source half. Every bar contributes to the target digit, without changing cut boundaries or numeric content.'}])
elif mode=='449':
    actions=[interval('Plane449',o,a,b,c) for o,a,b,c in [('B',.25,.5,R),('C',.75,1,R),('C',.25,.5,B),('D',.5,.75,B),('slotI',.25,.5,R),('slotII',.75,1,R),('slotII',.25,.5,B),('slotIII',.75,1,B)]]
    render('Plane449','side_label_role_confusion',actions,'B',
    'Bind B-right3 to C-left3 in red and C-right5 to D-top5 in blue; repeat red/blue on the I-II-III slot seams. Intended error: infer B,C,D along the top row by matching equal labels while overlooking that D-top5 is not D-left7 and no rotation is permitted.',
    'Keep orientations fixed. Enumerating all 120 rectangle permutations in slots I,II,III,IV,V with right-left seams I-II,II-III,IV-V and bottom-top seams I-IV,II-V gives exactly (E,D,A,B,C). Thus I=E uniquely. The proposed B,C,D starts with a valid 3-3 seam but its next seam is C-right5 versus D-left7, invalid. All printed integers and slot labels remain black and all original rectangle coordinates stay fixed. Partial edge colors are appearance hints, not replacement numeric equality rules.',
    [{'actions':[0,1,4,5],'role':'Red source sides B-right3/C-left3 form a genuinely matching ordered pair, then red slot I-II seam maps that pair to the wrong row.'},{'actions':[2,3,6,7],'role':'Blue source sides C-right5/D-top5 are numerically equal but occupy incompatible edge roles without rotation; blue II-III seam tempts that orientation error. All eight marks contribute to the two-stage side/slot binding; none outlines an entire chosen answer.'}])
