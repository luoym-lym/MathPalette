from bootstrap import install,OWN
install()
from research import load
import json
p=next((OWN/'Plane480').glob('r52_*/native_snapshot_difference.json'));d=load(p)
def diff(a,b,path='$'):
    if type(a)!=type(b):return [{'path':path,'before':a,'after':b}]
    if isinstance(a,dict):
        result=[]
        for k in set(a)|set(b):
            if k not in a or k not in b:result.append({'path':path+'.'+k,'before':a.get(k),'after':b.get(k)})
            elif a[k]!=b[k]:result.extend(diff(a[k],b[k],path+'.'+k))
        return result
    if isinstance(a,list):
        if len(a)!=len(b):return [{'path':path,'before_length':len(a),'after_length':len(b)}]
        return sum([diff(x,y,path+f'[{i}]') for i,(x,y) in enumerate(zip(a,b)) if x!=y],[])
    return [{'path':path,'before':a,'after':b}]
print(json.dumps(diff(d['before'],d['after']),ensure_ascii=False,indent=2))
