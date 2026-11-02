from tools28 import *
folder=TASK/'Solid123/r28_L_leg_to_bar_span'
assert not (folder/'tests').exists()
p=folder/'design.json';before=p.read_bytes();d=read(p)
(folder/'design_before_pretest_math_correction.json').write_bytes(before)
d['unique_original_mathematics']='The assembled3cube has27cells. Exact cover enumerates every proper rotation and integer translation of the5-cellL,3-cellbar and1-cellwhite blocks, with exposed front/top/right material cells fixed from the source. There are8unseen cells (only one fully interior cell). The22allowed placements yield exactly one compatible cover:2Ls,2bars,11white. Thus27-10-6=11. Matching a3-unit L leg to a3-unit bar does not equate their5versus3volumes. See primary_unique_math_enumeration.json.'
d['pretest_math_correction']={'at':now(),'reason':'Initial prose conflated the single wholly interior cell with all unseen cells. Corrected before any calls using exact cover, retaining original draft evidence. No image, plugin, hypothesis or preset change.','proof':str(TASK/'Solid123/primary_unique_math_enumeration.json')}
with p.open('w',encoding='utf-8',newline='\n') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
write(folder/'pretest_math_correction.json',{'created_at':now(),'draft_design_sha256':hashlib.sha256(before).hexdigest(),'final_pretest_design_sha256':file_hash(p),'image_unchanged_sha256':file_hash(folder/'candidate.png'),'preset_unchanged':'15','API_calls_before_correction':0,'details':d['pretest_math_correction']})
