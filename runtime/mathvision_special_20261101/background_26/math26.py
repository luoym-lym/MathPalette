from tools26 import *
import math,itertools
def native(q):
    r=read(HERE/q/'formal_record.json');return read(next(ROOT/'PlaneGeometry'/x for x in r['runtime_dependencies'] if '/items/'+q+'/scene.json' in x))
def pts(s,o):return [s['points'][x] if isinstance(x,str) else x for x in o['points']]
def area(p):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2
if __name__=='__main__':
    for q in ['Plane175','Plane282','Plane408']:
        s=native(q);print(q)
        for o in s['objects']:
            p=pts(s,o);print(o['id'],json.dumps(p),'area',area(p))
