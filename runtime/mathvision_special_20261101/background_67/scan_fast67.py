from env67 import *
import base64
import gc
import re
A=read(OWN/'snapshots/background_67_assignment.json')
items={v['question_id']:v for v in A['questions']}
targets={v['frozen_source_files_sha256']['candidate.png']:q for q,v in items.items()}
aliases={q:{v['variant_id'],v['source_directory'],v['source_directory'].replace('\\','/'),v['frozen_source_files_sha256']['design.json'],v['frozen_source_files_sha256']['candidate.png']} for q,v in items.items()}
source=(OWN/'audit67.py').read_text(encoding='utf-8')
fragment=source.split('# Whole-task scan including legacy workbench runtime.',1)[1]
fragment=fragment[fragment.index('\nroots='):]
assert fragment.count('gc.collect()')==1
fragment=fragment.replace('gc.collect()','gc.collect() if file_count % 250 == 0 else None')
save('scan_gc_optimization_audit.json',{'at':now(),'source':str(OWN/'audit67.py'),'source_sha256':sha(OWN/'audit67.py'),'changes':['Only the whole-task scanning section is executed; initialization audits already completed and retained.','Garbage collection every 250 files; per-file data/value/base64 objects are still released immediately.'],'scope_roots_and_matching_logic_unchanged':True,'API_logic_present':False,'partial_scan_retained':str(OWN/'whole_task_scan_files.partial_before_gc_optimization.jsonl')})
exec(compile(fragment,str(OWN/'scan_fast67.py'),'exec'),globals())
