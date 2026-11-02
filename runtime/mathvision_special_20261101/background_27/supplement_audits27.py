from tools27 import *
import numpy as np

q='Plane318';a=HERE/q/'refinement_assessment.json'
write(HERE/q/'primary_math_correction.json',{'stage':'material_refinement','question_id':q,'created_at':now(),
    'supersedes_only_primary_math_sentence_in':str(a),'previous_assessment_sha256':file_hash(a),
    'correction':'The earlier screening sentence omitted the final halfturn in its displayed matrix. R180 * Mx * Rcw90 = [[0,1],[1,0]], so the final map is(x,y)->(y,x), not(-y,-x). The formal answerA and no-clean-hypothesis screening decision are unchanged.',
    'exact_integer_matrix_proof':{'clockwise90':[[0,1],[-1,0]],'right_edge_flip':[[-1,0],[0,1]],'halfturn':[[-1,0],[0,-1]],'composition':[[0,1],[1,0]]},
    'api_calls_for_this_question':0,'no_formal_data_modified':True})

src=['B','W','G','W','G','B','W','B','G']
step1=['W' if x=='B' else x for x in src]
step2=['B' if x=='G' else x for x in step1]
final=['G' if x=='W' else x for x in step2]
options={'A':['G','G','B','G','B','G','G','G','B'],'B':['W','G','B','G','B','W','G','W','B'],
 'C':['G']*9,'D':src,'E':['B','G','B','G','B','B','G','B','B']}
assert [k for k,v in options.items() if v==final]==['A']
write(HERE/'Plane159'/'fresh_discrete_math.json',{'source_classes_from_native_original':src,'step1':step1,'step2':step2,
    'step3':final,'all_native_options':options,'unique_answer':'A','wrong_dark_union_image':options['E'],
    'semantic_fills_unchanged_by_edge_style':True})

grey={(1,3),(2,3),(2,2),(0,1),(1,1),(0,0)}
letters={'A':(3,3),'B':(4,3),'C':(5,0),'D':(4,1),'E':(4,0)}
true={(5-c,r) for c,r in grey};false={(5-c,1-r) if r<=1 else (5-c,r) for c,r in grey}
assert [k for k,v in letters.items() if v not in true]==['E']
assert [k for k,v in letters.items() if v not in false]==['D']
write(HERE/'Plane203'/'fresh_discrete_math.json',{'grey_cells':sorted(grey),'letter_cells':letters,'true_reflection':sorted(true),
    'false_lower_L_halfturn_with_upper_L_true_reflection':sorted(false),'true_unique_uncovered':'E','predeclared_false_unique_uncovered':'D',
    'cell_map_true':'(c,r)->(5-c,r)','cell_map_false_lower_part':'(c,r)->(5-c,1-r)',
    'every_marker_bottom_source_to_top_false_destination':True})

def segments(ob):
    return {tuple(sorted(tuple(float(t) for t in p) for p in o['points'])) for o in ob}
def transform(seg,sx,sy,dx,dy):
    return {tuple(sorted((sx*x+dx,sy*y+dy) for x,y in s)) for s in seg}
ob={o['id']:o for o in json.loads((HERE/'Plane362'/'source_scene_snapshot.json').read_text(encoding='utf-8'))['objects']}
source=segments([ob['o'+str(i)] for i in range(24)])
true=transform(source,1,-1,0,11) # source y8..10 becomes option y1..3
mirror=transform(source,-1,1,21.4,-14) # source x10..16.4 becomes D x5..11.4, y-6..-4
actual_B=segments([ob['o'+str(i)] for i in range(48,72)])
actual_D=segments([ob['o'+str(i)] for i in range(96,120)])
def roundsegs(s):return {tuple(tuple(round(c,10) for c in p) for p in pair) for pair in s}
assert roundsegs(true)==roundsegs(actual_B)
assert roundsegs(mirror)==roundsegs(actual_D)
write(HERE/'Plane362'/'fresh_discrete_math.json',{'exact_source_segment_count':24,'source_digits':'2008','true_matrix':[[1,0],[0,-1]],
 'true_full_segment_set_matches_B':True,'true_result':'5008','false_horizontal_mirror_full_segment_set_matches_D':True,'false_result':'8005',
 'source_handed_segments':{'o1':ob['o1'],'o3':ob['o3']},'target_handed_segments':{'o116':ob['o116'],'o118':ob['o118']}})

refs=[]
for p in sorted(BASE.glob('batch_*/manifest.json')):
    d=json.loads(p.read_text(encoding='utf-8-sig'))
    for c in d['candidates']:
        refs.append({'batch':p.parent.name,'manifest_sha256':file_hash(p),**{k:c.get(k) for k in ['question_id','mechanism','expected_wrong_answer','tested_final_answers','original_control_answers','quality_review']}})
write(HERE/'readonly_delivery_reference_audit.json',{'all_nine_batches_read':True,'candidates':refs,
 'principle_transferred':'Match actual source features, groups or end identities to a concrete wrong geometric operation; full uniform answer salience is insufficient. Controls and two-call samples do not establish causality.'})
print(json.dumps({'discrete_proofs':['Plane159','Plane203','Plane362'],'delivery_references':refs},ensure_ascii=False))
