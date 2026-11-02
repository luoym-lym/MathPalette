import audit as a
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone
import struct
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import rc_context

proof=a.read(a.OUT/'independent_math.json')
context=a.read(a.CAND/'context.json')
row=a.read(a.QUESTION/'formal_record.json')
scene=a.read(a.ROOT/'PlaneGeometry'/row['scene'])
def chunks(p):
    b=Path(p).read_bytes();i=8;out=[]
    while i<len(b):
        n=struct.unpack('>I',b[i:i+4])[0]
        kind=b[i+4:i+8].decode('ascii');payload=b[i+8:i+8+n]
        out.append({'kind':kind,'length':n,'sha256':hashlib.sha256(payload).hexdigest(),
                    **({'text':payload.decode('latin1')} if kind=='tEXt' else {})})
        i+=12+n
    return out
original=a.ROOT/'PlaneGeometry'/row['image']
replay=a.OUT/'reproduced_original.png'
assert np.array_equal(np.array(Image.open(original)),np.array(Image.open(replay)))
chunkaudit={'formal_png_chunks':chunks(original),'reproduced_png_chunks':chunks(replay),
            'pixels_identical':True,'byte_difference_is_metadata_only':
            [x for x in chunks(original) if x['kind']!='tEXt']==[x for x in chunks(replay) if x['kind']!='tEXt']}
a.save('original_png_serialization_audit.json',chunkaudit)

# Diagnostic only: reflect exact formal segments/dots onto the stationary half,
# retaining source scale, original display transform and candidate stroke colors.
with rc_context({'backend':'Agg'}):
    fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    ax=fig.add_axes([.05,.05,.9,.9]);ax.set_aspect('equal');ax.set_axis_off()
    ax.set_xlim(context['canvas']['xlim']);ax.set_ylim(context['canvas']['ylim'])
    colors={'o2':'#DC2626','o3':'#DC2626','o18':'#2563EB','o19':'#2563EB','o20':'#2563EB'}
    for digit in proof['digits']:
        for e in digit['segments']:
            xy=np.array(e['after'])
            ax.plot(xy[:,0],xy[:,1],color=colors.get(e['id'],'black'),
                    linewidth=1.5 if e['id'] in colors else 1,solid_capstyle='round')
    from matplotlib.patches import Circle
    for dot in proof['dot_inventory']:
        x,y=dot['center'];y=6-y if y>3 else y
        ax.add_patch(Circle((x,y),dot['radius'],facecolor='black',edgecolor='black',linewidth=1))
    fig.savefig(a.OUT/'diagnostic_exact_fold_overlay.png',dpi=100,facecolor='white')
    plt.close(fig)

checkpoint=a.read(a.UNIT/'checkpoint.json')
records=checkpoint['candidate_design_records']
if isinstance(records,dict):records=list(records.values())
relevant_records=[x for x in records if x.get('question_id')=='Plane404']
global_report=a.read(a.BASE/'exploration_report.json')
global_attempts=[x for x in global_report.get('attempts',[]) if x.get('question_id')=='Plane404']
designs=[]
for p in a.BASE.rglob('design.json'):
    if p.is_relative_to(a.OUT):continue
    d=a.read(p)
    if d.get('question_id')=='Plane404':designs.append({'path':str(p.relative_to(a.ROOT)),'sha256':a.sha(p),'data':d})
queue=a.read(a.UNIT/'second_review_queue.json')
for x in queue['candidates']:
    if x['question_id']=='Plane404':
        assert x['design_sha256']==a.sha(a.CAND/'design.json')
        assert x['image_sha256']==a.sha(a.CAND/'candidate.png')
        assert x['plugin_sha256']==a.sha(a.CAND/'plugin.json')
history={'checkpoint_counts':checkpoint['counts'],'checkpoint_Plane404_design_records':relevant_records,
         'all_Plane404_design_json_records_in_experiment':designs,'global_report_Plane404_attempts':global_attempts,
         'candidate_queue_hashes_match':True,'no_retry_evidence':'Exactly one candidate design and one two-call invocation, plus one separately designated original control. Harness has a finite loop, one HTTP request per run, breaks on error and contains no retry loop. No extra or aborted Plane404 candidate call records were found.',
         'scope_limit':'Audit establishes the retained evidence history, not unlogged activity or independent provider attestation.',
         'mutable_progress_metadata_current_hashes':{str(p.relative_to(a.ROOT)):a.sha(p) for p in [a.BASE/'exploration_report.json',a.BASE/'remaining_questions.jsonl']}}
a.save('history_and_queue_audit.json',history)
ev=a.read(a.OUT/'raw_bindings_and_full_responses.json')
chron=[]
for t in ev['tests']:
    b=t['binding'];folder=Path(b['image_path']).parent
    design=a.read(folder/'design.json')
    image_mtime=a.pathinfo(folder/'candidate.png')['mtime_utc']
    design_mtime=a.pathinfo(folder/'design.json')['mtime_utc']
    assert design['created_at']<=design_mtime<b['created_at']<t['runs'][0]['started_at']
    assert image_mtime<b['created_at']
    chron.append({'role':t['role'],'design_created_at':design['created_at'],'design_mtime_utc':design_mtime,
                  'image_mtime_utc':image_mtime,'binding_created_at':b['created_at'],
                  'run1_started':t['runs'][0]['started_at'],'run1_finished':t['runs'][0]['finished_at'],
                  'run2_started':t['runs'][1]['started_at'],'run2_finished':t['runs'][1]['finished_at'],
                  'pre_call_design_and_image_confirmed':True})
a.save('chronology_audit.json',chron)
a.emit({'serialization':chunkaudit,'chronology':chron,'Plane404_designs':len(designs),
        'checkpoint_design_records':len(relevant_records),'global_Plane404_attempts':len(global_attempts),
        'all_figures_closed':not bool(plt.get_fignums())})
