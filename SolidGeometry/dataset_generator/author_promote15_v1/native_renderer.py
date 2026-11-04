"""Frozen author-scene capture. Imports create no files and never render.

capture(scene, family) returns actual artists indexed by original object ID.
render(scene, family, plugin=None, schema=None) returns PNG bytes. Partial
intervals require the bundled author_partial_style module and exact path hash.
"""
from __future__ import annotations
import copy, io, math, re
from dataclasses import dataclass
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Patch
from matplotlib.collections import PathCollection

@dataclass
class Capture:
    fig: object
    ax: object
    artists: dict
    objects: list
    snap_points: list
    settings: dict
    family: str
    native: bool = True
    def close(self): plt.close(self.fig)

def capture(scene, family):
    settings = dict(mpl.rcParamsDefault); settings['backend']='Agg'
    settings['font.family']='DejaVu Sans'
    if family == 'surface':
        settings.update({'lines.solid_capstyle':'butt','lines.dash_capstyle':'butt','savefig.facecolor':'white'})
    with mpl.rc_context(settings):
        fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
        ax=fig.add_axes([.05,.05,.9,.9]); ax.set_aspect('equal'); ax.axis('off')
        if family == 'surface':
            M=scene['projection']['matrix']
            def proj(p): return tuple(sum(M[j][i]*p[i] for i in range(3)) for j in range(2))
            points=[proj(p) for o in scene['objects'] for p in o['points']]
            xx=[p[0] for p in points]; yy=[p[1] for p in points]
            span=max(max(xx)-min(xx), max(yy)-min(yy))/.86
            mx=(min(xx)+max(xx))/2; my=(min(yy)+max(yy))/2
            ax.set_xlim(mx-span/2,mx+span/2); ax.set_ylim(my-span/2,my+span/2)
        else:
            ax.set_xlim(*scene['view']['xlim']); ax.set_ylim(*scene['view']['ylim'])
        if family == 'delete_points': ax.set_autoscale_on(False)
        artists={}
        def own(oid, artist):
            if oid in artists: raise ValueError('Duplicate stable object ID: '+oid)
            artists[oid]=[artist]
        if family == 'octahedron':
            net=scene['planar_net']
            for e in net['edges']:
                a,b=e['planar_endpoints']; line,=ax.plot([a[0],b[0]],[a[1],b[1]],color='#000000',linewidth=1,solid_capstyle='round',zorder=1); own(e['id'],line)
                label=net['edge_labels'].get(e['id'])
                if label:
                    f=net['faces'][e['incident_planar_faces'][0]]; xy=[c['planar_xy'] for c in f['corners']]; mx=(a[0]+b[0])/2; my=(a[1]+b[1])/2; dx=mx-sum(t[0] for t in xy)/3; dy=my-sum(t[1] for t in xy)/3; mag=math.hypot(dx,dy)
                    ax.text(mx+.19*dx/mag,my+.19*dy/mag,label,fontsize=16,ha='center',va='center',color='black',zorder=2)
            for f in net['faces']:
                if f['label']:
                    xy=[c['planar_xy'] for c in f['corners']]; ax.text(sum(t[0] for t in xy)/3,sum(t[1] for t in xy)/3,f['label'],fontsize=16,ha='center',va='center',color='black')
        else:
            objs=scene['objects']
            if family=='surface': objs=sorted(objs,key=lambda o: 0 if o['linestyle']=='dashed' else 1)
            for o in objs:
                typ=o.get('type',o.get('kind')); oid=o['id']
                if family=='tiling':
                    a,b=o['p1'],o['p2']; line,=ax.plot([a[0],b[0]],[a[1],b[1]],color='#000000',linewidth=1,solid_capstyle='butt'); own(oid,line)
                elif family=='connect':
                    if typ=='triangle':
                        pts=[scene['points'][x] for x in o['vertices']]; pts+=pts[:1]; line,=ax.plot([p[0] for p in pts],[p[1] for p in pts],color='#000000',linewidth=1,linestyle='-',zorder=2); own(oid,line)
                    elif typ=='point':
                        x,y=scene['points'][o['point']]; own(oid,ax.scatter([x],[y],s=o['size_pt2'],c=['#000000'],edgecolors=['#000000'],linewidths=0,zorder=3))
                    else: raise ValueError(typ)
                elif family=='delete_points':
                    x,y=scene['points'][o['point']]['xy']; own(oid,ax.scatter([x],[y],s=36,c='#000000',edgecolors='#000000',linewidths=1,zorder=4))
                elif family=='folding':
                    if typ=='line':
                        a,b=o['a'],o['b']; line,=ax.plot([a[0],b[0]],[a[1],b[1]],color='#000000',linewidth=1,linestyle='--' if o.get('linestyle')=='dashed' else '-',solid_capstyle='round'); own(oid,line)
                    elif typ=='circle': own(oid,ax.add_patch(Circle(o['center'],o['radius'],fill=False,edgecolor='#000000',linewidth=1)))
                    else: raise ValueError(typ)
                elif family=='cube':
                    a,b=o['xy']; line,=ax.plot([a[0],b[0]],[a[1],b[1]],color='#000000',lw=1,solid_capstyle='butt',dash_capstyle='butt');
                    if o['linestyle']=='dashed': line.set_dashes([4,3])
                    own(oid,line)
                elif family=='surface':
                    a,b=map(proj,o['points']); line,=ax.plot([a[0],b[0]],[a[1],b[1]],color='#000000',linewidth=1,solid_capstyle='butt',zorder=2)
                    if o['linestyle']=='dashed': line.set_dashes([4,3])
                    own(oid,line)
                else: raise ValueError('Unknown family '+family)
        if family not in ('surface','octahedron'):
            for label in scene['labels']:
                if family=='tiling': ax.text(*label['xy'],label['text'],ha='center',va='center',fontsize=16,fontfamily='DejaVu Sans')
                elif family=='connect': ax.text(*label['xy'],label['text'],ha='center',va='center',fontsize=label['fontsize_pt'],family='DejaVu Sans',color='black')
                elif family=='folding': ax.text(*label['xy'],label['text'],ha='center',va='center',fontsize=label.get('size',16))
                elif family=='cube': ax.text(*label['xy'],label['text'],fontsize=18,fontfamily='DejaVu Sans',ha='center',va='center')
        objects=[{'id':oid,'styleable':True,'kind': 'point' if isinstance(a[0],PathCollection) else 'outline', 'source_call': 'author_frozen_scene', 'frozen_visibility': 'visible'} for oid,a in artists.items()]
        return Capture(fig,ax,artists,objects,[],settings,family)

def png_bytes(scene):
    with mpl.rc_context(scene.settings):
        out=io.BytesIO(); scene.fig.savefig(out,dpi=100,facecolor='white'); return out.getvalue()

def check_schema(value, rule, schema, path='plugin'):
    if '$ref' in rule: return check_schema(value,schema['$defs'][rule['$ref'].split('/')[-1]],schema,path)
    if 'oneOf' in rule:
        count=0
        for r in rule['oneOf']:
            try: check_schema(value,r,schema,path); count+=1
            except ValueError: pass
        if count!=1: raise ValueError(path+': invalid action')
        return
    typ=rule.get('type'); valid={'object':isinstance(value,dict),'array':isinstance(value,list),'string':isinstance(value,str),'boolean':type(value) is bool,'number':type(value) in (int,float) and math.isfinite(value)}
    if typ and not valid.get(typ,False): raise ValueError(path+': expected '+typ)
    if 'const' in rule and (type(value) is not type(rule['const']) or value!=rule['const']): raise ValueError(path+': invalid constant')
    if 'enum' in rule and value not in rule['enum']: raise ValueError(path+': invalid choice')
    if typ=='object':
        if set(rule.get('required',()))-value.keys() or rule.get('additionalProperties') is False and value.keys()-rule.get('properties',{}).keys(): raise ValueError(path+': missing or extra field')
        for k,v in value.items():
            if k in rule.get('properties',{}): check_schema(v,rule['properties'][k],schema,path+'.'+k)
    elif typ=='array':
        if not rule.get('minItems',0)<=len(value)<=rule.get('maxItems',math.inf): raise ValueError(path+': invalid length')
        for i,v in enumerate(value): check_schema(v,rule['items'],schema,path+str(i))
    elif typ=='string':
        if not rule.get('minLength',0)<=len(value)<=rule.get('maxLength',math.inf) or 'pattern' in rule and re.search(rule['pattern'],value) is None: raise ValueError(path+': invalid string')
    elif typ=='number' and not rule.get('minimum',-math.inf)<=value<=rule.get('maximum',math.inf): raise ValueError(path+': out of range')

def apply(scene, plugin, schema):
    check_schema(plugin,schema,schema)
    actions=copy.deepcopy(plugin['params']['actions'])
    ids=set(scene.artists)
    for a in actions:
        if a['type']=='set_object_style':
            if a['target'] not in ids or not any(k in a for k in ('color','linewidth_pt','linestyle')): raise ValueError('Invalid style target or empty style')
            if 'interval' in a and isinstance(scene.artists[a['target']][0],PathCollection): raise ValueError('Point has no selectable outline interval')
        else:
            if a['id'] in ids: raise ValueError('Duplicate action ID')
            ids.add(a['id'])
            for p in ([a['xy']] if a['type']=='add_point' else a['endpoints']):
                if not scene.ax.get_xlim()[0]<=p[0]<=scene.ax.get_xlim()[1] or not scene.ax.get_ylim()[0]<=p[1]<=scene.ax.get_ylim()[1]: raise ValueError('Action outside frozen viewport')
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location('_author_partial_style',Path(__file__).with_name('author_partial_style.py'))
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    apply_partial_styles=module.apply_partial_styles
    with mpl.rc_context(scene.settings):
        partial=apply_partial_styles(scene,actions)
        for a in actions:
            typ=a['type']
            if typ=='set_object_style':
                if a['target'] in partial: continue
                for artist in scene.artists[a['target']]:
                    if isinstance(artist,PathCollection):
                        if 'linestyle' in a or 'linewidth_pt' in a: raise ValueError('Point styles only support color')
                        if 'color' in a: artist.set_facecolor(a['color']); artist.set_edgecolor(a['color'])
                        continue
                    dashes=copy.deepcopy(getattr(artist,'_dash_pattern',(0,None)))
                    if 'color' in a:
                        if isinstance(artist,Patch): artist.set_edgecolor(a['color'])
                        else: artist.set_color(a['color'])
                    with mpl.rc_context({'lines.scale_dashes':False}):
                        if 'linewidth_pt' in a:
                            artist.set_linewidth(a['linewidth_pt'])
                            if 'linestyle' not in a and dashes[1] is not None: artist.set_linestyle(dashes)
                        if 'linestyle' in a: artist.set_linestyle((0,[3.7,1.6]) if a['linestyle']=='dashed' else 'solid')
            elif typ=='add_point': scene.ax.scatter(*a['xy'],s=a.get('size_pt2',50),marker='o',facecolors=a.get('color','#DC2626'),edgecolors=a.get('color','#DC2626'),linewidths=a.get('edge_linewidth_pt',1),zorder=10,clip_on=True)
            elif typ=='add_line':
                p,q=a['endpoints']; line,=scene.ax.plot([p[0],q[0]],[p[1],q[1]],color=a.get('color','#2563EB'),linewidth=a.get('linewidth_pt',1),solid_capstyle='butt',dash_capstyle='butt',zorder=2 if scene.family=='delete_points' else 9,clip_on=True)
                if a.get('linestyle','dashed')=='dashed':
                    with mpl.rc_context({'lines.scale_dashes':False}): line.set_linestyle((0,a.get('dash_pattern_pt',[3.7,1.6])))

def render(scene, family, plugin=None, schema=None):
    if plugin is not None and plugin.get('question_id')!=scene['id']: raise ValueError('Plugin question ID mismatch')
    c=capture(scene,family)
    try:
        if plugin is not None:
            if schema is None: raise ValueError('Branch schema required')
            apply(c,plugin,schema)
        return png_bytes(c)
    finally: c.close()
