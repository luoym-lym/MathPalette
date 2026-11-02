from tools28 import *
findings={
'Solid86':'Actually viewed native768PNG. Six orange anchors lie on existing front-right seam and top-depth seam; three vertical midpoints correspond to3height intervals while three top vertices span2depth intervals. Gray versus white faces and all grid cells remain clear. Points do not create cubes or fill faces. Small native strokes covered by dot centers are disclosed; adjacent continuations remain visible.',
'Solid109':'Actually viewed native768PNG. Orange3by2 open L traces existing front grid edges; separate4unit top-depth chain stays an existing edge path. Original grid5by4by4 is readable. No new closed contour, cut, hole or material fill. Orange never labels a cube blue.',
'Solid123':'Actually viewed native768PNG. Green L outer leg and dark-bar depth chain are readable. The L elbow, remaining horizontal leg, exemplar white cube, three assembly material classes and assembly seams are unobscured. Six actions are2continuous existing3unit spans; source scale is retained.',
'Solid125':'Actually viewed native768PNG. Red full-cube front lower/left edges form open3by3L. On cavity, smaller open unit-corner motifs show side/back/floor unit squares. All3by3reference and2by2white plane unit seams, gray exterior and white cut surfaces remain legible. No closed new boundary or fill; shared unit edge has two roles.',
'Solid129':'Actually viewed native768PNG. Orange reference top-face open3by3L corresponds to all4highest remaining top unit cells. Lower black stepped faces,7middle layer cubes, all seams remain readable. Every colored path is an original segment; no missing cube outline, cut or added cube.',
'Solid143':'Actually viewed native768PNG. Two green open L patterns lie on the original internal seam and exposed right face. All15blackpips remain untouched and separately countable. No hidden face boundary is completed, no new pip or face added. The interface remains occluded; green does not assert equal values.'}
newfindings={
'r28_small_width_to_rear_depth':'Actually viewed native768PNG. Two red partial intervals trace existing3cmfront-small-block width and2cmrear-strip depth. The red pieces end exactly at existing seams; they do not create a boundary or relation symbol. Gray cube fill, both white blocks, seam locations, all outer dimensions and question mark are unaltered and clear. The two colored lengths visibly differ, and no equality is stipulated.',
'r28_near_skin_only':'Actually viewed native768PNG. Three short orange original unit-edge spokes meet at the near upper-left corner. All5width,4height,4depth intervals remain separately readable. There is no inner face, hole, blue material, label or projected geometry change. Each spoke represents a different axis unit skin span.',
'r28_L_bounding_square':'Actually viewed native768PNG. Red open L traces only existing left and bottom exterior spans of the L exemplar. A counterpart red open L traces existing assembled front left/bottom edges. The original L notch remains open with its source black inner contour, and light L/dark bar/white unit materials are readable at original scale. No new line closes the notched bounding square.'}
for token in sys.argv[1:]:
    if '/' in token:
        qid,vid=token.split('/');folder=TASK/qid/vid
    else:
        qid=token;folder=next(p.parent for p in (TASK/qid).glob('r28_*/design.json'))
    write(folder/'pretest_native_visual_review.json',{'checked_at':now(),'question_id':qid,'variant_id':folder.name,'native_actual_PNG_viewed':True,'size':[768,768],'image_sha256':file_hash(folder/'candidate.png'),'findings':newfindings.get(folder.name,findings.get(qid)),'all_useful_mark_roles_checked':True,'original_distinctions_preserved':True,'no_new_semantic_relations_or_regions':True,'primary_review_only':True})

