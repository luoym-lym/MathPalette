from tools51 import *

# Retain exact report provenance and task-specific objections without copying old evidence.
reports={
    'Plane295':'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
    'Plane342':'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json',
    'Plane242':'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json'}
lessons={}
for key,rel in reports.items():
    p=BASE/rel;r=read(p)
    lessons[key]=dict(path=str(p),sha256=sha(p),decision=r['decision'],reason=r.get('reason'),
        concrete_objections=r.get('concrete_objections'),human_semantics=r.get('human_semantics',r.get('human_semantics_disposition')),
        primary_proof_corrections=r.get('primary_proof_corrections'),
        application='No text/legend/question repair and no assumption that legal styling resolves a competing human reading. Numerical vase levels, grid cube counts and actual spatial angles were checked on their own wording; no blanket color-preservation constraint added.')
for name in ['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']:
    p=BASE/name;lessons[name]=dict(path=str(p),sha256=sha(p),contents=read(p))
write(HERE/'reference_semantics_lessons_applied.json',lessons)

old=read(BASE/'background_04/checkpoint.json')
prescreen=old['solid_worker_results']['prescreens']['Solid185']
write(HERE/'Solid185'/'exact_old_prescreen_record.json',dict(source=str(BASE/'background_04/checkpoint.json'),source_sha256=sha(BASE/'background_04/checkpoint.json'),record=prescreen))

# Readonly examples of established source/receiver information in all delivered batches.
refs=[]
for b in sorted(BASE.glob('batch_*')):
    if not b.is_dir() or not (b/'manifest.json').exists(): continue
    for p in b.glob('**/design.json'):
        if 'original_control' in str(p):continue
        d=read(p)
        refs.append(dict(path=str(p),sha256=sha(p),question_id=d.get('question_id'),name=d.get('name',d.get('variant_id')),
            mechanism=d.get('mechanism',d.get('hypothesis')),marker_roles=d.get('marker_roles',d.get('information_roles'))))
write(HERE/'delivered_information_binding_references.json',refs)
print('Read',len(refs),'delivered design references across14batches. Applied exact rejection reports;185 old prescreen source saved.')

old_outcomes={
'Solid153':dict(old_preset='E',manual_full_finals=['A','A'],outcome='MISS',complete_pair=True),
'Solid158':dict(old_outcome='prescreen only; no draft/calls'),
'Solid180':dict(old_preset='1820',manual_full_finals=['273','216'],outcome='MISS',complete_pair=True,
    related152='r40 presetD100, first TLS UNEXPECTED_EOF with start+error+summary; zero completed calls; frozenPNG c11e0fb78c7a9390fde24e4c5ecf972c7e107f469bd724175259e886c0c60e19 excluded forever.'),
'Solid182':dict(old_outcome='prescreen only; no draft/calls'),
'Solid183':dict(old_preset='11',manual_full_finals=['10','11'],outcome='MISS',complete_pair=True,
    related155_old_preset11_finals=['10','10'],related155_r40_preset12_finals=['10','11'],
    related_r40_155_and_178='Both first-tested in46; no longer untested drafts.155/178 old40 artifacts not modified.'),
'Solid185':dict(old_outcome='prescreen only, actual nested checkpoint record read, no draft/calls'),
'Solid194':dict(old_outcome='prescreen only; primary tetrahedral proof, no draft/calls'),
'Solid202':dict(old_preset='D',manual_full_finals=['B'],run2='started then aborted after6min; aborted.json preserved',
    complete_pair=False,outcome='MISS/ABORTED, not untested',
    correction='Assignment old_summary.tests=[] is incomplete discovery, not absence of calls. One actual complete raw B and one started aborted call exist. Old B reasoning places60 atZ in a different geometry; true current60 isW. Neither file repaired.')}
write(HERE/'old_history_manual_outcomes_and_corrections.json',dict(read_at=now(),outcomes=old_outcomes,
    old_evidence_files_modified=False,old_failed_or_aborted_PNGs_retested=False,all_raw_complete_answers_read_manually=True,
    metadata_corrections_are_separate_new_records=True))

# More precise frozen source bindings for the new styles.
for qid in ['Solid153','Solid183','Solid202']:
    spec=read(HERE/qid/'spec_r51.json');d=HERE/qid/spec['name'];ctx=read(d/'context.json')
    obj={o['id']:o for o in ctx['objects']};paths=read(HERE/qid/'exact_paths.json');plugin=read(d/'plugin.json')
    bindings=[]
    for i,act in enumerate(plugin['params']['actions']):
        target=act['target'];assert target in obj and obj[target]['styleable']
        for p in paths[target]:
            if act.get('interval') and p['id']==act['interval']['path_id']:
                assert p['sha256']==act['interval']['path_sha256']
        bindings.append(dict(index=i,action=act,source_object=obj[target],full_precision_paths=paths[target]))
    write(d/'exact_action_bindings.json',dict(question_id=qid,bindings=bindings,context_sha256=sha(d/'context.json'),
        full_path_inventory_sha256=sha(HERE/qid/'exact_paths.json'),geometry_projection_visibility_not_modified=True,
        only_original_appearance_styles=True,no_add_points_lines_fills_text_or_fake_relations=True))
print('Full precision bindings saved; all support operations offline/read-only outside own root.')
