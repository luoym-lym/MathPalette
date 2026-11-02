from design_tools import *
import itertools
q='Solid95';vid='r25_full_pillars_plus_shared_slab'
p=next(ROOT/'SolidGeometry'/s for s in AD.records[q]['runtime_dependencies'] if s.endswith('/scene.json'))
sc=json.loads(p.read_text(encoding='utf-8-sig'))
vox=set(map(tuple,sc['voxel_model']))
base={(x,y,0) for x,y in itertools.product(range(5),repeat=2)}
feet=sorted({(x,y) for x,y,z in vox if z>0})
pillars={(x,y,z) for x,y in feet for z in range(5)}
assert feet==list(itertools.product((0,2,4),repeat=2))
assert vox==base|pillars and len(vox)==61 and len(base&pillars)==9
math={'question_id':q,'unique_answer':'64','source_native_scene':str(p.relative_to(ROOT)),'source_native_scene_sha256':file_hash(p),'independently_recomputed':True,'pillar_footprints':feet,'pillar_total_height':5,'common_base_size':[5,5,1],'base_cells':sorted(base),'all_pillar_cells':sorted(pillars),'intersection_cells':sorted(base&pillars),'union_cells':sorted(vox),'counts':{'base':25,'full_pillars':45,'overlap':9,'remaining':61,'removed':64},'proof':'Each of 25 bottom positions is occupied. Above z=0 exactly9 columns each contain4 further cells. Thus25+9*4=61 remain and125-61=64 are removed. Equivalently25+45-9=61. These exhaust the frozen unit cells and the source visible grid.','specific_wrong_hypothesis':'Treat the full45 pillar cubes and25 slab cubes as disjoint:125-(45+25)=55, double-counting the9 common foot cubes.','marks_add_no_cells_or_equalities':True}
write(TASK/q/'primary_math_proof.json',math)
audit={'question_id':q,'variant_id':vid,'stage':'material_refinement','saved_before_any_calls':True,'old_design':'solid_explore/Solid95/pillar_height_capture','old_preset':'80','old_complete_finals':['80','24'],'old_mechanism':'Two fullheight red rails promote9*5 and OMIT commonbase. No two preset hits.','new_mechanism':'Independently group nine fullheight pillars and whole bottomslab, promoting the distinct double-counting error. Nine top edges index all pillar locations; one complete height rail includes the shared bottom tier; blue slab lower L and two one-tier risers mark its5x5x1 extent.','new_feature_correspondence':'Nine actual top-unit front edges share red with the full5-unit source pillar rail; distinct blue existing slab lower perimeter and thickness endpoints identify the overlapping slab group.','substantive_change':'New overlap-accounting misconception55, opposite to old omission80; newly targeted entire shared slab and allnine pillar footprints are absent from old design. Does not reuse an observed wrong answer.','expected_wrong_answer_frozen':'55','not_cosmetic':True,'prior_raw_evidence_sha256':file_hash(TASK/'all_prior_same_question_evidence.json'),'no_independent_objections_found_for_old_variant':True,'human_semantics':'Only existing edges restyled; groups are highlighted, never asserted to be disjoint. Visible bottom overlaps and all gridlines remain readable.'}
write(TASK/q/'design_difference_audit.json',audit)
actions=[];roles=[]
for x,y in feet:
    t=match_edge(q,'pillar',[[x,y,5],[x+1,y,5]])
    actions.append(style(t,RED,2));roles.append(f'One existing front top edge at pillar footprint({x},{y}); the nine red caps encode the actual9 pillars without inventing hidden cubes.')
for z in range(5):
    t=match_edge(q,'pillar',[[1,0,z],[1,0,z+1]])
    actions.append(style(t,RED,2));roles.append(f'Full-height exemplar rail tier{z+1}/5; lower tier intentionally remains included in the red pillar group, supplying the overlap-counting trap while every horizontal grid boundary remains visible.')
for x in range(5):
    t=match_edge(q,'pillar',[[x,0,0],[x+1,0,0]])
    actions.append(style(t,BLUE,2));roles.append(f'Original slab lower front boundary unit{x+1}/5; jointly identifies five-unit base extent and whole-layer grouping, without drawing a new partition.')
for y in range(5):
    t=match_edge(q,'pillar',[[5,y,0],[5,y+1,0]])
    actions.append(style(t,BLUE,2));roles.append(f'Original slab lower right boundary unit{y+1}/5; gives the second5-unit base extent, completing the true5x5 footprint cue.')
for x,y in [(0,0),(5,0)]:
    t=match_edge(q,'pillar',[[x,y,0],[x,y,1]])
    actions.append(style(t,BLUE,2));roles.append('Existing one-tier outer slab riser: marks actualbase thickness1, binding the blue base outline to the shared lower layer. It does not add a cut or hide the red rail bottom tier.')
folder=save_candidate(q,vid,'55',actions,roles,audit['new_mechanism'],math['proof'],TASK/q/'primary_math_proof.json')
write(folder/'design_difference_audit.json',audit)
print(folder)
