import review_bootstrap as r
import json
a=r.read(r.TASK/'parent_audits/native_u01_u04/method_fidelity.json')
print('PARENT_FIDELITY',json.dumps(a['Plane461'],ensure_ascii=False,indent=2))
h=r.read(r.TASK/'history_index.json')
q=next(x for x in h['questions'] if x['question_id']=='Plane461')
r.save(r.OWN/'old_history_Plane461.json',q)
print('HISTORY',len(q['designs']))
s=r.read(r.UNIT/'readonly_inputs_initial.json')
print('PRESERVATION_SAMPLE',json.dumps(s['files'][:2] if isinstance(s['files'],list) else list(s['files'].items())[:2]))
s=r.read(r.PROJECT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane461/scene.json')
print('SRC_SCENE_METADATA',json.dumps({k:v for k,v in s.items() if k not in ('objects','points')}))
print('GEOMETRY_COMPACT',json.dumps(s['objects'],ensure_ascii=False,separators=(',',':')))
