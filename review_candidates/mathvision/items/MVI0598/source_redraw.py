"""Deterministic standalone native renderer for MathVision 598.
All six cartoon animals are frozen native Bézier/ellipse layers in scene.json.
No raster/source image is opened while rendering; JPEG is read only for its hash.
"""
from pathlib import Path
import io, json, hashlib, platform, math
import numpy as np
from PIL import Image
import PIL, matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Ellipse, Polygon, FancyArrowPatch
from matplotlib.transforms import Affine2D
BASE=Path(__file__).resolve().parent

def rotation(deg):
    t=math.radians(deg);return np.array([[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]])
def reflection(deg):
    t=math.radians(2*deg);return np.array([[math.cos(t),math.sin(t)],[math.sin(t),-math.cos(t)]])
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def check_scene(s):
    pts={k:np.array(v,dtype=float) for k,v in s['points'].items()}; out=[]
    for con in s['constraints']:
        if con['type']=='regular_hexagons':
            residual=0.
            for prefix in con['tile_prefixes']:
                vs=np.array([pts[f'{prefix}_v{k}'] for k in range(6)])
                ds=np.linalg.norm(vs-np.roll(vs,1,axis=0),axis=1)
                rad=np.linalg.norm(vs-pts[prefix+'_center'],axis=1)
                residual=max(residual,float(np.ptp(ds)),float(np.max(np.abs(ds-rad))))
            assert residual<1e-8;out.append({'id':con['id'],'passed':True,'max_equal_side_radius_error':residual})
        elif con['type']=='mirror_chain':
            cs=np.array(con['centers']);axes=con['axes_degrees']; errs=[]
            for i,a in enumerate(axes):
                r=reflection(a); midpoint=(cs[i]+cs[i+1])/2
                errs.append(float(np.max(np.abs(midpoint+r@(cs[i]-midpoint)-cs[i+1]))))
            expected=[reflection(120),np.eye(2),reflection(60),reflection(120)@reflection(60)]
            errs += [float(np.max(np.abs(np.array(a)-b))) for a,b in zip(con['canonical_art_matrices'],expected)]
            assert max(errs)<1e-8;out.append({'id':con['id'],'passed':True,'max_reflection_error':max(errs),'axes_degrees':axes,'final_relative_to_canonical':expected[-1].tolist()})
        elif con['type']=='option_matrices':
            mats={k:np.array(v) for k,v in con['matrices'].items()}; target=np.array(con['expected_after_three_reflections_relative_to_fold1'])
            found=[k for k,m in mats.items() if np.allclose(m,target,atol=1e-10,rtol=0)]
            assert found==[con['matching_option']]
            assert all(np.linalg.norm(a-b)>1e-7 for i,a in enumerate(mats.values()) for b in list(mats.values())[i+1:])
            out.append({'id':con['id'],'passed':True,'unique_matching_option':found[0],'determinants':{k:float(np.linalg.det(v)) for k,v in mats.items()}})
        else:raise ValueError('Unknown constraint '+con['type'])
    # Every drawn copy of an animal references one frozen native definition.
    defs={o['id']:o for o in s['objects'] if o['type']=='native_artwork_definition'}
    inst=[o for o in s['objects'] if o['type']=='native_artwork_instance']
    assert len(defs)==6 and len(inst)==42
    assert all(o['artwork'] in defs for o in inst)
    out.append({'id':'native_artwork_reuse','passed':True,'definitions':6,'instances':42,'blank_later_tiles':all(not o['id'].startswith(('fold2_','fold3_')) for o in inst)})
    stroked_layers=[l for o in defs.values() for l in o['layers'] if l['stroke'] != 'none' and l['linewidth_pt'] > 0]
    assert all(l['linewidth_pt']==1 for l in stroked_layers)
    fold_edges=[o for o in s['objects'] if o.get('role')=='mirror_edge']
    assert len(fold_edges)==3 and all(o['linewidth_pt']==2.5 for o in fold_edges)
    out.append({'id':'protocol_stroke_widths','passed':True,'stroked_animal_layers':len(stroked_layers),'animal_stroke_pt':1,'semantic_bold_fold_edges':3,'semantic_bold_fold_stroke_pt':2.5})
    return out

def render(vector=False):
    s=json.loads((BASE/'scene.json').read_text());checks=check_scene(s)
    with matplotlib.rc_context({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'MathVision598native','path.simplify':False}):
        fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
        ax=fig.add_axes(s['view']['layout']['axes_position']);ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_aspect('equal');ax.set_axis_off();ax.set_autoscale_on(False)
        pts=s['points'];defs={o['id']:o for o in s['objects'] if o['type']=='native_artwork_definition'}
        for o in s['objects']:
            typ=o['type']
            if typ=='native_artwork_definition':continue
            if typ=='polygon':
                ax.add_patch(Polygon([pts[q] for q in o['points']],closed=True,fill=False,edgecolor='black',linewidth=o['linewidth_pt'],joinstyle='round',zorder=1))
            elif typ=='segment':
                a,b=[pts[q] for q in o['points']];ax.plot([a[0],b[0]],[a[1],b[1]],color='black',linewidth=o['linewidth_pt'],solid_capstyle='round',zorder=5 if o.get('role')=='mirror_edge' else 1)
            elif typ=='native_artwork_instance':
                art=defs[o['artwork']];mat=np.array(o['matrix']);scale=o['tile_radius']/100
                lin=scale*art['scale']*(mat@rotation(art['pose_degrees']));offset=np.array(o['center'])+scale*(mat@np.array(art['position']))
                transform=Affine2D(np.array([[lin[0,0],lin[0,1],offset[0]],[lin[1,0],lin[1,1],offset[1]],[0,0,1]]))+ax.transData
                for k,layer in enumerate(art['layers']):
                    kw={'facecolor':layer['fill'],'edgecolor':layer['stroke'],'linewidth':layer['linewidth_pt'],'antialiased':True,'zorder':2+k*.001,'transform':transform}
                    if layer['kind']=='path':patch=PathPatch(MPath(layer['vertices'],layer['codes']),joinstyle='round',capstyle='round',**kw)
                    elif layer['kind']=='ellipse':patch=Ellipse(layer['center'],2*layer['radii'][0],2*layer['radii'][1],angle=layer['angle_degrees'],**kw)
                    else:raise ValueError('Unknown art primitive '+layer['kind'])
                    ax.add_patch(patch)
            elif typ=='bezier_arrow':
                path=o['path'];ax.add_patch(PathPatch(MPath(path['vertices'],path['codes']),fill=False,edgecolor='black',linewidth=1,capstyle='round',zorder=3))
                ax.add_patch(FancyArrowPatch(o['arrow_previous'],o['arrow_tip'],arrowstyle='-|>',mutation_scale=10,linewidth=1,color='black',zorder=4))
            else:raise ValueError('Unknown object '+typ)
        for lab in s['labels']:ax.text(*lab['position'],lab['text'],fontsize=lab['font_size_pt'],ha=lab['ha'],va=lab['va'],color='black',clip_on=False)
        data=io.BytesIO();fig.savefig(data,format='svg' if vector else 'png',dpi=100,transparent=False,facecolor='white',bbox_inches=None,metadata={'Date':None} if vector else {'Software':'MathPalette MathVision 598 native Bézier renderer'})
        plt.close(fig)
    return data.getvalue(),checks

if __name__=='__main__':
    a,checks=render();b,_=render();ia=np.asarray(Image.open(io.BytesIO(a)));ib=np.asarray(Image.open(io.BytesIO(b)))
    assert ia.shape==(768,768,4) and np.all(ia[:,:,3]==255) and np.array_equal(ia,ib)
    (BASE/'image.png').write_bytes(a);(BASE/'image.svg').write_bytes(render(True)[0])
    yy,xx=np.where(np.any(ia[:,:,:3]<245,axis=2));bbox=[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())]
    center=[(bbox[0]+bbox[2])/2,(bbox[1]+bbox[3])/2];occupancy=max(bbox[2]-bbox[0]+1,bbox[3]-bbox[1]+1)/768
    assert max(abs(q-383.5) for q in center)<=2.0,(bbox,center)
    assert .85<=occupancy<=.87,(bbox,occupancy)
    assert min(bbox[0],bbox[1],767-bbox[2],767-bbox[3])>=.05*768
    protocol=BASE.parents[3]/'PlaneGeometry/dataset_generator/protocol.json'
    report={'source_sha256':sha(BASE/'original.jpg'),'scene_sha256':sha(BASE/'scene.json'),'renderer_sha256':sha(__file__),'script_sha256':sha(__file__),'protocol_sha256':sha(protocol) if protocol.exists() else None,'output_sha256':sha(BASE/'image.png'),'svg_sha256':sha(BASE/'image.svg'),'two_render_pixels_equal':True,'opaque_768_square':True,'content_bbox_px':bbox,'content_center_px':center,'longest_side_occupancy':occupancy,'constraints':checks,'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'native_rendering':{'raster_embedding':False,'pixel_tracing':False,'artwork':'Six hand-authored frozen Bézier/ellipse animal definitions; every animal occurrence uses an exact matrix transform of one shared definition.','semantic_colors':'Dog brown; butterfly green/blue; ant brown; ladybird red/cream; cat tan; dolphin gray.','stroke_policy':'All actual stroked animal details and ordinary geometric lines are 1pt. No-outline color fills remain fills. The three semantic bold fold edges are 2.5pt.'},'visual_check':'pending_author_view','independent_review':'pending','standalone_entrypoint':'passed'}
    (BASE/'redraw_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'image':str(BASE/'image.png'),'bbox':bbox,'center':center,'occupancy':occupancy,'deterministic':True,'answer_check':'B'},indent=2))
