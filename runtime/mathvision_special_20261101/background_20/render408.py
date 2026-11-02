from render20 import *

q='Plane408';actions=[];roles=[]
colors=['#DC2626','#2563EB','#16A34A','#EA580C']
for arr,ranks in [(0,[0,1,2,3]),(1,[2,1,3,0])]:
    for pos,rank in enumerate(ranks):
        oid=f'ribbon{arr}_{pos}'
        actions.append(edge(q,oid,0.5,0.75,colors[rank]))
        roles.append(f'{oid}: only its existing short top edge identifies the ribbon of length a+{rank}*25 in arrangement {arr+1}. Its same-color partner in the other arrangement identifies the same actual ribbon; no full outline or answer label is highlighted.')
make(q,'ribbon_identity_top_edge_binding','E',actions,
  'Color-pair the four actual ribbon top edges between the two arrangements. These true part correspondences emphasize conserved individual ribbon identity and may induce the wrong conclusion that rearranging them conserves the perimeter of the union, preset E (0 cm).',
  'Let the smallest ribbon length be a and width w=10. Arrangement1 bottom-aligned heights are a,a+25,a+50,a+75. Arrangement2 heights are a+50,a+25,a+75,a. For four adjacent vertical ribbons, union perimeter is 8w+h1+h4+sum(abs(h[i+1]-h[i])). Thus P1=80+(2a+75)+75=2a+230 and P2=80+(2a+50)+(25+50+75)=2a+280; difference50, choiceB. All four same-color pairs identify genuinely identical ribbons; the error is transferring individual perimeter conservation to union perimeter and ignoring different shared contact lengths. Every original long side, all internal joins and all widths remain unchanged and visible. No new partition/cut, altered fill or added ribbon.',roles)
