from tools34 import *
branch=sys.argv[1]
engine=adapter(branch)
from dataset_tools.mathvision_workbench import png_bytes
from workbench_io import pixel_hash
for qid in IDS:
    if branch_of(qid)!=branch: continue
    before=source_files(qid)
    check=eligibility(qid)
    assert check['eligible'],check
    context=engine.inspect_question(qid)
    write(UNIT/qid/'fresh_context.json',context)
    scene=engine.scene(qid)
    try:
        data=png_bytes(scene)
    finally: scene.close()
    (UNIT/qid/'no_op.png').write_bytes(data)
    rec=record(qid); original=PROJECT/branch/rec['image']
    assert pixel_hash(data)==pixel_hash(original)
    assert source_files(qid)==before
    write(UNIT/qid/'no_op_audit.json',{'at':now(),'baseline_pixel_equal':True,'formal_png_sha256':sha(original),'no_op_png_sha256':sha(UNIT/qid/'no_op.png'),'pixel_sha256':pixel_hash(data),'source_files_unchanged':True,'isolation':ISOLATION})
    print(json.dumps({'question_id':qid,'objects':len(context['objects']),'snap_points':len(context.get('snap_points',[])),'baseline_pixel_equal':True}))
