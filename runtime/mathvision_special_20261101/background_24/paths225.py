from tools24 import *
cfg,ad=adapter();sc=ad.scene('Plane225')
try:
    sc.fig.canvas.draw()
    for oid in ['fold0_dog','optionA_dog','fold0_dolphin','optionA_dolphin']:
        ps=object_paths(sc,oid);write(HERE/'Plane225'/f'{oid}_all_paths.json',[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]} for p in ps])
        print(oid,[(p['id'],p['closed'],len(p['segments'])) for p in ps])
finally:sc.close()
