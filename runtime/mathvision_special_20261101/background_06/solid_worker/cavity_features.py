from design_tools import *
q='Solid127';audit=json.loads((TASK/q/'cavity_congruence_audit.json').read_text());models=AD.scenes[q]['visibility']['models'];objects=source_objects(q)
source=[o for o in objects if o['id'].startswith('given_incomplete_cuboid') and o.get('styleable') and o['geometry']['type']=='segment']
candidate=[o for o in objects if o['id'].startswith('C') and o.get('styleable') and o['geometry']['type']=='segment']
out=[]
for mi,mapping in enumerate(audit['maps']['C']):
    m=np.array(mapping['matrix']);cell_shift=np.array(mapping['cell_origin_translation'])
    # Cell origins under negative-axis maps require one extra unit in that axis for boundary vertices.
    vertex_shift=cell_shift+np.array([int(np.any(row==-1)) for row in m])
    for obj in candidate:
        ends=np.array(obj['geometry']['points'])-models['C']['world_offset'];mapped=ends@m.T+vertex_shift+models['given_incomplete_cuboid']['world_offset']
        for given in source:
            a=np.array(given['geometry']['points'])
            if np.allclose(a,mapped,atol=1e-9,rtol=0) or np.allclose(a,mapped[::-1],atol=1e-9,rtol=0):
                out.append({'map_index':mi,'C':obj['id'],'given':given['id'],'C_local_endpoints':ends.tolist(),'given_cavity_local_endpoints':(a-models['given_incomplete_cuboid']['world_offset']).tolist(),'matrix':m.tolist(),'vertex_translation':vertex_shift.tolist()})
write(TASK/q/'available_reflected_cavity_correspondences.json',out)
print(json.dumps(out,separators=(',',':')))
