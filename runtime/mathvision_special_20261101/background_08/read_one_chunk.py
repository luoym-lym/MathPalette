from tools08 import *
q,v,n,start,end=sys.argv[1:];folder=next((HERE/q/v/'tests').glob('quicktest3_*'));r=json.loads((folder/f'run_{int(n):02d}.json').read_text(encoding='utf-8'));answer=r['answer'];a=int(start);b=int(end)
print(json.dumps({'characters':len(answer),'chunk_start':a,'chunk_end':min(b,len(answer)),'response_model':r['response_model'],'thinking_field_length':len(r.get('thinking','')),'finish_reason':r['finish_reason'],'truncated':r['truncated']}));print(answer[a:b])
