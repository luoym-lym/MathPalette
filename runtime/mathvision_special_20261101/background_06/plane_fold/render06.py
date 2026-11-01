from tools06 import *
from partial_style import object_paths
import copy
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
def style(target,color=RED,width=1.5):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
def path_record(p):return {'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]}
def interval_action(target,path,start,end,color=RED,width=1.5):
    return dict(style(target,color,width),interval={'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False})
def render(qid,vid,spec):
    check=eligibility(qid);assert check['eligible'],check
    cfg,ad=adapter();before=inputs(ad,qid);m=ad.inspect_question(qid);renderer=PluginRenderer(cfg,ad,{qid:m})
    scene=ad.scene(qid);bindings=[];actions=[]
    try:
        scene.fig.canvas.draw()
        for entry in spec['marks']:
            if 'snap_point' in entry:
                source=next(p for p in m['snap_points'] if p['id']==entry['snap_point'])
                action={'type':'add_point','id':entry['id'],'xy':copy.deepcopy(source['xy']),'color':entry.get('color',RED)}
                actions.append(action);bindings.append({'action_index':len(actions)-1,'action':copy.deepcopy(action),'role':entry['role'],'source_snap_point':source})
                continue
            target=entry['target'];paths=object_paths(scene,target);path=paths[entry.get('path_index',0)]
            action=interval_action(target,path,*entry['interval'],entry.get('color',RED),entry.get('width',1.5)) if 'interval' in entry else style(target,entry.get('color',RED),entry.get('width',1.5))
            actions.append(action);bindings.append({'action_index':len(actions)-1,'action':copy.deepcopy(action),'role':entry['role'],'source_object':next(o for o in m['objects'] if o['id']==target),'paths':[path_record(p) for p in paths]})
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':spec['mechanism'],'intent':'Predeclared wrong answer '+spec['wrong'],'params':{'actions':actions}}
    norm,data,pixels=renderer.render(plugin);norm2,data2,pixels2=renderer.render(norm,frozen=True)
    assert data==data2 and norm==norm2 and pixels==pixels2 and before==inputs(ad,qid)
    folder=HERE/qid/vid;folder.mkdir(parents=True,exist_ok=False)
    write(folder/'context.json',m);write(folder/'eligibility_before_design.json',check);write(folder/'exact_marker_bindings.json',bindings)
    write(folder/'plugin.json',norm);(folder/'candidate.png').write_bytes(data)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':spec['wrong'],'correct_answer':ad.records[qid]['answer'],'created_at':datetime.now(timezone.utc).isoformat(),'mechanism':spec['mechanism'],'mathematical_solution':spec['math'],'marker_roles':[b['role'] for b in bindings],'human_gate':spec['human_gate'],'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_SECOND_REVIEW','limits':spec.get('limits',[])})
    write(folder/'render_check.json',{'baseline_pixel_match':True,'schema_normalized':True,'two_byte_identical_redraws':True,'pixel_sha256':pixels,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'no_source_writes':True})
    print(str(folder),flush=True)

SPEC203={
'wrong':'C',
'mechanism':'The three original lower grey cells form an L. Red existing borders bind that input L to a copy translated four columns right, instead of reflected in the black fold x=3. This specific false source-to-destination correspondence covers E and leaves C uncovered. The true reflected lower L covers C and leaves E uncovered. All marks are existing cell borders, without new fills or text.',
'math':'Use cells (column,row) from the lower-left corner. The grey cells are (1,3),(2,3),(2,2),(0,1),(1,1),(0,0). Reflection in x=3 sends column c to5-c, preserving row, so destinations are (4,3),(3,3),(3,2),(5,1),(4,1),(5,0). Letter positions are A=(3,3), B=(4,3), C=(5,0), D=(4,1), E=(4,0). A/B/C/D are covered; E alone is not. No colored border changes the grey set, the fold, or a letter coordinate, so E remains unique. The false translation targets (4,1),(5,1),(4,0) for the lower L and incorrectly omits C.',
'human_gate':'Six grey cells remain distinctly filled. The black thick fold atx=3 is untouched and visibly distinct. Every letter remains black, unobscured in its cell. Red borders use only the existing grid and grey-square outlines; no squarefill or new gridline is added. The three-cell counts, cell adjacency and distances from the fold remain readable.',
'limits':['No original control or statistical marker ablation. Any two wrong calls would establish only this frozen candidate possibility, pending NEW independent second review.'],
'marks':[
{'target':'o16','role':'Source lower-L upper-left grey cell(0,1): red outline identifies this member of the three-cell translated part.'},
{'target':'o17','role':'Source lower-L upper-right grey cell(1,1): red outline identifies the horizontal arm of the translated part.'},
{'target':'o18','role':'Source lower-L bottom grey cell(0,0): red outline is falsely bound to E cell(4,0), the decisive translation-versus-reflection error.'},
{'target':'o4','interval':[0,2/5],'role':'Red x=4 grid interval y0..2 is the left boundary of both falsely translated left cells, including E.'},
{'target':'o5','interval':[0,2/5],'role':'Red x=5 grid interval y0..2 closes E on the right and divides the two upper cells of the falsely translated L.'},
{'target':'o6','interval':[1/5,2/5],'role':'Red x=6 grid interval y1..2 closes the falsely translated upper-right cell.'},
{'target':'o7','interval':[4/6,5/6],'role':'Red y=0 grid interval x4..5 is the bottom edge of the false E destination for source(0,0).'},
{'target':'o8','interval':[4/6,1],'role':'Red y=1 grid interval x4..6 closes both upper translated cells and the top of the E destination.'},
{'target':'o9','interval':[4/6,1],'role':'Red y=2 grid interval x4..6 is the top boundary of the falsely translated horizontal arm.'}
]}
if __name__=='__main__':
    if sys.argv[1]=='Plane203':render('Plane203','lower_L_translation_binding',SPEC203)
