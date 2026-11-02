from tools57 import *
import ast
import difflib
native={
'Solid79':'Actual768PNG viewed. Blue front and right basal spans are three original unit segments each in both panels; their same-layer correspondence is readable. Orange gives one upper-course unit at front-left and rear-right in both panels. All other black seams, tower supports, exposed nine-cell bottom course and seven absent upper cells remain discernible. No top-tile ink, added cube, junction, point or hidden line. Even literal surviving edge ink is consistent across the remove-cubes operation.',
'Solid234':'Actual768PNG viewed. Original6cm axial range and8cm diameter range are black, complete and clearly separated. One existing top generator is blue and meets the blue original dashed cutting trace at the far top tangent. Original circular ends, lower silhouette, exact cut dash topology and fill remain readable. The cut still spans zero-to-six axially; no radius, center, new cut, solid replacement line or painted region is introduced. Numeric volume question has no moving printed-pattern ambiguity.'}
for q,visual in native.items():
    spec=read(HERE/q/'spec_r57.json');d=HERE/q/spec['variant_id']
    e=eligibility(q);assert e['eligible']
    for p,h in read(HERE/q/'source_hashes_initial.json').items(): assert sha(PROJECT/p)==h,p
    c=read(d/'context.json');objects={o['id']:o for o in c['objects']};paths=read(HERE/q/'exact_paths.json')
    bindings=[]
    for i,a in enumerate(read(d/'plugin.json')['params']['actions']):
        target=a['target'];assert target in objects and objects[target]['styleable']
        bindings.append(dict(index=i,action=a,role=spec['marker_roles'][i]['role'],original_object=objects[target],exact_paths=paths[target]))
    write(d/'marker_bindings.json',bindings)
    write(d/'primary_native_review.json',dict(reviewed_at=now(),role='PRIMARY designer only',actual_native_768_PNG_viewed=True,png_sha256=sha(d/'candidate.png'),design_sha256=sha(d/'design.json'),plugin_sha256=sha(d/'plugin.json'),specific_findings=visual,unique_original_math=spec['primary_math_proof'],each_marker_review=spec['marker_roles'],readability='All original labels, units, edge topology, distinctions and unique answer preserved.',schema_normalized_and_double_identical_render=True,semantics='Task-specific numerical/solid reading; no physical-pattern color erasure premise needed.',proceed_with_exact_frozen_two_calls=True,limits=spec['limits']))
# Only relocation and strict own-scope bootstrap; reference request functions byte-text unchanged.
ref=BASE/'harness/quicktest3_isolated.py';original=ref.read_text(encoding='utf-8')
patched=original.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
needle='sys.dont_write_bytecode = True\n'
patched=patched.replace(needle,needle+'sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom bootstrap import HERE as OWN_ROOT\n',1)
orig_functions={n.name:ast.dump(n) for n in ast.parse(original).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
new_functions={n.name:ast.dump(n) for n in ast.parse(patched).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
assert orig_functions==new_functions
p=HERE/'harness/quicktest3_isolated.py';p.parent.mkdir(exist_ok=True);p.write_text(patched,encoding='utf-8',newline='\n')
write(HERE/'harness_relocation_audit.json',dict(reference_path=str(ref),reference_sha256=sha(ref),local_path=str(p),local_sha256=sha(p),all_reference_function_ASTs_identical=True,unchanged_functions=list(orig_functions),diff=list(difflib.unified_diff(original.splitlines(),patched.splitlines(),lineterm='')),no_model_profile_thinking_systemprompt_credential_token_timeout_retry_changes=True,own_write_guard_before_project_imports=True))
print('Two frozen native-reviewed designs ready. No API calls yet.')
