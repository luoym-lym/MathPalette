from tools08 import *
R='#DC2626';B='#2563EB'
mode=sys.argv[1]
if mode=='449':
    old=HERE/'Plane449/side_label_role_confusion';d=json.loads((old/'design.json').read_text(encoding='utf-8'));p=json.loads((old/'plugin.json').read_text(encoding='utf-8'))
    write(old/'prescreen_rejection.json',{'reason':'Two pairs of slot-edge actions coincide exactly, so two actions have no separate visual role. Never tested. Superseded by six-action clean design before any solver call.','tested':False})
    roles=[{'actions':[0,1,4],'role':'B-right3 and C-left3 red match; single red slot I-II seam binds this pair to the tempting wrong row.'},{'actions':[2,3,5],'role':'C-right5 and D-top5 blue numeric correspondence, plus single blue II-III seam, tempt ignoring side orientation. Source D-left7 remains clear. All six actions have distinct visible roles.'}]
    render('Plane449','side_label_role_binding_clean',[p['params']['actions'][i] for i in [0,1,2,3,4,6]],'B',d['mechanism'],d['primary_mathematical_proof'],roles)
elif mode=='446':
    render('Plane446','tail_orientation_correspondence',[{'type':'set_object_style','target':'o'+str(i),'color':R,'linewidth_pt':3} for i in range(2,19,2)],'1',
    'Emphasize each recurring diagonal tail, linking the same positive-slope direction across upper and lower motifs. Intended error: treat that direction as a fixed one-way orientation and overlook the half-turn exchanging upper-right with lower-left, leaving only translation.',
    'Upper/lower square centers alternate as (4k+0.5,0.5),(4k+2.5,-0.5). A half-turn about (1.5,0) maps full upper square and upper-right tail to a lower square and lower-left tail; translation by 4 along ell also works. Horizontal reflection fails staggered squares; vertical reflection fails tail corner handedness. Exactly two listed transformation types work. All tails receive the same style so the real half-turn and translation also preserve the red marks. This design preserves the unique answer2, with no geometry, added arrows or color-asymmetric conditions.',
    [{'actions':['o'+str(i) for i in range(2,19,2)],'role':'All nine tails form one repeated directional correspondence. Each red stroke identifies the actual corner attachment and slope in a different repeat; the misleading cue is failing to reverse both endpoints under a half-turn. Square outlines and infinite line remain black and intact.'}])
