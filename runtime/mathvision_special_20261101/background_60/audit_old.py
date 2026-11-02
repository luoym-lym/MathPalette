from tools60 import *

def main():
    selected=[]
    for parent,dirs,files in os.walk(BASE):
        directory=Path(parent)
        if directory==HERE:
            dirs[:]=[];continue
        if any(q in directory.parts for q in IDS+RELATED):
            # Newly active refinement siblings are outside historical initial evidence.
            first=directory.relative_to(BASE).parts[0]
            if first.startswith('background_') and first[11:].isdigit() and int(first[11:])>22:
                continue
            selected.extend(directory/name for name in files)
    selected += [BASE/'background_19/sliding_bar_proof.json']
    selected += [BASE/'annotation_semantics_lessons_20261102.json',BASE/'annotation_semantics_lesson_plane242_r24_20261102.json']
    selected += list((BASE/'independent_review').glob('Plane263*/independent_review.json'))
    selected += list((BASE/'independent_review').glob('Plane192_v03*/independent_review.json'))
    selected += list((BASE/'independent_review').glob('Plane233_two_U*/independent_review.json'))
    selected += [BASE/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',BASE/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']
    selected=sorted(set(p for p in selected if p.is_file()))
    finals={q:[] for q in IDS+RELATED}; materials={q:[] for q in IDS+RELATED}; hashes={}
    for p in selected:
        hashes[str(p.relative_to(PROJECT)).replace('\\','/')]=sha(p)
        if p.suffix!='.json':continue
        try: d=read(p)
        except Exception as err:
            print('OLD JSON ERROR',p,type(err).__name__);continue
        q=next((q for q in IDS+RELATED if q in p.parts),None)
        if q and p.name.endswith('_response.json'):
            choices=d.get('choices',[])
            finals[q].append({'path':str(p),'sha256':sha(p),'finish_reason':choices[0].get('finish_reason') if choices else None,'full_response':d})
        elif q and (p.name in ('design.json','plugin.json','assessment.json','prescreen.json','prescreen_assessment.json','prescreen_rejection.json','primary_visual_review.json','primary_outcome_review.json','manual_final_review.json') or 'abort' in p.name):
            materials[q].append({'path':str(p),'sha256':sha(p),'content':d})
        del d;gc.collect()
    write(HERE/'old_evidence_hashes_initial.json',hashes)
    for q in IDS+RELATED:
        write(HERE/'old_history'/q/'materials.json',materials[q])
        write(HERE/'old_history'/q/'full_raw_responses.json',finals[q])
        print(q,'material records',len(materials[q]),'raw replies',len(finals[q]))
    write(HERE/'old_history_inventory.json',{'file_count':len(selected),'paths':[str(p) for p in selected],'streamed_one_file_at_a_time':True,'own_directory_write_guard':True})
if __name__=='__main__':main()
