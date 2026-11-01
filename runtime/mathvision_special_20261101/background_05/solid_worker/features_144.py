from tools_local import *
import numpy as np
audit=json.loads((TASK/'Solid144/lattice_corner_congruence_audit.json').read_text(encoding='utf-8'));context=json.loads((TASK/'Solid144/context.json').read_text(encoding='utf-8'))
def geometry(name):
    g=audit['groups'][name];f=np.array(g['frame']);origin=np.array(g['origin']);matrix=np.eye(3) if name=='given_gray' else np.array(audit['matches'][name][0]['lattice_matrix'])
    cloud=np.array(g['lattice_corners'])@matrix.T;offset=np.min(cloud,axis=0);edges={}
    for o in context['objects']:
        if not o['id'].startswith(name+'e'):continue
        p=(np.array(o['geometry']['points'])-origin)@f@matrix.T-offset
        if np.max(np.abs(p-np.rint(p)))>1e-7:continue
        p=np.rint(p).astype(int);key=tuple(sorted(map(tuple,p.tolist())))
        edges[key]=o
    return edges
all_edges={n:geometry(n) for n in ['given_gray','X','Z']};available=[]
for key,o in all_edges['given_gray'].items():
    if o['frozen_visibility']!='visible':continue
    if not all(key in all_edges[n] and all_edges[n][key]['frozen_visibility']=='visible' for n in ['X','Z']):continue
    row={'given':o['id'],'reference_lattice_endpoints':key,'X':all_edges['X'][key]['id'],'Z':all_edges['Z'][key]['id']};available.append(row)
write(TASK/'Solid144/available_reflected_edge_correspondences.json',{'candidates':available})
print(json.dumps(available))
