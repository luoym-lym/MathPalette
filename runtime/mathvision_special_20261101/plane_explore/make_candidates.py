import os
import sys
import json
import hashlib
import copy
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
os.environ['MPLCONFIGDIR']=str(HERE/'mplcache')
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for variable,directory in [('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
    target=HERE/directory
    target.mkdir(parents=True,exist_ok=True)
    os.environ[variable]=str(target)
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(HERE.parent))
from runtime_isolation import install
install(HERE/'render_tmp')
from workbench_io import load_config,canonical_hash,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer

def style(target,color='#DC2626',width=1.5):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}

DESIGNS=[
 ('Plane175','v01','B',[style('given_notched_piece'),style('option1')],
  '将已知凹口纸片与错误选项B轮廓同色，诱导形状匹配。仅改原有描边，不改变几何、尺寸、文字。'),
 ('Plane261','v01','B',[style('o1'),style('o9')],
  '给定暗格与保持原朝向的错误选项B暗格同红色描边，诱导忽略180度旋转。保留灰度填充和F点。'),
 ('Plane444','v01','C',[style('o2'),style('o11')],
  '给定F与错误选项C同红色描边，诱导复合变换中选错左右朝向。坐标轴和文字不变。'),
 ('Plane189','v01','C',[style('rectangle'),style('triangle'),style('circle','#2563EB',1)],
  '矩形与三角同红、圆蓝，诱导将应排除三角误作共同包含而回答13。原边界、数字和范围不变。'),
 ('Plane196','v01','C',[style('square'),style('triangle')],
  '方形和三角形同红色轮廓，诱导误判袋鼠处于这两者内部。保留所有边界和袋鼠位置。'),
 ('Plane175','v02','C',[style('given_notched_piece'),style('option2',width=2)],
  '已知凹口纸片和错误选项C用同红色轮廓，诱导局部凹口相似性匹配而忽略完整拼接。'),
 ('Plane192','v01','D',[style('route3_'+str(i),width=2) for i in range(8)],
  '将最接近水平基线但含最多折返的D路线用红色强调，诱导按视觉高度误判最短，原有路径和格线不变。'),
 ('Plane253','v01','A',[style('route0_'+str(i),width=2) for i in range(4)],
  '将错误路线A用红色强调，诱导对较短可视斜段的整体长度判断，所有车辆和路径不变。'),
 ('Plane171','v01','E',[style('lawn4',width=2)],
  '将凹陷较明显的错误草坪E用红色轮廓强调，诱导按凹口判断最小面积，不改边界、点位。'),
 ('Plane452','v01','E',[style('r4',width=2)],
  '仅强调中间阴影矩形的红色轮廓，诱导以接近正方形的显示比例选择2x3，而非按拼接约束求解。'),
 ('Plane421','v01','C',[style('hex1'),style('hex2')],
  '将两正六边形以红色轮廓分组，诱导将白色双六边形面积误作三分之二，进而回答阴影三分之一。'),
 ('Plane236','v01','E',[style('o24',width=2),style('o31',width=2)],
  '入射线与通向E的原有上排虚线同红色，诱导直通而忽略镜面反射；原有镜面和虚线仍全部可辨。'),
 ('Plane478','v01','3',[style('r0','#DC2626',2),style('r1','#2563EB',2),style('r2','#16A34A',2)],
  '三条原始矩形轮廓分别用红蓝绿分组，诱导只数三个来源矩形而忽略交叠产生的组合矩形。描边以外不改图。'),
 ('Plane459','v01','4',[style('outer',width=2),style('BD','#2563EB',1.5),style('DE','#2563EB',1.5)],
  '外三角红、内部两线同蓝，诱导只数三个最小三角和一个外三角，漏掉右侧组合三角。未增删线。'),
 ('Plane179','v01','B',[style('triangle0',width=2),style('triangle1',width=2),style('triangle2',width=2)],
  '以红色连贯描边强调斜三角边界，诱导将格点位置近似成十二个单位小三角面积。网格和灰色区域不变。'),
 ('Plane462','v01','C',[style('I',width=2),style('II',width=2)],
  '将两四边形用相同红色轮廓分组，诱导从面积相同过度推断周长也相同。保留所有点位与边界。'),
 ('Plane458','v01','D',[style('triangle',width=2)],
  '仅以红色强调细长三角形，诱导将半单位面积误判为一单位；所有网格点、标签、真实顶点不变。'),
 ('Plane472','v01','C',[style('blade0',width=2),style('blade2',width=2),style('blade1','#2563EB',2),style('blade3','#2563EB',2)],
  '对向叶片按红蓝两组描边，诱导将每片误当作2单位面积而总计8，保留阴影、边界和全部网格。'),
 ('Plane175','v03','B',[style('given_notched_piece',width=3),style('option1',width=3)]+
  [dict(style('option'+str(i),'#2563EB',1),linestyle='dashed') for i in [0,2,3,4]],
  '给定凹口纸片及错误选项B用3pt红色共同强调，其余选项保留完整蓝色虚线轮廓，诱导错误匹配。'),
 ('Plane192','v02','D',[style('route3_'+str(i),width=3) for i in range(8)]+
  [dict(style('route'+str(j)+'_'+str(i),'#2563EB',1),linestyle='dashed') for j,n in [(0,2),(1,4),(2,4)] for i in range(n)],
  'D路线以3pt红色强调，其余三条保留完整蓝色虚线，诱导把最靠基线的锯齿路线判为最短。四条路径坐标不变。'),
 ('Plane421','v02','C',[style('hex1','#2563EB',3),style('hex2','#2563EB',3),style('outline',width=2)],
  '同蓝色粗轮廓凸显两个白色六边形，并以红色标示外框，诱导把白色部分当作三分之二，阴影误判为三分之一。'),
 ('Plane236','v02','D',[style('o31',width=3),style('o22',width=3),style('o23',width=2)],
  '入射线、最右竖向虚线及下排虚线同红色强调，诱导在C列转向后提前回答出口D，漏掉底部镜面继续反射。保留全部镜面和原线型。'),
 ('Plane459','v02','6',[style('outer',width=3),style('BD',width=3),style('DE',width=3)],
  '所有三角形原线条统一红色3pt描边，诱导把中间组合区域重复计数为六个。顶点连接和可见三角形完全不变。'),
 ('Plane478','v02','7',[style('r0',width=3),style('r1',width=3),style('r2',width=3)],
  '三个重叠矩形统一红色粗描边，强化交叠区域分块，诱导按可见分区数七而漏掉跨分区组合矩形。全部边界和交点位置不变。'),
 ('Plane236','v03','D',[style('o31',width=3),style('o22',width=3),style('o23',width=3),style('o30','#2563EB',0.5)],
  '红色入射线与右列和下排虚线构成强连通，底部右镜面改为细蓝色但完整保留，诱导沿虚线提前判出口D。'),
 ('Plane463','v01','189',[style('kite',width=3)],
  '用红色粗轮廓强调网格风筝，诱导在读到宽高均三倍后错误回答放大风筝189而非题目所问的小风筝。全部网格点和尺寸语义不变。'),
 ('Plane483','v01','8',[style('gray',width=3)],
  '四个阴影叶片同红粗轮廓分组，诱导每片按2单位估计而答8，保留原灰色填充和4x4格线。'),
 ('Plane236','v04','D',[style('o24',width=3),style('o31',width=3)],
  '入射激光与上排原虚线统一3pt红色，不修改任一镜面。预设模型在到达C列后漏追下排反射而误答D。此前2pt方案误答D/D但预设E而淘汰，本份在测试前改用更强3pt新PNG并预设D。'),
 ('Plane478','v03','4',[style('r0',width=2),style('r1',width=2),style('r2',width=2),
  {'type':'add_point','id':'triple_overlap_focus','xy':[2.14,2.18],'color':'#2563EB'}],
  '三个来源矩形同红轮廓，并在三重交叠空白区域加一个蓝色注意点，诱导把三个来源矩形加一个中心交叠计为4，漏掉其他组合。蓝点不在边界或交点、不新增边或矩形。'),
 ('Plane488','v01','32.5',[
  dict(style('o0',width=3),interval={'path_id':'p0','path_sha256':'e2b1d396ff2b5e7466e20cbd801ee86495a6c253899e575276820a40071679f3','start':0.578125,'end':0.671875,'wrap':False}),
  dict(style('o0',width=3),interval={'path_id':'p0','path_sha256':'e2b1d396ff2b5e7466e20cbd801ee86495a6c253899e575276820a40071679f3','start':0.75,'end':1.0,'wrap':False})],
  '上方两折线之间的短边与标5的左侧边同红色局部强调，诱导把同色当等长，误将所得梯形上底当5，计算(8+5)*5/2=32.5。未添加等长符号，原5、8标注与所有折线保持。'),
 ('Plane192','v03','A',[style('route0_'+str(i),width=3) for i in range(2)]+
  [dict(style('route'+str(j)+'_'+str(i),'#2563EB',1),linestyle='dashed') for j,n in [(1,4),(2,4),(3,8)] for i in range(n)],
  '把只有两段且转弯最少的A路线用红3pt强调，其余三条完整蓝色虚线，诱导把最少段数当最短距离。所有路径仍由45度单位斜段构成，几何长度相等不变。'),
 ('Plane175','v04','C',[
  dict(style('given_notched_piece',width=3),interval={'path_id':'p0','path_sha256':'45cb6dda5f89415768148a0f8efe409941de61668161432a3854e4d17d175f9a','start':1/3,'end':2/3,'wrap':False}),
  dict(style('option2',width=3),interval={'path_id':'p0','path_sha256':'f52f00e61b9fdacbbd3c97923c21aef9b9710edfebedfdd5035cb798ff8acd00','start':1/3,'end':2/3,'wrap':False})],
  '仅把已知纸片与错误选项C的V形凹口两条局部边同红3pt强调，诱导按局部匹配选择C，忽略完整方形拼接。其余轮廓全黑保持，未添加线或关系符号。'),
 ('Plane175','v05','C',[
  dict(style('given_notched_piece',width=2),interval={'path_id':'p0','path_sha256':'45cb6dda5f89415768148a0f8efe409941de61668161432a3854e4d17d175f9a','start':1/3,'end':2/3,'wrap':False}),
  dict(style('option2',width=2),interval={'path_id':'p0','path_sha256':'f52f00e61b9fdacbbd3c97923c21aef9b9710edfebedfdd5035cb798ff8acd00','start':1/3,'end':2/3,'wrap':False}),
  {'type':'add_point','id':'source_notch_anchor','xy':[9.414213562373096,6.707106781186548],'color':'#2563EB'},
  {'type':'add_point','id':'option_notch_anchor','xy':[9.414213562373096,0.3535533905932738],'color':'#2563EB'}],
  '已知纸片与错误C仅V形凹口两边同红2pt，并对两个凹口已有顶点加蓝色对应点。诱导错误边/点匹配，忽略整体拼接，四个标记均有对应功能。顶点xy来自本图snap_points完整精度。'),
 ('Plane440','v01','B',[
  {'type':'add_line','id':'diagonal_height_lure','endpoints':[[6.5,0.5],[6.5,1.9142135623730951]],'color':'#2563EB','linestyle':'dashed'},
  {'type':'add_point','id':'diagonal_lower_anchor','xy':[6.5,0.5],'color':'#DC2626'},
  {'type':'add_point','id':'diagonal_upper_anchor','xy':[6.5,1.9142135623730951],'color':'#DC2626'}],
  '只连接旋转单位正方形的上下顶点，以两红点和一蓝色虚线突出竖直对角线sqrt2，诱导把它当B到地面的完整高度，遗漏下顶点距地面的1/2。未改正方形、接触点、地面或B标签。'),
 ('Plane434','v01','A',[
  dict(style('o1',width=3),interval={'path_id':'p0','path_sha256':'0'*64,'start':23/36,'end':0.75,'wrap':False}),
  dict(style('o1',width=3),interval={'path_id':'p0','path_sha256':'0'*64,'start':5/36,'end':0.25,'wrap':False})],
  '只把水平矩形上左与下右两个外露短段同红3pt标示，诱导将外露段4误归属为灰色交叠平行四边形的底边，乘宽3误答12(A)。灰色区域实际底5、高3、面积15(D)，原矩形与重叠边不变。'),
 ('Plane166','v01','A',[
  dict(style(target,width=2),interval={'path_id':'p0','path_sha256':'0'*64,'start':0.0,'end':1.0,'wrap':False})
  for target in ['gear_contour_0','gear_contour_1','gear_contour_2','gear_contour_3']],
  '仅标红给定和错误选项A两齿轮的黑齿外缘，对应四个黑齿局部位置，诱导把小齿轮整转后复位错误推广到大齿轮。黑色填充、齿数和轮廓均保留，不给其他齿或整幅选项加色。'),
 ('Plane434','v02','B',[
  {'type':'add_line','id':'half_rectangle_lure','endpoints':[[0.0,0.0],[9.0,3.0]],'color':'#2563EB','linestyle':'dashed'},
  {'type':'add_point','id':'rectangle_corner_a','xy':[0.0,0.0],'color':'#DC2626'},
  {'type':'add_point','id':'rectangle_corner_c','xy':[9.0,3.0],'color':'#DC2626'}],
  '以两红点及蓝色虚线标出水平3x9矩形的对角线，诱导误把灰色交叠区域当对角线切下的半矩形，答27/2=13.5(B)。灰色区域仍跨对角线两侧，实际底5高3面积15(D)，原阴影不变。'),
 ('Plane175','v06','B',[
  dict(style('given_notched_piece',width=2),interval={'path_id':'p0','path_sha256':'45cb6dda5f89415768148a0f8efe409941de61668161432a3854e4d17d175f9a','start':1/3,'end':2/3,'wrap':False}),
  dict(style('option1',width=2),interval={'path_id':'p0','path_sha256':'0'*64,'start':1/3,'end':2/3,'wrap':False}),
  {'type':'add_point','id':'source_notch_anchor','xy':[9.414213562373096,6.707106781186548],'color':'#2563EB'},
  {'type':'add_point','id':'option_notch_anchor','xy':[5.767766952966369,0.7071067811865476],'color':'#2563EB'}],
  '将已知纸片V形凹口与错误B的斜边-横边凹口作红边蓝顶点对应，诱导忽略凹口角度及整形拼接而选B。四个标记仅建立错误对应，原轮廓、给定小方块与所有其他选项保持。'),
 ('Plane435','v01','4',[style('o23',width=3),style('o24',width=3)],
  '只把左右两个圆同红3pt配对，诱导只看同形而忽略两圆距折线不同，把三个真正匹配加上圆错误计为4。圆心位置、网格、折线及所有图形保持，原圆灰填充不变。'),
 ('Plane435','v02','5',[style('o23','#2563EB',2),style('o24','#2563EB',2),
  dict(style('o25',width=3),interval={'path_id':'p0','path_sha256':'0'*64,'start':1/3,'end':2/3,'wrap':False}),
  dict(style('o26',width=3),interval={'path_id':'p0','path_sha256':'0'*64,'start':1/3,'end':2/3,'wrap':False})],
  '两个位置不对称的圆同蓝轮廓，底部两个同朝向而非镜像的三角形斜边同红。两组错误对应诱导忽略反射位置和手性，把五对同形都算作折叠重合。只有四个原轮廓动作，无新增图形。'),
]

def main():
    config=load_config()
    config['runtime_dir']=str(HERE/'render_runtime')
    config['output_dir']=str(HERE/'render_output')
    adapter=RendererAdapter(config)
    metadata={}
    renderer=PluginRenderer(config,adapter,metadata)
    records=[]
    for qid,vid,wrong,actions,reason in DESIGNS:
        actions=copy.deepcopy(actions)
        directory=HERE/qid/vid
        directory.mkdir(parents=True,exist_ok=True)
        if (directory/'design.json').exists():
            records.append(json.loads((directory/'design.json').read_text(encoding='utf8')))
            continue
        try:
            metadata[qid]=adapter.inspect_question(qid)
            if any(a.get('interval',{}).get('path_sha256')=='0'*64 for a in actions):
                from partial_style import object_paths
                reference=adapter.scene(qid)
                try:
                    reference.fig.canvas.draw()
                    for action in actions:
                        if action.get('interval',{}).get('path_sha256')=='0'*64:
                            paths=object_paths(reference,action['target'])
                            path=next(p for p in paths if p['id']==action['interval']['path_id'])
                            action['interval']['path_sha256']=path['sha256']
                            if qid=='Plane166':
                                from matplotlib.path import Path as MplPath
                                import numpy as np
                                pairs={'gear_contour_0':'o6','gear_contour_1':'o25','gear_contour_2':'o38','gear_contour_3':'o57'}
                                item=next(o for o in adapter.frozen_scenes[qid]['objects'] if o['id']==pairs[action['target']])
                                polygon=MplPath(np.array(item['points'],dtype=float))
                                middle=[np.asarray(segment['control']).mean(axis=0) for segment in path['segments']]
                                indices=np.flatnonzero(polygon.contains_points(middle,radius=1e-7)).tolist()
                                assert indices and max(indices)-min(indices)<0.2*len(path['segments']),indices
                                action['interval']['start']=min(indices)/len(path['segments'])
                                action['interval']['end']=(max(indices)+1)/len(path['segments'])
                finally:reference.close()
            if qid=='Plane440':
                known={tuple(p['xy']) for p in metadata[qid]['snap_points']}
                assert (6.5,0.5) in known and (6.5,1.9142135623730951) in known
            (directory/'context.json').write_text(json.dumps(metadata[qid],ensure_ascii=False,indent=2),encoding='utf8')
            plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
                    'description':reason,'intent':f'预设诱导错误答案 {wrong}', 'params':{'actions':actions}}
            normalized,data,digest=renderer.render(plugin)
            normalized2,data2,digest2=renderer.render(normalized,frozen=True)
            assert digest==digest2 and data==data2
            (directory/'plugin.json').write_text(json.dumps(normalized,ensure_ascii=False,indent=2),encoding='utf8')
            (directory/'candidate.png').write_bytes(data)
            record={'question_id':qid,'variant_id':vid,'correct_answer':adapter.records[qid]['answer'],
                    'predicted_wrong_answer':wrong,'design_reason':reason,'plugin_path':str(directory/'plugin.json'),
                    'image_path':str(directory/'candidate.png'),'pixel_sha256':digest,'png_sha256':hashlib.sha256(data).hexdigest(),
                    'input_record_sha256':canonical_hash(adapter.records[qid]),'schema_valid':True,'baseline_pixels_match':True,
                    'deterministic_redraw':True,'action_count':len(actions),'review_status':'unreviewed','test_status':'pending'}
            (directory/'design.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf8')
            records.append(record)
            print(qid,vid,'OK',flush=True)
        except Exception as exc:
            print(qid,vid,type(exc).__name__,str(exc),flush=True)
            (directory/'error.txt').write_text(type(exc).__name__+': '+str(exc),encoding='utf8')
    (HERE/'designs.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')

if __name__=='__main__':main()
