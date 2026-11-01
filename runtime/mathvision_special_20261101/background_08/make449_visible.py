from tools08 import *
old=HERE/'Plane449/side_label_role_binding_clean';p=json.loads((old/'plugin.json').read_text(encoding='utf-8'));d=json.loads((old/'design.json').read_text(encoding='utf-8'))
write(old/'prescreen_rejection.json',{'tested':False,'reason':'Actual PNG shows the earlier-drawn slot seam overlays do not survive later shared-edge black outlines consistently. No API calls. Preserve and replace with the visible later-drawn left edges.'})
m=json.loads((HERE/'Plane449/context.json').read_text(encoding='utf-8'))
def seam(o,c):
    t=next(t for t in m['canvas']['targets'] if t['id']==o);p=t['partial_paths'][0]
    return {'type':'set_object_style','target':o,'color':c,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':.75,'end':1,'wrap':False}}
render('Plane449','visible_side_label_role_binding',p['params']['actions'][:4]+[seam('slotII','#DC2626'),seam('slotIII','#2563EB')],'B',d['mechanism'],d['primary_mathematical_proof'],d['marker_roles'])
