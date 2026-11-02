import env
from env import OWN
from prepare import read,dump
from create_designs import make,interval,BLUE,GREEN

if __name__=='__main__':
    old=OWN/'Plane407/r43_full_base_to_center_half_binding'
    d=read(old/'design.json');c=read(old/'context.json')
    dump(old/'precall_hold.json',{'status':'HOLD_BEFORE_ANY_API','reason':'Native audit found styled centreline overpaints exact center pixels of right two black center dots. Untested draft and PNG retained. Same conceptual hypothesis will receive a pre-call occlusion repair, not be counted as another API experiment.','api_calls':0,'source_and_old_history_changed':False})
    p0,p1,p2,p3=2.5714285714285716,11.571428571428573,19.285714285714285,28.28571428571429
    b0,b1=5.142857142857143,20.571428571428573
    top=lambda x:.5+(36.-x)/144.
    # The native center marker is the frozen 64-gon, radius0.2.
    # Use its actual leftmost coordinate, never draw through its black interior.
    scene=read(env.PROJECT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane407/scene.json')
    rims={o['id']:min(x[0] for x in o['points']) for o in scene['objects'] if o['id'] in ['o7','o9']}
    actions=[interval(c,'o0',top(18),top(b0),BLUE,2),interval(c,'o4',(b0-p0)/(p1-p0),(rims['o7']-p0)/(p1-p0),BLUE,2),interval(c,'o0',top(36),top(b1),GREEN,2),interval(c,'o5',(b1-p2)/(p3-p2),(rims['o9']-p2)/(p3-p2),GREEN,2)]
    roles=d['marker_roles']
    roles[1]['role']+=' Colored portion stops at the exact left rim of the original black centre disk, leaving the disk wholly black; the existing black dot still identifies the true half-width endpoint.'
    roles[3]['role']+=' Colored portion likewise stops at the exact left rim of its original black centre disk.'
    make('Plane407','r43_full_base_to_center_half_clear_dots','E',actions,roles,d['primary_math_proof'],d['mechanism'],
       'Original unit03 had no design/call. New substantive hypothesis is the same source full-width to receiver half-width correspondence recorded in the untested r43 draft. That first local draft is retained HOLD because its colored line overpainted center-dot pixels; before any API, two interval endpoints now stop at the frozen disk rims. This is a technical legibility repair of ONE new hypothesis, not another material hypothesis or a rerun; no call exists on the old local draft.',
       d['human_semantics']+' Both original right centre disks remain black, including exact centre pixels. No text or shape legend is introduced.')
