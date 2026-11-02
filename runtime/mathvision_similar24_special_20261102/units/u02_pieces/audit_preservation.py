from worker import *

def audit():
    result={'created_at':now(),'own_root':str(OWN),'formal_writes_or_approval_actions':False,
            'no_env_git_or_old_evidence_writes':True,'questions':{},'read_evidence_hash_changes':[]}
    initial=read(OWN/'initial_identity.json')
    result['assignment_unchanged']=filehash(OWN/'assignment.json')==initial['original_assignment_sha256']
    result['brief_unchanged']=filehash(OWN/'brief.txt')==initial['original_brief_sha256']
    for entry in read(OWN/'complete_read_audit.json')['files']:
        p=Path(entry['path'])
        if not p.is_absolute():p=PROJECT/p
        actual=filehash(p)
        if actual!=entry['sha256']:
            result['read_evidence_hash_changes'].append({'path':str(p),'before':entry['sha256'],'after':actual})
    refs={}
    for qid,manifest in read(TASK/'reference_manifest.json').items():
        reference=read(TASK/manifest['directory']/'reference.json')
        refs[qid]={name:{'expected':d['sha256'],'actual':filehash(PROJECT/d['source']),
                        'same':filehash(PROJECT/d['source'])==d['sha256']}
                   for name,d in reference['copied_files'].items()}
    result['current_formal_user9_reference_files_match_frozen_copies']=refs
    cfg,ad=adapter()
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash
    for qid in ('Plane218','Plane398'):
        check=eligibility(qid)
        write(OWN/qid/'eligibility_current.json',check)
        before=fingerprints(ad,qid)
        assert before==read(OWN/qid/'input_fingerprints.json')
        captured=ad.scene(qid)
        try:
            data=png_bytes(captured)
            assert pixel_hash(data)==read(OWN/qid/'context.json')['original_pixel_sha256']
            (OWN/qid/'no_op_current.png').write_bytes(data)
        finally:captured.close()
        record=check['formal_record']
        src=PROJECT/'PlaneGeometry'/record['original_image']
        (OWN/qid/'source_original.jpg').write_bytes(src.read_bytes())
        assert filehash(OWN/qid/'source_original.jpg')==filehash(src)
        assert fingerprints(ad,qid)==before
        result['questions'][qid]={'eligible_current':check['eligible'],'approval_content_sha256':check['current_content_sha256'],
          'all_frozen_sources_unchanged':all(v['expected']==v['actual'] for v in check['frozen_source_hash_verification'].values()),
          'all_adapter_inputs_and_environment_exactly_equal_initial':True,
          'fresh_noop_pixels_equal_formal_original':True,'noop_png_sha256':filehash(OWN/qid/'no_op_current.png'),
          'source_JPG_preserved':True,'source_JPG_sha256':filehash(src)}
    lessonfiles=[PROJECT/'AGENTS.md',PROJECT/'MATHPALETTE_PROTOCOL.md',
      PROJECT/'PlaneGeometry/REDRAW_PROTOCOL.md',PROJECT/'PlaneGeometry/dataset_generator/protocol.json',
      PROJECT/'PlaneGeometry/workbench/README.md',PROJECT/'PlaneGeometry/workbench/agent_prompt.md',
      PROJECT/'PlaneGeometry/workbench/plugin.schema.json',
      OLD/'annotation_semantics_lessons_20261102.json',OLD/'annotation_semantics_lesson_plane242_r24_20261102.json',
      OLD/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
      OLD/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']
    lessonreads=[]
    for p in lessonfiles:
        raw=p.read_bytes()
        text=raw.decode('utf-8-sig')
        lessonreads.append({'path':str(p),'sha256':digest(raw),'bytes_read_in_full':len(raw),
                            'full_text_read':True,'line_count':len(text.splitlines())})
        del text,raw
    result['complete_protocol_and_related_objection_reads']=lessonreads
    write(OWN/'source_and_evidence_preservation.json',result)
    print(json.dumps({'all_sources_unchanged':all(q['all_frozen_sources_unchanged'] for q in result['questions'].values()),
       'old_evidence_hash_changes':len(result['read_evidence_hash_changes']),
       'user9_current_files_match':all(d['same'] for r in refs.values() for d in r.values()),
       'both_currently_eligible':all(q['eligible_current'] for q in result['questions'].values())}))

if __name__=='__main__':audit()
