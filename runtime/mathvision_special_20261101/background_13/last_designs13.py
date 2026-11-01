from design13 import *
mode=sys.argv[1]
if mode=='corner':
    save('Solid162','white_planarity_axis_swap','E',[
        style('maine20',R,'Horizontal source edge of white top terminal',3),
        style('maine12',B,'Receding source edge of same white top terminal',3),
        style('maine35',G,'Vertical source edge of lower white side terminal',3),
        style('Ee12',R,'Horizontal upper branch edge of E, falsely matching top white terminal',3),
        style('Ee21',B,'Receding rear branch edge of E, falsely matching source white top-depth direction',3),
        style('Ee16',G,'Vertical upper branch edge of E, falsely binding source lower side terminal')],
        'Associate three source boundary directions with E three spatial arms; infer a nonplanar tripod from projected faces instead of recovering the forced planar T.',
        'Exactly four gray and four dark cells are observed, so the white complement is (0,1,0),(1,1,0),(2,1,0),(1,1,1). It is planar, with three collinear cubes and one central branch: optionD. E has three perpendicular branch directions and affine dimension3, hence cannot be congruent. The three colored direction correspondences concern existing edges on visible white faces, not true hidden voxel adjacency. No material fill or cube division changes. This corrects the untested predecessor target-role misbinding; the predecessor is rejected, kept intact, and never sent to API.')
elif mode=='square':
    save('Solid198','visible_pair_to_square_top','D',[
        style('maine20',R,'Back horizontal edge of first visible white top cell',3),
        style('maine12',R,'Left receding edge of first visible white top cell',3),
        style('maine29',B,'Back horizontal edge of second visible white top cell',3),
        style('maine30',B,'Right receding edge of second visible white top cell',3),
        style('De2',R,'Back top edge of D left top cube, paired to source first white face',3),
        style('De3',R,'Left receding edge of D left top cube',3),
        style('De9',B,'Back top edge of D right top cube, paired to source second white face',3),
        style('De12',B,'Right receding edge of D right top cube',3)],
        'Match the contiguous pair of white top faces to the two contiguous top faces of square D; overcomplete the unseen lower pair directly below instead of applying the nonwhite quotas.',
        'All nonwhite piece cells are fixed by four visible cubes of each material. White complement is (0,1,0),(1,1,0),(1,1,1),(2,1,1), a planar zigzag optionC. Its lower pair is offset one unit from its upper pair. D would align both pairs to make a2x2 square and contradict observed nonwhite cells. Only the visible two-face fragment is matched; original materials, seams and views remain frozen. This square-completion misconception differs from predecessor E long-row terminal separation.')
elif mode=='roll':
    items=[]
    for target in ['ground18part0','ground24part0','ground35part0','ground0part0','ground13part0','ground19part0']:
        items.append(style(target,R,'One unit curb on the opposing east/west travel runs; red falsely suggests inverse roll cancellation',2))
    for target in ['ground26part0','ground28part0','ground31part0','ground4part0','ground7part0','ground10part0']:
        items.append(style(target,B,'One unit curb on opposing north/south runs; blue falsely suggests inverse cancellation',2))
    items.extend([style('diee0',R,'Die initial horizontal bottom edge ties red path family to its initial roll axis'),style('diee4',B,'Die initial receding bottom edge ties blue path family to second roll axis')])
    save('Solid91','opposed_run_cancellation','1',items,
        'Pair the opposite path runs by color and match the die initial edges, tempting cancellation of opposite three-roll sequences despite their noncommuting interleaving.',
        'The path has three east rolls, three south rolls, three west rolls and three north rolls. Assign the six faces fixed distinct labels and propagate exact quarter-turn rotations. The one-circuit orientation is a nonidentity order-three rotation (cyclically permutes three axes); two circuits still differ and three return all six labels. Therefore3 is unique. Grouping opposite runs by color cannot commute intervening rotations or change the legal path or twelve cells. No colored points/pips or arrows are added.')
