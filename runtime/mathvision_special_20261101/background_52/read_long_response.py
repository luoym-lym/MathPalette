from audit_io import install,OWN,load,sha
install()
import sys,json
p=next((OWN/'Plane483').glob('r52_*/tests/*/run_02_response.json'))
d=load(p);s=d['choices'][0]['message']['content']
chunk=int(sys.argv[1]);size=14000
print(json.dumps({'raw':str(p),'raw_sha256':sha(p),'body_characters':len(s),'chunk':chunk,'start':chunk*size,'end':min(len(s),(chunk+1)*size),'number_of_chunks':(len(s)+size-1)//size}))
print(s[chunk*size:(chunk+1)*size])
