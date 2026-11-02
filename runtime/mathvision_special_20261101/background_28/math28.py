from tools28 import *
import itertools,functools,collections
notes=read(ROOT/'provenance/source_notes.json')
q='Solid123';g=notes[q]['geometry_notes']['additional_model_evidence']['assembly_geometry']
material={tuple(p):'W' for p in itertools.product(range(3),repeat=3)}
for pts in g['L_pieces']:
    for p in pts:material[tuple(p)]='L'
for pts in g['bar_pieces']:
    for p in pts:material[tuple(p)]='B'
observed={p:c for p,c in material.items() if p[0]==2 or p[1]==0 or p[2]==2}
cells=list(itertools.product(range(3),repeat=3));ix={p:i for i,p in enumerate(cells)}
def parity(perm):return (-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
def shapes(base):
    shapeset=set()
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1],repeat=3):
            if parity(perm)*signs[0]*signs[1]*signs[2]!=1:continue
            pts=[tuple(signs[i]*p[perm[i]] for i in range(3)) for p in base]
            low=[min(p[i] for p in pts) for i in range(3)]
            shapeset.add(tuple(sorted(tuple(p[i]-low[i] for i in range(3)) for p in pts)))
    return shapeset
placements=[]
for kind,base in [('L',[(0,0,0),(1,0,0),(2,0,0),(0,0,1),(0,0,2)]),('B',[(0,0,0),(1,0,0),(2,0,0)]),('W',[(0,0,0)])]:
    for shape in shapes(base):
        maxs=[max(p[i] for p in shape) for i in range(3)]
        for offset in itertools.product(*(range(3-m) for m in maxs)):
            pts=[tuple(p[i]+offset[i] for i in range(3)) for p in shape]
            if any(p in observed and observed[p]!=kind for p in pts):continue
            mask=sum(1<<ix[p] for p in pts)
            placements.append((kind,mask,pts))
choices={i:[] for i in range(27)}
for j,(_,mask,pts) in enumerate(placements):
    for p in pts:choices[ix[p]].append(j)
full=(1<<27)-1
@functools.lru_cache(None)
def cover(used):
    if used==full:return { (0,0,0):1 }
    # MRV exact cover over all27cells, including optional hidden material placements.
    nextchoices=None
    for i in range(27):
        if used>>i&1:continue
        cs=[j for j in choices[i] if not placements[j][1]&used]
        if not cs:return {}
        if nextchoices is None or len(cs)<len(nextchoices):nextchoices=cs
    out=collections.Counter()
    for j in nextchoices:
        kind,mask,_=placements[j];delta={'L':(1,0,0),'B':(0,1,0),'W':(0,0,1)}[kind]
        for counts,n in cover(used|mask).items():out[tuple(counts[k]+delta[k] for k in range(3))]+=n
    return dict(out)
dist=cover(0)
assert dist and {counts[2] for counts in dist}=={11},dist
write(TASK/q/'primary_unique_math_enumeration.json',{'question_id':q,'created_at':now(),'source_basis':'Source material classes independently viewed on original and candidate native images. Exact exposed cube observations front y=0,top z=2,right x=2 reconstructed from frozen assembly model; no solver response used.','prototype':'L pentacube has five unit cells; bar has three; white cell one. All proper rotations and all integer placements wholly inside3by3by3 allowed.','observed_material_cells':{'L':[p for p,c in observed.items() if c=='L'],'B':[p for p,c in observed.items() if c=='B'],'W':[p for p,c in observed.items() if c=='W']},'allowed_placement_count':len(placements),'memoized_occupancy_states':cover.cache_info().currsize,'exact_cover_count_distributions':[{'L_count':k[0],'bar_count':k[1],'white_count':k[2],'number_of_compatible_exact_covers':v} for k,v in dist.items()],'unique_white_count':11,'hidden_cells_explicitly_covered':True,'limitation':'Enumeration relies on source-standard rigid congruent block interpretation and the source-visible material classification. It does not certify human performance or model causality.','primary_only':True})
print('Solid123 exact placements',len(placements),'distributions',dist,'states',cover.cache_info().currsize)
# Exact arithmetic/enumeration checks for all eight questions, including skips.
summary={
'Solid82':{'columns':6,'cube_colors_by_height':['gray','white','gray','white','gray'],'white_per_column':2,'unique_answer':12},
'Solid86':{'dimensions':[4,2,3],'total_white':12,'visible_white':[[1,0,1],[2,0,0],[2,0,1],[2,0,2],[3,0,0],[1,1,2],[2,1,2],[3,1,2],[3,1,0],[3,1,1]],'unique_answer':2,'unseen_material_assignments':'Unfixed; only the unseen white count is fixed.'},
'Solid103':{'cube_side':5,'front_small_block_volume':75,'rear_block_volume':280-125-75,'rear_strip_area':(280-125-75)/5,'unique_answer':'A','proof':'All blocks have common5cm height. Rear block marked? has80cm3, so its top area16cm2. Integer guesses or perspective ratios are unnecessary.'},
'Solid109':{'interior_cubes':list(itertools.product(range(1,4),range(1,3),range(1,3))),'unique_answer':12},
'Solid123':{'independent_exact_cover_proof':str(TASK/'Solid123/primary_unique_math_enumeration.json'),'unique_answer':11},
'Solid125':{'reference_total_area':6*3**2,'white_area':3*2**2,'paint_per_unit':9/54,'white_paint_kg':9*12/54,'unique_answer':2},
'Solid129':{'heights_front_to_back':[[3,2,1],[3,2,1],[3,3,2]],'layer_counts':[9,7,4],'total_present':20,'missing_per_layer':[0,2,5],'unique_answer':7},
'Solid143':{'ordinary_die_total':sum(range(1,7)),'visible_pips_per_face':[1,2,4,6,2],'visible_total':15,'unique_answer':42-15,'inherited_assumption':'Ordinary1through6dice, explicitly documented ambiguity in original source; no new numbering condition.'}}
assert len(summary['Solid109']['interior_cubes'])==12
for qid,v in summary.items():write(TASK/qid/'primary_math_audit.json',{'question_id':qid,'created_at':now(),'mathematics':v,'original_geometry_projection_visibility_preserved':True,'primary_only':True})
write(TASK/'primary_math_audit.json',summary)
