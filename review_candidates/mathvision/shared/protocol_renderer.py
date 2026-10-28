"""Strict vector replay of frozen MathVision native geometry.

Native modules are copied into a temporary, historically compatible layout.
A small, fingerprinted AST adaptation exposes the completed Figure before native
serialization. No raster is read to construct geometry and no global Matplotlib
method is replaced. The reviewed native source remains intact.
"""
from __future__ import annotations
import argparse, ast, contextlib, hashlib, importlib.util, io, json, os
from pathlib import Path
import platform, shutil, sys, tempfile
os.environ.setdefault('MPLCONFIGDIR','/tmp/mathpalette-protocol-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.text import Text
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.collections import Collection
import numpy as np
from PIL import Image
import PIL

HERE=Path(__file__).resolve().parent
ROOT=next((p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file()),None)
def machine_protocol(branch):
    candidate=ROOT/branch/'dataset_generator/protocol.json' if ROOT else None
    return candidate if candidate and candidate.is_file() else HERE/'native/geometry'/branch/'dataset_generator/protocol.json'
SUPPORTED={'segment','polygon','face','point','circle','polyline','circular_arc','closed_arc_path','arc','ellipse','open_arc_path','open_cubic_path','native_artwork_instance','text','sector','arrow','angle_arc','native_artwork_definition','bezier_arrow','right_angle','equal_tick','parallel_mark'}
ACTIVE=None

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def _active(item):
    global ACTIVE
    ACTIVE=item.get('id') if isinstance(item,dict) else None

def _artist(ax, method, *args, **kwargs):
    result=getattr(ax,method)(*args,**kwargs)
    for artist in result if isinstance(result,list) else [result]:
        if hasattr(artist,'set_gid') and ACTIVE is not None: artist.set_gid(ACTIVE)
    return result

class ExposeFigure(ast.NodeTransformer):
    """Expose vector figures, and bind emitted artists to current scene objects."""
    def visit_For(self,node):
        self.generic_visit(node)
        if isinstance(node.target,ast.Name) and isinstance(node.iter,ast.Subscript) and isinstance(node.iter.slice,ast.Constant) and node.iter.slice.value in {'objects','labels'}:
            node.body.insert(0,ast.Expr(ast.Call(ast.Name('_protocol_active',ast.Load()),[ast.Name(node.target.id,ast.Load())],[])))
        elif isinstance(node.target,ast.Name) and isinstance(node.iter,ast.Call) and isinstance(node.iter.func,ast.Attribute) and node.iter.func.attr=='get' and node.iter.args and isinstance(node.iter.args[0],ast.Constant) and node.iter.args[0].value=='face_text':
            node.body.insert(0,ast.Expr(ast.Call(ast.Name('_protocol_active',ast.Load()),[ast.Name(node.target.id,ast.Load())],[])))
        return node
    def visit_Call(self,node):
        self.generic_visit(node)
        if isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id=='ax' and node.func.attr in {'add_patch','plot','scatter','text','annotate'}:
            return ast.copy_location(ast.Call(ast.Name('_protocol_artist',ast.Load()),[node.func.value,ast.Constant(node.func.attr)]+node.args,node.keywords),node)
        return node
    def visit_FunctionDef(self,node):
        self.generic_visit(node)
        if node.name not in {'render','render_scene','image_bytes'}: return node
        class Serialization(ast.NodeTransformer):
            def visit_Expr(self,n):
                if isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and n.value.func.attr=='savefig':
                    return ast.copy_location(ast.Return(ast.Tuple([ast.Name('fig',ast.Load()),ast.Call(ast.Attribute(ast.Call(ast.Name('locals',ast.Load()),[],[]),'get',ast.Load()),[ast.Constant('checks'),ast.List([],ast.Load())],[])],ast.Load())),n)
                return self.generic_visit(n)
        return Serialization().visit(node)

def adapt(path):
    tree=ExposeFigure().visit(ast.parse(Path(path).read_text(encoding='utf-8-sig')))
    ast.fix_missing_locations(tree)
    prefix='from protocol_renderer import _active as _protocol_active, _artist as _protocol_artist\n'
    # Future imports must stay first.
    future=[n for n in tree.body if isinstance(n,ast.ImportFrom) and n.module=='__future__']
    tree.body=[n for n in tree.body if n not in future]
    tree.body=future+ast.parse(prefix).body+tree.body
    return ast.unparse(tree)+'\n'

@contextlib.contextmanager
def native_environment(item):
    """Source-level adaptation is confined to temporary native execution files."""
    config=read(item/'execution.json')
    oldpath=sys.path[:]; oldmods=dict(sys.modules)
    with tempfile.TemporaryDirectory(prefix='mathvision-protocol-') as td:
        root=Path(td)/'MathPalette';shutil.copytree(HERE/'native/geometry',root)
        stage=root/'.runtime/mathvision_redraw_720';shutil.copytree(HERE/'native/helpers',stage,dirs_exist_ok=True)
        target=stage/config['source_category']/str(config['source_id']);target.mkdir(parents=True,exist_ok=True)
        for name in config['files']:
            dest=(target/name).resolve()
            if not dest.is_relative_to(target): raise ValueError('Unsafe execution path')
            dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(item/name,dest)
        shutil.copyfile(item/'source_redraw.py',target/'render.py')
        # Repository machine protocols, never historical private substitutes.
        for branch in ('PlaneGeometry','SolidGeometry'):
            shutil.copyfile(machine_protocol(branch),root/branch/'dataset_generator/protocol.json')
        fingerprints={}
        for path in root.rglob('*.py'):
            original=path.read_bytes();path.write_text(adapt(path),encoding='utf-8')
            fingerprints[str(path.relative_to(root))]={'source_sha256':hashlib.sha256(original).hexdigest(),'adapted_sha256':sha(path)}
        for name in ['common_renderer','renderer','renderer_semantic','renderer_rotated','upper_comb_renderer','upper_comb_renderer_v2','upper_comb_renderer_fillonly','upper_comb_solid_renderer','upper_solid_face_text_renderer']:
            sys.modules.pop(name,None)
        branch='SolidGeometry' if read(item/'scene.json').get('subject')=='SolidGeometry' else 'PlaneGeometry'
        sys.path[:0]=[str(target),str(target.parent),str(root/branch/'dataset_generator'),str(HERE)]
        try: yield target,fingerprints
        finally:
            sys.path[:]=oldpath
            for name in list(sys.modules):
                module=sys.modules[name];file=getattr(module,'__file__',None)
                if file and str(file).startswith(str(root)):
                    if name in oldmods:sys.modules[name]=oldmods[name]
                    else:sys.modules.pop(name,None)

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module);return module

def figure(target,scene):
    # Import-safe adaptation also suppresses native main entrypoints.
    module=load(target/'render.py','_protocol_native_entry')
    if hasattr(module,'render'):
        result=module.render(False)
    elif hasattr(module,'image_bytes'):
        result=module.image_bytes(scene)
    else:
        fn=module.draw if hasattr(module,'draw') else None
        owner=sys.modules.get(getattr(fn,'__module__',''))
        if owner is None:
            owner=getattr(module,'r',None) or getattr(module,'common_renderer',None) or getattr(getattr(module,'F',None),'R',None)
        if owner is None: raise ValueError('Native entrypoint does not expose supported renderer')
        if hasattr(owner,'render_scene'):result=owner.render_scene(scene,check_layout=False)
        elif hasattr(owner,'image_bytes'):result=owner.image_bytes(scene)
        else:raise ValueError('Native renderer cannot expose vector figure')
    if not isinstance(result,tuple) or not hasattr(result[0],'axes'):
        raise ValueError('Native function did not expose a vector Figure')
    return result

def decisions(review,kind):
    result={}
    for entry in review.get(kind,[]):
        if not entry.get('reason','').strip() or not isinstance(entry.get('object_ids'),list):raise ValueError('Semantic decision requires object_ids and a specific reason')
        for name in entry['object_ids']:result[name]=entry
    return result

def normalize(fig,scene,review,protocol):
    fills=decisions(review,'semantic_fills');colors=decisions(review,'semantic_colors')
    labels={o.get('id'):o for o in scene.get('labels',[])}
    objects={o['id']:o for o in scene['objects']}
    objects.update({o['id']:{**o,'type':'native_face_text'} for o in scene.get('face_text',[])})
    records=[]
    for ax in fig.axes:
        ax.set_position(protocol['figure']['axes_position']);ax.set_aspect('equal');ax.set_autoscale_on(False);ax.set_axis_off()
        for artist in list(ax.lines)+list(ax.patches)+list(ax.collections)+list(ax.texts):
            gid=artist.get_gid();color=colors.get(gid,colors.get('*'));fill=fills.get(gid,fills.get('*'))
            if isinstance(artist,Text):
                label=labels.get(gid,{})
                vertex=label.get('type')=='vertex'
                artist.set_fontfamily(protocol['font']['family']);artist.set_fontsize(protocol['font']['vertex_size_pt'] if vertex else protocol['font']['size_pt']);artist.set_fontstyle('italic' if vertex else 'normal');artist.set_color('black');artist.set_bbox(None);artist.set_clip_on(False)
            elif isinstance(artist,Line2D):
                artist.set_linewidth(protocol['stroke']['linewidth_pt']);artist.set_antialiased(True)
                if objects.get(gid,{}).get('type')=='point':
                    artist.set_markersize(protocol['point']['area_pt2']**.5);artist.set_markeredgewidth(1);artist.set_markeredgecolor('black');artist.set_markerfacecolor('black' if objects.get(gid,{}).get('filled',True) else 'white')
                artist.set_color((color.get('color') if color.get('color') not in (None,'preserve') else artist.get_color()) if color else 'black')
            elif isinstance(artist,Patch):
                face=artist.get_facecolor();edge=artist.get_edgecolor()
                hasface=face[3]>0;hasedge=edge[3]>0 and artist.get_linewidth()>0
                if hasedge:artist.set_linewidth(1);artist.set_edgecolor((color.get('color') if color.get('color') not in (None,'preserve') else edge) if color else 'black')
                else:artist.set_linewidth(0)
                if hasface and color and color.get('color') not in (None,'preserve'):artist.set_facecolor(color['color'])
                if hasface and not color:
                    white=np.allclose(face[:3],1)
                    obj=objects.get(gid,{})
                    if white and obj.get('type') in {'face','native_artwork_instance'}:artist.set_facecolor('white')
                    elif fill:
                        choice=fill.get('color',protocol['fill']['semantic_facecolor'])
                        gray=float(np.dot(face[:3],[.2126,.7152,.0722]));artist.set_facecolor((gray,gray,gray,face[3]) if choice=='preserve' else choice)
                        # Semantic opacity belongs to the face, never the
                        # mathematical outline. A global Patch alpha would
                        # fade the separately standardized black edge too.
                        face_alpha=fill.get('alpha',1 if choice in {'preserve','#000000','#FFFFFF','#ffffff'} else protocol['fill']['semantic_alpha'])
                        rgb=artist.get_facecolor()[:3]
                        artist.set_alpha(None)
                        artist.set_facecolor((*rgb,face_alpha))
                    elif obj.get('type') in {'point','native_face_text'} or artist.__class__.__name__=='FancyArrowPatch':artist.set_facecolor('black')
                    else:artist.set_facecolor('none')
                artist.set_antialiased(True)
            elif isinstance(artist,Collection):
                artist.set_linewidth(1)
                if hasattr(artist,'set_sizes'):artist.set_sizes([protocol['point']['area_pt2']])
                if not color:
                    artist.set_edgecolor('black');artist.set_facecolor('black' if objects.get(gid,{}).get('filled',True) else 'white')
            record={'object_id':gid,'artist_type':type(artist).__name__,'linewidth_pt':float(artist.get_linewidth()) if isinstance(artist,(Line2D,Patch)) else None,'font_size_pt':float(artist.get_fontsize()) if isinstance(artist,Text) else None,'font_family':artist.get_fontfamily() if isinstance(artist,Text) else None,'font_style':artist.get_fontstyle() if isinstance(artist,Text) else None}
            if isinstance(artist,Line2D):record.update(stroke_rgba=list(to_rgba(artist.get_color())),linestyle=artist.get_linestyle(),marker=artist.get_marker(),marker_size_pt=artist.get_markersize(),marker_face_rgba=list(to_rgba(artist.get_markerfacecolor())))
            elif isinstance(artist,Patch):record.update(stroke_rgba=list(artist.get_edgecolor()),face_rgba=list(artist.get_facecolor()),linestyle=artist.get_linestyle(),alpha=artist.get_alpha())
            elif isinstance(artist,Collection):record.update(stroke_rgba=artist.get_edgecolors().tolist(),face_rgba=artist.get_facecolors().tolist(),linewidths_pt=artist.get_linewidths().tolist(),sizes_pt2=artist.get_sizes().tolist() if hasattr(artist,'get_sizes') else None)
            elif isinstance(artist,Text):record.update(text=artist.get_text(),position=list(artist.get_position()),color_rgba=list(to_rgba(artist.get_color())))
            records.append(record)
    fig.set_size_inches(protocol['figure']['figsize_in']);fig.set_dpi(protocol['figure']['dpi']);fig.set_facecolor('white')
    return records

def serialize(fig,vector=False):
    buf=io.BytesIO()
    with matplotlib.rc_context({'svg.fonttype':'path','svg.hashsalt':'MathPalette.MathVision.protocol.1','savefig.bbox':None}):
        fig.savefig(buf,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,pad_inches=0,metadata={'Date':None} if vector else {'Software':'MathPalette strict protocol renderer'})
    return buf.getvalue()

def metrics(data):
    a=np.asarray(Image.open(io.BytesIO(data)).convert('RGBA'));y,x=np.where(np.any(a[:,:,:3]!=255,axis=2))
    if not len(x):raise ValueError('Empty vector rendering')
    bbox=[int(x.min()),int(y.min()),int(x.max()),int(y.max())];center=[(bbox[0]+bbox[2])/2,(bbox[1]+bbox[3])/2];occ=max(bbox[2]-bbox[0]+1,bbox[3]-bbox[1]+1)/768
    return {'content_bbox_px':bbox,'content_center_px':center,'longest_side_occupancy':occ,'opaque_768_square':a.shape==(768,768,4) and bool(np.all(a[:,:,3]==255)),'centered_within_2px':max(abs(v-383.5) for v in center)<=2,'occupancy_85_to_87_percent':.85<=occ<=.87,'minimum_5_percent_margin':min(bbox[0],bbox[1],767-bbox[2],767-bbox[3])>=38.4}

def render_item(item,output_dir,fit=False):
    item=Path(item).resolve();out=Path(output_dir).resolve();scene=read(item/'scene.json');review=read(item/'protocol_review.json');candidate_id=f"MVI{int(read(item/'execution.json')['source_id']):04d}"
    unknown={o['type'] for o in scene['objects']}-SUPPORTED
    if unknown:raise ValueError(f'Unsupported objects: {unknown}')
    unknown_labels={o.get('type') for o in scene.get('labels',[])}-{'text','vertex','angle',None}
    if unknown_labels:raise ValueError(f'Unsupported labels: {unknown_labels}')
    branch='SolidGeometry' if scene.get('subject')=='SolidGeometry' else 'PlaneGeometry';protocolpath=machine_protocol(branch);protocol=read(protocolpath)
    with native_environment(item) as (target,fingerprints):
        def once():
            # Standalone native functions read their frozen local scene.
            (target/'scene.json').write_text(json.dumps(scene,ensure_ascii=False,indent=2)+'\n')
            fig,checks=figure(target,scene);artists=normalize(fig,scene,review,protocol)
            return fig,checks,artists
        if fit:
            for _ in range(8):
                fig,_,_=once();m=metrics(serialize(fig));plt.close(fig)
                b=m['content_bbox_px'];span=scene['view']['xlim'][1]-scene['view']['xlim'][0];scale=768*.9/span
                # Center in data coordinates; image Y increases downwards.
                dx=(m['content_center_px'][0]-383.5)/scale;dy=-(m['content_center_px'][1]-383.5)/scale
                cx=sum(scene['view']['xlim'])/2+dx;cy=sum(scene['view']['ylim'])/2+dy
                newspan=span*m['longest_side_occupancy']/.86
                scene['view']['xlim']=[cx-newspan/2,cx+newspan/2];scene['view']['ylim']=[cy-newspan/2,cy+newspan/2]
                if m['centered_within_2px'] and m['occupancy_85_to_87_percent']:break
            scene['view']['layout']={'axes_position':protocol['figure']['axes_position'],'fit_method':'frozen_content_fit','target_long_side_fraction':.86}
            (item/'scene.json').write_text(json.dumps(scene,ensure_ascii=False,indent=2)+'\n')
        outputs=[]
        for _ in range(2):
            fig,checks,artists=once();outputs.append((serialize(fig),serialize(fig,True)));plt.close(fig)
    out.mkdir(parents=True,exist_ok=True)
    for suffix,data in zip(('png','svg'),outputs[0]):(out/f'image.{suffix}').write_bytes(data)
    repeat=(ROOT/'.runtime/protocol_redraw/repeat' if ROOT else out/'.repeat')/candidate_id;repeat.mkdir(parents=True,exist_ok=True)
    for suffix,data in zip(('png','svg'),outputs[1]):(repeat/f'image.{suffix}').write_bytes(data)
    png_equal=np.array_equal(np.asarray(Image.open(io.BytesIO(outputs[0][0]))),np.asarray(Image.open(io.BytesIO(outputs[1][0]))))
    source=item/read(item/'execution.json')['original_image_name']
    report={'schema_version':1,'id':candidate_id,'scene_id':scene['id'],'status':'pending_user_review','source_sha256':sha(source),'scene_sha256':sha(item/'scene.json'),'decision_sha256':hashlib.sha256(json.dumps({k:review.get(k) for k in ('schema_version','semantic_fills','semantic_colors')},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'protocol_sha256':sha(protocolpath),'renderer_sha256':sha(__file__),'native_dependencies':fingerprints,'output_sha256':sha(out/'image.png'),'svg_sha256':sha(out/'image.svg'),'two_render_pixels_equal':png_equal,'two_render_png_bytes_equal':outputs[0][0]==outputs[1][0],'two_render_svg_bytes_equal':outputs[0][1]==outputs[1][1],'layout':metrics(outputs[0][0]),'constraints':checks,'geometry_sha256':hashlib.sha256(json.dumps({k:scene.get(k) for k in ('points','objects','constraints','dimensions','distance_markers')},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'projection_sha256':hashlib.sha256(json.dumps(scene.get('projection'),sort_keys=True,separators=(',',':')).encode()).hexdigest(),'visibility_sha256':hashlib.sha256(json.dumps(scene.get('visibility'),sort_keys=True,separators=(',',':')).encode()).hexdigest(),'object_coverage':[{'id':o['id'],'type':o['type'],'emitted_artists':sum(a['object_id']==o['id'] for a in artists),'nonemitting_reason':'shared definition' if o['type']=='native_artwork_definition' else 'frozen occlusion' if o.get('visibility')=='occluded' else None} for o in scene['objects']],'artists':artists,'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'agent_visual_review':'pending','native_vector_geometry':True}
    (out/'redraw_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');return report

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('item',type=Path);parser.add_argument('--output-dir',required=True,type=Path);parser.add_argument('--fit',action='store_true');args=parser.parse_args()
    report=render_item(args.item,args.output_dir,args.fit);print(json.dumps({'id':report['id'],'layout':report['layout'],'deterministic':report['two_render_pixels_equal']}))
if __name__=='__main__':
    sys.modules.setdefault('protocol_renderer',sys.modules[__name__]);main()
