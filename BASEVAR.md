# Basevar construction standard

Basevar supplements MathPalette with perturbations whose placement or design is unrelated to the mathematical evidence needed for the current question. Irrelevance is judged from the question and diagram before model evaluation. It is not a claim that the perturbation will have no effect on a model.

The unit of construction is the **question**, not each Special variant. Basevars do not need a one-to-one correspondence with Specials: several Specials may use the same intervention method at different locations.

## Categories and per-question allocation

The target is five Basevars per eligible question, organized as follows. Only the first category is being constructed now.

| Slot | Category | Construction |
| --- | --- | --- |
| B01 | Type 1: task-irrelevant diagram intervention | Use the first retained Special's intervention method at noncritical locations. |
| B02 | Type 1: task-irrelevant diagram intervention | A second, visibly distinct design using the same reference method. |
| B03 | Type 1: task-irrelevant diagram intervention | An independently designed irrelevant intervention, such as an auxiliary line; it need not follow any Special's method. |
| B04 | Type 2: image-level perturbation | Reserved for a future specification. |
| B05 | Type 2: image-level perturbation | Reserved for a future specification. |

Use IDs such as `Ana01_B01`, preserving the original question ID. These are separate from the existing `Cxx` Special slots and do not change their Collect counts or approval records.

Type 1 uses diagram elements such as red points and auxiliary lines to introduce visible distraction away from the current question's critical evidence. Type 2 concerns image-level changes; reduced resolution and whole-image rotation are possible examples, not finalized operations. The exact Type 2 transformations, strengths, validity criteria and rendering rules remain undecided. Do not generate B04 or B05, or count them as completed samples, until those rules are specified.

Five slots are a construction target, not a requirement to fabricate an unsuitable sample. Record exceptions when a compliant design is unavailable.

## Reference and design for Type 1

### B01 and B02: follow one reference method

Use the first retained, passed Special in the question's existing `special_variants` list, normally C01. Record its original ID. Do not restore deleted slots or create a replacement Special to obtain a reference.

Identify the reference's intervention method, then construct two Basevars from the original diagram using that method. For example, a red-point Special leads to two red-point Basevars. The remaining Specials do not each require their own Basevar.

Reuse the reference's visual style and element count by default: point color, size and shape; line color, width and dash style; and any applicable opacity. This establishes a recognizable relationship to the reference method, rather than exact geometric equivalence.

**Rigid translation is not required.** Points may be placed independently, and their relative positions need not be preserved. Auxiliary-line endpoints, orientation and length may be chosen to suit a noncritical location. Mixed interventions may be rearranged as needed, provided the reference method remains recognizable and the actual elements and parameters are recorded.

B01 and B02 must be visibly different placements or arrangements. They must not be duplicate images or merely different filenames. Neither should place the intervention so inconspicuously that it ceases to be a visible distraction.

### B03: independent irrelevant intervention

Design an additional Type 1 intervention without requiring a match to the reference Special. Prefer a different intervention method from B01 and B02 when a valid design is available. An irrelevant auxiliary line is a natural option, including when B01 and B02 use red points. Another suitable diagram intervention may be used when a line would not satisfy the validity criteria.

B03 must be visibly distinct from B01 and B02 and meet the same standards of task irrelevance and information preservation. It must not introduce image-level degradation from Type 2.

### Placement flexibility

Choose locations based on the current question and diagram. Visually distracting but noncritical locations are acceptable; uniformly random placement, maximally distant corners, fixed quadrants and a universal distance threshold are not required.

Distance from a Special's original position alone does not establish irrelevance. Assess the new element's relationship to the evidence needed to solve the question. Conversely, a location need not be completely disconnected from every original graphical element if it does not obscure or confuse the relevant evidence.

The earlier temporary point pilot's rigid translations and numerical distance thresholds are implementation choices for that pilot, not requirements of this standard.

## Prior validity criteria

Every Type 1 Basevar must satisfy all of the following criteria.

1. **Question-specific irrelevance.** Identify the mathematical evidence needed for the current question and explain why the new intervention does not participate in reading that evidence. The same location may be critical for a different question.
2. **Preserved source content.** Keep the original question, answer, choices, mathematical geometry and necessary visual evidence unchanged. Build each Basevar independently from the original drawing, not by accumulating changes on a Special or another Basevar.
3. **Preserved readability.** Do not obscure necessary curves, points, endpoints, labels, tick values or other information required for a valid solution. Original information must remain readable without guessing.
4. **No new targeted ambiguity.** Do not introduce a plausible alternative reading or mathematical relation directly relevant to the question. For example, avoid new markers on the zero-counting axis, extra intersections in a region where intersections are being counted, or a line that looks like a competing radius in a radius-reading question.
5. **Visible intervention.** Keep the intended perturbation clearly visible. Do not obtain apparent harmlessness by clipping it, moving it off-canvas, making it nearly transparent, or reducing it to an imperceptible size.

Examples of critical evidence include the relevant branch and endpoint near a queried limit, the x-axis crossings in a root-counting problem, the curves inside a specified intersection-counting domain, and the center and boundary evidence needed to determine a circle's radius.

These criteria are semantic and visual checks, not a requirement that every added element avoid every curve or axis. An auxiliary line may pass through a noncritical region if it preserves readability and does not create a question-relevant ambiguity.

## Review and exceptions

Review candidates using only the original question, original diagram, reference method where applicable, and the construction criteria above. Do not use model answers, accuracy or reasoning traces to choose locations or decide whether a candidate qualifies.

A model error on a compliant Basevar is an experimental result, not grounds to remove or redesign that sample. A correct model answer does not make a noncompliant construction valid. Any later construction correction must have a documented reason independent of model performance.

Record an exception when a reference method cannot reasonably be applied in a noncritical way. This may occur with whole-curve restyling, large filled regions or other interventions tightly tied to the relevant structure. Do not silently replace the method for B01 or B02, weaken the criteria, or invent a sample merely to fill a slot. Explain the reason and leave the affected slot unfilled. An independent B03 may still be feasible.

Construction review does not approve the question again and does not create a historical Collect/Pass record. Preserve existing approval and collection dates. New candidates remain pending user review until actually reviewed and accepted.

## Construction records and implementation

For each candidate, retain:

- The original question ID, Basevar slot and category.
- The reference Special ID and intervention method for B01 and B02; mark B03 as independently designed.
- The intervention's actual elements, coordinates and appearance parameters.
- A description of the critical evidence and a concrete explanation of the proposed placement's irrelevance.
- Source drawing and output image references, image hash, and current review status.
- Any exception or revision reason, without invented review dates or claims of approval.

Follow [DRAWING_PROTOCOL.md](DRAWING_PROTOCOL.md) for Type 1 rendering. Keep question-specific construction in the question's Python class using `drawing.py` directly. Retain the original canvas and drawing settings; Type 1 does not lower resolution or rotate the whole image. Temporary prototypes, previews and construction records belong in `.runtime/` while awaiting review.

The existing temporary pilot is exploratory material. Its per-Special pairings and B-slot filenames do not establish compliance with the new per-question allocation. Reassess or rebuild those candidates under this standard rather than treating their old names as accepted B01-B03 assignments.

`MathPalette_Dataset/` remains the only formal dataset directory. Publishing this document does not publish or approve Basevar images, alter the existing dataset counts, or add reserved Type 2 samples. When approved Basevars are incorporated, synchronize image references, manifests, metadata hashes and `SHA256SUMS` with the actual accepted samples.
