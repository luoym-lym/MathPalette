from bootstrap import install, OWN, PROJECT, SESSION
ISOLATION=install()
from research import save,load,sha,IDS
import json
from pathlib import Path

def find_matches(node, qids, at='$'):
    found=[]
    if isinstance(node,dict):
        if node.get('question_id',node.get('id')) in qids:
            return [{'json_path':at,'content':node}]
        for k,v in node.items():
            if k in qids: found.append({'json_path':at+'.'+k,'content':v})
            else: found.extend(find_matches(v,qids,at+'.'+k))
    elif isinstance(node,list):
        for i,v in enumerate(node):found.extend(find_matches(v,qids,f'{at}[{i}]'))
    return found

def compact(node):
    # Full reports are loaded; repeated hash and exact-control annexes have their
    # own immutable file binding, leaving all semantic findings to read here.
    if isinstance(node,dict):
        return {k:compact(v) for k,v in node.items() if k not in ['reviewed_source_evidence_hashes','timestamps_and_immutable_artifact_hashes','formal_source_hash_audit','per_file_hashes','input_hashes','source_hashes','all_choice_feature_comparison','marker_reviews','evidence_bindings','independent_evidence_bindings','source_preservation_audit','preservation_audit','evidence_file_hashes','frozen_input_audit','scoped_input_audit']}
    if isinstance(node,list):return [compact(v) for v in node]
    return node

files=[]
for unit in ['background_22','background_16','plane_explore']:
    p=SESSION/unit/'checkpoint.json'
    d=load(p)
    matching=find_matches(d,set(IDS))
    files.append({'path':str(p),'sha256':sha(p),'matching_sections':matching})
save(OWN/'old_checkpoint_sections.json',files)
for f in files: print(json.dumps({'kind':'checkpoint',**f},ensure_ascii=False,separators=(',',':')))

for folder in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']:
    p=SESSION/'independent_review'/folder/'independent_review.json'
    d=load(p)
    save(OWN/'reference_read'/f'{folder}.json',{'source':str(p),'sha256':sha(p),'full_report':d})
    print(json.dumps({'kind':'reject_report','path':str(p),'all_top_level_keys':list(d),'content':compact(d)},ensure_ascii=False,separators=(',',':')))
