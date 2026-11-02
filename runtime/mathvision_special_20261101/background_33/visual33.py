from tools33 import *
import numpy as np
from PIL import Image
from itertools import combinations
from fractions import Fraction
q='Plane325';v='r33_dihedral_arm_orbit_local_completion';out=HERE/q/v
im=np.asarray(Image.open(out/'candidate.png').convert('RGB'))
red=(im[:,:,0]>180)&(im[:,:,1]<100)&(im[:,:,2]<100)
m=np.array(read(HERE/q/'context.json')['canvas']['data_to_pixel']);orbit=read(out/'design.json')['extra_certificate']['orbit']
edges=[]
for x,y in orbit:
    ps=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    for a,b in zip(ps,ps[1:]+ps[:1]):
        hits=[]
        for t in np.linspace(.1,.9,41):
            p=(1-t)*np.array(a)+t*np.array(b);u=m@np.array([*p,1]);xx,yy=round(u[0]),round(u[1])
            hits.append(bool(red[max(0,yy-2):yy+3,max(0,xx-2):xx+3].any()))
        edges.append({'cell':[x,y],'endpoints':[a,b],'red_visible_fraction':sum(hits)/len(hits)})
write(out/'visible_annotation_edge_audit.json',{'sample_method':'At 41 interior positions per intended edge, examine 5x5 native PNG neighborhood for visible red pixel. Does not replace full native visual inspection.','edges':edges,'minimum_visible_edge_fraction':min(e['red_visible_fraction'] for e in edges)})
print(json.dumps(edges))
