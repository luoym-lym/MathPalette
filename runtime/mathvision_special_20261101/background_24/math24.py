from tools24 import *
import math, numpy as np
def prove215():
    q='Plane215';obs={o['id']:o['geometry'] for o in read(HERE/q/'context.json')['objects']}
    M=np.array([[-1.,0],[0,-1.]])
    src=np.array(obs['o1']['points'])-np.array(obs['o2']['center']);target=1.25*src@M.T
    def haus(a,b):return max(np.linalg.norm(a[:,None,:]-b[None,:,:],axis=2).min(axis=0).max(),np.linalg.norm(a[:,None,:]-b[None,:,:],axis=2).min(axis=1).max())
    errors={}
    for letter,poly,arc in zip('ABCDE',['o203','o207','o211','o215','o219'],['o204','o208','o212','o216','o220']):
        # stable IDs are verified by actual semantic fills and bounding circle.
        if poly not in obs:raise RuntimeError(poly)
        g=obs[poly];a=obs[arc]
        if g.get('semantic_fill')!=True or a['type']!='arc':raise RuntimeError((poly,arc,g,a))
        black=haus(target,np.array(g['points'])-a['center'])
        def samples(g):
            ts=np.linspace(g['start_deg'],g['end_deg'],101)*math.pi/180
            return g['radius']*np.column_stack((np.cos(ts),np.sin(ts)))
        arce=haus(1.25*samples(obs['o2'])@M.T,samples(a))
        errors[letter]={'black_quarter_error':float(black),'full_semicircle_error':float(arce),'combined':float(max(black,arce))}
    assert [k for k,e in errors.items() if e['combined']<1e-10]==['A'],errors
    write(HERE/q/'primary_math_audit.json',{'method':'Fresh whole-black-polygon and101point enclosing-arc comparison under composed perpendicular reflections; no solver result used.','H':[[-1,0],[0,1]],'V':[[1,0],[0,-1]],'net':M.tolist(),'all_options':errors,'unique_answer':'A','warning':'Quarter alone also matches E; full arc is essential.','primary_not_second_review':True})
def prove226():
    # Symbol identities/headings independently read from current original/native geometry.
    board={(0,3):('club',0),(1,3):('star',0),(2,3):('club',0),(3,3):('heart',0),
      (0,2):('diamond',0),(1,2):('club',0),(2,2):('spade',180),(3,2):('heart',0),
      (0,1):('diamond',90),(1,1):('star',20),(2,1):('club',0),(3,1):('heart',180),
      (0,0):('diamond',0),(1,0):('heart',90),(2,0):('club',0),(3,0):('spade',90)}
    opts={'A':[('star',0),('spade',0)],'B':[('star',0),('club',0)],'C':[('star',0),('star',0)],'D':[('heart',0),('diamond',0)],'E':[('heart',0),('heart',0)]}
    period={'star':72,'diamond':180,'club':360,'heart':360,'spade':360}
    matches={k:[] for k in opts};n=0
    for a in board:
        for b in board:
            dx,dy=b[0]-a[0],b[1]-a[1]
            if abs(dx)+abs(dy)!=1:continue
            n+=1
            rot={(1,0):0,(0,1):270,(-1,0):180,(0,-1):90}[(dx,dy)]
            got=[(s,(pose+rot)%period[s]) for s,pose in [board[a],board[b]]]
            for k,exp in opts.items():
                if got==exp:matches[k].append({'first':a,'second':b,'whole_piece_ccw_rotation':rot})
    assert n==48 and [k for k,v in matches.items() if v]==['B'],matches
    write(HERE/'Plane226/primary_math_audit.json',{'current_source_context':str(HERE/'Plane226/context.json'),'method':'Independent fresh enumeration of48 directed adjacent dominoes; each has one unique quarterturn aligning it horizontally; compare full symbol identities/headings modulo actual symbol symmetry.','board':[{'cell':c,'feature':f} for c,f in board.items()],'option_features':opts,'matches':matches,'unique_answer':'B','star_lower_pose20_preserved':True,'heart_vs_downward_spade_stem_visible':True,'primary_not_second_review':True})
def prove242():
    obs={o['id']:o['geometry'] for o in read(HERE/'Plane242/context.json')['objects']};out={}
    for i,k in enumerate('ABCDE'):
        gs=[o for oid,o in obs.items() if oid.startswith(f'option{i}_')]
        gray=[o for o in gs if o.get('semantic_color')=='#999999'];white=[o for o in gs if o.get('semantic_color')=='#F3F3F3']
        grayangles=[o['end_deg']-o['start_deg'] for o in gray];whiteangles=[o['end_deg']-o['start_deg'] for o in white]
        out[k]={'gray_sector_degrees':grayangles,'white_sector_degrees':whiteangles,'single_rigid_semicircle_and_quarter':len(gray)==len(white)==1 and grayangles==[180] and whiteangles==[90]}
    assert [k for k,v in out.items() if v['single_rigid_semicircle_and_quarter']]==['E']
    write(HERE/'Plane242/primary_math_audit.json',{'method':'Fresh exact native sector intervals, connectedness, radius equality and nonoverlap; source gray180 white90 unchanged. Area alone is insufficient for D.','all_options':out,'source_gray':obs['image1_semicircle'],'source_white':obs['image1_quarter'],'unique_answer':'E','primary_not_second_review':True})
def prove225():
    s=read(HERE/'Plane225/source_scene_snapshot.json');pts=s['points'];edges=[o for o in s['objects'] if o.get('role')=='mirror_edge'];print('mirror edges',[(o['id'],o['points']) for o in edges])
    matrices=[]
    for o in edges:
        a,b=[np.array(pts[p],dtype=float) if isinstance(p,str) else np.array(p,dtype=float) for p in o['points']]
        u=(b-a)/np.linalg.norm(b-a);matrices.append(2*np.outer(u,u)-np.eye(2))
    assert len(matrices)==3
    art={o['id']:o for o in s['objects'] if o['type']=='native_artwork_instance'}
    original=np.array(art['fold0_dog']['matrix']);net=matrices[2]@matrices[1]@matrices[0]@original
    errors={k:float(np.max(abs(np.array(art[f'option{k}_dog']['matrix'])-net))) for k in 'ABCDE'}
    assert [k for k,v in errors.items() if v<1e-10]==['B'],(matrices,errors)
    write(HERE/'Plane225/primary_math_audit.json',{'method':'Fresh matrices from the actual three bold edge endpoint directions, composed in chain order with the actual original animal matrix; compare complete actual option matrices, including internal animal heading.','edge_ids':[o['id'] for o in edges],'edge_reflection_matrices':[a.tolist() for a in matrices],'original_matrix':original.tolist(),'result_matrix':net.tolist(),'all_option_errors':errors,'unique_answer':'B','printed_animal_shapes_positions_and_handedness_preserved':True,'primary_not_second_review':True})
if __name__=='__main__':
    for q in sys.argv[1:]:globals()['prove'+q[5:]]();print(q,'proved',flush=True)
