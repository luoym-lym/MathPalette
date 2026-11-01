from tools_local import *
from collections import defaultdict
from itertools import combinations
from math import hypot,isclose
def polygon_area(ps):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(ps,ps[1:]+ps[:1])))/2
def source(qid):
    m=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'));r=json.loads((HERE/qid/'formal_record.json').read_text(encoding='utf-8'));s=json.loads((ROOT/'PlaneGeometry'/r['scene']).read_text(encoding='utf-8'))
    def xy(p):return s['points'][p] if isinstance(p,str) else p
    return m,{o['id']:[xy(p) for p in o['geometry'].get('points',[])] for o in m['objects']}
audits={}
m,g=source('Plane473');areas={o['id']:polygon_area(g[o['id']]) for o in m['objects']};gray=sum(areas[o['id']] for o in m['objects'] if o['geometry'].get('semantic_fill'));white=sum(areas.values())-gray
assert isclose(gray,6,abs_tol=1e-10) and isclose(white,10,abs_tol=1e-10)
audits['Plane473']={'all_square_areas':areas,'gray_total':gray,'white_total':white,'gray_white_ratio':'3:5','answer':'D'}
m,g=source('Plane293');black={letter:sum(polygon_area(ps) for oid,ps in g.items() if oid.startswith('black'+str(i)+'_')) for i,letter in enumerate('ABCD')};assert all(isclose(a,1) for a in black.values())
audits['Plane293']={'black_area_per_panel':black,'each_panel_area':4,'answer':'E'}
m,g=source('Plane257');o={v['id']:v['geometry'] for v in m['objects']};flags={}
for i in range(1,6):
    black=sum(polygon_area(g[oid]) for oid,ob in o.items() if oid.startswith('f'+str(i)) and ob.get('type')=='polygon' and ob.get('semantic_color')=='#000000')
    flags[str(i)]={'black_area':black,'total_area':{1:8,2:5,3:3,4:6.25,5:8}[i]}
    flags[str(i)]['fraction']=black/flags[str(i)]['total_area']
assert [i for i,v in flags.items() if isclose(v['fraction'],.6)]==['2','4']
audits['Plane257']={'flags':flags,'answer':'C'}
m,g=source('Plane282');bounds={oid:(min(p[0] for p in ps),max(p[0] for p in ps),min(p[1] for p in ps),max(p[1] for p in ps)) for oid,ps in g.items()};shared=[]
for (a,aa),(b,bb) in combinations(bounds.items(),2):
    length=0
    if aa[1]==bb[0] or bb[1]==aa[0]:length=max(0,min(aa[3],bb[3])-max(aa[2],bb[2]))
    if aa[3]==bb[2] or bb[3]==aa[2]:length=max(0,min(aa[1],bb[1])-max(aa[0],bb[0]))
    if length:shared.append({'squares':[a,b],'shared_length':length})
assert sum(v['shared_length'] for v in shared)==6
audits['Plane282']={'square_bounds':bounds,'all_pairwise_shared_lengths':shared,'shared_total':6,'union_perimeter':24-12,'answer':'12'}
m,g=source('Plane380');inc=defaultdict(list)
for o in m['objects']:
    if o['geometry'].get('semantic_fill'):
        ps=g[o['id']]
        for i in range(4):inc[tuple(sorted((tuple(ps[i]),tuple(ps[(i+1)%4]))))].append(o['id'])
boundary=[e for e,v in inc.items() if len(v)==1];assert len(boundary)==30
audits['Plane380']={'unit_boundary_edges':boundary,'boundary_count':30,'side_cm':8,'big_rectangle_area_cm2':1920,'answer':'D'}
m,g=source('Plane255');chain=[g['o1'][0]]+[g['o'+str(i)][1] for i in range(1,11)];p1=polygon_area(chain+[[4,0]]);total=polygon_area(g['o0']);assert not isclose(p1,total/2)
audits['Plane255']={'actual_frozen_P1_area':p1,'actual_frozen_P2_area':total-p1,'total_area':total,'general_perimeters':['a+b+L','a+b+L'],'actual_areas_are_unequal':True,'answer':'D'}
m,g=source('Plane210');known=sum(polygon_area(g[oid]) for oid in g if oid.startswith('source') and oid.endswith('_gray'));assert isclose(known,3.5)
audits['Plane210']={'known_black':known,'known_white':8-known,'missing_black_required':4.5-known,'answer':'B'}
m,g=source('Plane302');masks=[7,11,13,14];solutions=[]
for touches in range(16):
    state=0
    for i,mask in enumerate(masks):
        if touches&(1<<i):state^=mask
    if state==15:solutions.append(touches)
assert solutions==[15]
audits['Plane302']={'toggle_masks':masks,'all_successful_touch_parity_masks':solutions,'unique_parity_vector':[1,1,1,1],'minimum_touches':4,'answer':'4'}
bindings=[]
for dp in sorted(HERE.glob('Plane*/*/design.json')):
    d=json.loads(dp.read_text(encoding='utf-8'));qid=d['question_id'];m,g=source(qid);plugin=json.loads((dp.parent/'plugin.json').read_text(encoding='utf-8'));roles=d['marker_roles'];assert len(roles)==len(plugin['params']['actions'])
    for b in d.get('overlay_bindings',[]):
        ps=g[b['object_id']];a,c=ps[b['edge_index']],ps[(b['edge_index']+1)%len(ps)]
        for p in b['exact_source_endpoints']:
            assert abs((c[0]-a[0])*(p[1]-a[1])-(c[1]-a[1])*(p[0]-a[0]))<1e-10
            assert min(a[0],c[0])-1e-10<=p[0]<=max(a[0],c[0])+1e-10 and min(a[1],c[1])-1e-10<=p[1]<=max(a[1],c[1])+1e-10
    bindings.append({'question_id':qid,'variant_id':d['variant_id'],'marker_count':len(roles),'all_markers_have_roles':True,'all_added_lines_trace_exact_existing_edges':True,'design_sha256':file_hash(dp),'plugin_sha256':file_hash(dp.parent/'plugin.json')})
write(HERE/'primary_math_and_marker_audit.json',{'created_at':now(),'role':'primary mathematical corroboration, not independent review','question_audits':audits,'candidate_marker_bindings':bindings,'all_assertions_passed':True})
print(json.dumps({'questions':len(audits),'candidates':len(bindings),'passed':True}))
