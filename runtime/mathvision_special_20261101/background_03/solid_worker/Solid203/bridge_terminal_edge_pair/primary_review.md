# Solid203 / bridge_terminal_edge_pair — primary review

This is a possible candidate for a NEW independent second-review task. It has not been published as qualified and has no Pass/Collect record.

The immutable predeclared target is A; the formal answer is E. Both complete QuickTest3 responses finish with A (run 1: “Correct Answer: A”; run 2: “Final Answer: A:A”). Both have finish_reason=stop and truncated=false. The same frozen PNG, design and request body were used for the two independent requests. Full answers were manually read, including the erroneous intermediate geometry.

## Unique mathematical solution

Use regular-octahedron vertices ±e1, ±e2, ±e3. Each face takes one vertex from each antipodal pair. Across any shared edge, the third vertices of the adjacent triangular faces are antipodal. Start the net face (n0,n2,n3) at (e1,e2,e3) and propagate over all eight faces. This gives n4=-e1, n5=-e3, n6=-e2, n7=e1, n8=e3, n9=-e1, and n1=-e3. All eight folded face triples are distinct. Thus x=n8–n9 is {e3,-e1}; E=n3–n4 is the same unordered pair. A=n7–n8 is {e1,e3}, B and C have {e1,-e3}, and D has {e1,e3}. E is the sole labelled match. Exact propagation and all labelled endpoints are recorded in folding_verification.json. These coordinates are verification evidence only and are not sent to the model.

## Every marker's role and actual appearance

1. line_20 (n8–n9), the original boundary carrying x, is red #DC2626 and 2 pt. This anchors the requested target edge in a visual correspondence pair.
2. line_24 (n7–n8), the original boundary carrying A, receives the same color and width. This is the upper free boundary of the adjacent terminal triangle. Pairing these two terminal edges suggests a false local seam closure and bypasses tracking the full six-triangle strip.

Both selected objects were checked against the frozen scene and the actual candidate PNG. They are the two distinct edges carrying x and A; they do not merely frame the same face. Removing either marker breaks the target-to-candidate correspondence. There are no extra marks. Labels, original edge endpoints, fills, visibility style, 3D geometry, projection and question are unchanged. The red boundary pair neither adds a mathematical condition nor changes face incidence.

The actual 768×768 PNG was viewed. x and A remain clearly readable beside their respective edges; all other labels and the reference octahedron remain visible and unchanged. The pair is compact and does not cover geometry or labels.

## Technical checks

Current accepted/collected records were read before work; the question was eligible. The prepared plugin/design/PNG were copied byte-for-byte into this runtime folder. A runtime-local copy of the dedicated bridge wrapper redirects only its PROJECT/TASK location; the formal renderer and PluginRenderer are unchanged. Fresh inspect_question passed the formal-PNG no-op guard. The actual schema/default normalization passed, two new redraws were byte-identical, and both matched the prepared/tested PNG exactly. Frozen input fingerprints, exact formal source_key=test:1943 and revision, copy hashes and replay metadata are retained locally. No formal source, workbench state, approvals, recipes or indices were written.

## Effectiveness and causal limits

Run 1 explicitly attributes closure to the two red line segments and their apparent V-shape. Run 2 also follows the mistaken local closure, while making additional errors in triangle counting. Two target hits are evidence for this fixed image and preset, not a statistical reliability estimate. A separate original-PNG control is recorded in control_tests; its final outcomes are in manual_results.json/checkpoint.json. The control does not alter the candidate's predeclared target or count toward its two hits. Independent second review is still required for mathematical rigor, information targeting, marker necessity and clarity.
