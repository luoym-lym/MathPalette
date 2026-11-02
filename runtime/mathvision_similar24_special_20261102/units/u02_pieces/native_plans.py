from color_mathematics import *

def metadata(qid):
    common = {
      'groups':[], 'marking_mode':'native_boundary',
      'source_reference':'Current user Plane233 C01: colored original open boundary runs as length/placement correspondences. All current nine PNGs and plugins were read. This proposal preserves actual colored material under explicit cut/assembly witnesses rather than declaring colors ignorable.',
      'human_semantics':'Only existing boundary edge portions receive permitted colors and 1.5pt width. Original geometry, fills, labels and grid topology are unchanged. The independent color-preserving enumeration explicitly keeps all ink and proves the original unique answer, including actual legal witnesses for every other choice. Thus neither annotation nor intrinsic-ink reading changes the answer.',
      'conciseness':'Each action covers one necessary original unit-edge portion in a contiguous source/option boundary comparison; every marked run has a documented transport role. No fake internal source partition or new line is drawn.'}
    if qid=='Plane218':
        return {**common,'variant_id':'p03_native_outer_boundary_conservation',
          'expected_wrong_answer':'D','correct_answer':'A',
          'mechanism':'Color the two true three-unit vertical board boundaries red, and trace the inherited red boundary on every candidate shape. Two A/B/C/E copies each account for six red units; two D copies account for only four. Predicted error: require every original red edge to survive in the two cut pieces, and incorrectly exclude D. D is legal because its two unused edge cells retain the missing red units; cutting two pieces does not require using the entire grid.',
          'wrong_answer_semantics':'D means the four-cell bar with an upper cell in the second column cannot supply two disjoint identical pieces. The saved geometric and color-preserving proofs both construct such a pair, leaving two edge cells unused. Letter and value are D.',
          'difference':'Old Plane218 was prescreen only. Own p01 C bounding-box comparison and p02 U orientation comparison both ended B,C and are not retried. This new native-boundary design compares global retained-perimeter accounting across every choice, with no external bracket, no fixed source cut and no selected-option salience. It introduces an independently certified exact material-color reading and a specific false conservation inference unique to D.',
          'color_proof_path':str(OWN/qid/'p03_color_preserving_boundary_proof.json')}
    return {**common,'variant_id':'p03_native_L_arm_transport_all_options',
      'expected_wrong_answer':'A','correct_answer':'E',
      'mechanism':'Mark the source L top arm red and left arm blue. Trace their actual transported outer boundaries in A-D: A has red right/blue top after a clockwise quarter-turn, while B-D have red top/blue left. In E mark the same real top/left four-unit trial spans, which match lengths/colors but fail the unchanged black-white pattern. Predicted error: reject the changed arm orientation of A and accept the locally matching E corner, overlooking legal rotation and full pattern matching.',
      'wrong_answer_semantics':'A asserts that the first 4 by 4 tile cannot be assembled. It is exactly achievable with both pieces rotated clockwise a quarter-turn, including every red and blue boundary unit. The unique impossible black-white/color tile remains E.',
      'difference':'Old on-material C trial colored an invalid reflected L orientation and failed D/A against C; it is not repeated. Own p01 A square-only brackets ended C/B. Own p02 compares independent rotations at B and its original request is preserved separately. The new design tracks the seven-cell L in all five options, transports colors correctly in every constructible choice, and checks E only as a local trial. The substantive information is arm identity under a quarter-turn, not square orientation or a chosen failed corner.',
      'color_proof_path':str(OWN/qid/'p03_color_preserving_boundary_proof.json')}

def build_actions(qid, ad, context):
    actions=[]; roles=[]
    if qid=='Plane218':
        groups,colors=colored218()
        originals={}
        for group in ('given','A','B','C','D','E'):
            objs=[o for o in context['objects'] if o['id'].startswith(group+'_')]
            pts=[p for o in objs for p in o['geometry']['points']]
            x0=min(x for x,y in pts);y0=min(y for x,y in pts)
            for o in objs:
                a,b=o['geometry']['points']
                local=edge((a[0]-x0,a[1]-y0),(b[0]-x0,b[1]-y0))
                if colors[group][local] == BLACK:continue
                actions.append({'type':'set_object_style','target':o['id'],'color':RED,'linewidth_pt':1.5})
                purpose = ('One real vertical source-perimeter unit; the two sides total six red units.' if group=='given' else
                           'One unit of the actual inherited red outer-board boundary in a legal cut placement of '+group+'. Compare its two-copy total with the source; unused material may retain red ink.')
                roles.append({'action_index':len(actions)-1,'target':o['id'],'source_endpoints':[a,b],
                    'group':group,'purpose':purpose,'receiver':'all candidate red runs' if group=='given' else 'given six-unit red perimeter',
                    'native_edge_only':True,'source_or_transport_proof':str(OWN/qid/'p03_color_preserving_boundary_proof.json')})
        assert len(actions)==20
        return actions,roles
    groups,colors=colored398()
    scenejson=read(OWN/qid/'frozen_scene_readonly_snapshot.json')
    from partial_style import object_paths
    captured=ad.scene(qid)
    try:
        captured.fig.canvas.draw()
        for group in ('piece2','A','B','C','D','E'):
            objs=[o for o in scenejson['objects'] if o['id'].startswith('cell'+group)]
            pts=[scenejson['points'][p] for o in objs for p in o['points']]
            x0=min(x for x,y in pts);y0=min(y for x,y in pts)
            for o in objs:
                vertices=[scenejson['points'][p] for p in o['points']]
                for i,(a,b) in enumerate(zip(vertices,vertices[1:]+vertices[:1])):
                    local=edge((a[0]-x0,a[1]-y0),(b[0]-x0,b[1]-y0))
                    color=colors[group][local]
                    if color==BLACK:continue
                    path=object_paths(captured,o['id'])[0]
                    assert path['closed'] and len(path['segments'])==4
                    # Compare identical representations exactly: frozen context path SHA,
                    # and untransformed native polygon vertices in source-coordinate order.
                    # object_paths controls include the renderer's deterministic transform
                    # round trip and must not be substituted for source-scene coordinates.
                    target=next(t for t in context['canvas']['targets'] if t['id']==o['id'])
                    frozenpath=next(p for p in target['partial_paths'] if p['id']==path['id'])
                    assert path['sha256']==frozenpath['sha256'], (o['id'],'real path drift')
                    rawvertices=path['segments'][i]['artist'].get_path().vertices[:4].tolist()
                    assert rawvertices==vertices, (o['id'],'source artist vertices changed')
                    actions.append({'type':'set_object_style','target':o['id'],'color':color,'linewidth_pt':1.5,
                       'interval':{'path_id':path['id'],'path_sha256':path['sha256'],
                                   'start':i/4,'end':(i+1)/4,'wrap':False}})
                    roles.append({'action_index':len(actions)-1,'target':o['id'],
                        'source_endpoints':[a,b],'group':group,'color':color,
                        'purpose':('One unit of the source L top red/left blue four-unit arms, used as distinct transported edge identities.' if group=='piece2' else
                                  'One unit of the true clockwise-quarter-turn L arm in A; preserves source red/blue identity at its legal assembled position.' if group=='A' else
                                  'One unit of the true zero-turn L arm in '+group+'; source-to-target geometric and black-white match is certified.' if group in 'BCD' else
                                  'One unit of the real top/left E boundary in a trial local L placement. Length/color match is real, but complete black-white matching fails; this is not asserted to be a valid assembly.'),
                        'receiver':'source L arms' if group!='piece2' else 'all five option arm comparisons',
                        'native_edge_only':True,'fresh_path_sha256':path['sha256'],
                        'source_or_transport_proof':str(OWN/qid/'p03_color_preserving_boundary_proof.json')})
    finally:
        captured.close()
    assert len(actions)==48, len(actions)
    return actions,roles
