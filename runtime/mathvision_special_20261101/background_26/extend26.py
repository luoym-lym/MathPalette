from prepare26 import *
def add_history(q,vid,manual_finals):
    prior=read(HERE/q/'prior_history_audit.json');out=HERE/q/vid;d=read(out/'design.json')
    results=[]
    for p in out.glob('tests/*/run_*_response.json'):
        raw=read(p);results.append({'path':str(p.relative_to(ROOT)),'sha256':file_hash(p),'full_raw_response':raw,'full_final_content':raw['choices'][0]['message']['content']})
    assert len(results)==2 and (out/'api_process_finished.json').exists()
    prior['history'].append({'variant_id':vid,'candidate':str(out.relative_to(ROOT)),'preset':d['expected_wrong_answer'],'full_design':d,'full_plugin':read(out/'plugin.json'),'manual_final_answers':manual_finals,'raw_responses':results,'primary_review':read(out/'primary_review_before_calls.json'),'actual_native_image_read':True,'all_files_sha256':{str(p.relative_to(ROOT)):file_hash(p) for p in out.rglob('*') if p.is_file()}})
    filename='prior_history_before_second_design.json';write(HERE/q/filename,prior);return filename
def second252():
    q='Plane252';prior=add_history(q,'r26_optimal_six_joint_correspondence',['8','4']);s=native(q);oo={o['id']:o for o in s['objects']};actions=[];roles=[]
    for k in [0,1]:
        for j in range(8):
            oid=f'wire{k}_{j}';a,b=pts(s,oo[oid]);horizontal=a[1]==b[1]
            actions.append(whole(oid,R if horizontal else B));roles.append(f'{oid}: actual unit '+('horizontal' if horizontal else 'vertical')+' segment belongs to the red horizontal / blue vertical orientation family. Its same-color partners in both wires group current directions, inviting refusal to match red to blue after a quarterturn; no orientation constraint is actually given.')
    w=[[tuple(map(tuple,pts(s,oo[f'wire{k}_{j}']))) for j in range(8)] for k in [0,1]];edge=lambda a,b:tuple(sorted((tuple(a),tuple(b))))
    aa={edge(*e) for e in w[0]};by_orientation=[]
    for refl in [-1,1]:
        for rot in range(4):
            def f(p):
                x,y=p;x*=refl
                for _ in range(rot):x,y=-y,x
                return x,y
            bb=[(f(a),f(b)) for a,b in w[1]];best=0
            for dx in range(-12,13):
                for dy in range(-12,13):best=max(best,len(aa&{edge((a[0]+dx,a[1]+dy),(b[0]+dx,b[1]+dy)) for a,b in bb}))
            by_orientation.append({'reflection':refl,'quarter_turns':rot,'maximum_length':best,'keeps_horizontal_and_vertical_classes':rot%2==0})
    locked=max(a['maximum_length'] for a in by_orientation if a['keeps_horizontal_and_vertical_classes']);assert locked==4
    make(q,'r26_current_direction_family_lock','4',actions,'Group every existing horizontal unit red and every existing vertical unit blue in both wires. Predict4 by treating current direction classes as fixed matching identities and disallowing the quarterturn that exchanges red-horizontal and blue-vertical directions.', 'Prior current design marked six joints in a REAL optimal5-edge chain and targeted counting vertices as length6, returning8/4. It remains failed. This new design leaves all joints black and instead colors all sixteen original unit EDGES by current orientation, targeting an orientation-lock constraint that reduces the geometric optimum from5 to4. It also differs from old selected U and incompatible local-run pairings; no old observed4 is adopted cosmetically.', 'Unrestricted rigid placement has maximum5 by a fresh D4/integer-translation enumeration and the explicit reflection-free witness T(x,y)=(2-y,x-5). A halfturn or translations alone can attain only4, as can the entire orientation-preserving color-class subgroup in the saved audit. A legitimate quarterturn exchanges current horizontal and vertical direction labels, which are annotations rather than physical constraints. All sixteen unit segments, eighteen joints and the permitted free relative placement remain unchanged, so correct5 is unique.',roles,{'maximum_by_D4_orientation':by_orientation,'unrestricted_maximum':5,'wrong_orientation_locked_maximum':4,'completeness':'Any positive-length coincidence requires parallel original lattice edges; for each orientation, maxima in translation occur at integer endpoint breakpoints. Enumerated -12..12 covers every intersecting envelope.'},prior)
def second408():
    q='Plane408';assert len(sys.argv)==4,'Provide both complete manually read final answers';prior=add_history(q,'r26_exposed_step_variation_binding',sys.argv[2:4]);actions=[];roles=[]
    specs=[('ribbon0_0',35,35,R),('ribbon0_1',60,60,B),('ribbon0_2',85,85,G),('ribbon1_0',85,60,R),('ribbon1_1',60,60,B),('ribbon1_2',110,35,G)]
    for oid,height,contact,color in specs:
        start=1/4;end=(1+contact/height)/4
        actions.append(part(q,oid,start,end,color));roles.append(f'{oid}: existing right-side internal gluing contact, y0..{contact}, colored by first/second/third seam position. These six contacts give totals180 and155; every colored interval is shared by two actual ribbon sides, so loss25 changes outer perimeter by TWICE25. No external step is colored.')
    make(q,'r26_shared_contact_single_count','C',actions,'Group the three actual shared ribbon-contact intervals in each arrangement by seam order. Predict C=25cm by subtracting shared-contact totals180-155 and forgetting that each internal contact removes two ribbon-side contributions from the outer perimeter.', 'Old design conserved ribbon identities using short top edges; the first r26 design compared exposed external steps and predicted75. Its exact full finals are retained in the prior-history audit. The new design removes ALL those marks and encodes only internal two-ribbon CONTACT intervals, a different geometric quantity and explicit factor-of-two cancellation error, with predeclared wrong25 rather than any retargeting to the observed output.', 'The sum of all four separate ribbon perimeters is unchanged. Joining removes both copies of each contact length: P_union=P_separate-2*S. Contact sums are first35+60+85=180, second60+60+35=155. Therefore P_second-P_first=2*(180-155)=50cm, B. Counting each contact only once gives25cm, C, the frozen wrong hypothesis. Source heights, overlaps, interfaces, all outer edges and four ribbons stay fixed.',roles,{'contact_arrays':[[35,60,85],[60,60,35]],'contact_sums':[180,155],'contact_difference':25,'two_sides_per_contact':2,'correct_perimeter_difference':50},prior)
if __name__=='__main__':
    if sys.argv[1]=='Plane252':second252()
    elif sys.argv[1]=='Plane408':second408()
