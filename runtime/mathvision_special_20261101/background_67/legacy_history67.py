from env67 import *
import gc
legacy=PROJECT/'.runtime/mathvision_qt3_explore_20261031'
folders={'Solid140':legacy/'discover_m/Solid140','Solid219':legacy/'discover_i/Solid219','Solid236':legacy/'discover_p/Solid236'}
audit=[]
for q,folder in folders.items():
    with (OWN/q/'legacy_full_finals.txt').open('x',encoding='utf-8') as out:
        for p in sorted(folder.rglob('*')):
            if not p.is_file(): continue
            data=p.read_bytes(); row={'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'full_byte_read':True}
            if p.suffix=='.json':
                try: v=json.loads(data.decode('utf-8-sig'))
                except (UnicodeError,ValueError) as exc: row['parse_error']=str(exc)
                else:
                    if p.name.startswith('quicktest3_run'):
                        out.write('\nFILE '+str(p)+'\nSTATUS '+str(v.get('status'))+' FINISH '+str(v.get('finish_reason'))+'\n'+str(v.get('answer'))+'\n')
                        row.update({'status':v.get('status'),'finish_reason':v.get('finish_reason'),'image_sha256':v.get('png_sha256'),'historical_expectation':v.get('expectation_before_testing'),'starts':v.get('started_at'),'legacy_required_runs':v.get('required_runs'),'full_final_read_for_audit':True})
                    del v
            audit.append(row); del data; gc.collect()
    print(q,'LEGACY_HISTORY_FULL_BYTE_AND_JSON_READ',sum(1 for r in audit if q in Path(r['path']).parts),flush=True)
save('legacy_scoped_full_history_audit.json',audit)
save('legacy_vs_frozen_reuse_difference_audit.json',{'at':now(),'new_design_count':0,'scope':list(QIDS),'purpose':'Audit additional extant .runtime history, not restore deleted reports/logs/scores or authorize their historical test protocol. Frozen r59 files remain untouched.','Solid140':{'legacy_variants':['two_tank_frames','two_water_levels','upright_frame_level'],'legacy_presets':['B'],'frozen_preset':'A','comparison':'Legacy full water perimeters are one uniform orange style targeting a mistaken 2x2 final base, not an ordered width/depth correspondence. The original frozen r59 open L has distinct width and depth roles across both water surfaces, with true widths 4 to 1 and unchanged depth 2, targeting area-unit invariance and unchanged 25cm. A broader old water-boundary emphasis exists and is disclosed; this is first testing of the already frozen r59 image, with no new-mechanism claim.'},'Solid219':{'legacy_variants':['corresponding_first_cuts','second_cut_group','w_side_cut_edges'],'legacy_presets':[['B','C'],['B','C'],['C','D']],'frozen_preset':'E','comparison':'Old designs style cut families or only Figure 2 W-side edges plus second dashed cuts. Frozen r59 pairs the same real complete triangular end section in BOTH figures, using two exact half-depth intervals, to transfer an actual 1/4 first prism to a proper W subpiece. It does not style second-cut lines. Existing legacy observed values are not new presets.'},'Solid236':{'legacy_variants':['given_midpoint_edges','original_section_perimeter','section_opposite_edges'],'legacy_preset':'D','frozen_preset':'E','comparison':'Legacy marks use source midpoint edges/dots or section perimeter/sides to suggest a square. Frozen r59 uses two previously unmarked genuine section diagonals and the body-versus-midplane diagonal product, without adding midpoint dots. No redraw or re-preset occurred.'},'older_test_protocol_not_reused':'Legacy required_runs=3 and multi-answer expectations are history only. This task permits exactly one immutable wrong preset and exactly two actual complete calls per image.'})
