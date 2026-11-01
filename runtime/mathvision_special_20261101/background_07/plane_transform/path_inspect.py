from tools_local import *
for qid,ids in [('Plane215',['o1','o2','o215','o216']),('Plane259',['o10','o14']),('Plane187',['o18','o20','o81','o83'])]:
    cfg,ad=adapter();meta=ad.inspect_question(qid);sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw()
        for oid in ids:
            ps=object_paths(sc,oid)
            data=[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'i':i,'type':s['kind'] if 'kind' in s else list(s.keys()),'control':s['control'].tolist()} for i,s in enumerate(p['segments'])]} for p in ps]
            write(HERE/qid/(oid+'_paths.json'),data)
            print(json.dumps({'qid':qid,'oid':oid,'paths':[{'id':p['id'],'segment_count':len(p['segments']),'first':p['segments'][0]['control'].tolist(),'last':p['segments'][-1]['control'].tolist()} for p in ps]}))
    finally:sc.close()
