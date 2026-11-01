# Solid MathVision exploration checkpoint

All artifacts are below this runtime directory. No Pass or Collect was performed, and no formal file was edited.

## Results ready for the parent's batch

- `Solid176/false_flap_pair`: predeclared D, independent answers D/D; formal C. Four original flap edges are recolored. The parent team performed an independent mathematical/visual review and tentatively recommended it. `human_review.json` contains explicit folded-cap triangle coordinates. The single original-image control answered B, also wrong, so the evidence proves two hits on the specified D, not an isolated causal effect of the annotation.
- `Solid220/false_face_pair`: raw A/A, original control E correct, but **hold for quality**. The original two marks are Z's upper/lower boundaries because the first is shared with X, so the picture mostly frames Z. Do not deliver it as an informative X/Z correspondence. Two genuinely separate X/Z revisions were independently tested and returned E/E for each, so neither revision qualifies.
- Other tested candidates failed the two-predeclared-hit requirement. Final answer summaries and exact evidence paths are in `CHECKPOINT.json`. Keep failures; do not relabel the intended wrong answer after seeing responses.

## Important renderer finding

`baseline_inventory.json` records the generic Solid workbench adapter: 84/164 eligible questions replayed exactly; 80 failed. This report is retained unchanged.

The existing repository module `dataset_tools/mathvision_workbench.py` already supports **SolidGeometry** and the frozen MathVision renderer. Its `build_scene` preserves the actual native drawing and object IDs. `bridge_adapter.py` is a runtime-only wrapper around that existing bridge and the existing `SolidGeometry/workbench/render_plugins.py`. It does not edit their code or bypass a pixel check.

The wrapper selects runtime cache/temp paths, uses the parent's `runtime_isolation.py` write guard, requires exact formal-PNG baseline pixels, validates all actions with the checked-in schema/PluginRenderer, redraws twice, and checks frozen input hashes before/after rendering. `bridge_baseline_inventory.json` contains the dedicated bridge's whole eligible-set result. Failed generic baselines should not be treated as a permanent inability to design those questions.

To use the wrapper from a new runtime script:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path('runtime/mathvision_special_20261101/solid_explore').resolve()))
from bridge_adapter import RuntimeBridgeAdapter
adapter = RuntimeBridgeAdapter()
context = adapter.inspect_question('Solid166')
# Targets/snap points must come from this returned context.
# Write a new design.json declaring the intended wrong answer before testing.
report = adapter.render_candidate(plugin, new_runtime_candidate_directory)
```

`new_runtime_candidate_directory` must not already exist and must be below root `runtime/`. The helper writes PNG, normalized plugin, context, and render/frozen-input evidence. It launches no API and performs no review.

## Three already investigated candidates prepared for continuation

`bridge_prepared_candidates.json` lists them. All three were actually viewed, use two original-edge style actions, match the formal baseline, and reproduce exactly twice. **None has been API-tested or second-reviewed.**

1. `Solid166/bridge_terminal_edge_pair`: expected wrong `1`, formal `5`. The actual x edge and the incorrect edge 1 are marked alike to encode a false closing-edge correspondence.
2. `Solid203/bridge_terminal_edge_pair`: expected wrong `A`, formal `E`. Equivalent lettered octahedron-edge correspondence; x and A are marked alike.
3. `Solid240/bridge_false_hinge_mapping`: expected wrong `6`, formal `1`. The Q/6 hinge in the flat net and the Q/? edge in the 3D drawing are marked alike, encoding an incorrect folding-edge mapping. This is more informative than merely highlighting the number 6 or framing Q.

Example next API invocation, only after checking that the prepared PNG/design remain unchanged:

```powershell
python -B -X utf8 runtime/mathvision_special_20261101/harness/quicktest3_isolated.py --branch SolidGeometry --question Solid166 --image runtime/mathvision_special_20261101/solid_explore/Solid166/bridge_terminal_edge_pair/candidate.png --design runtime/mathvision_special_20261101/solid_explore/Solid166/bridge_terminal_edge_pair/design.json --output runtime/mathvision_special_20261101/solid_explore/Solid166/bridge_terminal_edge_pair/tests --runs 2
```

Do not reuse any old response for the new bridge images. Old `Solid166/false_edge_pair`, `Solid203/false_edge_pair`, and `Solid240/adjacent_face_capture` failed before producing candidates through the generic adapter; they never had model tests.

## Further targeted ideas, not yet designed or tested

- Prioritize the newly accessible octahedron/cube nets and source-to-net boundary correspondence tasks. Follow the user's requirement for concrete geometric information, simple annotations, two independent hits, and independent second review.
- `Solid95`: the two full-height pillar cues yielded 80/24, so they did not stabilize. A distinct three-front-pillar height grouping may be worth exploring, but the shared base must stay fully visible and counted by a human.
- `Solid160` / `Solid196`: the four cubes form a 2×2×1 slab, with **four** cube-to-cube contacts. Two full cross lines on the front coincide with four individual contact-boundary segments and could induce counting only two contacts: 96−2×8=80 (Solid160 option A; Solid196 number 80) instead of 64. Preserve the entire original partition. This proposal has not been rendered or tested.
- `Solid96` / `Solid205`: consider two-color correspondence between the two original sheet cuts and the two seams of the assembled cylinder. The true circumference doubles at fixed height, so volume quadruples. A predeclared linear-volume distractor would be A/2-times or 200. These ideas have not been rendered or tested.
- `Solid216`: highlighting the three actual HBD triangle edges may induce misuse of the nearby 45° and 60° as triangle angles, giving cos75° (option E), while the actual spatial answer remains D. This proposal has not been rendered or tested.

No additional API should be launched by the ending native agent. The parent will hand the checkpoint to its background continuation mechanism.
