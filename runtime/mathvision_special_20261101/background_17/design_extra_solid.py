from tools import *
RED='#DC2626';BLUE='#2563EB'
q='Solid90'
candidate(q,'face_body_diagonal_identity','sqrt(55)',[
 {'type':'set_object_style','target':'diagp000p011','color':RED,'linewidth_pt':2},
 {'type':'set_object_style','target':'diagp011p100','color':RED,'linewidth_pt':2}],
 'Pair actual face diagonal XZ and body diagonal XA by the same red dashed style, targeting transfer of the explicitly given sqrt(55) from XZ to XA. Both share X but have different named endpoints. The purpose is face/body edge correspondence, with all labels and original hidden dashes retained.',
 'Let squared edge lengths be u,v,w. The three given face diagonals give u+v=64,u+w=81,v+w=55. Their sum is200=2(u+v+w), so XA^2=u+v+w=100 and XA=10 uniquely. XZ and XA remain distinct original segments; color is not an equality relation.',
 [{'action_index':1,'role':'Given-length face diagonal XZ: first actual edge in the false face/body identity correspondence.'},{'action_index':2,'role':'Requested body diagonal XA: second edge, inviting copying sqrt(55).'}])
q='Solid159';c=AD.inspect_question(q);points={p['id']:p['xy'] for p in c['snap_points']}
names=['L','R','T','F','B'];actions=[];roles=[]
for i,n in enumerate(names):
    color=BLUE if n in ['L','R'] else RED
    actions.append({'type':'add_point','id':'role_'+n,'xy':points[n],'color':color})
    roles.append({'action_index':i+1,'role':{'L':'Given 5 vertex at left screen extreme: blue anchor for false horizontal apex pair.','R':'Right screen extreme: blue companion, inviting value5 as the other supposed apex.','T':'Given 1 vertex: red anchor for false three-member equatorial group.','F':'Projected central/front vertex: red member of the false equatorial triple.','B':'Lower true apex: red member of the false equatorial triple.'}[n]})
candidate(q,'projected_extreme_apex_grouping','13',actions,
 'Color the two horizontal screen extremes L/R blue and the other three existing vertices T/F/B red. This targets mistaking screen extremes for the two bipyramid apices, assigning the blue pair 5 and red triple1 and reporting13. Every marker coincides with a frozen existing vertex; no graph edge, face, or number changes.',
 'The six faces are TLF,TFR,TRL,BLF,BFR,BRL. Equal totals for the top three give L=F=R. Given L=5, all equatorial vertices are5. Comparing TLF with BLF gives T=B; given T=1, B=1. Total is3*5+2*1=17 uniquely. The valid graph classes are T/B and L/F/R, and the colored screen-based grouping is not a number equality condition.',roles)
