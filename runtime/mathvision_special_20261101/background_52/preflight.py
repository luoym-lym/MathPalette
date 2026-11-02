from bootstrap import install, OWN, PROJECT, SESSION
ISOLATION=install()
from research import save,load,sha,IDS
import json,sys,ast,difflib
from pathlib import Path
from datetime import datetime,timezone

native_findings={
 'Plane480':'Viewed actual768PNG: the one-unit source above-left and four two-unit bases are visible. Twelve black polygon edges, gray1cm grid and middle subdivision crossings remain readable; no closed new target contour. The base highlights coincide with real grid lines, with no point or dimension symbol. Each of five marks is one member of the declared base-length substitution. Human can count2 grid units on each recipient and recover13.',
 'Plane481':'Viewed actual768PNG: source complete-square open L at upper-left and recipient triangular-half-cell open L are visible. Recipient red is pale because the original semitransparent gray fill overlays grid strokes; it still reads as the paired red frame. This compositing is disclosed, not claimed exact same raster red. All12 oblique black target boundaries, all original gray cells and both Math Team words remain readable. Source/receiver have the same true1x1 dimensions; the diagonal still halves the receiver. Four marks have frame roles; area remains10.',
 'Plane483':'Viewed actual768PNG: reference red base1/blue height1 belongs to a fully shaded unit cell; corresponding red unit bases and blue two-unit altitudes of two left triangles are clear. Long altitudes retain intermediate grid intersections. The lower-left altitude foot is on the extension of the triangle base line, not the base segment; this is a valid distance-to-line computation, no new foot point is drawn. Every original sloping gray boundary and16-cell grid remains black/readable; right quadrilaterals unchanged. No added gray region. Human still sees exact area6.',
 'Plane488':'Viewed actual768PNG: red original top flap sides match red upper dotted reflected sides; blue original vertical sides match blue lower dotted reflected sides. Both original black dashed crease lines and central untouched top base, numeric5/8 and the common dotted contact point remain clear. Eight intervals form four actual side-image pairs, useful for original/flap-copy attribution. Even a physical ink-preserving reading is internally consistent because original-to-image side colors agree, and the numeric requested footprint area stays55/2; no answer-choice image loses colored ink. No added cut or extra paper region.',
 'Plane482':'Viewed actual768PNG: both diagonal families are distinct black widths throughout the4 allowed gray-white samples and all9 example tiles. All blank9 squares, sample4 tiles, example9 cells and original gray halves are retained. No colorful paint/gray region is introduced; no single2x2 window is selected. Thickness is consistently assigned by slope, so each complete example tile is exactly one of the4 complete styled library patterns up to translation. This also addresses the reasonable intrinsic-tile-ink reading: it has the same4 tiles and unchanged gray-diamond event, not a fifth tile or no-solution. All13 marks serve source/receiver slope classification; gray side is the real information wrongly discarded by the frozen hypothesis. Two widths alone do not prove targeting success, which requires the separate pair.'
}

for qid,findings in native_findings.items():
    design_path=next((OWN/qid).glob('r52_*/design.json'))
    d=load(design_path);f=design_path.parent
    reviews=[]
    for m in d['marker_roles']:
        reviews.append({'index':m['index'],'role':m['role'],'action':m['action'],'native_actual_visual_status':'visible on intended original path; useful member of the source/recipient grouping described in this exact design','not_an_equality_or_extra_given':True})
    save(f/'primary_review_before_calls.json',{'question_id':qid,'variant_id':d['variant_id'],'reviewer':'background_52 primary research worker','independent_second_review':False,'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'formal_question_and_upstream_read_full':True,'actual_source_JPG_formal_PNG_and_candidate_viewed':True,'native_candidate_dimensions':[768,768],'image_sha256':sha(f/'candidate.png'),'design_sha256':sha(design_path),'plugin_sha256':sha(f/'plugin.json'),'unique_math_proof':str(OWN/qid/'primary_math_proof.json'),'human_semantics_and_targeting_findings':findings,'per_marker':reviews,'schema_and_noop_and_repeat':load(f/'render_check.json'),'primary_admissible_for_own_two_calls':True,'limitations':['Primary review only. A NEW parent independent review is required before delivery.','No original-image incremental effect, human performance, statistical reliability, mechanism-faithful narration or per-marker causal effect is claimed.','The numerical/geometric hypotheses are prospective and are not solver inputs.']})

skips={
 'Plane484':{'reason':'Formal and upstream full wording omit ray membership and alternation; actual JPG illustrates initial alternation without imposing its continuation universally. Same-ray A_i=i*u is an arbitrary-length counterexample. Stored90 and upstream solution cannot supply the missing premise.','not_designed':True,'calls':0},
 'Plane489':{'reason':'Independent six-face enumeration and combinatorial proof give69/125. Colored edges could reasonably be additional paint on formerly white cell boundaries, so no colored design is admissible. Considered black unit-edge widths pairing white outer edge cells to center white cell, or opposite edge strips; this single-face diagram contains no drawn3D shared-block receiver, and the proposed same/different ownership inference has no clean actual counterpart. Replacing old redcorner/internal correspondence with black widths would only be a cosmetic semantic repair without a new geometric grouping. No genuinely different concise information transfer was established, so no forced design/call.','not_designed':True,'calls':0},
 'Plane490':{'reason':'Full vertex negation and nonzero vertex mean independently force unique180. Same-side parallel shafts as0 and arbitrary perpendicular edges as90 repeat the old no-design issues and omit the arrowhead. A new matching colored/width pattern on noncorresponding sides also reasonably asks for a printed-pattern-preserving rotation with no solution; matching true opposite parts simply reinforces180. No substantive unambiguous wrong mapping established; no design/call.','not_designed':True,'calls':0}
}
for qid,d in skips.items():save(OWN/qid/'skip_assessment.json',{'question_id':qid,'primary_only':True,'math_proof':str(OWN/qid/'primary_math_proof.json'),'current_eligibility':str(OWN/qid/'eligibility_initial.json'),**d})

old={
 'Plane480':{'saved_designs':0,'calls':0,'old_disposition':'no clean information hypothesis'},
 'Plane481':{'preset':'12','manual_finals':['10','3'],'both_stop':True,'status':'MISS'},
 'Plane482':{'preset':'B','manual_finals':['C','D'],'both_stop':True,'status':'MISS'},
 'Plane483':{'preset':'8','manual_finals':['8','6.5'],'both_stop':True,'status':'MISS: one hit'},
 'Plane484':{'saved_designs':0,'calls':0,'old_disposition':'missing alternating-ray condition'},
 'Plane488':{'preset':'32.5','manual_finals':['45.625','32'],'both_stop':True,'status':'MISS'},
 'Plane489':{'preset':'53/125','manual_finals':['48/125','27/125'],'both_stop':True,'status':'MISS'},
 'Plane490':{'saved_designs':0,'calls':0,'old_disposition':'no clear grounded wrong correspondence'}
}
save(OWN/'old_manual_outcomes.json',{'all_complete_raw_bodies_read':True,'outcomes':old,'existing_original_controls':[],'no_control_repeated':True,'no_old_outcome_relabelled':True})

protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','runtime/mathvision_special_20261101/continuation_brief.txt','runtime/mathvision_special_20261101/background_52_brief.txt','runtime/mathvision_special_20261101/background_52_assignment.json','runtime/mathvision_special_20261101/annotation_semantics_lessons_20261102.json','runtime/mathvision_special_20261101/annotation_semantics_lesson_plane242_r24_20261102.json']
save(OWN/'protocol_read_receipt.json',{'files':[{ 'path':str(PROJECT/p),'sha256':sha(PROJECT/p),'read_in_full':True} for p in protocols],'applicable_authorization':'Current explicit user instruction authorizes autonomous designs and exact two QuickTest3 calls, overriding branch descriptive manual-only/no-automatic-test instructions. No formal original, approvals, Pass/Collect or publication authorized.','source_specific_lessons':'Full exact independent rejects loaded under reference_read; competing drawing/printed-paper color reading can yield no matching answer. Reject such cases without a legend or question change. Numerical area styling requires its own interpretation; Plane488 transports colors consistently, Plane482 black diagonal styles preserve exactly the same allowed4 complete tile patterns and all possible locations.'})

# Own copy, solver behavior unchanged. Only paths and strict runtime bootstrap.
source=SESSION/'harness/quicktest3_isolated.py';s=source.read_text(encoding='utf-8')
oldline='PROJECT = Path(__file__).resolve().parents[3]'
newlines='sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom bootstrap import install, OWN\ninstall()\nPROJECT = Path(__file__).resolve().parents[4]'
assert s.count(oldline)==1
t=s.replace(oldline,newlines)
t=t.replace('if not target.is_relative_to(RUNTIME) or target == RUNTIME:', 'if not target.is_relative_to(OWN) or target == OWN:')
target=OWN/'harness/quicktest3_isolated.py';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(t,encoding='utf-8')
def funcs(text):return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(text).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
sf,tf=funcs(s),funcs(t)
assert all(sf[k]==tf[k] for k in sf if k!='runtime_path')
save(OWN/'harness_isolation_audit.json',{'source_path':str(source),'source_sha256':sha(source),'isolated_path':str(target),'isolated_sha256':sha(target),'all_functions_other_than_runtime_path_AST_identical':True,'path_only_diff':list(difflib.unified_diff(s.splitlines(),t.splitlines(),fromfile=str(source),tofile=str(target))),'solver_model_thinking_systemprompt_API_config_parsing_retry_timeout_tokenlogic_unchanged':True,'not_called_for_key_check_or_ping':True})
print(json.dumps({'primary_admissible':list(native_findings),'skips':list(skips),'harness_path':str(target),'source_sha256':sha(source),'isolated_sha256':sha(target),'solver_calls_so_far':0},ensure_ascii=False))
