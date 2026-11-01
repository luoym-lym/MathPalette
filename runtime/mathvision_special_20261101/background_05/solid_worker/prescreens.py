from tools_local import *
graphs={
 'A':[(0,0,0),(0,0,1),(0,0,2),(1,0,0)],
 'B':[(0,0,0),(1,0,0),(2,0,0),(1,0,1)],
 'C':[(0,0,0),(1,0,0),(0,0,1),(1,0,1)],
 'D':[(0,0,0),(1,0,0),(1,1,0),(1,1,1)],
 'E':[(0,0,0),(0,0,1),(0,0,2),(0,0,3)]}
def matchings(vertices):
    if not vertices:return [[]]
    a=vertices[0];result=[]
    for b in vertices[1:]:
        if sum(abs(x-y) for x,y in zip(a,b))!=1:continue
        for rest in matchings([v for v in vertices if v!=a and v!=b]):result.append([[a,b],*rest])
    return result
graph_audit={k:{'cube_centers':v,'domino_tilings':matchings(v)} for k,v in graphs.items()}
assert [k for k,v in graph_audit.items() if not v['domino_tilings']]==['B']
write(TASK/'Solid81/domino_matching_audit.json',{'question_id':'Solid81','method':'Read four-cube adjacency from the unchanged original. Enumerate all face-adjacent domino perfect matchings. B is K1,3; each domino can cover its central cube only once, leaving two unmatched leaves.','figures':graph_audit,'unique_answer':'B'})
screens={
 'Solid81':{'reason':'No sufficiently specific wrong block correspondence found that preserves a clear two-domino assembly interpretation. Pairing nonadjacent cubes by new marks would visually impose a false piece partition; merely framing an entire option is not informative enough.','math':'Unique B: its four cube graph is K1,3 and has no perfect matching; A,C,D,E have face-adjacent two-domino tilings.','math_evidence':'domino_matching_audit.json'},
 'Solid97':{'reason':'The intended 2-versus-5 error is reversal of die handedness. The right target face is intentionally non-visible. Outlining that absent face would add geometry; recoloring dots would alter the givens; no clean visible-seam-only mapping with a concrete independent wrong interpretation was found.','math':'Let the first die normals be +x=4, +y=6, +z=2, consistent with the visible -x=3, -y=1, +z=2. In the second die R(+x)=-y (4 front), R(+y)=+z (6 top). Proper rotation forces R(+z)=(-y) cross (+z)=-x, so 2 is left and opposite 5 is right: A.','math_evidence':'Explicit right-handed cross-product proof in this record.'},
 'Solid105':{'reason':'Visible piece silhouettes are small and heavily overlap at projected cube seams. No exact wrong pair partition with a readable, unambiguous feature correspondence was established. Generic highlighting of two answer pieces would not identify a meaningful source-feature relationship.','math':'Formal correct answer A retained. This prescreen did not independently complete a full spatial packing enumeration; it is not a candidate or a math-qualified result.','math_limit':'No candidate was produced or tested, so no unproved unique-answer claim is made.'},
 'Solid133':{'reason':'Only the cube edges are styleable; animal stickers are semantic images and cannot be restyled by the schema. A false edge map around the common ladybird was considered, but no internally interpretable wrong-opposite pairing was found without creating a conflicting additional identity cue.','math':'The common ladybird fixes the relative cyclic orientation across the two shown corners. Preserved original opposite pairs are ladybird/elephant, mouse/dog, duck/fly; the formal target is E (fly). No modified image was constructed.','math_limit':'No exhaustive sticker-rotation enumeration was performed for this prescreen-only rejection.'},
 'Solid149':{'reason':'A source-to-option edge recoloring without recovering a full spatial correspondence would only highlight an option. New connecting lines would risk false cube seams or changed structure. No concrete readable false part mapping was established from the frozen edge context.','math':'Formal answer A retained. The displayed source has its terminal arms in different spatial directions; simple planar U-shape matching is insufficient. No full independent all-view rotation proof was completed in this prescreen, and no candidate was offered.','math_limit':'Prescreen rejection, not a qualified mathematical verification of all five views.'}}
for qid,data in screens.items():
    check=eligibility(qid);assert check['eligible'],check
    write(TASK/qid/'primary_prescreen.json',{'question_id':qid,'status':'prescreen_only_rejected','review_role':'Primary research screening only','checked_at':datetime.now(timezone.utc).isoformat(),'eligibility_rechecked':check,'actual_original_png_viewed':True,'fresh_formal_png_noop_match':True,'fresh_context_path':str(TASK/qid/'context.json'),'formal_record_path':str(TASK/qid/'formal_record.json'),'frozen_input_hashes_path':str(TASK/qid/'frozen_inputs.json'),'saved_design_count':0,'api_calls':0,'no_qualification_or_approval':True,**data})
print(json.dumps({'prescreen_questions':list(screens),'no_saved_variants_or_calls':True}))
