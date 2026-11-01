from render06 import *
SPEC=copy.deepcopy(SPEC203)
SPEC['mechanism']='Three individual source bottom edges in the lower grey L receive red/blue/orange identities, each matched to its +4-column translated bottom edge. This unit-edge correspondence replaces the first design whole-L grouping: it individually binds source(0,1)→(4,1), source(1,1)→(5,1), source(0,0)→E(4,0). The intended misconception is translation instead of reflection, leaving C apparently uncovered while E is falsely covered. No new line,fill or text is added.'
SPEC['marks']=[
 {'target':'o16','interval':[0,1/4],'color':RED,'role':'Red original lower-L grey cell(0,1) bottomedge identifies the first individual source member.'},
 {'target':'o8','interval':[4/6,5/6],'color':RED,'role':'Red target bottomedge at(4,1) binds this destination to source(0,1) by the wrong +4 translation.'},
 {'target':'o17','interval':[0,1/4],'color':BLUE,'role':'Blue original grey cell(1,1) bottomedge identifies the source horizontal-arm member.'},
 {'target':'o8','interval':[5/6,1],'color':BLUE,'role':'Blue target bottomedge at(5,1) binds the horizontal-arm member by the same wrong translation.'},
 {'target':'o18','interval':[0,1/4],'color':ORANGE,'role':'Orange original grey cell(0,0) bottomedge identifies the decisive bottom source member.'},
 {'target':'o7','interval':[4/6,5/6],'color':ORANGE,'role':'Orange E-cell bottomedge at(4,0) binds E to source(0,0), despite its true mirror image being C(5,0).'}
]
SPEC['human_gate']='Only six existing unit bottom edges are recolored1.5pt. All original source outlines and six greyfills remain, and every letter is entirely unobscured. The black thick fold and all gridline lengths are unchanged. Three colored edge pairs preserve individual source-to-destination identities; colors do not establish a new formal mapping rule.'
SPEC['limits'].append('First distinct whole-L-contour design produced full finalanswers B/E and failed its C preset; no results are combined across images. This new unit-edge identity design has its own immutable C preset and two calls.')
render('Plane203','three_unit_edge_translation',SPEC)
