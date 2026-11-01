import json
import hashlib
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / 'root_explore'
OUT.mkdir(exist_ok=True)
for key, name in [('MPLCONFIGDIR','mpl_cache'),('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
    directory = OUT / name
    directory.mkdir(exist_ok=True)
    os.environ[key] = str(directory)
sys.path.insert(0, str(ROOT / 'PlaneGeometry/workbench'))
sys.path.insert(0, str(ROOT))
from runtime_isolation import install
ISOLATION = install(OUT / 'render_tmp')

def sheet(qids, destination):
    from PIL import Image, ImageDraw
    result = Image.new('RGB',(1200,425*((len(qids)+2)//3)), 'white')
    draw=ImageDraw.Draw(result)
    for i,qid in enumerate(qids):
        image=Image.open(ROOT/'PlaneGeometry/image'/f'{qid}.png').convert('RGB')
        image.thumbnail((396,396))
        x=(i%3)*400; y=(i//3)*425
        result.paste(image,(x,y+25)); draw.text((x+10,y+5),qid,fill='black')
    result.save(destination)

def inspect(qids):
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    config=load_config()
    config['runtime_dir']=str(OUT/'state')
    config['output_dir']=str(OUT/'output')
    adapter=RendererAdapter(config)
    for qid in qids:
        target=OUT/qid
        target.mkdir(exist_ok=True)
        metadata=adapter.inspect_question(qid)
        (target/'context.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2),encoding='utf-8')
        print(qid, 'objects',len(metadata['objects']), flush=True)

def design():
    from workbench_io import load_config, environment_versions
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    config=load_config()
    config['runtime_dir']=str(OUT/'state')
    config['output_dir']=str(OUT/'output')
    adapter=RendererAdapter(config)
    presets=[
        ('Plane321','short_sector','A',[
            {'type':'set_object_style','target':'o0','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o2','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o3','color':'#2563EB','linewidth_pt':2},
        ],'把共享顶点处的短角两边同红、起始外边蓝色，诱导忽略逆时针方向而报60°。'),
        ('Plane367','triangle_salience','D',[
            {'type':'set_object_style','target':'shape3','color':'#DC2626','linewidth_pt':2},
        ],'仅强调外观最高、斜边最长的D三角形轮廓，诱导用视觉跨度替代方格面积。'),
        ('Plane321','outer_rays','B',[
            {'type':'set_object_style','target':'o0','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':2},
        ],'用两条同红的外射线突出120°总夹角，诱导将顶点对应关系误写成D到B，预设B=120°。此前短角方案未命中；本方案重新设计并在两次新调用前冻结。'),
        ('Plane367','solid_target','D',[
            {'type':'set_object_style','target':'shape0','linestyle':'dashed'},
            {'type':'set_object_style','target':'shape1','linestyle':'dashed'},
            {'type':'set_object_style','target':'shape2','linestyle':'dashed'},
            {'type':'set_object_style','target':'shape4','linestyle':'dashed'},
            {'type':'set_object_style','target':'shape3','color':'#DC2626','linewidth_pt':3},
        ],'四个其余轮廓用细虚线，D保持粗红实线；利用完整闭合轮廓与视觉跨度诱导D最大，面积与格点不变。'),
        ('Plane360','circle_pair','C',[
            {'type':'set_object_style','target':'o1','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o184','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o185','color':'#DC2626','linewidth_pt':2},
        ],'滚动小圆与错误选项C的两个圆使用同色轮廓，诱导把点的轨迹误认成上下双环。'),
        ('Plane367','zigzag_salience','C',[
            {'type':'set_object_style','target':'shape2','color':'#DC2626','linewidth_pt':3},
            {'type':'set_object_style','target':'shape3','color':'#2563EB'},
        ],'将锯齿状C轮廓标为粗红、规则D三角形标蓝，诱导把跨越上下两排的路径长度当成面积。探索后的新候选，保持原格点与其它形状实线。'),
        ('Plane321','outer_reflex','D',[
            {'type':'set_object_style','target':'o0','color':'#DC2626','linewidth_pt':3},
            {'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':3},
            {'type':'set_object_style','target':'o2','linestyle':'dashed'},
        ],'强调外两射线而将共享边改虚，诱导错误顶点对应并取外射线间逆时针240°，预设D；所有顶点与题干等边条件不变。'),
        ('Plane333','serpentine_cut','C',[
            {'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':2},
            {'type':'add_line','id':'explore_cut','endpoints':[[7.55,-1.3],[10.4,1.3]],'color':'#2563EB','linestyle':'dashed','linewidth_pt':1},
        ],'S轮廓红色与单条蓝色斜切示意诱导最大分块落在C，仍保留M轮廓及最大化问题；辅助线不改纸片形状。'),
        ('Plane387','triangle_outline','12',[
            {'type':'set_object_style','target':'grey','color':'#DC2626','linewidth_pt':2},
        ],'仅将阴影三角形边界标红，诱导按近似完整小三角数量计12而漏算分割小片；阴影与格线全部不变。'),
        ('Plane387','unit_diamond','5.5',[
            {'type':'set_object_style','target':'grey','color':'#2563EB','linewidth_pt':1.5},
            *[{'type':'set_object_style','target':oid,'color':'#DC2626','linewidth_pt':2} for oid in ['edge0_0_1_0','edge0_0_0_1','edge1_0_0_1','edge0_1_1_0']],
        ],'把两个单位三角形的外周四边组成红色菱格，内部原黑对角线保持，诱导把菱格误当成1平方厘米并报半值5.5；题干明确每小三角形面积为1，人类可据此唯一得到11。'),
        ('Plane321','vertex_correspondence','D',[
            {'type':'set_object_style','target':'o0','color':'#DC2626','linewidth_pt':2},
            {'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':2},
            {'type':'add_point','id':'paired_B','xy':[0.0,5.196152422706632],'color':'#2563EB'},
            {'type':'add_point','id':'paired_D','xy':[9.0,0.0],'color':'#2563EB'},
        ],'在未改坐标的B/D两个命名顶点加同蓝点、外两边同红，引导错误地将D对应B；保留逆时针方向时误答240°。两个标记不表示等长等角或固定点。'),
        ('Plane333','letter_salience','C',[
            {'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':3},
            {'type':'set_object_style','target':'o5','color':'#2563EB'},
        ],'仅将S轮廓显著标红、M轮廓标蓝，诱导把S斜切的多次穿越当成最大分块；保留所有纸片轮廓，无辅助切线。'),
        ('Plane300','local_L_pair','B',[
            *[{'type':'set_object_style','target':oid,'color':'#DC2626','linewidth_pt':2} for oid in ['o8','o9','o12','o32','o33','o36']],
        ],'题面与错误B各取三个原有暗格组成同红L形外框，引导只比局部旋转匹配而忽略剩余暗格；灰白填充全部保持。'),
        ('Plane300','local_domino_pair','C',[
            *[{'type':'set_object_style','target':oid,'color':'#DC2626','linewidth_pt':2} for oid in ['o5','o6','o52','o56']],
        ],'源图两个水平相邻暗格与错误C两个竖直相邻暗格同红，突出90°局部配对，引导忽略其余暗格。保留原全部灰白填充。'),
        ('Plane333','H_cut','D',[
            {'type':'set_object_style','target':'o4','color':'#DC2626','linewidth_pt':2},
            {'type':'add_line','id':'H_cut_hint','endpoints':[[12.0,1.3],[15.0,-1.3]],'color':'#2563EB','linestyle':'dashed'},
        ],'强调H三道横跨分支的斜切示意，诱导误把H当可分最多块；M等其余原字形保留，辅助线不增加纸片/限制可选切法。'),
        ('Plane387','lattice_basis','5.5',[
            {'type':'set_object_style','target':'grey','color':'#2563EB','linewidth_pt':1.5},
            {'type':'add_line','id':'base_trace','endpoints':[[0.0,0.0],[6.0,0.0]],'color':'#DC2626','linestyle':'solid'},
            {'type':'add_line','id':'left_trace','endpoints':[[0.0,0.0],[3.0,5.196152422706632]],'color':'#DC2626','linestyle':'solid'},
            {'type':'add_point','id':'basis_i','xy':[1.0,0.0],'color':'#DC2626'},
            {'type':'add_point','id':'basis_j','xy':[0.5,0.8660254037844386],'color':'#DC2626'},
        ],'只在原外边界重合描红并标明相邻两个原格点，诱导在三角格基底使用单位正方格面积，误报11的一半5.5；不添加坐标值/箭头/直角条件，题干每三角形面积1保持。'),
    ]
    numbered_points={1:[9.0,6.732050807568877],2:[8.0,5.0],3:[11.0,3.267949192431123],4:[12.0,5.0],5:[11.0,6.732050807568877],6:[9.0,3.267949192431123]}
    for name, wrong, first in [('consecutive_groups','A',[1,2,3]),('upper_lower_groups','C',[1,2,4]),('crossed_groups','D',[1,3,4])]:
        actions=[{'type':'add_point','id':f'group_{i}','xy':numbered_points[i],'color':'#DC2626' if i in first else '#2563EB'} for i in range(1,7)]
        reason=f'六个原命名点重合标色，以红组{first}和其余蓝组编码错误分组，对应错误选项{wrong}；诱导按颜色而非题干奇偶分组。原数字、点坐标与选项都保持，不画错误三角边、不增加等长条件。'
        presets.append(('Plane308',name,wrong,actions,reason))
    for name,wrong,first,index in [('consecutive_color_match','A',[1,2,3],0),('upper_lower_color_match','C',[1,2,4],2)]:
        actions=[{'type':'add_point','id':f'group_{i}','xy':numbered_points[i],'color':'#DC2626' if i in first else '#2563EB'} for i in range(1,7)]
        actions += [{'type':'set_object_style','target':f'option{index}_{j}','color':color,'linewidth_pt':2} for j,color in enumerate(['#DC2626','#2563EB'])]
        reason=f'红蓝点组在原标号位置编码错误分组{first}/其余点，同时将错误选项{wrong}两三角边界对应为红蓝；诱导将颜色分区当成奇偶分区。每个点标出分组成员，每条三角轮廓给出该组连线对应，数字全部可读且原题无颜色条件。'
        presets.append(('Plane308',name,wrong,actions,reason))
    for qid,name,wrong,actions,reason in presets:
        target=OUT/qid/name
        target.mkdir(parents=True,exist_ok=True)
        if (target/'design.json').exists():
            continue
        metadata=adapter.inspect_question(qid)
        renderer=PluginRenderer(config,adapter,{qid:metadata})
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':reason,'intent':reason,'params':{'actions':actions}}
        normalized,data,pixels=renderer.render(plugin)
        again,data_again,pixels_again=renderer.render(normalized,frozen=True)
        assert data==data_again and pixels==pixels_again
        (target/'plugin.json').write_text(json.dumps(normalized,ensure_ascii=False,indent=2),encoding='utf-8')
        (target/'candidate.png').write_bytes(data)
        entry={'question_id':qid,'name':name,'expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':reason,'action_count':len(actions),'human_readability':'允许的原对象样式覆盖和声明式点/线标记；逐份检查原文字可读、原坐标与填充不变、连接语义及唯一答案保持，新增标记不构成新条件。','review_status':'unreviewed','pixel_sha256':pixels,'png_sha256':hashlib.sha256(data).hexdigest(),'no_op_baseline':metadata['original_pixel_sha256'],'repeat_render_identical':True,'environment':environment_versions()}
        (target/'design.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2),encoding='utf-8')
        print(str(target),flush=True)

if __name__=='__main__':
    qids=sys.argv[2:] or ['Plane321','Plane367','Plane360','Plane343','Plane378','Plane314']
    if sys.argv[1]=='sheet':
        sheet(qids, OUT/'original_contact.png')
    elif sys.argv[1]=='inspect':
        inspect(qids)
    elif sys.argv[1]=='design':
        design()
