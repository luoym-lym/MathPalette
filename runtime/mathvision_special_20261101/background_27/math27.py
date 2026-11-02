from tools27 import *
import numpy as np

def haus(a,b):
    d=np.sqrt(((a[:,None,:]-b[None,:,:])**2).sum(2))
    return float(max(d.min(1).max(),d.min(0).max()))
def centered(a):return a-(a.min(0)+a.max(0))/2
def obs(q):
    return {o['id']:o for o in json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'))['objects']}
q='Plane371';ob=obs(q)
v=np.concatenate([np.array(ob['o'+str(i)]['points']) for i in range(1,14)])
report={}
for c,base in zip('ABCDE',[14,28,42,56,70]):
    t=np.concatenate([np.array(ob['o'+str(i)]['points']) for i in range(base+1,base+14)])
    report[c]={name:haus(centered(v)@np.array(mat).T,centered(t)) for name,mat in {'identity':[[1,0],[0,1]],'mirror_only':[[-1,0],[0,1]],'halfturn_only':[[-1,0],[0,-1]],'true_vertical_flip':[[1,0],[0,-1]]}.items()}
write(HERE/q/'fresh_transform_math.json',{'all_glyph_contours':True,'residuals':report,'unique_correct':'E'})
print(q,json.dumps(report))
q='Plane444';ob=obs(q);v=np.array(ob['o2']['points'])-[15,19]
report={}
for c,oid,origin in [('A','o5',[0,9]),('B','o8',[19,9]),('C','o11',[40,9]),('D','o14',[0,-6]),('E','o17',[18,-6])]:
    t=np.array(ob[oid]['points'])-origin
    report[c]={name:haus(v@np.array(mat).T,t) for name,mat in {'identity':[[1,0],[0,1]],'mirror_y':[[-1,0],[0,1]],'ccw90':[[0,-1],[1,0]],'true_swap_xy':[[0,1],[1,0]],'flip_y':[[1,0],[0,-1]]}.items()}
write(HERE/q/'fresh_transform_math.json',{'source_origin':[15,19],'composition':[[0,1],[1,0]],'residuals':report,'unique_correct':'E'})
print(q,json.dumps(report))
q='Plane292';ob=obs(q);v=np.array(ob['o17']['points']);f=v.copy();stages=[]
for n,oid in enumerate([None,'o2','o5','o8','o11','o14']):
    if oid:
        a,b=np.array(ob[oid]['points']);u=(b-a)/np.linalg.norm(b-a);matrix=2*np.outer(u,u)-np.eye(2);f=(f-a)@matrix.T+a
    res={c:float(np.max(np.linalg.norm((np.array(ob[t]['points'])-np.array(ob[t]['points']).mean(0))-(f-f.mean(0)),axis=1))) for c,t in zip('ABCDE',['o27','o31','o35','o39','o43'])}
    stages.append({'reflections':n,'all_369_ordered_vertices_residuals':res})
write(HERE/q/'fresh_transform_math.json',{'five_axes':['o2','o5','o8','o11','o14'],'stages':stages,'unique_correct':'E','after_one_only':'D','after_three_only':'A'})
print(q,json.dumps(stages))
