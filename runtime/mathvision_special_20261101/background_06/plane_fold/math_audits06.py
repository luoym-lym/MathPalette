from tools06 import *
from collections import Counter
qid='Plane165';m=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
source=Counter(o['id'].rsplit('_',1)[-1] for o in m['objects'] if o['id'].startswith('source') and not o['id'].endswith('_square'))
pieces={l:Counter(o['id'].rsplit('_',1)[-1] for o in m['objects'] if o['id'].startswith(f'option{i}_') and not o['id'].endswith('_square')) for i,l in enumerate('ABCDE')}
total=sum(pieces.values(),Counter());omissions={l:{k:total[k]-c[k] for k in source} for l,c in pieces.items()}
assert [l for l,v in omissions.items() if v==source]==['D']
cover={'A':[(0,0),(1,0),(0,1),(1,1)],'B':[(2,0),(2,1),(2,2),(1,2)],'C':[(0,2),(0,3),(1,3)],'E':[(3,0),(3,1),(3,2),(3,3),(2,3)]}
cells=[p for ps in cover.values() for p in ps];assert len(cells)==len(set(cells))==16
write(HERE/qid/'symbol_inventory_math_audit.json',{'source_symbol_counts':dict(source),'piece_counts':{l:dict(c) for l,c in pieces.items()},'remaining_counts_by_omission':omissions,'only_inventory_compatible_omission':'D','nonoverlapping_cell_cover':cover,'complete_source_cell_cover':True,'interpretation':'Symbols mark cell types; no new orientation/length/equality condition is introduced. Inventory already proves unique unused D from the stated premise that4pieces form the square.','source_fingerprints_path':str(HERE/qid/'input_fingerprints.json')})
qid='Plane203';grey={(1,3),(2,3),(2,2),(0,1),(1,1),(0,0)};folded={(5-x,y) for x,y in grey};letters={'A':(3,3),'B':(4,3),'C':(5,0),'D':(4,1),'E':(4,0)};uncovered=[l for l,p in letters.items() if p not in folded];assert uncovered==['E']
write(HERE/qid/'reflection_cell_math_audit.json',{'zero_based_lower_left_cells':True,'original_grey_cells':sorted(grey),'fold':'x=3;columnc→5−c,rowunchanged','folded_cells':sorted(folded),'letter_cells':letters,'unique_uncovered_letter':'E','candidate_marks_change_fills_or_fold':False,'wrong_translation_target_cells':[(4,1),(5,1),(4,0)]})
try:
 from shapely.geometry import Polygon
 import math
 m=json.loads((HERE/'Plane195/context.json').read_text(encoding='utf-8'));objects={o['id']:o['geometry']['points'] for o in m['objects']};h=math.sqrt(3)
 pairs={
  'A':[[(-1,0),(1,0),(0,h)],[(-1,2.0784609690826525),(1,2.0784609690826525),(0,2.0784609690826525-h)]],
  'B':[[(5,0),(5,2),(5-h,1)],[(5,0),(5,2),(5+h,1)]],
  'C':[[(10,0),(10,2),(10+h,1)],[(11.039230484541326,0),(11.039230484541326,2),(12.771281292110203,1)]],
  'D':[[(15,0),(15,2),(15+h,1)],[(15+h,0.5),(15+h,2.5),(15,1.5)]]}
 residuals={l:Polygon(pair[0]).union(Polygon(pair[1])).symmetric_difference(Polygon(objects['option'+str(i)])).area for i,(l,pair) in enumerate(pairs.items())}
 assert max(residuals.values())<1e-10
 write(HERE/'Plane195/explicit_card_union_audit.json',{'constructive_two_side2_equilateral_card_pairs':pairs,'source_outline_symmetric_difference_areas':residuals,'tolerance':1e-10,'convex_vertex_obstruction_for_E':'Any convex union vertex must survive from an original triangle and has60degrees. Edge-crossing union vertices are concave; E90degree convex corners cannot occur.','all_ABCD_constructions_match':True})
except ImportError:
 write(HERE/'Plane195/explicit_card_union_audit.json',{'shapely_available':False,'constructive_pairs_and_analytic_proof':'primary_prescreen.json','no_solver_call_or_source_change':True})
print('Math audits complete')
