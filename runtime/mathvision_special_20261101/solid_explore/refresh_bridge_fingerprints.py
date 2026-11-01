"""Complete pre-test source-image fingerprints without changing any PNG/plugin."""
from pathlib import Path
import json
from bridge_adapter import RuntimeBridgeAdapter,PluginRenderer,file_hash
OUT=Path(__file__).resolve().parent
adapter=RuntimeBridgeAdapter()
for item in json.loads((OUT/'bridge_prepared_candidates.json').read_text(encoding='utf-8')):
    folder=Path(item['path']);qid=item['question_id']
    old=json.loads((folder/'render_check.json').read_text(encoding='utf-8'))
    (folder/'render_check_initial_before_source_fingerprint.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    before=adapter.frozen_inputs(qid);metadata=adapter.inspect_question(qid)
    renderer=PluginRenderer(adapter.config,adapter,{qid:metadata})
    plugin=json.loads((folder/'plugin.json').read_text(encoding='utf-8'))
    _,data,pixel=renderer.render(plugin);_,data2,pixel2=renderer.render(plugin)
    assert data==data2==(folder/'candidate.png').read_bytes() and pixel==pixel2==old['pixel_sha256']
    assert before==adapter.frozen_inputs(qid)
    updated={**old,'frozen_inputs':before,'pre_test_fingerprint_completion':'Added original source image/config/scene_png dependency hashes; both new redraws byte-match the already prepared candidate PNG. Initial report retained. No API run and no PNG/plugin/design change.'}
    (folder/'render_check.json').write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'question_id':qid,'byte_identical':True,'source_image_hash_included':True},ensure_ascii=False),flush=True)
