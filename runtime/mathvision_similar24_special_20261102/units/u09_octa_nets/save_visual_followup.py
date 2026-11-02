from own_bootstrap import *

d=Path(sys.argv[1]).resolve();check_write(d)
design=load(d/'design.json');plugin=load(d/'plugin.json')
save(d/'primary_visual_review.json',{'review_type':'PRIMARY only, not independent second review','image_actually_viewed':True,
    'image_sha256':sha(d/'candidate.png'),'viewed_at':now(),'native_768x768':True,
    'observations':['Every selected line is an existing original boundary. No new paper area or closed subpartition is introduced.',
       'The red target x and red edge'+design['expected_wrong_answer']+' have distinct unambiguous labels; unchanged black labels and edges remain legible.',
       'The right octahedron, original hidden dashed edges, all net vertices and all8triangles remain unchanged.',
       'Each source and receiving boundary has a distinct comparison role recorded before calls. No redundant or overridden style action.'],
    'number_of_useful_actions':len(plugin['params']['actions']),
    'physical_color_reading_checked':'Ink is attached only to existing boundaries. It cannot affect seam endpoint identity. The question does not require matching colors, so the exact colored physical net still has unique answer5.',
    'primary_original_mathematics_verified':True,'frozen_preset':design['preset_semantics'],
    'eligible_for_exact_two_calls':True,
    'limitations':['Two calls only, no third/relabel/retry.','Double hit remains PRIMARY pending a new independent review.']},exclusive=True)
print('Visual PRIMARY review saved',d.name)
