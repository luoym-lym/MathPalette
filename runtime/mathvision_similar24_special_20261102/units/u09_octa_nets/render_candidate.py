from own_bootstrap import *
from unit_tools import eligibility,render_setup,snapshot
import io

def canonical(v):
    return json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)

def render(directory,replay=False):
    directory=Path(directory).resolve()
    check_write(directory)
    plugin=load(directory/'plugin.json')
    qid=plugin['question_id']
    eligibility_report=eligibility(qid)
    adapter,renderer,context,isolation=render_setup(qid)
    from renderer_adapter import scene_png
    from render_plugins import check_schema
    from workbench_io import pixel_hash,environment_versions
    schema=load(PROJECT/'SolidGeometry/workbench/plugin.schema.json')
    check_schema(plugin,schema,schema)
    assert canonical(renderer.normalize(plugin))==canonical(plugin)
    if (OWN/qid/'context.json').exists():
        assert canonical(context)==canonical(load(OWN/qid/'context.json'))
    capture=adapter.scene(qid)
    try: noop,noop_digest=scene_png(capture)
    finally: capture.close()
    assert noop_digest==context['original_pixel_sha256']==pixel_hash(PROJECT/'SolidGeometry/image'/f'{qid}.png')
    normalized,first,digest=renderer.render(plugin)
    normalized2,second,digest2=renderer.render(plugin)
    assert canonical(normalized)==canonical(normalized2)==canonical(plugin)
    assert first==second and digest==digest2
    if replay:
        assert first==(directory/'candidate.png').read_bytes()
    else:
        with (directory/'candidate.png').open('xb') as f:f.write(first)
        with (directory/'candidate_repeat.png').open('xb') as f:f.write(second)
        save(directory/'context.json',context,exclusive=True)
    from PIL import Image
    with Image.open(io.BytesIO(first)) as im:
        assert im.size==(768,768)
        rgba=im.convert('RGBA')
        assert rgba.getextrema()[3]==(255,255)
        rgba.close()
    out={'question_id':qid,'independent_process':replay,'pid':os.getpid(),'timestamp':now(),
         'fresh_schema_validation':True,'normalization_exact_after_JSON_canonicalization':True,
         'baseline_pixel_equality':True,'same_process_repeat_byte_equality':True,
         'candidate_png_sha256':hashlib.sha256(first).hexdigest(),'candidate_pixel_sha256':digest,
         'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':sha(directory/'design.json'),
         'context_sha256':sha(OWN/qid/'context.json'),'environment':environment_versions(),
         'appearance_changes':renderer.appearance_changes(plugin),'source':snapshot(),
         'eligibility':eligibility_report,'isolation':isolation,'strict_writeguard':str(OWN),
         'frozen_paths':{'project':str(PROJECT),'own_root':str(OWN),'plugin':str(directory/'plugin.json'),'image':str(directory/'candidate.png')},
         'source_geometry_projection_visibility_changed':False}
    save(directory/('independent_replay_gate.json' if replay else 'render_gate.json'),out,exclusive=True)
    print(json.dumps({k:out[k] for k in ('question_id','independent_process','pid','candidate_png_sha256','candidate_pixel_sha256')},ensure_ascii=False))

if __name__=='__main__':
    render(sys.argv[1],len(sys.argv)>2 and sys.argv[2]=='--replay')
