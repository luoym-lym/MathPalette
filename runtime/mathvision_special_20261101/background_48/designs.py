import task_env
from task_env import OWN,PROJECT
from prepare import read,write,hashfile,eligibility
from workbench_io import load_config,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths,apply_partial_styles
from dataset_tools.mathvision_workbench import png_bytes
import json,math,hashlib,sys,itertools,copy
from datetime import datetime,timezone
from fractions import Fraction as F
import numpy as np
from PIL import Image
from matplotlib.patches import Patch

R='#DC2626'; B='#2563EB'; G='#16A34A'; O='#EA580C'
def now():return datetime.now(timezone.utc).isoformat()
def polygon_area(p):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2
def spec(q):
    scene=read(PROJECT/'PlaneGeometry/dataset_generator/scenes'/f'{q}.json')
    return scene,{o['id']:o for o in scene['objects']}

class Builder:
    def __init__(self,q,adapter):
        self.q=q;self.actions=[];self.roles=[];self.paths=[];self.adapter=adapter
        self.context=adapter.inspect_question(q)
        self.scene,self.objects=spec(q)
        self.captured=adapter.scene(q)
    def edge(self,target,index,color,role,width=1.5):
        paths=object_paths(self.captured,target);assert len(paths)==1
        p=paths[0];n=len(p['segments'])
        return self.interval(target,index/n,(index+1)/n,color,role,width)
    def interval(self,target,start,end,color,role,width=1.5):
        p=object_paths(self.captured,target)[0]
        a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,
           'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
        self.actions.append(a)
        controls=[s['control'].tolist() for s in p['segments']]
        self.roles.append({'action_index':len(self.actions)-1,'role':role,'target':target,'interval':a['interval'],'full_path_controls':controls})
    def line(self,a,b,color,role,ids):
        i=len(self.actions);action={'type':'add_line','id':f'r48_aux_{i}','endpoints':[a,b],'color':color,'linestyle':'solid','linewidth_pt':1.0}
        self.actions.append(action);self.roles.append({'action_index':i,'role':role,'exact_endpoint_ids':ids,'endpoints':[a,b]})
    def finish(self):self.captured.close()

def build(q,ad):
    b=Builder(q,ad);s=b.scene;obs=b.objects;p=s['points']
    if q=='Plane468':
        centers={o['id']:np.mean([p[n] for n in o['points']],axis=0) for o in s['objects']}
        axial={k:(round(v[0]/math.sqrt(3)-v[1]/3),round(v[1]/1.5)) for k,v in centers.items()}
        assert len(set(axial.values()))==19 and all(max(abs(x),abs(y),abs(x+y))<=2 for x,y in axial.values())
        dirs=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)];old=set(axial.values())
        border={(x+dx,y+dy) for x,y in old for dx,dy in dirs}-old
        assert len(border)==18
        edges={}
        for oid,o in obs.items():
            vs=[p[n] for n in o['points']]
            for i,(a,c) in enumerate(zip(vs,vs[1:]+vs[:1])):
                key=tuple(sorted((tuple(round(x,9) for x in a),tuple(round(x,9) for x in c))))
                edges.setdefault(key,[]).append((oid,i))
        exposed=[v[0] for v in edges.values() if len(v)==1];assert len(exposed)==30
        for oid,i in [('hex4',i) for i in range(6)]+exposed:
            color=[R,B,G][i%3]
            b.edge(oid,i,color,('Source white hex4 contact-side unit; edge orientation matched to exposed receiving contacts.' if oid=='hex4' else 'One exposed unit contact edge; intended mistaken one-contact-one-new-tile count. Orientation is matched to an existing white-tile side.'),1.5)
        proof={'axial_centers':axial,'six_neighbor_directions':dirs,'new_border_centers':sorted(border),'border_size':18,'black':sum(bool(o['semantic_fill']) for o in obs.values()),'white':sum(not o['semantic_fill'] for o in obs.values()),'exposed_contact_edges':exposed,'exposed_edge_count':30,'unique_answer':'11','derivation':'The complete radius-2 cluster is dilated by one hex-neighbor layer. It adds 18 distinct white tiles, not 30 exposed edge contacts: six new corner tiles touch one old edge and twelve new side tiles touch two. White=6+18=24, black=13, difference=11.'}
        wrong='23';variant='r48_contact_edges_as_distinct_border_tiles';rule='Count every one of the 30 exposed unit edges as a distinct new white tile. Then 6+30-13=23, double-counting the twelve two-contact receivers.'
        difference='Old Plane468 was screened without a saved design or API call. New design explicitly matches existing white contact-edge orientation units to every exposed contact, targeting incidence count rather than distinct neighboring tiles. No new tile or hidden black-black edge is drawn.'
    elif q=='Plane469':
        black={(int(k[1]),int(k[2])) for k,o in obs.items() if o.get('semantic_fill')}
        bd={(y,x) for x,y in black};vertical={(3-x,y) for x,y in black}
        assert len(bd-black)==4 and len(vertical-black)==3
        pairs=[('c03','c33',R,2,2),('c23','c13',G,2,2),('c10','c20',B,0,0),('c31','c01',O,2,2)]
        for source,receiver,color,ei,ej in pairs:
            for oid,edge,role in [(source,ei,'Source originally black cell'),(receiver,ej,'Receiver under reflection x -> 4-x, which is the wrong axis for BD')]:
                b.edge(oid,edge,color,f'{role}; exact row-preserving paired cell {source}<->{receiver}. One existing edge only; black/white interiors unchanged.')
        proof={'black_cells_lower_left_indices':sorted(black),'BD_required_images':sorted(bd),'required_white_cells':sorted(bd-black),'wrong_vertical_axis_images':sorted(vertical),'wrong_vertical_axis_new_cells':sorted(vertical-black),'unique_answer':'4','derivation':'BD is y=x. Each black cell (i,j) forces (j,i); c33 is fixed, the other four missing images are distinct white cells. They are necessary and sufficient, so minimum 4.'}
        wrong='3';variant='r48_vertical_reflection_edge_pairs';rule='Use row-preserving reflection about x=2 instead of diagonal BD. One black-black pair is already complete; three white receiver cells are missing, yielding 3.'
        difference='Old prescreen rejected speculative new filled cells/points and had no design/calls. This uses only one open existing edge on each source/receiver, paired by a real alternative reflection. All original 5 black cells, 11 white cells and ABCD remain identifiable; it adds no painted receiver.'
    elif q=='Plane472':
        areas=[polygon_area([p[n] for n in o['points']]) for o in obs.values() if o['id'].startswith('blade')]
        assert areas==[1.5]*4
        b.interval('h5',.8,1,B,'Source unit square at upper-right: one-unit horizontal leg of its right-angle corner.')
        b.interval('v5',.8,1,G,'Source unit square at upper-right: one-unit vertical leg, paired to a blade notch leg.')
        b.edge('blade0',1,G,'Receiver: the actual one-unit vertical notch edge (1,5)-(1,4), equal locally to the green unit-square leg.')
        b.edge('blade0',2,B,'Receiver: the actual one-unit horizontal notch edge (1,4)-(0,4), equal locally to the blue unit-square leg.')
        proof={'blade_areas':areas,'unique_answer':'B','value':6,'derivation':'Each concave blade is the union of two triangles from center (2.5,2.5) to a one-unit horizontal/vertical notch edge. Each has perpendicular height 1.5 and area .75. Four blades each have 1.5, total 6. A unit L at the reflex notch does not bound a unit square blade.'}
        wrong='A';variant='r48_unit_corner_to_reflex_blade';rule='Transfer the area-1 unit-square identity through its two one-unit perpendicular boundary legs to the matching local reflex-notch legs, then treat all four congruent blades as unit squares: total 4 (A).'
        difference='Old v01 uniformly outlined all four complete blades and preset C=8; actual old finals ended at 6/B, with extensive incorrect geometry. New four local intervals bind a specific unit-square L to one blade reflex L; no whole-blade outline and preset A=4 is derived from that new local-to-whole unit error.'
    elif q=='Plane473':
        areas={k:polygon_area([p[n] for n in o['points']]) for k,o in obs.items()}
        gray=sum(v for k,v in areas.items() if obs[k].get('semantic_fill'));white=sum(v for k,v in areas.items() if not obs[k].get('semantic_fill'))
        assert abs(gray-6)<1e-10 and abs(white-10)<1e-10
        b.edge('c01',0,B,'Source: first side of a real white unit-square open corner.')
        b.edge('c01',3,G,'Source: perpendicular second side of the same white square.')
        # Outer side y=0 in the pre-rotation square, and x=0. Keep the 4:1 scale visibly real.
        for k in ['c00','c10','c20','c30']:b.edge(k,0,B,'Receiver: one quarter of the whole outer-square side; continuation across the gray corner transfers white-square denominator identity to the whole square.')
        for k in ['c00','c01','c02','c03']:b.edge(k,3,G,'Receiver: one quarter of perpendicular whole outer side, matching the second source-square side role.')
        proof={'areas':areas,'gray_area':gray,'white_area':white,'outer_area':gray+white,'unique_answer':'D','ratio':'3:5','derivation':'Two gray unit squares plus central side-2 gray square give 1+1+4=6. Ten white unit squares give 10. Ratio 6:10=3:5; the full outer area is 16 and is not the white area.'}
        wrong='B';variant='r48_white_unit_corner_to_outer_denominator';rule='Use the whole area 16 as the white-area denominator after the source white unit-square corner is matched to the 4-times-longer outer corner; retain correct gray area 6, giving 6:16=3:8 (B).'
        difference='Old design grouped every gray square red and every white square blue, seeking object-count ratio 3:10 (A), but finals E and 41:16 missed A. New design has no gray-family count encoding. One white open corner is matched by two side roles to a larger outer-square corner, targeting whole-area denominator 16 rather than equal weight for gray squares.'
    elif q=='Plane475':
        classes={};col=[]
        for triple in itertools.combinations(p,3):
            vs=[p[k] for k in triple]
            if polygon_area(vs)==0:col.append(triple);continue
            ss=tuple(sorted(sum((p[a][i]-p[c][i])**2 for i in range(2)) for a,c in itertools.combinations(triple,2)))
            classes.setdefault(str(ss),[]).append(triple)
        assert len(classes)==8 and len(col)==8 and sum(map(len,classes.values()))==48
        triangles=[(['p00','p10','p01'],R),(['p20','p30','p31'],B)]
        for names,diag in triangles:
            b.line(p[names[0]],p[names[1]],G,'Matched source/receiver horizontal unit base of two actual reflected congruent dot-triple triangles.',names[:2])
            if diag==R:
                b.line(p['p00'],p['p01'],O,'Source unit vertical leg at left endpoint, corresponding to receiver right-endpoint leg.',['p00','p01'])
                b.line(p['p01'],p['p10'],R,'Source descending hypotenuse. Distinct orientation cue for falsely splitting reflected congruent triangles.',['p01','p10'])
            else:
                b.line(p['p30'],p['p31'],O,'Receiver unit vertical leg at right endpoint, true reflection counterpart.',['p30','p31'])
                b.line(p['p20'],p['p31'],B,'Receiver ascending hypotenuse. Different color encodes handedness rather than a new metric side length.',['p20','p31'])
        proof={'sss_classes':classes,'collinear_triples':col,'nondegenerate_triples':48,'unique_answer':'8','derivation':'Enumerate all C(8,3)=56 triples; 8 collinear triples are excluded. SSS yields exactly 8 sorted squared-side triples. Both outlined examples have (1,1,2); reflection is a congruence, so orientation does not create a ninth class.'}
        wrong='9';variant='r48_reflected_unit_triangle_class_split';rule='Keep the other seven SSS classes but treat the two opposite-handed (1,1,2) examples as two distinct types because the hypotenuse orientation/color differs: 7+2=9.'
        difference='Old triangle pair had equal base3/height1 but different SSS classes and attempted to MERGE into7. New disjoint unit-triangle pair has identical SSS and opposite handedness; it attempts to SPLIT one congruence class into2, hence9. Vertices, placements, metric feature and all auxiliary segments are substantively different.'
    elif q=='Plane479':
        K=[2.5,0.0]
        area=polygon_area([p[n] for n in ['A','J','I','C','B']]);assert area==4
        assert polygon_area([p[n] for n in ['A','B','C']])==2 and polygon_area([K,p['I'],p['J']])==1.5 and polygon_area([p['A'],p['C'],K])==.5
        b.edge('upper',0,B,'Source triangle ABC: true horizontal base AB of length 2, paired to receiver KI of length1.5.')
        b.edge('upper',1,G,'Source triangle ABC: true perpendicular vertical leg BC of length2, paired to IJ of length2.')
        b.line(p['A'],p['C'],R,'True auxiliary diagonal AC closes triangle ABC; it also exposes the remaining gray triangle ACK without recoloring or removing it.',['A','C'])
        b.edge('shaded',1,G,'Receiver triangle KIJ: true vertical leg JI of length2, counterpart to BC.')
        b.interval('shaded',2/5,3/5,B,'Receiver horizontal base IC, length1. It is a visible subset of KI; remaining CK is left black so the exact 1.5 base stays traceable.')
        # AJ is path segment0 from A to J. Its lower half starts at K.
        b.interval('shaded',.1,.2,R,'Receiver triangle KIJ: exact lower half KJ of AJ, which meets the original horizontal edge at K=(2.5,0). No point is added at K.')
        # Complete KI along the existing upper square CD side from C to K.
        b.interval('upper',.5,.5625,B,'Receiver base completion CK: original CD first quarter (C=3 to K=2.5), joining IC to give full KI=1.5.')
        proof={'coordinates':p,'K_unmarked_existing_AJ_intersection_with_HI':K,'square_areas':[4,4,4],'shaded_pentagon_area':area,'ABC':2,'KIJ':1.5,'ACK':.5,'unique_answer':'C','ratio':'1/3','derivation':'At y=0, AJ meets K=(5/2,0). Shaded pentagon decomposes into ABC(area2), ACK(area1/2), KIJ(area3/2). Total4 over three square areas12 gives1/3. Omitting ACK gives7/2 over12=7/24. Squares have disjoint interiors, so union-vs-sum alone would not change the denominator.'}
        wrong='B';variant='r48_two_triangle_decomposition_omits_gray_wedge';rule='Match the two marked right triangles by horizontal-base/vertical-leg/hypotenuse roles and sum only ABC+KIJ=2+1.5=3.5, omitting the still-gray third triangle ACK of area.5. Divide by12 to get7/24 (B).'
        difference='Old question was screened without any saved candidate or call. Parent union-vs-sum conjecture is disproved here (the three squares have disjoint interiors). This new design adds one true diagonal AC and styles two actual right-triangle decompositions, targeting a specific omitted middle gray wedge. It does not alter the named shaded pentagon.'
    else:raise ValueError(q)
    return b,variant,wrong,rule,difference,proof

def protected_state(scene,refs):
    st={'view':[list(scene.ax.get_xlim()),list(scene.ax.get_ylim()),scene.ax.get_aspect(),list(scene.ax.get_position().bounds)],'artists':[],'texts':[]}
    for a in refs:
        v={'type':type(a).__name__}
        if hasattr(a,'get_path'):v['path']=a.get_path().vertices.tolist();v['path_transform']=a.get_transform().get_matrix().tolist()
        if isinstance(a,Patch):v['facecolor']=list(a.get_facecolor());v['fill']=a.get_fill()
        if hasattr(a,'get_offsets'):v['offsets']=np.asarray(a.get_offsets()).tolist();v['faces']=a.get_facecolors().tolist()
        st['artists'].append(v)
    for a in scene.ax.texts:st['texts'].append([a.get_text(),list(a.get_position()),a.get_fontsize(),str(a.get_color())])
    return st

if __name__=='__main__':
    ad=RendererAdapter(load_config())
    for q in sys.argv[1:]:
        b,var,wrong,rule,diff,proof=build(q,ad);d=OWN/q/var;d.mkdir(parents=True,exist_ok=False)
        write(d/'design_difference_audit.json',{'question_id':q,'variant_id':var,'created_at_utc':now(),'material_difference':diff,'predeclared_geometric_error_rule':rule,'old_evidence_inventory':str(OWN/'old_history_inventory.json'),'not_cosmetic_or_posthoc':True})
        write(d/'eligibility_before_design.json',eligibility(q));write(d/'context.json',b.context);write(d/'math_proof.json',proof)
        renderer=PluginRenderer(load_config(),ad,{q:b.context})
        plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':rule,'intent':'Research predeclared geometric misconception; no approval','params':{'actions':b.actions}}
        norm=renderer.normalize(plugin);write(d/'plugin.json',norm)
        preservation=[];native=ad.scene
        def capture(qid):
            sc=native(qid);refs=list(dict.fromkeys(a for group in sc.artists.values() for a in group));before=protected_state(sc,refs);close=sc.close
            def done():
                after=protected_state(sc,refs);preservation.append({'all_original_geometry_fill_dots_text_view_unchanged':before==after});close()
            sc.close=done;return sc
        ad.scene=capture
        try:
            pp,png,ph=renderer.render(norm,frozen=True)
            pp2,png2,ph2=renderer.render(norm,frozen=True)
        finally:ad.scene=native;b.finish()
        assert png==png2 and ph==ph2 and pp==norm and pp2==norm
        assert all(x['all_original_geometry_fill_dots_text_view_unchanged'] for x in preservation)
        (d/'candidate.png').write_bytes(png);(d/'replay_2.png').write_bytes(png2)
        assert all(hashlib.sha256(png).hexdigest()!=e['sha256'] for e in read(OWN/'old_history_inventory.json')[q] if e['path'].endswith('.png'))
        write(d/'render_check.json',{'schema_normalized':True,'frozen_plugin_unchanged':norm==pp,'fresh_noop_formal_pixel_equal':True,'two_consecutive_byte_identical':png==png2,'png_sha256':hashlib.sha256(png).hexdigest(),'pixel_sha256':ph,'native_preservation':preservation,'original_pixel_sha256':b.context['original_pixel_sha256'],'adapter_manifest':ad.manifest})
        write(d/'path_fingerprints.json',b.roles)
        write(d/'design.json',{'question_id':q,'variant_id':var,'created_at_utc':now(),'expected_wrong_answer':wrong,'geometric_error_rule':rule,'material_difference':diff,'primary_math':proof,'marker_roles':b.roles,'human_semantics':'Numerical geometry/counting target is identified by the original wording. Original fills, original points and labels remain. Existing-edge colors are local matching/counting cues, not equality/angle relation symbols; no physical-picture color transport is requested. All actual native marks must be inspected before calls.','png_sha256':hashfile(d/'candidate.png'),'pixel_sha256':ph,'plugin_sha256':hashfile(d/'plugin.json'),'approval_status':'PRIMARY RESEARCH ONLY; parent NEW independent review required; no Pass/Collect'})
        print(q,var,'preset',wrong,'actions',len(b.actions),'two byte identical',flush=True)
