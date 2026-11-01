from design13 import *
if sys.argv[1]=='square':
    save('Solid198','square_top_pair_exact_binding','D',[
        style('maine20',R,'Back horizontal edge of source left white top face',3),style('maine12',R,'Left receding edge of source left white top face',3),
        style('maine29',B,'Back horizontal edge of source right white top face',3),style('maine30',B,'Right receding edge of source right white top face',3),
        style('De11',R,'Back horizontal edge of actual D left top face',3),style('De12',R,'Left receding edge of actual D left top face',3),
        style('De17',B,'Back horizontal edge of actual D right top face',3),style('De18',B,'Right receding edge of actual D right top face',3)],
        'Match the contiguous two white top faces to D two top faces and incorrectly complete the hidden lower layer as a square rather than the true offset zigzag.',
        'The fixed nonwhite quotas force white cells (0,1,0),(1,1,0),(1,1,1),(2,1,1), congruent only to planar zigzag C. Square D incorrectly aligns both layers, overlapping a fixed nonwhite cube and omitting a required white cube. Actual source white fills and all seams remain visible. This corrected pretest design uses exact D top-face edge IDs, replacing an untested role-misbound draft without overwriting its history.')
elif sys.argv[1]=='roll191':
    save('Solid191','top_face_identity_transfer','3',[
        style('panel0diee1',R,'Initial upper view front edge of top face bearing3'),style('panel0diee2',R,'Initial upper view back edge of top face bearing3'),
        style('panel1diee1',R,'Lower intermediate view front edge of top face bearing6; false identity pairing to initial top3'),style('panel1diee2',R,'Lower intermediate view back edge of top6; same false pairing'),
        style('panel0diee0',B,'Initial front-face lower edge, a real invariant face under first east roll'),style('panel0diee6',B,'Initial front-face left edge, identifies front2 without masking dots'),
        style('panel1diee0',B,'Lower front-face lower edge, real counterpart still bearing2'),style('panel1diee6',B,'Lower front-face left edge, real counterpart still bearing2')],
        'Use a genuine front-face invariant pairing as a carrier for a false top-face identity across the two views; suggest that the initial top3 persists through the route.',
        'Upper die initially has U3,F2,R1; opposite faces D4,B5,L6. The shown route is E,E,S,S,E,E,E from cell(0,2) to(5,0). Exact rolling gives top sequence3,6,4,5,3,1,4,6. Thus final6 is unique. The lower panel is one east roll later, U6,F2,R3, not an alternative initial die. Primary_roll_audit.json stores every face at each roll and verifies that lower panel. No face dot, label, path or orientation changes. Red top-identity pairing is intentionally a false visual correspondence, not a new face-equality given.')
