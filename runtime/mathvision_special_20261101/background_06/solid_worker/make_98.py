from design_tools import *
q='Solid98';actions=[];roles=[]
for prefix,origin,z,pattern,label in [('given',[13,0,6],6,'WWGG','input bar bottom rail'),('B',[7,0,0],0,'WWGG','B lower front row'),('B',[7,0,0],2,'GGWW','B upper front row')]:
    for i,color_letter in enumerate(pattern):
        x=origin[0]+i;ends=[[x,0,z],[x+1,0,z]];target=match_edge(q,prefix,ends)
        color=RED if color_letter=='W' else BLUE
        actions.append(style(target,color))
        roles.append(f'{label}, unit interval {i+1}: {color_letter} cell edge. Red binds the ordered white pair and blue binds the ordered gray pair to the actual source bar; the two visible B front rows match the source directly/reversed. The false inference is that these two locally legal rows suffice for the entire cuboid, ignoring B back-top WWWW row.')
folder=save_candidate(q,'front_row_color_correspondence','B',actions,roles,'Bind actual ordered WW/GG input edge pairs to both B front rows, encouraging local front-row agreement as a substitute for full four-bar tiling.','Every length4 bar must run along x in a4x2x2 box. Every y,z row must be WWGG or GGWW. Only A admits all visible colours; B/C have all-white back-top rows, D has all-gray back-top row, and E has all-gray bottom-front row. Exact-cover witnesses and impossibilities independently computed.',TASK/q/'exact_colored_tiling_audit.json')
print(folder)
