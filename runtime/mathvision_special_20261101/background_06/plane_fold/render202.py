from render06 import *
SPEC={
'wrong':'4',
'mechanism':'The diagonally opposite outer-ear tips are paired red(TL/BR) and blue(TR/BL). The rising diagonal foldline is red and the falling diagonal is blue, binding those selected approximate ear-tip correspondences to the two invalid reflection axes. The intended misconception is to infer full kangaroo reflection symmetry from four nearly square corner features, and count both colored diagonals in addition to the two genuine horizontal/vertical axes. Exact silhouettes and their orientation remain unchanged.',
'math':'The displayed line set contains exactly x=0,y=0,y=x,y=-x. The four kangaroos are produced by reflecting a single upper-left outline in x=0 and y=0, so both horizontal and vertical folds superpose the corresponding figures. A diagonal swaps horizontal and vertical features, and does not preserve even the set of outer ear tips: upper-left(-0.96,0.98) under y=x goes to(0.98,-0.96), whereas the lower-right outer ear tip is(0.96,-0.98). More decisively, reflecting the snout/head outline sends it into an ear/neck configuration; the entire frozen head-segment set fails either diagonal. Only the two orthogonal midlines work. Appearance points lie exactly at four preexisting endpoints and do not define extra lines or modify the target count.',
'human_gate':'Only four existing outer-ear endpoints receive fixed50pt2 point overlays, and the two existing diagonal lines receive1.5pt color. The full ears, snouts, eyes, neck curves, squareboundary and both valid midlines remain visible at native768px. The points identify existing tips, without adding another animal or extra candidate foldline. No equality or angle symbol is added.',
'limits':['The selected tip positions only approximately correspond under diagonals; the mismatch is explicitly part of the false partial-feature hypothesis, not an asserted geometric fact.','No original control or statistical marker ablation.'],
'marks':[
{'snap_point':'vertex_45173fd01581b456','id':'ear_tl_red','color':RED,'role':'Upper-left original outer-ear tip, red first endpoint of the false rising-diagonal feature correspondence.'},
{'snap_point':'vertex_bcc321f9a5eaad74','id':'ear_br_red','color':RED,'role':'Lower-right original outer-ear tip, red approximate partner falsely used as the full-outline reflection image.'},
{'target':'o1603','color':RED,'width':1.5,'role':'Existing rising diagonal y=x is red to bind the TL/BR selected-tip pair to the wrong reflection axis.'},
{'snap_point':'vertex_0ec5fe1da6e76691','id':'ear_tr_blue','color':BLUE,'role':'Upper-right original outer-ear tip, blue first endpoint of the false falling-diagonal feature correspondence.'},
{'snap_point':'vertex_e65c368be52195ca','id':'ear_bl_blue','color':BLUE,'role':'Lower-left original outer-ear tip, blue approximate partner falsely used as the whole kangaroo reflection image.'},
{'target':'o1604','color':BLUE,'width':1.5,'role':'Existing falling diagonal y=-x is blue to bind the TR/BL selected-tip pair to the other wrong axis.'}
]}
render('Plane202','outer_ear_diagonal_binding',SPEC)
