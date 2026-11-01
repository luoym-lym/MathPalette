from tools04 import *
paths=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','runtime/mathvision_special_20261101/background_04_brief.txt','runtime/mathvision_special_20261101/continuation_brief.txt']
items=[]
for name in paths:
    raw=(ROOT/name).read_bytes();text=raw.decode('utf-8-sig');items.append({'path':name,'bytes':len(raw),'lines':len(text.splitlines()),'sha256':hashlib.sha256(raw).hexdigest(),'read_in_full':True})
previous=json.loads((ROOT/'runtime/mathvision_special_20261101/background_03/checkpoint.json').read_text(encoding='utf-8-sig'))
report=json.loads((ROOT/'runtime/mathvision_special_20261101/exploration_report.json').read_text(encoding='utf-8-sig'))
inventory=json.loads((ROOT/'runtime/mathvision_special_20261101/inventory.json').read_text(encoding='utf-8-sig'))
write(HERE/'instructions_read.json',{'files':items,'previous_unit_new_question_ids':previous['new_question_ids'],'previous_remaining_recommendations':previous['remaining_recommendations'],'previous_explored_question_ids':sorted({a['question_id'] for a in report['attempts']}),'assigned_disjoint_from_previous_attempts':not set(ASSIGNED)&{a['question_id'] for a in report['attempts']},'prior_inventory_plane_eligible':inventory['PlaneGeometry']['eligible_count'],'authority':'User explicitly authorizes autonomous multiple designs, two real quicktest3 calls and runtime-only scope; this overrides local manual-only and .runtime draft paths.'})
print('Full instructions read; assigned IDs disjoint from prior attempts.')
