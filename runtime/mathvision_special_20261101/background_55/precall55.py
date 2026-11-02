from tools55 import *
import difflib

base_source=BASE/'harness/quicktest3_isolated.py'
original=base_source.read_text(encoding='utf-8')
routed=original.replace('sys.dont_write_bytecode = True\nPROJECT = Path(__file__).resolve().parents[3]',
    'sys.dont_write_bytecode = True\nsys.path.insert(0,str(Path(__file__).resolve().parents[1]))\nfrom bootstrap import HERE as OWN_ROOT\nPROJECT = Path(__file__).resolve().parents[4]')
assert routed!=original and routed.count('from bootstrap import HERE as OWN_ROOT')==1
target=HERE/'harness/quicktest3_isolated.py';target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(routed,encoding='utf-8')
write(HERE/'harness_routing_audit.json',dict(source=str(base_source),source_sha256=sha(base_source),routed_sha256=sha(target),
    diff=list(difflib.unified_diff(original.splitlines(),routed.splitlines())),changes='Only project-root resolution and import of own-root bootstrap. Existing API/model/profile/thinking/system/payload/timeout/token/error loop unchanged. Harness cache paths become own/harness; own audit hook guards every write.'))

reviews={
 'Solid195':dict(native='Viewed candidate768x768. Three colored connected two-quarter chains end and change color only at genuine signed-axis junctions. Every black remaining hoop arc stays visible. Six original false-projection crossing gaps remain open; no line bridges a depth gap, no new junction dot/start label/arrow exists. The middle within-group junction and the between-group junction are visibly different grouping roles but both original physical joins.',semantics='Numerical count of actual arcs; colored ink, even if physical, cannot change hoop topology or the right/left travel rule. This is not a picture-match or printed-pattern option task. Counting the three color-groups is the specified wrong unit; actual six quarter-arcs still reconstruct uniquely.'),
 'Solid206':dict(native='Viewed candidate768x768. Left end triangle LAD has one solid and two original dashed edges, all red. Right end RCB has three solid red edges. Blue ridge L-R still carries2s, base A-B still carriess, and hidden D-C stays black dashed. No fill, new face, perpendicular symbol or height line. Every original dimension is legible.',semantics='Numerical volume; color groups identify real end-face boundaries and one connector, with no explicit equal-length or parallel-face symbols. Original lengths s,s,2s of the connectors refute the prism interpretation for a careful human.'),
 'Solid207':dict(native='Viewed candidate768x768. The input upper half-side from existing cut endpointsm to corners2 is red and stops exactly at the cut endpoint. Only the full upper-right A panel side is also red. All6A/B pieces, original cut, original hexagon, all hinge edges and A/B labels remain black/readable. No added face, piece, fold or dot.',semantics='Numerical volume; physical colored edging can remain ink without altering any length or the enclosed solid. No transformed printed-pattern answer is demanded. Same color is a comparison cue, not a numerical equality stipulation; the full12 square and its6 half-side remain inferable.'),
}
for qid in ['Solid195','Solid206','Solid207']:
 spec=read(HERE/qid/'spec_r55.json');d=HERE/qid/spec['name'];design=read(d/'design.json');check=read(d/'render_check.json')
 assert design['png_sha256']==sha(d/'candidate.png') and sha(d/'candidate.png')==sha(d/'repeat.png')
 value=eligibility(qid);assert value['eligible'];write(d/'eligibility_before_calls.json',value)
 context=read(d/'context.json');objects={o['id']:o for o in context['objects']}
 per=[]
 for role,action in zip(spec['marker_roles'],read(d/'plugin.json')['params']['actions']):
  assert role['target']==action['target'] and objects[action['target']]['styleable']
  path=read(HERE/qid/'exact_paths.json')[action['target']]
  if 'interval' in action:assert action['interval']['path_sha256']==path[0]['sha256']
  per.append(dict(**role,action=action,current_object=objects[action['target']],frozen_exact_paths=path,legality='actual schema/default normalization passed; allowed color/width, original dashes preserved',native_visibility='Actually visible in the native candidate PNG; no marker added merely to meet a quota.'))
 write(d/'primary_visual_marker_review.json',dict(question_id=qid,checked_at=now(),image_sha256=sha(d/'candidate.png'),design_sha256=sha(d/'design.json'),
    actually_viewed_native=True,source_JPG_and_formal_PNG_actually_viewed=True,**reviews[qid],per_marker_reviews=per,
    no_op_formal_pixels_equal=read(HERE/qid/'baseline_check.json'),schema_normalized=True,twice_byte_identical=check['twice_byte_identical'],unique_answer_preserved=True,
    primary_only=True,parent_new_independent_review_required=True,no_Pass_Collect_delivery_or_approval=True))
print('Preregistered three native-viewed candidates; original solver helper routing only; no API yet.')
