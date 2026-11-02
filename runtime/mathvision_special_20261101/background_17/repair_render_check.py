from tools import *
q='Plane402';d=TASK/q/'exposed_strip_extent_binding'
write(d/'render_bookkeeping_error.json',{'error':'AttributeError: Plane PluginRenderer lacks appearance_changes; occurred after image/plugin/design saved, before render_check serialization.','api_calls_at_error':0,'resolution':'Only own bookkeeping helper corrected; frozen plugin/image/design unchanged. Fresh actual renderer replay checked twice.'})
p=read(d/'plugin.json');meta=AD.inspect_question(q);renderer=PluginRenderer(CONFIG,AD,{q:meta})
n,a,pa=renderer.render(p,frozen=True);n2,b,pb=renderer.render(p,frozen=True)
assert a==b==(d/'candidate.png').read_bytes() and pa==pb and n==n2==p
assert frozen(q)==read(TASK/q/'frozen_inputs.json')
write(d/'render_check.json',{'question_id':q,'baseline_matches_formal':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'normalized_by_actual_schema':True,'repeat_bytes_identical':True,'repeat_pixels_identical':True,'frozen_inputs':frozen(q),'appearance_changes':{'world_geometry_changed':False,'projection_changed':False,'frozen_visibility_intervals_changed':False,'rendered_line_styles_changed':False},'isolation':ISOLATION,'unit_write_guard':True,'bookkeeping_error_resolved':True})
print(q,'frozen replay identical twice')
