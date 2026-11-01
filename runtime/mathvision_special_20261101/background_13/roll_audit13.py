from tools13 import *
def roll(d,a):
    z=dict(d)
    if a=='E':z.update(U=d['L'],R=d['U'],D=d['R'],L=d['D'])
    elif a=='W':z.update(U=d['R'],L=d['U'],D=d['L'],R=d['D'])
    elif a=='S':z.update(U=d['B'],F=d['U'],D=d['F'],B=d['D'])
    elif a=='N':z.update(U=d['F'],B=d['U'],D=d['B'],F=d['D'])
    else:raise ValueError(a)
    return z
d={'U':3,'D':4,'F':2,'B':5,'R':1,'L':6};seq=[{'step':0,'faces':d}]
for i,a in enumerate('EESSEEE',1):d=roll(d,a);seq.append({'step':i,'direction':a,'faces':d})
assert d['U']==6
write(TASK/'Solid191/primary_roll_audit.json',{'coordinate_convention':'E=+x, S=-y; F is face toward-y. Right hand rigid rolling, all labels carried exactly.','start':seq[0]['faces'],'route':'EESSEEE','states':seq,'lower_panel_matches_after_first_E':seq[1]['faces']['U']==6 and seq[1]['faces']['F']==2 and seq[1]['faces']['R']==3,'unique_final_top':6})
initial={k:k for k in ['U','D','F','B','R','L']};d=initial;states=[]
for lap in range(1,4):
    for a in 'EEESSSWWWNNN':d=roll(d,a)
    states.append({'lap':lap,'faces':d,'all_initial':d==initial})
assert [r['all_initial'] for r in states]==[False,False,True]
write(TASK/'Solid91/primary_roll_audit.json',{'method':'Label all six faces distinctly; propagate every quarter roll exactly, preserving opposite pairs and orientation.','initial':initial,'one_circuit':'EEESSSWWWNNN','lap_end_states':states,'unique_first_return_circuits':3,'note':'Choosing the opposite circuit orientation inverts the same order3 transformation.'})
print('Solid191 tops',[r['faces']['U'] for r in seq]);print('Solid91 return',[r['all_initial'] for r in states])
