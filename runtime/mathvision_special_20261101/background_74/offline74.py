from audit74 import *
import math

def offline():
    e=eligibility(); write('eligibility_before_offline.json',e); assert e['eligible']
    from runtime_isolation import install
    isolation=install(HERE/'render_tmp')
    sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
    from workbench_io import load_config, environment_versions
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    from dataset_tools.mathvision_workbench import png_bytes
    from PIL import Image
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output')
    adapter=RendererAdapter(cfg)
    context=adapter.inspect_question(QID);write('offline/fresh_context.json',context)
    scene=adapter.scene(QID)
    try: baseline=png_bytes(scene)
    finally: scene.close()
    (HERE/'offline/no_op.png').write_bytes(baseline)
    formal=PROJECT/'SolidGeometry'/e['record']['image']
    with Image.open(formal) as a, Image.open(HERE/'offline/no_op.png') as b:
        assert a.size==b.size==(768,768)
        assert a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
    del baseline
    plugin=read(SOURCE/'plugin.json')
    renderer=PluginRenderer(cfg,adapter,{QID:context})
    normalized=renderer.normalize(plugin); assert normalized==plugin
    receipts=[]
    for name in ['first.png','repeat.png','exact_offline_replay.png']:
        n,data,pixel=renderer.render(plugin,frozen=True)
        target=HERE/'offline'/name;target.write_bytes(data)
        digest=hashlib.sha256(data).hexdigest()
        assert digest==TARGET_SHA and n==plugin
        receipts.append(dict(path=str(target),sha256=digest,pixel_sha256=pixel,normalization_stable=n==plugin))
        del n,data
    assert context==read(SOURCE/'context.json'), 'Fresh exact native context differs'
    native=[]
    for p in [PROJECT/'SolidGeometry'/e['record']['original_image'],formal,SOURCE/'candidate.png']:
        with Image.open(p) as im:
            im.load(); native.append(dict(path=str(p),size=list(im.size),mode=im.mode,sha256=sha(p)))
    report=dict(checked_at=now(),unchanged_dedicated_bridge=str(BASE/'delivery_bridge_adapter.py'),
        approved_plugin_renderer=str(PROJECT/'SolidGeometry/workbench/render_plugins.py'),isolation=isolation,
        environment=environment_versions(),schema_valid=True,defaults_normalized_and_stable=True,
        no_op_formal_pixels_equal=True,no_op_byte_sha256=sha(HERE/'offline/no_op.png'),formal_byte_sha256=sha(formal),
        fresh_context_exact_equal=True,repeat_byte_identity=True,exact_offline_replay=True,renders=receipts,native=native,
        source_hashes_before=e['source_hashes'],source_hashes_after=eligibility()['source_hashes'])
    assert report['source_hashes_before']==report['source_hashes_after']
    write('offline_render_audit.json',report)
    import matplotlib.pyplot as plt
    plt.close('all')
    print(json.dumps({k:report[k] for k in ['schema_valid','no_op_formal_pixels_equal','fresh_context_exact_equal','repeat_byte_identity','exact_offline_replay']}))

def proof():
    e=eligibility()
    paths=[PROJECT/'SolidGeometry'/e['record']['scene'],PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid234/scene.json']
    checks=[]
    for p in paths:
        scene=read(p);pts=scene['points']; cut=next(x for x in scene['objects'] if x['id']=='cut_section')
        vertices=[pts[k] for k in cut['points']]
        plane_error=max(abs(x-3-3*z/4) for x,y,z in vertices)
        cylinder_error=max(abs(y*y+z*z-16) for x,y,z in vertices)
        assert plane_error<1e-12 and cylinder_error<1e-12
        assert pts['T0']==[0,0,4] and pts['T6']==[6,0,4]
        assert pts['B0']==[0,0,-4] and pts['B6']==[6,0,-4]
        assert cut['linestyle']=='dashed'
        gen=next(x for x in scene['objects'] if x['id']=='line_2')
        assert gen['points']==['T0','T6']
        checks.append(dict(path=str(p),sha256=sha(p),point_count=len(pts),cut_samples=len(vertices),max_plane_residual=plane_error,
            max_cylinder_residual=cylinder_error,cut_x_bounds=[min(x[0] for x in vertices),max(x[0] for x in vertices)],
            dimensions=scene['dimensions'],projection=scene['projection'],visibility=scene['visibility'],view=scene['view'],
            original_objects=[{k:v for k,v in x.items() if k!='points'}|{'point_ids_count':len(x.get('points',[]))} for x in scene['objects']]))
    choices={k:float(v) for k,v in e['record']['choices'].items()}
    correct=48*math.pi; wrong=96*math.pi
    correct_d={k:abs(v-correct) for k,v in choices.items()};wrong_d={k:abs(v-wrong) for k,v in choices.items()}
    assert min(correct_d,key=correct_d.get)=='C' and min(wrong_d,key=wrong_d.get)=='D'
    report=dict(checked_at=now(),kind='Fresh PRIMARY mathematical and human semantic assessment; no independent review or approval',
        actual_source_formal_candidate_viewed=True,
        proof={
          'domain':'0<=x<=6; y^2+z^2<=16 (diameter8, axial length6)',
          'cut_plane_derivation':'A planar cut x=a+by+cz tangent to the two end disks at B0=(0,0,-4) and T6=(6,0,4) gives a=3,c=3/4. Since the complete section lies within 0<=x<=6 and touches its extreme at y=0,z=+-4, a nonzero b would exceed an end near one tangency (disk support radius4*sqrt(b^2+c^2)>3). Thus b=0; the frozen sampled cut independently satisfies x=3+3z/4. This uses true tangencies and a complete untruncated planar section, never ellipse pixel lengths.',
          'extent_bounds_and_construction':'For -4<=z<=4, 0<=3+3z/4<=6; B0 and T6 attain0 and6. Hence exact min0 and max6. These are extent bounds for this hypothesis; the question requests nearest volume, not a new optimization condition.',
          'volume':'Integral_D (3+3z/4) dy dz =3 area(D)+(3/4) integral_D z =3*16*pi=48pi, by oddness. Equivalently central inversion (x,y,z)->(6-x,-y,-z) interchanges the wedges so both halves have volume48pi. Which side is called the wedge does not change the answer.',
          'correct_value':correct,'correct_distances_to_all_listed_choices':correct_d,'unique_closest':'C:151',
          'frozen_error':'Replacing varying extent by its maximum6 everywhere gives disk_area16pi*6=96pi. This is an erroneous full-cylinder calculation; among the actual finite list its unique nearest value is192, D, even though301.59 is not itself listed.',
          'wrong_value':wrong,'wrong_distances_to_all_listed_choices':wrong_d,'immutable_wrong_preset':'D:192'},
        scene_checks=checks,
        every_marker=[
          dict(index=0,target='line_2',action='blue #2563EB,1.5pt only; existing solid silhouette generator',
            useful_true_information='Source: the displayed whole axial span exactly6cm also attained at the high end of the cut; shares dimension endpoints T0,T6.',
            human_role='A clear existing upper silhouette, not a new edge or equality mark. Original length bracket and6cm label remain black and fully readable.'),
          dict(index=1,target='cut_section',action='blue #2563EB,1.5pt only; original entire dashed cut trace',
            useful_true_information='Receiver: existing planar cutting boundary shows the changing axial extent from0 through3 to6. Matching blue permits comparison with the maximum-length generator.',
            human_role='The closed dashed ellipse is still a cut trace with original sample path and dash semantics; no extra section, painted face, numerical equality, fixed partition or new material is asserted.')],
        native_readability='Source JPG and768x768 formal/candidate viewed individually.6cm and8cm remain complete, separate, correctly bound; both circular end contours, bottom generator and full cut trace readable. At the far top tangent the solid source and dashed receiver meet their true common point. No added text, arrows, centers, marks or alternate target. Blue styling does not obscure the distinguishing variable cut boundary.',
        task_specific_semantics='Numerical volume of a fixed cylinder and cut; neither printed-pattern completion nor physical ink transport nor counting painted surfaces. Both recolored objects are existing boundary information; shared color is a comparison cue and supplies no new equality/parallelism/angle condition. Original neutral fill, dimensions, labels, dashes, projection and visibility are unchanged.',
        difference_or_reuse='Exact r57 hypothesis/date/preset/plugin/PNG/context preserved; zero new mechanisms. Old difference audit remains a historical claim about r57 relative to r15, not a new r74 change.',
        limits=['Primary evidence only; any two-hit observation requires a NEW independent delegate review by the parent before delivery.','No causal gain/control-correctness or per-marker ablation hard gate imposed.'])
    write('fresh_math_native_every_marker_review.json',report)
    print(json.dumps(dict(correct=correct,wrong=wrong,closest_correct='C',closest_wrong='D',cut_plane_verified=True)))

if __name__=='__main__':
    if sys.argv[1]=='offline': offline()
    elif sys.argv[1]=='proof': proof()
