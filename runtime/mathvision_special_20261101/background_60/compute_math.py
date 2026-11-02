from tools60 import *
from fractions import Fraction as F
from itertools import permutations

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def double_area(poly):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))
def clipped(poly,tri):
    if cross(*tri)<0:tri=list(reversed(tri))
    for a,b in zip(tri,tri[1:]+tri[:1]):
        out=[]
        for c,d in zip(poly,poly[1:]+poly[:1]):
            u=cross(a,b,c);v=cross(a,b,d)
            if u>=0:out.append(c)
            if (u<0 and v>0) or (u>0 and v<0):
                t=u/(u-v);out.append((c[0]+t*(d[0]-c[0]),c[1]+t*(d[1]-c[1])))
        poly=out
        if not poly:break
    return poly

def main():
    target=[(F(0),F(1)),(F(3),F(3)),(F(4),F(0))]
    cells=[]
    for j in range(6):
        for i in range(6-j):
            up=[(i,j),(i+1,j),(i,j+1)]
            tris=[('up',up)]
            if i+j<=4:tris.append(('down',[(i+1,j),(i+1,j+1),(i,j+1)]))
            for orient,pts in tris:
                pts=[(F(a),F(b)) for a,b in pts]
                p=clipped(pts,target);weight=double_area(p) if p else F(0)
                cells.append(dict(i=i,j=j,orientation=orient,vertices=[[str(x),str(y)] for x,y in pts],area_of_shaded_part=str(weight),clipped_polygon=[[str(x),str(y)] for x,y in p]))
    assert len(cells)==36 and sum(F(x['area_of_shaded_part']) for x in cells)==11
    write(HERE/'Plane387/exact_cell_clipping.json',dict(method='Exact rational clipping in oblique lattice coordinates. Unit elementary triangle determinant area =1 cm^2.',target_lattice=[[0,1],[3,3],[4,0]],target_determinant=11,cells=cells,intersected_positive_area_count=sum(F(c['area_of_shaded_part'])>0 for c in cells),whole_cell_count=sum(F(c['area_of_shaded_part'])==1 for c in cells)))
    print('Plane387',[(c['i'],c['j'],c['orientation'],c['area_of_shaded_part']) for c in cells if F(c['area_of_shaded_part'])>0])
    s=read(PROJECT/'PlaneGeometry/dataset_generator/scenes/Plane367.json')
    results=[]
    for obj in s['objects']:
        if obj['id'].startswith('shape'):
            pts=[s['points'][p] if isinstance(p,str) else p for p in obj['points']]
            area=double_area(pts)/2
            results.append(dict(object_id=obj['id'],points=pts,area=area))
    write(HERE/'Plane367/exact_area_audit.json',dict(method='Shoelace on original frozen vertex coordinates',results=results,unique_choice='E'))
    s=read(PROJECT/'PlaneGeometry/dataset_generator/scenes/Plane449.json')
    labels=s['labels'];print('449 labels',json.dumps(labels,ensure_ascii=False))
    vals={'A':(1,6,9,4),'B':(0,3,6,1),'C':(8,5,2,3),'D':(5,4,8,7),'E':(2,7,0,9)}
    solutions=[];local=[]
    for p in permutations(vals):
        i,ii,iii,iv,v=p
        checks=[vals[i][1]==vals[ii][3],vals[ii][1]==vals[iii][3],vals[iv][1]==vals[v][3],vals[i][2]==vals[iv][0],vals[ii][2]==vals[v][0]]
        if all(checks):solutions.append(p)
        if checks[3] and checks[4]:local.append(p)
    assert solutions==[('E','D','A','B','C')]
    write(HERE/'Plane449/exact_permutation_audit.json',dict(side_order=['top','right','bottom','left'],labels=vals,all_permutations=120,seam_order=['I-II','II-III','IV-V','I-IV','II-V'],unique_solutions=solutions,vertical_only_solutions=local,new_misconception_witness={'placement':['D','E','A','C','B'],'seam_checks':[False,False,False,True,True]}))
    print('367 areas',results)
    print('449 solutions',solutions,'vertical only',local)
if __name__=='__main__':main()
