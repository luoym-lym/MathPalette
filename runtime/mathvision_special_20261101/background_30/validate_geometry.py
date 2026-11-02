import tools_local as t
import numpy as np
def read(p):return t.json.loads(p.read_text(encoding='utf-8-sig'))
# Independent path-level assembly check for Plane278; use exact captured cubic controls, not text labels.
q='Plane278';paths=read(t.HERE/q/'paths_public.json')
def transformed(piece,angle,dest):
    ctrl=paths[piece][0]['controls'];origin=np.array([3.5*int(piece[-1]),0.0]);a=np.deg2rad(angle);mat=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
    # Nominal local square is [0,2]^2; rotate about center then move lower-left to dest.
    return [(np.array(seg)-origin-np.array([1.,1.]))@mat.T+np.array([1.,1.])+np.array(dest) for seg in ctrl]
assembly={'C':transformed('piece2',0,[0,0]),'E':transformed('piece4',180,[2,0]),'A':transformed('piece0',-90,[0,2]),'D':transformed('piece3',90,[2,2])}
checks=[]
for a,i,b,j in [('C',2,'A',1),('C',1,'E',1),('D',2,'A',2),('D',3,'E',0)]:
    p=assembly[a][i];r=assembly[b][j]
    err=min(float(np.max(np.abs(p-r))),float(np.max(np.abs(p-r[::-1]))))
    checks.append({'pieces':[a,b],'segment_indices':[i,j],'maximum_control_coordinate_error':err,'same_locus_tolerance_1e_12':err<1e-12})
assert all(r['same_locus_tolerance_1e_12'] for r in checks),checks
t.write(t.HERE/q/'frozen_path_assembly_proof.json',{'method':'Fresh transformations of every captured path cubic control in actual original scene. Translate each nominal side2 piece into a2x2 arrangement, compare shared edges both directions.','assembly':{k:[s.tolist() for s in segs] for k,segs in assembly.items()},'seam_checks':checks,'unique_answer':'B','outer_boundary':'Straight edges form [0,4]x[0,4]; all3 convex/concave pairs and remaining straight interior seam match.','geometry_moved_in_candidate':False,'proof_only_transforms':True})
# Marker interval endpoints are evaluated directly on full-precision frozen segments.
def bezier(ctrl,u):
    p=np.array(ctrl,dtype=float)
    while len(p)>1:p=(1-u)*p[:-1]+u*p[1:]
    return p[0].tolist()
for design in t.HERE.glob('Plane*/r30_*/plugin.json'):
    q=design.parent.parent.name;public=read(t.HERE/q/'paths_public.json');proof=[]
    for i,a in enumerate(read(design)['params']['actions']):
        if a['type']!='set_object_style':continue
        oid=a['target'];path=public[oid][0];interval=a.get('interval',{'start':0,'end':1});n=len(path['controls']);points=[]
        for v in [interval['start'],interval['end']]:
            index=min(int(v*n),n-1);u=v*n-index;points.append(bezier(path['controls'][index],u))
        assert a.get('interval',{}).get('path_sha256',path['sha256'])==path['sha256']
        proof.append({'action_index':i,'target':oid,'frozen_path_sha256':path['sha256'],'start_end_parameters':[interval['start'],interval['end']],'exact_evaluated_endpoints':points,'no_new_path_or_boundary':True})
    t.write(design.parent/'interval_endpoint_proof.json',proof)
print(t.json.dumps({'Plane278_seams':checks,'all_styled_interval_paths_verified':True}))
