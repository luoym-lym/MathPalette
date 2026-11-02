from worker_env import *
import argparse
import gc

def initial():
    init={'started_at':now(),'unit':'u07_corner_cut','assigned':['Plane194','Plane245'],
          'brief_sha256':sha(OWN/'brief.txt'),'assignment_sha256':sha(OWN/'assignment.json'),
          'isolation':ISOLATION,'environment':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},
          'pid':os.getpid(),'argv':sys.argv,'no_subagents_servers_worktrees':True}
    write(OWN/'initialization.json',init,True)
    write(OWN/'checkpoint.json',{'updated_at':now(),'status':'reading_and_primary_mathematics','questions':{q:{'status':'in_progress','new_API_calls':0} for q in init['assigned']},'new_API_calls':0})
    write(OWN/'second_review_queue.json',[])
    history=read(TASK/'history_index.json')
    histories=[]
    for h in history['questions']:
        if h['question_id'] not in init['assigned']:continue
        paths=set(h['other_scoped_history_file_references']+h['additional_math_manual_history_references']+h['independent_review_references'])
        for d in h['designs']:
            paths.add(d['design_path']); paths.add(d['plugin_path'])
            for p in (PROJECT/d['directory']).rglob('*'):
                if p.is_file() and p.suffix in ('.json','.txt','.md','.log','.bin','.png','.py'):
                    paths.add(p.relative_to(PROJECT).as_posix())
        records=[]
        for p in sorted(paths):
            path=PROJECT/p
            detail={'path':p,'sha256':sha(path),'bytes':path.stat().st_size}
            if path.suffix=='.json':
                value=read(path)
                detail['json_fully_parsed']=True
                if path.name=='request.json':
                    detail['sent_question']=value['messages'][1]['content'][0]['text']
                    detail['image_data_url_length']=len(value['messages'][1]['content'][1]['image_url']['url'])
                elif path.name.endswith('_response.json'):
                    detail['complete_raw_response']=value
                elif path.name in ('primary_prescreen.json','design.json','manual_final_review.json','primary_review.json','mathematical_audit.json'):
                    detail['complete_content']=value
                del value
            records.append(detail);gc.collect()
        histories.append({'question_id':h['question_id'],'history_index_entry':h,'actual_files_read':records})
    write(OWN/'history_audit.json',histories,True)
    references={}
    for qid,v in read(TASK/'reference_manifest.json').items():
        folder=TASK/v['directory'];entry={}
        for n in ('C01.json','recipes.json','reference.json'):
            value=read(folder/n)
            entry[n]={'sha256':sha(folder/n),'complete_content':value}
        entry['C01.png']={'sha256':sha(folder/'C01.png'),'actually_viewed_in_conversation':True}
        assert entry['C01.png']['sha256']==v['png_sha256']
        assert entry['C01.json']['sha256']==v['plugin_sha256']
        references[qid]=entry
    write(OWN/'references_read.json',references,True)
    protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md',
        'PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md',
        'PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']
    write(OWN/'protocol_fingerprints.json',{p:sha(PROJECT/p) for p in protocols},True)
    for qid in init['assigned']:
        e=eligibility(qid);write(OWN/qid/'eligibility_initial.json',e,True)
        assert e['eligible'],qid
    config,adapter,metadata,renderer=setup_renderer()
    from workbench_io import environment_versions
    for qid,meta in metadata.items():
        write(OWN/qid/'context.json',meta,True)
        write(OWN/qid/'input_manifest.json',adapter.question_fingerprint(qid) if hasattr(adapter,'question_fingerprint') else {'adapter_manifest':adapter.manifest,'dependencies':adapter.dependencies(qid)},True)
        scene=adapter.scene(qid)
        try:
            geometry=[]
            for oid,artists in scene.artists.items():
                for a in artists:
                    obj={'id':oid,'artist_type':type(a).__name__}
                    if hasattr(a,'get_data'):obj['data']=[list(map(float,c)) for c in a.get_data()]
                    if hasattr(a,'get_xy'):obj['xy']=a.get_xy().tolist()
                    if hasattr(a,'get_text'):obj['text']=a.get_text()
                    geometry.append(obj)
            write(OWN/qid/'captured_geometry.json',geometry,True)
        finally:scene.close()
    write(OWN/'render_environment.json',{'versions':environment_versions(),'config':config,'adapter_manifest':adapter.manifest},True)
    print(json.dumps({'initialized':True,'history_files_read':{h['question_id']:len(h['actual_files_read']) for h in histories},'contexts':{q:len(m['objects']) for q,m in metadata.items()}},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['initial']);args=parser.parse_args()
    if args.mode=='initial':initial()
