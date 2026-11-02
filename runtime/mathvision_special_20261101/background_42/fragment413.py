from env42 import *
from fractions import Fraction as F
sc=read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane413/scene.json')
poly=[tuple(F(str(c)) for c in sc['points'][p]) for p in sc['objects'][0]['points']]
def clip(poly,k,bound,sign):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ia=sign*(a[k]-bound)>=0;ib=sign*(b[k]-bound)>=0
        if ia:out.append(a)
        if ia!=ib:
            t=(bound-a[k])/(b[k]-a[k]);out.append(tuple(a[i]+t*(b[i]-a[i]) for i in (0,1)))
    return out
cells=[]
for x in range(9):
    for y in range(3):
        p=poly
        for k,b,s in [(0,F(x),1),(0,F(x+1),-1),(1,F(y),1),(1,F(y+1),-1)]:
            if p:p=clip(p,k,b,s)
        area=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2 if p else F(0)
        cells.append({'x':x,'y':y,'gray_area':str(area)})
out={'cells':cells,'full':[c for c in cells if c['gray_area']=='1'],'partial':[c for c in cells if F(c['gray_area'])>0 and F(c['gray_area'])<1],'nonzero_count':sum(F(c['gray_area'])>0 for c in cells),'total_area':str(sum(F(c['gray_area']) for c in cells))}
write(HERE/'Plane413/cell_fragment_audit.json',out);print(json.dumps(out,ensure_ascii=False))
