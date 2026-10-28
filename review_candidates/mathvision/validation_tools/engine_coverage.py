"""Read-only final native vector artist coverage/style audit."""
from pathlib import Path
import collections,hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[3]
ITEMS=ROOT/'review_candidates/mathvision/items'
ENGINE=ROOT/'review_candidates/mathvision/shared/protocol_renderer.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def patches(a):return isinstance(a.get('face_rgba'),list) and len(a['face_rgba'])==4 and isinstance(a['face_rgba'][0],(int,float))
def visible(a):
 if a['artist_type'] in ('Text','Annotation','Line2D'):return True
 f=a.get('face_rgba');e=a.get('stroke_rgba');lw=a.get('linewidth_pt')
 if f and isinstance(f[0],list):return any(c[3]>0 for c in f) or any(c[3]>0 for c in e)
 return bool(f and f[3]>0 or e and e[3]>0 and lw)
def covered(review,kind,oid):return any(oid in e.get('object_ids',[]) or '*' in e.get('object_ids',[]) for e in review.get(kind,[]))
def main():
 enginehash=sha(ENGINE);rows=[];totals=collections.Counter()
 for d in sorted(ITEMS.iterdir()):
  scene=read(d/'scene.json');r=read(d/'redraw_report.json');review=read(d/'protocol_review.json') if (d/'protocol_review.json').exists() else {};artists=r.get('artists',[]);by=collections.defaultdict(list)
  for a in artists:by[a['object_id']].append(a)
  oids={o['id'] for o in scene['objects']};lids={l.get('id') for l in scene.get('labels',[])};faceids={l['id'] for l in scene.get('face_text',[])}
  dimensionids={str(o.get('id'))+suffix for o in scene.get('dimensions',[]) for suffix in ('_range','_start','_end','_label')}
  current=r.get('renderer_sha256')==enginehash;bound=r.get('scene_sha256')==sha(d/'scene.json') and r.get('output_sha256')==sha(d/'image.png') and r.get('svg_sha256')==sha(d/'image.svg')
  issues=[];warnings=[]
  if not current: warnings.append({'type':'stale_renderer_report'})
  if not bound: warnings.append({'type':'stale_scene_or_image_report'})
  if not artists:warnings.append({'type':'no_artist_inventory'})
  if current and bound:
   for o in scene['objects']:
    if o['id'] not in by and o['type']!='native_artwork_definition' and o.get('visibility')!='occluded':issues.append({'type':'missing_object_artist','id':o['id'],'object_type':o['type']})
   for l in scene.get('labels',[]):
    if l.get('id') not in by:issues.append({'type':'missing_label_artist','id':l.get('id'),'text':l.get('text')})
   for oid,aa in by.items():
    if oid is None:warnings.append({'type':'unbound_artist','count':len(aa)})
    elif oid not in oids|lids|faceids|dimensionids:warnings.append({'type':'extra_artist_id','id':oid,'count':len(aa)})
    if not any(visible(a) for a in aa):
     obj=next((o for o in scene['objects'] if o['id']==oid),{})
     warnings.append({'type':'fully_invisible_object_after_normalization','id':oid,'scene_type':obj.get('type'),'scene_role':obj.get('role'),'scene_style':{k:obj[k] for k in ('fill','fill_color','semantic_color','facecolor','no_outline','white_hole') if k in obj},'fill_decision_present':covered(review,'semantic_fills',oid)})
   for o in scene['objects']:
    aa=[a for a in by[o['id']] if patches(a)];white=any(str(o.get(k)).lower() in ('white','#ffffff') for k in ('fill','fill_color','semantic_color','facecolor')) or o.get('white_hole')
    if white and aa and not any(a['face_rgba'][3]>0 and min(a['face_rgba'][:3])>.99 for a in aa):warnings.append({'type':'source_white_fill_removed_or_changed','id':o['id'],'object_type':o['type'],'white_hole':o.get('white_hole',False),'final_faces':[a['face_rgba'] for a in aa]})
   labels={l.get('id'):l for l in scene.get('labels',[])};objects={o['id']:o for o in scene['objects']}
   for a in artists:
    oid=a['object_id'];lw=a.get('linewidth_pt')
    for field in ('stroke_rgba','face_rgba','color_rgba'):
     value=a.get(field)
     samples=value if value and isinstance(value[0],list) else [value] if value else []
     for rgba in samples:
      if len(rgba)==4 and rgba[3]>0 and max(rgba[:3])-min(rgba[:3])>1e-8 and not covered(review,'semantic_colors',oid):issues.append({'type':'unapproved_chromatic_vector_artist','id':oid,'field':field,'rgba':rgba})
    if lw is not None and lw not in (0,1):issues.append({'type':'nonprotocol_stroke','id':oid,'width':lw})
    stroke=a.get('stroke_rgba')
    if lw and stroke and isinstance(stroke[0],(int,float)) and 0<stroke[3]<1:issues.append({'type':'nonopaque_stroke','id':oid,'rgba':stroke,'artist_alpha':a.get('alpha')})
    if any(v!=1 for v in a.get('linewidths_pt',[])):issues.append({'type':'nonprotocol_collection_stroke','id':oid,'widths':a['linewidths_pt']})
    if a.get('font_size_pt') is not None:
     vertex=labels.get(oid,{}).get('type')=='vertex';want=18 if vertex else 16
     if a['font_size_pt']!=want or a.get('font_family')!=['DejaVu Sans'] or a.get('font_style')!=('italic' if vertex else 'normal'):issues.append({'type':'nonprotocol_font','artist':a})
    if objects.get(oid,{}).get('type')=='point':
     if a.get('marker_size_pt') is not None and a['marker_size_pt']!=6:issues.append({'type':'nonprotocol_point_size','id':oid,'size':a['marker_size_pt']})
     if a.get('sizes_pt2') and any(v!=36 for v in a['sizes_pt2']):issues.append({'type':'nonprotocol_point_area','id':oid,'sizes':a['sizes_pt2']})
   for l in scene.get('face_text',[]):warnings.append({'type':'projected_native_vector_face_text','id':l['id'],'text':l['text'],'evidence':'upper_solid_face_text_renderer.py constructs TextPath with DejaVu Sans regular16pt in orthonormal3Dface basis; projected glyph sizes vary with face foreshortening; not ordinary page Text artist'})
  totals['items']+=1;totals['current_renderer']+=current;totals['current_input_output_bindings']+=bound;totals['issues']+=len(issues);totals['warnings']+=len(warnings);totals['items_with_issues']+=bool(issues)
  rows.append({'id':d.name,'scene_sha256':sha(d/'scene.json'),'png_sha256':sha(d/'image.png'),'svg_sha256':sha(d/'image.svg'),'report_sha256':sha(d/'redraw_report.json'),'renderer_current':current,'bindings_current':bound,'artist_count':len(artists),'issues':issues,'warnings':warnings})
 out={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'renderer_sha256':enginehash,'scope':'Read-only current final artist reports, coverage, normalized style and source-white mask candidates. Invisible decorative shading is a warning for curator assessment, not an automatic geometry failure. Stale in-flight reports excluded from detailed findings.','summary':dict(totals),'items':rows}
 path=ROOT/'.runtime/protocol_redraw/audit/engine_coverage.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['summary']));return bool(totals['issues'] or totals['current_renderer']!=totals['items'] or totals['current_input_output_bindings']!=totals['items'])
if __name__=='__main__':raise SystemExit(main())
