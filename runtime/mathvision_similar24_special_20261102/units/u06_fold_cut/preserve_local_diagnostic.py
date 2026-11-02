from local_env import *
root=OWN/'Solid146'
dest=root/'diagnostics/context_serialization_02'
dest.mkdir(parents=True,exist_ok=False)
for leaf in ['eligibility_before_design.json','formal_record.json','context.json','path_fingerprints.json','raw_paths.json']:
    (root/leaf).rename(dest/leaf)
save(dest/'error.json',{'type':'local diagnostic serialization error','error':'TypeError: Object of type Line2D is not JSON serializable',
     'stage':'saving own raw_paths.json after successful original-adapter no-op check',
     'cause':'own raw-vector diagnostic attempted to serialize live artist reference',
     'repair':'omit live artist handle from diagnostic; all original control arrays, styles, path IDs, order and SHA remain exact',
     'library_modified':False,'API_calls':0,'native_render_failure':False,
     'required':'rerun all context/noop/schema/repeat/fresh-replay gates before any calls','created_at':now()},True)
