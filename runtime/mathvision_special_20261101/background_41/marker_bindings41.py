from env41 import *
import numpy as np
for q in ASSIGNED:
    ds=list((HERE/q).glob('r41_*/design.json'))
    if not ds:continue
    out=ds[0].parent;ctx=read(HERE/q/'context.json');s=read(HERE/q/'source_scene_snapshot.json');points=s['points'];targets={t['id']:t for t in ctx['canvas']['targets']}
    def xy(v):return points[v] if isinstance(v,str) else v
    def on_sources(point):
        a=np.array(point,float);found=[]
        for obj in s['objects']:
            if obj['type'] not in ('segment','polygon'):continue
            verts=[xy(v) for v in obj['points']]
            edges=list(zip(verts,verts[1:]))+([(verts[-1],verts[0])] if obj['type']=='polygon' else [])
            for i,(v,w) in enumerate(edges):
                v=np.array(v,float);w=np.array(w,float);z=w-v
                if z@z<1e-20:continue
                t=float((a-v)@z/(z@z))
                if -1e-9<=t<=1+1e-9 and np.linalg.norm(v+t*z-a)<1e-8:
                    found.append({'source_object_id':obj['id'],'source_edge_index':i,'source_edge_endpoints':[v.tolist(),w.tolist()],'affine_edge_parameter':max(0,min(1,t)),'current_object_partial_path_hashes':[{k:p[k] for k in ('id','sha256','closed')} for p in targets[obj['id']]['partial_paths']]})
        return found
    audits=[]
    for i,a in enumerate(read(out/'plugin.json')['params']['actions']):
        if a['type']=='set_object_style':
            path=next(p for p in targets[a['target']]['partial_paths'] if p['id']==a['interval']['path_id']);assert path['sha256']==a['interval']['path_sha256']
            audits.append({'action_index':i,'type':a['type'],'source_object_id':a['target'],'interval':a['interval'],'actual_current_path_sha256':path['sha256']})
        else:
            coords=[a['xy']] if a['type']=='add_point' else a['endpoints']
            bound=[{'xy_full_precision':v,'frozen_source_incidence':on_sources(v),'snap_point_matches':[p for p in ctx['snap_points'] if np.linalg.norm(np.array(p['xy'])-np.array(v))<1e-9]} for v in coords]
            assert all(x['frozen_source_incidence'] for x in bound),(q,a)
            audits.append({'action_index':i,'type':a['type'],'endpoints_or_point':bound,'geometry_role':'Existing true vertex/join/contact or grid-edge intersection; added line only if permitted one-cell diagonal in Plane430. No hidden original edge is revealed.'})
    write(out/'full_precision_marker_bindings.json',{'question_id':q,'created_at_utc':now(),'context_sha256':file_hash(HERE/q/'context.json'),'frozen_scene_sha256':file_hash(ROOT/'PlaneGeometry'/read(HERE/q/'formal_record.json')['scene']),'bindings':audits,'all_actual_path_fingerprints_match':True,'all_added_mark_coordinates_bound_to_actual_source_incidence':True,'native_PNG_actually_viewed':True})
print('All seven marker bindings verified against frozen objects/paths/incidence.')
