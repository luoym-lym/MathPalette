from render06 import *
SPEC={
'wrong':'B',
'mechanism':'Four ordered source symbols at(row1,col0),(row1,col1),(row1,col2),(row2,col2) form a genuine local copy of D. Four corresponding symbol outlines in D receive the same red/blue/green/orange roles. This privileges a locally valid D placement; after spending its three diamonds, only one source diamond remains, inviting the wrong claim that B(three diamonds) is unused. The global star/circle inventory rules out this greedy placement. This is a source-part correspondence, not coloration of the predicted wrong B.',
'math':'Count the source:5stars,4diamonds,4circles,3arrows. A=(3stars,1diamond), B=(3diamonds,1circle), C=(2stars,1circle), D=(1star,3diamonds), E=(2circles,3arrows). Allfive together give6stars,7diamonds,4circles,3arrows, so removing D gives exactly the source inventory. Removing any other option does not. Existence: using source columns0..3 and rows0..3 from top, A occupies the top-left2x2; B occupies(2,0),(2,1),(2,2),(1,2); C occupies(0,2),(0,3),(1,3); E occupies(3,0),(3,1),(3,2),(3,3),(2,3). These four shapes fit by quarterturns/translations with the pictured symbols, including E arrows rotated to point right. Thus D is the unique unused piece. The marked local D consumes cells(0,1),(1,1),(2,1),(2,2), but cannot extend to a valid four-piece tiling.',
'human_gate':'All sixteen source cells and every star,diamond,circle andarrow remain present and recognizable. Every optionletter and internal symbol remains black or a fixed allowed contour color, with no fill, count,geometry or symbol orientation changed. B, the preset wrong answer, receives no mark. Color pairs identify concrete existing symbols and do not assert extra equality or changed piece rules.',
'limits':['Source symbols are small in the formal768px layout. Candidate must be inspected at native size; no resized solverimage is permitted.','No original control or per-marker ablation is provided.'],
'marks':[
{'target':'source0_1_star','color':RED,'role':'Red source star at(row1,col0) anchors the left endpoint of the locally fitting D part.'},
{'target':'option3_0_star','color':RED,'role':'Red D star binds the same local-part anchor to source(row1,col0).'},
{'target':'source1_1_diamond','color':BLUE,'role':'Blue source diamond at(row1,col1) marks the middle position in the local D top row.'},
{'target':'option3_1_diamond','color':BLUE,'role':'Blue D middle diamond binds that ordered source position.'},
{'target':'source2_1_diamond','color':GREEN,'role':'Green source diamond at(row1,col2) marks the right top position and elbow of the local D.'},
{'target':'option3_2_diamond','color':GREEN,'role':'Green D top-right diamond binds that elbow to the local source shape.'},
{'target':'source2_2_diamond','color':ORANGE,'role':'Orange source diamond at(row2,col2) marks the downward arm of the locally fitting D.'},
{'target':'option3_3_diamond','color':ORANGE,'role':'Orange D lower diamond binds the final member of the four-symbol local correspondence.'}
]}
render('Plane165','greedy_local_D_binding',SPEC)
