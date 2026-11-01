from design_tools import *
q='Solid119';actions=[];roles=[]
for color,z,x,label in [(RED,6,18,'first longitudinal rail'),(BLUE,7,19,'second longitudinal rail')]:
    for i in range(2):
        target=match_edge(q,'brick0',[[6+i,0,z],[7+i,0,z]])
        actions.append(style(target,color));roles.append(f'Input white domino {label}, unit{i+1}. Its two-unit longitudinal rail binds to the correspondingly colored vertical rail of D front white column; the mapping is a90degree rotation of this actual2x1 face.')
        target=match_edge(q,'D',[[x,0,i],[x,0,i+1]])
        actions.append(style(target,color));roles.append(f'D white front column {label}, unit{i+1}. Exact2x1 local face matches the input white brick, inviting this one valid local placement to substitute for checking the remaining exposed white cubes at rear. Extra white top/right regions remain unchanged and disprove D.')
for prefix,ends,label in [('brick0',[[6,0,6],[6,0,7]],'input white domino starting cap'),('D',[[18,0,0],[19,0,0]],'D front white column bottom cap')]:
    target=match_edge(q,prefix,ends);actions.append(style(target,GREEN));roles.append(label+': binds the corresponding short terminal edge under the same90degree rotated local face map; preserves the distinction between two-unit rail and one-unit cap.')
print(save_candidate(q,'white_domino_local_column_binding','D',actions,roles,'Bind the actual input white domino long rails and short cap to D front white column, inviting a correct local2x1 face match to be accepted as an entire four-brick construction.','Four size2x1x1 bricks contain exactly two white unit cubes and six gray. D white front column does match the single white domino locally, but additional rear top/right white cells require extra white bricks. Exact-cover search constrained by every visible original color and one-white/three-gray stock admits only C.',TASK/q/'exact_colored_tiling_audit.json'))
q='Solid137';actions=[];roles=[]
for i,(prefix,ox,color) in enumerate([('brick0',3.0,RED),('brick1',6.7,BLUE)]):
    for t in range(2):
        target=match_edge(q,prefix,[[ox+t,0,6],[ox+t+1,0,6]])
        actions.append(style(target,color));roles.append(f'Input white brick{i+1}, longitudinal unit{t+1}. These two contiguous segments identify one real two-cube white building block. Red pairs it to C front-top white domino, blue to C second-top-row white domino.')
        ends=[[12+t,0,1],[13+t,0,1]] if i==0 else [[12+t,2,2],[13+t,2,2]]
        target=match_edge(q,'C',ends);actions.append(style(target,color));roles.append(f'C local white domino{i+1}, longitudinal unit{t+1}. This is a genuine two-cell white subset of the candidate and a corresponding length2 input feature. The false inference accepts two visible complete matches while overlooking the fifth white cell at right-side middle-bottom, which remains readable.')
print(save_candidate(q,'two_white_domino_local_bindings','C',actions,roles,'Bind each of the two actual white input domino long edges to a distinct two-cell white subset on C, inviting two valid local piece matches to substitute for full stock and tiling consistency.','Two white size2x1x1 bricks supply four white cells. C shows a white2x2 top-front region plus a fifth distinct white cell below at right-side middle. D has exactly the four necessary white cells and a consistent remaining gray tiling. Exhaustive exact-cover search with all visible colors and two-white/four-gray stock admits only D.',TASK/q/'exact_colored_tiling_audit.json'))
