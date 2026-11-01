from tools08 import *
R='#DC2626';B='#2563EB'
def style(oid,color,width=None):
    a={'type':'set_object_style','target':oid,'color':color}
    if width is not None:a['linewidth_pt']=width
    return a
if sys.argv[1]=='362':
    render('Plane362','unchanged_digit_side_binding',[style(o,R) for o in ['o1','o3','o25','o27']]+[style(o,B) for o in ['o23','o47']],'A',
    'Bind the two handed vertical strokes of the source 2 to the unchanged 2 in A, and the invariant middle stroke of 8 to A. Intended mistake: preserve glyph handedness after upside-down plus mirror.',
    'A 180-degree in-plane turn followed by left-right mirror has linear map diag(1,-1). It is a vertical flip, retaining left-to-right digit order. The source seven-segment 2 becomes 5; 0,0,8 are invariant. Thus the result is 5008, option B, uniquely. No segment or semantic fill is changed by these color-only actions.',
    [{'actions':['o1','o3'],'role':'Source 2 handed upper-right/lower-left pair, the discriminating input feature.'},{'actions':['o25','o27'],'role':'Same handed pair in the wrong unchanged output 2 in A; false visual correspondence across the requested vertical flip.'},{'actions':['o23','o47'],'role':'Source/output middle bars of invariant 8 preserve rightmost digit anchoring and make the mechanism a two-feature mapping rather than isolated answer highlighting.'}])
elif sys.argv[1]=='446':
    render('Plane446','square_skeleton_symmetry',[style('o'+str(i),R,3) for i in range(1,18,2)],'3',
    'Emphasize every recurring square boundary with the same red style while preserving black diagonal tails. Intended error: infer a perpendicular reflection from the square skeleton and overlook tail handedness, adding a third symmetry type.',
    'Write upper square centers as (4k+0.5,0.5), lower centers as (4k+2.5,-0.5). Translation by (4,0) preserves the whole pattern, as does a half-turn about (1.5,0), taking upper tails at upper-right corners to lower tails at lower-left corners. Reflection in ell fails because squares are staggered. Perpendicular reflection would have to preserve each square row; although square centers admit axes x=0.5+2k, upper-right tails would become upper-left tails, which do not exist. There are exactly two listed kinds. All square outlines receive identical style, so both genuine symmetries remain and the impossible ones stay impossible; no extra geometry is added.',
    [{'actions':['o'+str(i) for i in range(1,18,2)],'role':'All nine displayed square contours are members of the recurring skeleton. Uniform styling preserves its periodicity and the actual figure symmetry, while making false skeleton-only vertical reflection tempting; each repeated contour maintains the same source-feature correspondence.'}])
elif sys.argv[1]=='371':
    render('Plane371','letter_handedness_shortcut',[style(o,R) for o in ['o4','o18']]+[style(o,B) for o in ['o5','o19']],'A',
    'Pair source N and G outlines with the corresponding partial-transformation letters in A. Intended error: read a visually matched letter sequence while neglecting the handedness of each glyph under the composed flip.',
    'Turning glass onto its back about the right edge reverses x; a subsequent half-turn reverses x and y. Their composition is (x,y)->(x,-y) up to translation: horizontal order KANGAROO stays, while every glyph is reflected vertically. In the frozen source vectors option E is the full vertical reflection. Option A leaves some letters, including the N diagonal, in the wrong handed orientation. Color-only outlines do not move glyph boundaries, alter the black letter fill or change the glass outline. E stays uniquely correct.',
    [{'actions':['o4','o18'],'role':'N is a handed diagonal-bearing glyph: input N and wrong A N create the selective unchanged-diagonal association.'},{'actions':['o5','o19'],'role':'G provides a second ordered asymmetric-letter correspondence and keeps source/output reading positions aligned. No entire glass or choice is highlighted.'}])
