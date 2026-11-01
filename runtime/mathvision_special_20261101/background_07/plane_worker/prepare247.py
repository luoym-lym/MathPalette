from tools_local import *
q='Plane247';vid='open_stair_endcap_correspondence';out=HERE/q/vid
check=eligibility(q);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,q);m=ad.inspect_question(q)
scene=ad.scene(q)
try:
    scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
finally:scene.close()
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
lookup={edge(*o['geometry']['points']):o['id'] for o in m['objects'] if o['kind']=='segment'}
stair=[((2,4),(2,3)),((2,3),(2,2)),((2,2),(3,2)),((3,2),(3,1)),((3,1),(4,1))]
endcap=[((6,0),(6,1)),((6,1),(6,2)),((6,2),(6,3))]
actions=[];roles=[];bindings=[]
def mark(es,offset,color,role):
    for e in es:
        exact=[tuple(p[i]+offset[i] for i in range(2)) for p in e];oid=lookup[edge(*exact)]
        assert oid not in [a['target'] for a in actions]
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':oid,'role':role,'exact_source_endpoints':exact})
        p=paths[oid][0];bindings.append({'target':oid,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]})
mark(stair,(0,0),'#DC2626','Source gap lower-left open five-edge stair. This is one true local contour feature, not a closed proposed cut part.')
mark(stair,(8,0),'#DC2626','Piece1 matching open five-edge stair, exactly translated by(+8,0) from the source chain. Supplies a concrete feature match while leaving its different bottom cells visible.')
mark(endcap,(0,0),'#2563EB','Source gap right-hand open three-unit vertical endcap. This is a second true local contour feature, not a new internal division.')
mark(endcap,(19,1),'#2563EB','Piece4 matching open three-unit vertical endcap, exactly translated by(+19,+1) from the source chain. Under a half-turn it can face the source opening; the rest of piece4 remains visible and cannot complete the gap with piece1.')
mechanism='Red binds an actual open stair of the gap to the same five-edge stair on piece1; blue binds the actual three-unit straight endcap of the gap to piece4. Targets inferring global fit of pair1+4 from two accurate local boundary matches, despite the incompatible remaining cells. No closed source contour, internal cut, new grid edge, or answer letter is marked.'
math='The square has49 unit cells and the remaining drawing has32, so the gap has17 cells. The four candidate pieces have9,10,7,8 cells respectively. Only pairs1+4 and2+3 have17 cells. Exhaustive enumeration of every placement under all eight grid isometries finds zero exact gap covers for1+4 and exactly one unordered geometric cover for2+3. The saved mathematical_audit.json contains all cells, pair counts and the actual2+3 witness. Hence C is unique. The local1 stair is genuinely identical to the marked source stair, and4 genuinely has the same three-unit endcap, but neither fact establishes a complete two-piece tiling.'
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer D (1 and 4)','params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{q:m});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,q)
out.mkdir(parents=True,exist_ok=False)
write(out/'eligibility_before_design.json',check);write(out/'context.json',m);write(out/'path_fingerprints.json',bindings);write(out/'plugin.json',normalized)
(out/'candidate.png').write_bytes(png)
write(out/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'D','correct_answer':'C','mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'source_partition_semantics':'All16 styled edges coincide with original boundary edges, forming four open non-enclosing chains in total. The two source chains lie on the existing outside boundary of the gap. No input region is enclosed or presented as a fixed partition. Colored local matches do not assert that the full pieces occupy those positions.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':q,'baseline_pixel_match':True,'baseline_pixel_sha256':m['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True,'actual_source_chain_edge_count':8,'actual_piece_chain_edge_count':8})
print(json.dumps({'qid':q,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}))
