import task_env
from task_env import OWN
from prepare import read,write,eligibility,hashfile
from designs import Builder,protected_state,now,B,G,polygon_area
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
import hashlib

old=OWN/'Plane473/r48_white_unit_corner_to_outer_denominator'
write(old/'precall_render_failure.json',{'status':'LOCAL_RENDER_FAILURE_NO_API','error':'WorkbenchError object_changed: 局部区间路径已改变，请重新选择原对象。','candidate_PNG_created':False,'API_started':False,'preserved_plugin_and_context':True,'additional_primary_issue':'The c01 edge3 appeared both as source and outer receiver: redundant action. A new source corner at c10 and exact existing-edge overlays are prepared separately; this failed draft remains unchanged.'})
ad=RendererAdapter(load_config());b=Builder('Plane473',ad)
p=b.scene['points'];o=b.objects
def edge(oid,i,color,role):
    obj=o[oid];names=[obj['points'][i],obj['points'][(i+1)%4]]
    b.line(p[names[0]],p[names[1]],color,role,names)
    b.roles[-1].update(source_object=oid,source_edge_index=i)
edge('c10',2,B,'Source horizontal interior side of actual white unit square c10, paired to the complete horizontal outer side at 4-times scale.')
edge('c10',1,G,'Source perpendicular interior side of the same white unit square, paired to the complete vertical outer side.')
for k in ['c00','c10','c20','c30']:edge(k,0,B,'Receiver: one actual unit segment of the length4 complete outer side. This whole-square corner substitutes total area16 for white area10.')
for k in ['c00','c01','c02','c03']:edge(k,3,G,'Receiver: one actual unit segment of the perpendicular length4 complete outer side. No new location, fill or partition is drawn.')
var='r48_white_unit_corner_to_outer_denominator_exact_edges';d=OWN/'Plane473'/var;d.mkdir(exist_ok=False)
rule='Transfer white unit-square identity from its two interior corner sides to the 4-times-longer outer-square corner, and use total area16 as white denominator. Keep true gray area6, giving6:16=3:8 (B).'
diff='Against old tested square-object count scheme presetA, this is a whole-area denominator substitution presetB. Against the NEW untested local-render-failed draft, source moves from c01 to interior corner of c10, removing a duplicate source/receiver action; exact existing-edge auxiliary overlays use the unchanged schema and exact formal vertices rather than a rejected local-path fingerprint. No API was made on the failed draft, which is preserved.'
write(d/'design_difference_audit.json',{'created_at_utc':now(),'question_id':'Plane473','variant_id':var,'material_difference':diff,'predeclared_geometric_error_rule':rule,'old_failure_evidence':str(old/'precall_render_failure.json')})
write(d/'eligibility_before_design.json',eligibility('Plane473'));write(d/'context.json',b.context)
proof=read(old/'math_proof.json');write(d/'math_proof.json',proof)
pr=PluginRenderer(load_config(),ad,{'Plane473':b.context});plugin=pr.normalize({'plugin_schema_version':'1.0.0','question_id':'Plane473','category':'C','operation':'C_manual','description':rule,'intent':'Research only, no approval','params':{'actions':b.actions}})
write(d/'plugin.json',plugin)
checks=[];native=ad.scene
def capture(qid):
    sc=native(qid);refs=list(dict.fromkeys(a for group in sc.artists.values() for a in group));before=protected_state(sc,refs);close=sc.close
    def done():checks.append(before==protected_state(sc,refs));close()
    sc.close=done;return sc
ad.scene=capture
try:
    n,png,ph=pr.render(plugin,frozen=True);n2,png2,ph2=pr.render(plugin,frozen=True)
finally:ad.scene=native;b.finish()
assert png==png2 and n==plugin==n2 and ph==ph2 and all(checks)
(d/'candidate.png').write_bytes(png);(d/'replay_2.png').write_bytes(png2)
write(d/'render_check.json',{'schema_normalized':True,'frozen_plugin_unchanged':True,'fresh_noop_formal_pixel_equal':True,'two_consecutive_byte_identical':True,'png_sha256':hashfile(d/'candidate.png'),'pixel_sha256':ph,'original_geometry_fill_dots_text_view_unchanged':checks,'adapter_manifest':ad.manifest})
write(d/'path_fingerprints.json',b.roles)
write(d/'design.json',{'question_id':'Plane473','variant_id':var,'created_at_utc':now(),'expected_wrong_answer':'B','geometric_error_rule':rule,'material_difference':diff,'primary_math':proof,'marker_roles':b.roles,'human_semantics':'All13 original squares, gray6 area and white10 area remain; only thin exact existing-edge overlays; no added filled square or division. Numerical area question does not transport printed paper ink. Actual native review required.','png_sha256':hashfile(d/'candidate.png'),'pixel_sha256':ph,'plugin_sha256':hashfile(d/'plugin.json'),'approval_status':'PRIMARY RESEARCH ONLY; parent NEW independent review required'})
print('Plane473 new exact existing-edge variant ready; no API')
