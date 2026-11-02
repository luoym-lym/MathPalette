from tools51 import *
from collections import Counter, defaultdict
import numpy as np
import difflib

write(HERE/'offline_setup_errors.json',dict(errors=[dict(question_id=qid,stage='first local render entry point',
    error="ModuleNotFoundError: No module named 'workbench_io'",api_calls=0,design_or_PNG_created=False) for qid in ['Solid153','Solid183','Solid202']],
    correction='Local tools51.render now calls setup() before importing workbench_io, as inspect() already does. No checked-in helper, renderer, schema, API settings or frozen evidence changed.',
    kind='Offline orchestration import errors only; not solver/API failures; retained explicitly.'))

old={}
for qid in IDS+['Solid152','Solid155']:
    manifest_path=(HERE/qid if qid in IDS else HERE/'related_history'/qid)/'history_files.json'
    if not manifest_path.exists(): continue
    manifest=read(manifest_path)
    malformed=[]
    for name in manifest:
        p=Path(name)
        if p.suffix=='.json':
            try: read(p)
            except Exception as error: malformed.append(dict(path=str(p),sha256=sha(p),error=repr(error),bytes=p.stat().st_size))
    old[qid]=dict(files=len(manifest),malformed=malformed,all_old_bytes_still_match=all(sha(p)==h for p,h in manifest.items()))
write(HERE/'historical_parse_and_preservation_audit.json',old)

reasons={
'Solid158':dict(correct='B',math='Independent 120-ball tetrahedral lattice enumeration leaves20 interior balls with layer sizes10,6,3,1: a4-pyramid.',
    considered=['Pair a true side row in the separated six-ball base with an assembled boundary row to suggest shrinking the side width without removing the base.',
                'Use the displayed top/base roles to suggest only two layer losses (6-pyramid).'],
    rejection='The actual illustrated3-pyramid has no interior ball, and every displayed layer ball belongs to at least one outside face. The assembled panel in158 gives an outside silhouette, not an8-pyramid interior receiver. A valid shrinking-row comparison would give the correct triangular-array relation; getting6 requires omitting additional tetrahedral faces/base numerically. Coloring circle rims cannot make that omission a new geometric correspondence without falsely designating a displayed ball/row as interior. No plugin or calls.',
    old='background_18 assessment: no clean receiver; no old design or API calls.'),
'Solid194':dict(correct='4',math='Its own independent enumeration of a+b+c+d=7, all coordinates>=1, gives4 nonempty interior layers and20 white balls.',
    considered=['Compare all-black outside including the base with side-row width reductions.',
                'Pair side-row and top-row positions to confuse reduction of row width with reduction of vertical layer count (possible5 or6).'],
    rejection='Unlike158 the actual194 source has only three detached white-circle layer arrays and no assembled panel. None is a black/white8-pyramid or a surviving interior pyramid. A count-preserving rim style on an actual row cannot supply the requested white-layer receiver. Labeling some source balls as black shell or white interior through color would add a false classification; drawing an8-pyramid is forbidden. A numeric subtraction error alone is not an informative new image. No plugin or calls.',
    old='background_22 primary_math and source_primary_audit explicitly held the same missing-interior issue; no old API.'),
'Solid180':dict(correct='80',math='Let alternating strip widths a,b and strip height h.2(a+b)=26,a+h=10,b+h=7. Thus a+b=13,h=2,a=8,b=5, volume80; positive solution unique.',
    considered=['Bind the true5cm upper-panel free edge with the neighboring side-panel opposite edge to invite double-counting that common dimension as10, giving8*10*2=160.',
                'Bind two occurrences of a true8cm fold direction to invite volume320 or160.'],
    rejection='On the exact net the paired opposite panel edges are two occurrences of the same side, and a clean corresponding-edge style reinforces equality. It has no geometric receiver representing a concatenated box dimension. To make160 a determinate information-transfer trap would need a false concatenation/equality, hidden shared fold, or reusing the forbidden total-span-to-flap mechanism. The alternative total10/7/26 scope is old; the related152 PNG failed TLS and is not retried or renamed. No genuinely clear new local ownership substitution selected; no plugin/calls.',
    old='Own bounding_dimension_capture preset1820, full finals273/216 MISS. Related152/r40 first started call TLS UNEXPECTED_EOF, no completion/no retry; exact start/error/summary/PNG read.'),
'Solid185':dict(correct='E',math='Six arrow segments have lengths18,t,18,18-t,18,18. Sum5*18=90 for any source front-turn fraction, independently of schematic t=11.700000000000001. Unique E.',
    considered=['Bind a true18cm cube edge to two connected surface-path legs and substitute their chord.',
                'Bind complementary front horizontal portions to a full edge, then erroneously merge an additional unit segment.'],
    rejection='Combining the two complementary horizontal pieces into18 is valid and retains90. Merging another true unit requires ignoring a drawn arrowed path piece, duplicating the old4-unit omission. Actual native front/right corner chords produce neither the listed80 nor72 without arbitrary rounding or invented equality; drawing a shortcut or unfolding is forbidden. Non-route edge styling alone would not establish the wrong path grouping, while route recoloring would violate the required black-target preservation. No plugin/calls.',
    old='Actual background_04 checkpoint record rejects de-emphasizing horizontal pieces because route membership becomes ambiguous; no saved design/calls.'),
'Solid182':dict(correct='20 (intended depicted uniform panel pattern)',math='In the actual full frozen polyhedron, each of12 pentagons has5 hexagon neighbors, and every hexagon has3 pentagon neighbors.60 black-white edge incidences /3=20.',
    considered=['Match the five central pentagon contacts to five neighboring white-face records to make60 contact records stand for60 hexagons.',
                'Mark alternating contact sides on a real white hexagon to illustrate repeated ownership.'],
    rejection='The central5-neighbor comparison alone supplies only local salience and omits the actual multiply-shared receiver. Marking the three real contacts of a white hexagon instead explicitly supplies the correct /3 grouping, not a substantive false ownership correspondence. A repeated60-record drawing would add face/adjacency or imaginary tally objects. Moreover12 pentagons alone does not determine a general unseen hexagon count: even a trivalent fullerene satisfies Euler for varying hexagon counts.20 uses the intended uniform alternating adjacency depicted/reconstructed; the hidden full mesh is a renderer construction, not a new given. No strict unique-human certification beyond that interpretation and no clean new mark group, so no API.',
    old='background_18 assessment rejected connectors/new boundaries and isolated patch outlining; no old PNG or API.')
}

for qid,a in reasons.items():
    e=eligibility(qid); assert e['eligible']; write(HERE/qid/'eligibility_before_assessment.json',e)
    write(HERE/qid/'assessment.json',dict(question_id=qid,assessed_at=now(),status='prescreen_skip_no_clean_new_information_transfer',
        formal_source_JPG_and_formal_PNG_individually_viewed_native=True,fresh_exact_context_and_scene_audited=True,
        no_op_pixels_exact=True,**a,source_jpg_sha256=sha(PROJECT/BRANCH/e['record']['original_image']),
        formal_png_sha256=sha(PROJECT/BRANCH/e['record']['image']),new_designs=0,API_calls=0,unworked=False,
        review_level='PRIMARY researcher only; no independent second review/approval.'))

# Actual adjacency verification uses mesh edges, not a memorized ball formula.
e=eligibility('Solid182');item=read(PROJECT/BRANCH/next(x for x in e['record']['runtime_dependencies'] if x.endswith('/scene.json')))
faces=item['polyhedra'][0]['faces']; edges=defaultdict(list)
for i,f in enumerate(faces):
    for a,b in zip(f,f[1:]+f[:1]): edges[tuple(sorted((a,b)))].append(i)
assert all(len(v)==2 for v in edges.values())
counts={i:sum(len(faces[(v[0] if v[1]==i else v[1])])==5 for v in edges.values() if i in v) for i in range(len(faces))}
assert {counts[i] for i,f in enumerate(faces) if len(f)==6}=={3}
assert all(all(len(faces[v[0] if v[1]==i else v[1]])==6 for v in edges.values() if i in v) for i,f in enumerate(faces) if len(f)==5)
write(HERE/'Solid182'/'mesh_incidence_diagnostic.json',dict(full_frozen_faces=len(faces),face_sizes=dict(Counter(map(len,faces))),edges=len(edges),
    pentagon_neighbor_counts_by_face=counts,derivation='12*5=3H -> H20 for actual uniform mesh.',
    limitation='The undisplayed back mesh cannot be promoted into an extra verbal condition. Prescreen held, not used as a solver success or formal-original reapproval.'))

visuals={
'Solid153':'Actual768PNG has two red wide-end pairs A top/D bottom and two blue narrow-end pairs A bottom/D top. All five silhouettes, grey openings, A-E labels and full view preserved. No E waist ink, no waterline, no tick scale.8 actions form4 bilateral regions; both sides encode widths. Human uses water from base; decorative rim colors do not create a different capacity or answer.',
'Solid183':'Actual768PNG shows4red x-plane L traces,2green y-plane L traces and3blue z-plane L traces. All outer rims and P/Q labels remain black; cell boundaries are individually distinguishable at intersections.70unit fragments form9 continuous groups. Every fragment is an existing visible seam of its named true plane. No internal intersection, diagonal, hidden grid, dot or extra cube. Human10 remains unique;9 is a genuine boundary/visit error, not counting added ink as blocks.',
'Solid202':'Actual768PNG shows short red/blue rays atY andW, with long uncolored gaps along all four connecting sides. All four original black arcs and vertex labels, the hidden dashed tripod and cube edges remain visible. RedY->Z/W->X and blueY->X/W->Z give two directional correspondences. No right-angle/equal-angle glyph or polygon enclosure added. The angle atW remains the two actual face diagonals,60;330 is unique regardless of decorative colors.'}
for qid,description in visuals.items():
    spec=read(HERE/qid/'spec_r51.json');d=HERE/qid/spec['name'];e=eligibility(qid);assert e['eligible']
    assert all(sha(PROJECT/p)==h for p,h in read(HERE/qid/'source_hashes_initial.json').items())
    write(d/'primary_native_review.json',dict(reviewed_at=now(),role='PRIMARY designer only',actual_PNG_viewed_at_native_768=True,
        png_sha256=sha(d/'candidate.png'),design_sha256=sha(d/'design.json'),plugin_sha256=sha(d/'plugin.json'),
        specific_findings=description,math_proof=spec['primary_math_proof'],marker_roles=spec['marker_roles'],
        targeted_and_each_mark_useful=True,human_original_answer_preserved=True,concise_grouping=True,
        semantic_lesson='Unlike moving physical paper ink, these are numeric geometry questions. Colors add no material constraint, equality, extra object or transformation condition.',
        actual_schema_normalization_and_repeat_verified=True,proceed_to_exact_two_calls=True,
        limitations=spec['limits']))

# Preserve reference implementation; only relocate project path and install isolation.
ref=BASE/'harness/quicktest3_isolated.py';original=ref.read_text(encoding='utf-8')
patched=original.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
needle='sys.dont_write_bytecode = True\n'
insertion="sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom bootstrap import HERE as OWN_ROOT\n"
patched=patched.replace(needle,needle+insertion,1)
assert original.count('PROJECT = Path(__file__).resolve().parents[3]')==1
target=HERE/'harness/quicktest3_isolated.py';target.parent.mkdir(exist_ok=True)
target.write_text(patched,encoding='utf-8',newline='\n')
write(HERE/'harness_relocation_audit.json',dict(reference_path=str(ref),reference_sha256=sha(ref),local_path=str(target),local_sha256=sha(target),
    changes=list(difflib.unified_diff(original.splitlines(),patched.splitlines(),fromfile='reference',tofile='own_location',lineterm='')),
    unchanged_functions=[name for name in ['run_tests','reference_module','main','check_key','write_new_json'] if original[original.index('def '+name+'('):].split('\ndef ',1)[0]==patched[patched.index('def '+name+'('):].split('\ndef ',1)[0]],
    no_profile_timeout_token_APIconfig_system_prompt_or_retry_changes=True,
    bootstrap_installs_own_write_guard_before_any_project_import=True))
print('Five prescreen decisions saved; three native-reviewed frozen designs ready; zero API calls so far.')
