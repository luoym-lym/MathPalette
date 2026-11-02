from render20 import *

q='Plane431'
actions=[{'type':'set_object_style','target':'o127','color':R,'linewidth_pt':2},edge(q,'o0',1/8,2/8,B),edge(q,'o0',2/8,3/8,B)]
roles=[
 'Existing physical wheel circumference in A: a complete circular shape identifies the radius-based motion motif used incorrectly at a concave track corner.',
 'Existing A track descending face into its first concave valley identifies one side of the V contact constraint; the grey material is unchanged.',
 'Existing A track ascending face out of the first concave valley identifies the other simultaneous-contact constraint; no extra face/vertex is introduced.'
]
for index in range(33,63):
    actions.append({'type':'set_object_style','target':f'o{index}','color':R,'linewidth_pt':2})
    roles.append(f'o{index}: native polyline segment {index-32}/30 of A first smooth concave-valley locus bend, collectively one continuous existing curved feature. Red pairs this bend to the red wheel circumference, suggesting that the wheel center traces a radius arc at a valley as well as a crest. All 30 fragments are needed to color this one original bend continuously, not 30 separate decorations.')
make(q,'wheel_circle_to_concave_arc_binding','A',actions,
 'Pair the actual wheel circumference with the existing rounded first valley locus in A, and identify the two physical valley faces in blue. The new hypothesis is erroneous circular motion around a concave vertex, distinct from the earlier B hypothesis of retaining a sharp convex crest. Preset A is frozen for this new PNG and its own pair; no earlier result is reused.',
 'At a straight track face, the wheel center is offset by perpendicular distance r. At a convex crest it can pivot on the crest so its center follows a circle of radius r about that crest. At a concave V, before the apex can be reached the wheel touches both faces; its center is the intersection of the two face-offset lines. It then leaves the incoming straight center path and follows the outgoing straight path with a sharp switch at that intersection. A smooth arc centered on the valley vertex would intersect one face or lose the required contact relation, so A is wrong. Only E has rounded crests and sharp valleys. Original track and proposed loci, wheel size, all paths, labels and arrowheads are untouched except for existing stroke colors/width2. The red native bend consists of 30 already-existing straight sampling fragments; no point or path has been added. This design does not retest or alter the earlier B PNG/preset.',roles)
