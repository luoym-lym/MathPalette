from tools51 import *

def history(qids):
    for qid in qids:
        roots=[p for p in BASE.glob('**/'+qid) if p.is_dir() and not p.is_relative_to(HERE)]
        manifest={}
        for root in roots:
            for p in root.rglob('*'):
                if p.is_file(): manifest[str(p)]=sha(p)
        out=HERE/qid if qid in IDS else HERE/'related_history'/qid
        write(out/'history_files.json',manifest)
        print('\nQUESTION',qid,'files',len(manifest))
        for name in manifest:
            p=Path(name)
            if p.name in ('design.json','assessment.json','primary_math.json','primary_review.json','primary_visual_review.json','primary_first_test_review.json','primary_pretest_revalidation_46.json','aborted.json','run_01_started.json','run_02_started.json','run_01.json','run_02.json'):
                print('\nFILE',p)
                if p.name in ('run_01.json','run_02.json') and p.with_name(p.stem+'_response.json').exists():
                    try: print(json.dumps({k:v for k,v in read(p).items() if k not in ('answer','thinking')},ensure_ascii=False))
                    except Exception as error: print('MALFORMED',repr(error));print(p.read_text(encoding='utf-8-sig'))
                else: print(p.read_text(encoding='utf-8-sig'))
            elif p.name.endswith('_response.json'):
                print('\nRAW RESPONSE',p)
                try:
                    raw=read(p)
                    for c in raw.get('choices',[]):
                        print('finish_reason:',c.get('finish_reason')); print(c.get('message',{}).get('content')); print('thinking:',c.get('message',{}).get('reasoning_content'))
                except Exception as error:
                    print('MALFORMED:',repr(error)); print(p.read_text(encoding='utf-8-sig'))

def scene(qids):
    for qid in qids:
        e=eligibility(qid);rec=e['record']
        p=PROJECT/BRANCH/rec['scene']; s=read(p)
        item=PROJECT/BRANCH/next(x for x in rec['runtime_dependencies'] if x.endswith('/scene.json'))
        print('\nQUESTION',qid,'formal_scene_sha',sha(p),'item_scene_sha',sha(item),'same',s==read(item))
        print(json.dumps(s,ensure_ascii=False,separators=(',',':')))
        print('\nCONTEXT',qid)
        c=read(HERE/qid/'context.json');print(json.dumps(c,ensure_ascii=False,separators=(',',':')))

if __name__=='__main__':
    if sys.argv[1]=='history': history(sys.argv[2:])
    elif sys.argv[1]=='scene': scene(sys.argv[2:])
