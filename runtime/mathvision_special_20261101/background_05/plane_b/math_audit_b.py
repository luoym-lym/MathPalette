from tools_b import *
board={
 (0,3):('club',0),(1,3):('star',0),(2,3):('club',0),(3,3):('heart',0),
 (0,2):('diamond',0),(1,2):('club',0),(2,2):('spade',180),(3,2):('heart',0),
 (0,1):('diamond',90),(1,1):('star',20),(2,1):('club',0),(3,1):('heart',180),
 (0,0):('diamond',0),(1,0):('heart',90),(2,0):('club',0),(3,0):('spade',90)}
options={'A':[('star',0),('spade',0)],'B':[('star',0),('club',0)],'C':[('star',0),('star',0)],'D':[('heart',0),('diamond',0)],'E':[('heart',0),('heart',0)]}
sym={'star':72,'diamond':180,'club':360,'spade':360,'heart':360}
matches={k:[] for k in options}
def rotate(p,k):
 x,y=p
 for i in range(k):x,y=-y,x
 return x,y
for first,f1 in board.items():
 for second,f2 in board.items():
  delta=second[0]-first[0],second[1]-first[1]
  if sum(abs(v) for v in delta)!=1:continue
  for k in range(4):
   if rotate(delta,k)!=(1,0):continue
   for opt,fs in options.items():
    if all(src[0]==dst[0] and (src[1]+90*k-dst[1])%sym[src[0]]==0 for src,dst in zip([f1,f2],fs)):
     matches[opt].append({'source_first':first,'source_second':second,'rotation_ccw_deg':90*k})
assert [k for k,v in matches.items() if v]==['B'],matches
write(HERE/'Plane226'/'adjacency_math_audit.json',{'source':'Fresh context exact geometry; names/orientations manually identified from preserved glyph contours. Heart orientation0 means pointdown; spade0 pointup; star0 pointup; diamond0 tall vertical.','board':[{'cell':k,'feature':v} for k,v in board.items()],'all24_undirected_adjacencies_both_orders_four_rotations':True,'matches':matches,'unique_answer':'B','limits':'This is a primary geometric enumeration, not an independent second review or model performance study.'})
cycle=list('MMLLSMLSSSMLLMSLSS')
optionwords={'A':'LLSS','B':'LMSL','C':'MLMS','D':'LSSL','E':'SSLS'}
windows=[''.join(cycle[(i+j)%18] for j in range(4)) for i in range(18)]
occ={k:[i for i,w in enumerate(windows) if w==word] for k,word in optionwords.items()}
assert [k for k,v in occ.items() if v]==['B'],occ
write(HERE/'Plane234'/'cyclic_ray_math_audit.json',{'classification':{'S':['white',1.5],'M':['gray',1.75],'L':['dark',2]},'source_ray_clockwise_cycle':cycle,'option_words':optionwords,'all_cyclic_windows':windows,'matching_start_indices':occ,'unique_answer':'B','actual_fills_and_tip_radii_from_fresh_context':True})
print(json.dumps({'Plane226':matches,'Plane234':occ},ensure_ascii=False))
