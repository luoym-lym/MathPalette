import os,sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
os.environ['MPLCONFIGDIR']=str(HERE/'mplcache')
os.environ['TEMP']=os.environ['TMP']=str(HERE/'tmp')
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
sys.path.insert(0,str(ROOT))
from workbench_io import load_config,canonical_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from runtime_bridge import isolate_native_temporary_files
isolate_native_temporary_files(HERE/'render_tmp')

def style(target,color='#DC2626',width=2):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}

DESIGNS=[
 ('Plane236','v01','E',[style('o31'),style('o24')],
  '将入射激光及上方原有虚线同红色，形成横向直通的错误视觉连续性，诱导忽略反射而误到E。保留所有镜面、虚线线型与字母，未新增光路。'),
 ('Plane268','v01','B',[style('given_moving_body'),style('B_moving_body')],
  '给定滚动币与错误90度姿态B的袋鼠轮廓同红色，诱导把绕外侧滚动误作单纯四分之一周自转。原滚动箭头、姿态和圆均不变。'),
 ('Plane273','v01','C',[style('o49','#DC2626',3),style('o51','#2563EB',0.5),style('o96')],
  '突出到达钟表的短时针，并给错误C指针同色，诱导把3点半误读为3点整，进而得到2点整。保留原指针长度、端点与全部刻度，原长分针仅蓝色细线。'),
 ('Plane287','v01','A',[style('o13'),style('o28')],
  '原钟长针与错误选项A长针同红色，诱导镜像时间退10分钟时将方向反置。保留两针长度、角度及全部刻度，只有两条原线变色。'),
 ('Plane291','v01','D',[style('gray0'),style('gray1'),style('diag1','#2563EB',1)],
  '两个灰区轮廓同红色、另一对角线蓝色，诱导按两块三角形数量判断一半而忽略两者面积不同。灰度填充、分割线和全部几何保持不变。'),
 ('Plane254','v01','E',[style('o4'),style('o5','#2563EB'),style('o2','#DC2626',1)],
  '两段中心连线异色且强化中间分割边，诱导由视觉不等长误判总长随划分变化。原中心点和长度信息均保持，未添标记。'),
]

def main(specs=DESIGNS, summary='designs.json'):
    config=load_config()
    config['runtime_dir']=str(HERE/'render_runtime')
    config['output_dir']=str(HERE/'render_output')
    adapter=RendererAdapter(config)
    metadata={}
    renderer=PluginRenderer(config,adapter,metadata)
    results=[]
    eligible={json.loads(line)['id'] for line in (HERE.parent/'PlaneGeometry_eligible.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()}
    for qid,vid,wrong,actions,reason in specs:
        assert qid in eligible
        directory=HERE/qid/vid
        directory.mkdir(parents=True,exist_ok=True)
        metadata[qid]=adapter.inspect_question(qid)
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
                'description':reason,'intent':f'预设错误答案 {wrong}', 'params':{'actions':actions}}
        norm,data,digest=renderer.render(plugin)
        norm2,data2,digest2=renderer.render(norm,frozen=True)
        assert data==data2 and digest==digest2
        (directory/'plugin.json').write_text(json.dumps(norm,ensure_ascii=False,indent=2),encoding='utf-8')
        (directory/'candidate.png').write_bytes(data)
        design={'question_id':qid,'variant_id':vid,'correct_answer':adapter.records[qid]['answer'],
                'expected_wrong_answer':wrong,'design_reason':reason,'action_count':len(actions),
                'plugin_path':str(directory/'plugin.json'),'image_path':str(directory/'candidate.png'),
                'pixel_sha256':digest,'image_sha256':hashlib.sha256(data).hexdigest(),
                'input_record_sha256':canonical_hash(adapter.records[qid]),
                'schema_valid':True,'baseline_pixels_match':True,'deterministic_redraw':True,
                'review_status':'unreviewed','test_status':'pending'}
        (directory/'design.json').write_text(json.dumps(design,ensure_ascii=False,indent=2),encoding='utf-8')
        results.append(design)
        print(qid,vid,'OK',flush=True)
    (HERE/summary).write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
