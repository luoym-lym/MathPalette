from design import main,style
SPECS=[
 ('Plane268','v02','B',[style('given_moving_body',width=3),style('given_moving_head',width=2),style('B_moving_body',width=3),style('B_moving_head',width=2)],
  '将滚动币完整头身轮廓与错误B姿态同红色强化对应，诱导忽略外滚产生的额外自转而误作90度。只改四条原轮廓，不移动或覆盖任何图形。'),
 ('Plane287','v02','A',[style('o0',width=1.5),style('o15',width=1.5),style('o13',width=3),style('o28',width=3)],
  '给定钟与错误A的钟框、长针两层同色对应，诱导镜像时间倒退时方向反置。两针仍保持精确原长度、角度与全部刻度，未添加新时钟信息。'),
 ('Plane291','v02','A',[style('gray0',width=3),style('gray1','#2563EB',1),style('half_divider','#2563EB',1)],
  '突出左侧大灰三角形并将右下小灰三角形边界标为蓝色，诱导只计算大灰三角形即1/4。两处灰度填充完全不变，面积和分割线无变动。'),
 ('Plane248','v01','E',[style('source0'),style('source1'),style('option4')],
  '两块给定卡片与分支较多的错误E外轮廓同红色，诱导将尖角和分支外观误判成无法用两件拼接。所有拼图轮廓及禁止翻面规则不变。'),
 ('Plane266','v01','B',[style('given12'),style('piece1'),style('piece3'),style('piece6')],
  '将缺口邻接块与错误组合1、3、6同红色轮廓，诱导把仅上下凹凸不同的1号错作2号。保留全部榫卯方向、编号和未完成区域。'),
 ('Plane277','v01','D',[style('given_gray0'),style('option3_0')],
  '给定图中黑三角形与错误D的半黑三角形同红色描边，诱导局部半黑样式匹配替代全局面积配平。黑白填充与全部边界保持不变。'),
]
if __name__=='__main__': main(SPECS,'more_designs.json')
