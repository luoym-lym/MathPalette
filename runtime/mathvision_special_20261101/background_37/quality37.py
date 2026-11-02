from tools37 import *
import numpy as np
from PIL import Image
q='Solid230';f=next((TASK/q).glob('*/candidate.png')).parent
original=np.array(Image.open(TASK/q/'original.png').convert('RGBA'));candidate=np.array(Image.open(f/'candidate.png').convert('RGBA'))
s=read(TASK/q/'source_scene_snapshot.json');ctx=read(TASK/q/'context.json');pr=s['projection'];trans=np.array(ctx['canvas']['data_to_pixel']);checks=[]
for pid,p in s['points'].items():
    if 'pip' not in pid:continue
    xy=np.array(pr['matrix'])@(np.array(p)-np.array(pr['origin']))+np.array(pr['offset'])
    px=trans@np.r_[xy,1.];cx,cy=map(lambda t:int(round(t)),px[:2]);radius=9
    a=original[cy-radius:cy+radius+1,cx-radius:cx+radius+1];b=candidate[cy-radius:cy+radius+1,cx-radius:cx+radius+1]
    assert a.shape==(19,19,4) and np.array_equal(a,b),(pid,'pip pixels changed')
    checks.append({'id':pid,'world_xyz':p,'projected_xy':xy.tolist(),'pixel_xy':px[:2].tolist(),'patch_radius_pixels':radius,'original_and_candidate_patch_byte_equal':True,'patch_sha256':hashlib.sha256(a.tobytes()).hexdigest()})
assert len(checks)==22
write(f/'pip_pixel_preservation.json',{'created_at':now(),'original_sha256':file_hash(TASK/q/'original.png'),'candidate_sha256':file_hash(f/'candidate.png'),'all22original_black_pips_unchanged':True,'patches':checks,'observed_solver_misread':'Bothcallsreadactualmiddle-right6as5whilecountingboth1faces. This is NOT evidence ofthefrozenvalue-identitydedupmechanism.','disposition':'Hold information-targeting claim; parent may NEW-review exactimage but no qualified delivery.'})
f126=next((TASK/'Solid126').glob('*/candidate.png')).parent
write(f126/'primary_supplement.json',{'created_at':now(),'kind':'Author supplementary geometric derivation, not independent second review','original_cross_section':{'width':12,'height':8,'area':96,'perimeter':40},'removed_corner_rectangle':{'width':9,'height':3,'area':27},'remaining_L_cross_section':{'area':69,'perimeter':40},'extrusion_depth':6,'original_surface':'2*96+40*6=432','remaining_surface':'2*69+40*6=378','loss_percentage':'(432-378)/432=12.5%, uniqueB','why_red_blue_pairs_are_true':'Theghosttop9x6andnewfloor9x6cancel. Removedx0end-side3x6andnewx9cut-side3x6cancel. Both front/back endfaces lose9x3each; no newendcaps exist.','six_mark_roles':read(f126/'design.json')['pretest_marker_roles'],'old_and_new_evidence_distinction':'OldpresetC/A,A remainsMISS. New6edgearea-pairdesign presetA frozen beforecurrentA/A; no oldoutputiscountedasnewtrial.','causal_limit':'No originalcontrolcalls exist for theseassignedquestions; prior differentimageA/Aalso cautions that newimage effectisnotestablished.'})
print('Qualityverified:22unchangedpips; Solid126independentL-prismderivation432->378uniqueB')
