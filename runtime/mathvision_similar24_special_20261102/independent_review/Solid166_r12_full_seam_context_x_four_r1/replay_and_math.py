from review_bootstrap import *

def run():
    import runtime_isolation
    isolation = runtime_isolation.install(OWN/'cache/bridge', guard_writes=True)
    from delivery_bridge_adapter import RendererAdapter
    from workbench_io import load_config, pixel_hash, environment_versions
    from render_plugins import PluginRenderer, check_schema
    from renderer_adapter import scene_png
    from dataset_tools import catalog
    import io
    from PIL import Image
    config = load_config(PROJECT/'SolidGeometry/workbench/config.json')
    formal = next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid166')
    catalog.validate_formal_row(PROJECT, 'SolidGeometry', formal)
    approval = load(PROJECT/'provenance/approvals.json')['approvals']['Solid166']
    content = catalog.content(PROJECT, 'SolidGeometry', formal)
    fingerprint = catalog.digest(content)
    assignment = load(UNIT/'assignment.json')['questions'][0]
    assert canonical(formal)==canonical(assignment['formal_record'])
    assert canonical(approval)==canonical(assignment['approval'])
    assert fingerprint==approval['content_sha256']==assignment['current_content_sha256']
    source = {p:{'expected':h,'actual':sha(PROJECT/p)} for p,h in assignment['frozen_source_files_sha256'].items()}
    assert all(v['expected']==v['actual'] for v in source.values())
    special = PROJECT/'SolidGeometry/special_variant'
    status = {f:[r for r in catalog.rows(special/f) if r.get('question_id',r.get('id'))=='Solid166']
              for f in ('accepted_index.jsonl','collected_index.jsonl')}
    for f in ('recipes.json','collection.json'):
        p = special/'Solid166'/f
        status[f]=load(p) if p.exists() else None
    assert not any(status.values())
    save('current_eligibility.json', {'checked_at':now(),'formal_record':formal,'approval':approval,
        'recomputed_content_sha256':fingerprint,'content':content,'source_checks':source,
        'target_special_status':status,'eligible':True,'no_authority_changes':True})
    adapter = RendererAdapter(config)
    context = adapter.inspect_question('Solid166')
    frozen_context = load(CANDIDATE/'context.json')
    assert canonical(context)==canonical(frozen_context)
    plugin=load(CANDIDATE/'plugin.json')
    schema=load(PROJECT/'SolidGeometry/workbench/plugin.schema.json')
    check_schema(plugin,schema,schema)
    renderer=PluginRenderer(config,adapter,{'Solid166':context})
    assert canonical(renderer.normalize(plugin))==canonical(plugin)
    capture=adapter.scene('Solid166')
    try:
        noop,digest=scene_png(capture)
    finally:
        capture.close()
    formal_png=PROJECT/'SolidGeometry/image/Solid166.png'
    assert digest==context['original_pixel_sha256']==pixel_hash(formal_png)
    (OWN/'noop.png').write_bytes(noop)
    normalized, first, pixels=renderer.render(plugin)
    assert canonical(normalized)==canonical(plugin)
    assert first==(CANDIDATE/'candidate.png').read_bytes()
    assert pixels==pixel_hash(CANDIDATE/'candidate.png')
    (OWN/'candidate_replay.png').write_bytes(first)
    with Image.open(io.BytesIO(first)) as im:
        assert im.size==(768,768)
        assert im.convert('RGBA').getextrema()[3]==(255,255)
    replay={'checked_at':now(),'pid':os.getpid(),'isolation':isolation,'schema_valid':True,
        'exact_normalized_plugin':True,'exact_context_all_keys_values_ordered_arrays':True,
        'noop_formal_pixels_equal':True,'noop_bytes_equal_formal':noop==formal_png.read_bytes(),
        'formal_png_sha256':sha(formal_png),'noop_png_sha256':sha(OWN/'noop.png'),
        'noop_pixel_sha256':digest,'candidate_replay_bytes_equal':True,
        'candidate_png_sha256':sha(CANDIDATE/'candidate.png'),'candidate_pixel_sha256':pixels,
        'environment':environment_versions(),'appearance_changes':renderer.appearance_changes(plugin),
        'threads':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},
        'strict_write_root':str(OWN),'numeric_tolerances_used_for_comparison':False,
        'no_solver_API_or_subprocess':True}
    save('exact_replay.json',replay)

    # Independent combinatorial proof, seeded in the middle rather than taking
    # any source/primary answer or folding_verification as an input.
    scene=load(PROJECT/'SolidGeometry'/formal['scene'])
    faces={o['id']:tuple(tuple(p) for p in o['points']) for o in scene['objects'] if o['id'].startswith('netface')}
    edges={o['id']:tuple(tuple(p) for p in o['points']) for o in scene['objects'] if o['id'].startswith('netedge')}
    unit=((1,0,0),(0,1,0),(0,0,1))
    seed='netface3'
    labels=dict(zip(faces[seed],unit))
    walked={seed}
    steps=[]
    while len(walked)<len(faces):
        made=False
        for a in sorted(walked):
            for b in sorted(set(faces)-walked):
                common=set(faces[a]) & set(faces[b])
                if len(common)!=2:
                    continue
                old=next(p for p in faces[a] if p not in common)
                new=next(p for p in faces[b] if p not in common)
                value=tuple(-x for x in labels[old])
                if new in labels:
                    assert labels[new]==value
                labels[new]=value
                walked.add(b)
                steps.append({'from':a,'to':b,'hinge':sorted(common),'new_flat_vertex':new,'new_octahedral_vertex':value})
                made=True
                break
            if made:
                break
        assert made
    folded_faces={f:sorted(labels[p] for p in ps) for f,ps in faces.items()}
    assert len({tuple(map(tuple,v)) for v in folded_faces.values()})==8
    assert all(sorted(next(i for i,x in enumerate(p) if x) for p in ps)==[0,1,2] for ps in folded_faces.values())
    signatures={e:sorted(labels[p] for p in ps) for e,ps in edges.items()}
    multiplicity={e:sum(set(ps).issubset(face) for face in map(set,faces.values())) for e,ps in edges.items()}
    free={e:ps for e,ps in signatures.items() if multiplicity[e]==1}
    assert len(free)==10
    seams=[]
    remaining=set(free)
    while remaining:
        e=min(remaining)
        mates=[f for f in remaining if f!=e and free[f]==free[e]]
        assert len(mates)==1
        mate=mates[0]
        seams.append({'edges':[e,mate],'endpoint_signature':free[e]})
        remaining.remove(e); remaining.remove(mate)
    numbered={'1':'netedge11','2':'netedge9','3':'netedge13','4':'netedge2','5':'netedge4'}
    exhaustive={n:{'edge':e,'signature':signatures[e],'equals_x':signatures[e]==signatures['netedge15']} for n,e in numbered.items()}
    assert [n for n,v in exhaustive.items() if v['equals_x']]==['5']
    for a,b in [('netedge13','netedge9'),('netedge5','netedge14'),('netedge8','netedge16')]:
        assert signatures[a]==signatures[b]
    assert signatures['netedge15']!=signatures['netedge2']
    proof={'method':'Exact signed-axis combinatorial octahedron propagation, independent middle-face seed.',
      'formal_question':formal['question'],'option_semantics':'No option letters or separate choices; printed 1..5 identify boundaries, not lengths.',
      'argument':[
        'The actual source shows six alternating triangles in a strip, one upper flap on its leftmost triangle and one lower flap on its rightmost triangle. All eight original faces and the attachment graph are retained.',
        'Use the standard octahedron vertices +/-X,+/-Y,+/-Z as combinatorial names. Each face has one name on each axis. Across a shared edge the other triangular face replaces the opposite vertex with its negative; its two shared vertices are fixed.',
        'Fix the three vertices of netface3 to X,Y,Z in the saved point order. The connected face tree forces every remaining name by the adjacent-face rule. The eight resulting faces are exactly the eight distinct octahedral faces, so this is a complete closure, not a local possible fold.',
        'Any other seed choice is one global octahedral symmetry, including turning the sheet over. It preserves equality of unordered edge endpoint pairs; thus it cannot change which printed edge coincides with x.',
        'All ten free boundaries are paired exhaustively below. Exactly printed5 has the same two folded endpoints as x. Printed4 shares only a vertex with x, not a whole edge. Mere vertex contact cannot be the intended meaning of meets, since multiple numbered edges touch x at vertices; the conventional seam meaning and depicted net give one answer.',
        'This is a topological seam proof, not an inference from projected nearness, same color, source approved answer, primary proof or model prose.'],
      'seed':{'face':seed,'mapping':[{'flat':p,'world_name':labels[p]} for p in faces[seed]]},
      'fold_steps':steps,'folded_faces':folded_faces,'all_edge_signatures':signatures,
      'all_five_free_seams':seams,'exhaustive_numbered_edge_comparison':exhaustive,
      'unique_answer':'5','parent_proof_used_as_proof':False,'exact_integer_names_no_tolerance':True}
    save('independent_math.json',proof)

    # Projection/visibility audited separately using exact rational values of
    # the frozen binary floats, without a closeness threshold.
    from fractions import Fraction
    from itertools import combinations
    def sub(a,b): return tuple(x-y for x,y in zip(a,b))
    def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    def dot(a,b): return sum(x*y for x,y in zip(a,b))
    octa=[o for o in scene['objects'] if o['id'].startswith('octa')]
    vertices=sorted({tuple(Fraction(x) for x in p) for o in octa for p in o['points']})
    hull=[]
    normals={}
    for triple in combinations(range(6),3):
        a,b,c=(vertices[i] for i in triple)
        n=cross(sub(b,a),sub(c,a))
        sides=[dot(n,sub(vertices[i],a)) for i in range(6) if i not in triple]
        if all(v>0 for v in sides) or all(v<0 for v in sides):
            if all(v>0 for v in sides): n=tuple(-x for x in n)
            hull.append(triple);normals[triple]=n
    assert len(hull)==8
    visibility=[]
    for o in octa:
        ends={vertices.index(tuple(Fraction(x) for x in p)) for p in o['points']}
        adjacent=[f for f in hull if ends.issubset(f)]
        assert len(adjacent)==2
        visible=any(normals[f][2]>0 for f in adjacent)
        computed='visible' if visible else 'hidden'
        assert computed==o['visibility']
        visibility.append({'id':o['id'],'frozen':o['visibility'],'computed':computed,'adjacent_faces':adjacent})
    assert scene['projection']['matrix']==[[1,0,0],[0,1,0]]
    assert scene['projection']['toward_viewer']==[0,0,1]
    save('world_projection_visibility.json',{'scene_sha256':sha(PROJECT/'SolidGeometry'/formal['scene']),
        'world_geometry':'Original six-vertex octahedral pose, 8 convex hull facets, all 12 original edges; no candidate world change.',
        'net_geometry':'Eight planar triangles fixed at z=0. Signed-axis folded proof is separate from the display octahedron pose.',
        'projection':scene['projection'],'frozen_visibility':scene['visibility'],
        'exact_rational_hull_faces':hull,'visibility_checks':visibility,
        'partial_style_intervals':[],'hidden_edges':sum(o['visibility']=='hidden' for o in octa),
        'drawn_changes':'Eight full existing net boundary colors only; all original line types, fill, text, projection and visibility untouched.',
        'floating_tolerance_used':False,'separate_world_projection_visibility':True})
    print(canonical({'fingerprint':fingerprint,'replay':replay,'proof_answer':'5','all_seams':seams,'visibility_edges':len(visibility)}))

if __name__=='__main__': main(run)
