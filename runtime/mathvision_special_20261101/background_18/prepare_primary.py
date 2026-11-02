from tools18 import *
cfg,ad,Renderer=adapter()
cases=[('Plane366','directed_endpoint_binding')] if BRANCH=='PlaneGeometry' else [('Solid239','single_unfold_triangle_binding'),('Solid239','crease_axes_as_hole_edges'),('Solid145','front_strand_identity_transfer'),('Solid145','free_end_upper_side_binding')]
for q,v in cases:
    out=HERE/q/v;d=json.loads((out/'design.json').read_text(encoding='utf-8'))
    if not (out/'render_check.json').exists():
        m=ad.inspect_question(q);renderer=Renderer(cfg,ad,{q:m});p=json.loads((out/'plugin.json').read_text(encoding='utf-8'));before=inputs(ad,q)
        n,a,x=renderer.render(p,frozen=True);n2,b,y=renderer.render(p,frozen=True)
        assert a==b==(out/'candidate.png').read_bytes() and x==y and before==inputs(ad,q)
        write(out/'render_check.json',{'baseline_pixel_equal':True,'normalized_frozen_replay':True,'two_png_bytes_identical':True,'pixel_sha256':x,'png_sha256':file_hash(out/'candidate.png'),'frozen_inputs':before,'appearance_changes':{'style_only':True,'geometry_projection_visibility_unchanged':True},'isolation':ISOLATION,'render_metadata_error_recovered':'Initial artifact writing stopped after design because Plane PluginRenderer has no appearance_changes method; original design/plugin/PNG preserved byte-identically; no API had run.'})
        notes=json.loads((ROOT/'provenance/source_notes.json').read_text(encoding='utf-8-sig'))[q]
        write(out/'source_audit.json',{'question_id':q,'formal_record':ad.records[q],'source_audit':notes.get('audit'),'own_primary_proof':d['primary_math_proof'],'source_hashes':before})
    graph=None
    if q=='Solid145':
        opts={'A':[(1,0),(2,2),(3,3)],'B':[(0,1),(2,2),(3,3)],'C':[(0,1),(1,3),(3,3)],'D':[(0,2),(3,3)],'E':[(2,0),(2,3),(3,3)]}
        graph={}
        for opt,es in opts.items():
            edges=[('T0','B0'),('T1','B2'),('T2','B3'),('E0','T0'),('E1','T3')]+[('B'+str(a),'T'+str(b)) for a,b in es]
            adj={}
            for a,b in edges:adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
            seen=set();todo=['E0']
            while todo:
                a=todo.pop()
                if a in seen:continue
                seen.add(a);todo+=adj[a]
            graph[opt]={'edges':edges,'degrees':{a:len(b) for a,b in adj.items()},'connected':len(seen)==len(adj),'two_free_ends_only':sorted(a for a,b in adj.items() if len(b)==1)==['E0','E1'],'unbranched':all(len(b)<=2 for b in adj.values()),'tail_bottom':opt not in ['A','E']}
            graph[opt]['compatible']=all(graph[opt][k] for k in ['connected','two_free_ends_only','unbranched','tail_bottom'])
        assert [o for o,a in graph.items() if a['compatible']]==['B']
    visual={'Plane366':'Four short colored end intervals lie on existing black segments. Gray grid, open X/Y/Z/T circles and letters are distinct; 56% of each black segment remains black. No new point/line, cut, region or equality mark. Both geometric endpoint permutations remain visible.',
    'Solid239':'All three fold panels, open-layer stack, original diagonal dashed cut, reverse-side bands and five option holes remain visible. Color covers only existing crease/cut/hole edges. No new source region or cut boundary. Source fold and cut meanings still distinguishable from dashedness and layer context.',
    'Solid145':'At native768 size all source and option rope segments, notch placements, upper/lower free hooks, arrow and labels remain clear. Marks lie on real strands or hooks, no wood outline/fill/text changes; no new branch or crossing is added. Existing incorrect C shared bottom notch remains visible.'}[q]
    write(out/'primary_review.json',{'question_id':q,'variant_id':v,'review_kind':'primary_only_NOT_independent','actual_candidate_png_viewed':True,'native_size':True,'formal_original_png_viewed':True,'original_source_jpg_viewed':q.startswith('Solid'),'preserved_unique_answer':ad.records[q]['answer'],'unique_math_proof':d['primary_math_proof'],'independent_of_color_matching':True,'graph_audit':graph,'marker_roles':d['marker_roles'],'visual_findings':visual,'human_semantics':'Colors and widths are Special appearance annotations, not added mathematical givens; original geometry/text/fill/frozen projection/visibility untouched. Human should solve original geometric or rope/folding constraints; second reviewer must check whether a colored correspondence could reasonably be misread as a new mandatory given.','proceed_to_API':True,'controls':[],'limits':['No human study, statistical evidence, per-marker causal ablation or original control in this unit.','Two predeclared model outcomes can only establish the exact observed pair, not causality or robustness.'],'required_next_step_if_pair_hits':'Parent must create a NEW independent second reviewer before any delivery.','created_at':now()})
    print(q,v,'primary ready',flush=True)
