from design import main,style
SPECS=[
 ('Plane272','v02','6',[style('tile'+str(i),width=3) for i in range(3)]+[style('tile3','#2563EB',1)],
  '将T形顶排三个原格边界同红色、下方凸格蓝色，诱导仅把红色三格作为可用瓦片而按20÷3取6。四格灰色填充和连接关系全部保留，题干的灰色T块仍唯一。'),
 ('Plane228','v02','2',[style('source_'+str(i),'#2563EB',1) for i in (7,8,9,13)],
  '顶部原单位格描边蓝色、其余原边黑色，诱导把蓝色突出格当作提示而漏入原拼块计数，继而按四格去一格错答2种。未加减任何方格或候选轮廓。'),
 ('Plane275','v01','8',[style('outer_green'),style('Martin_firstgreen'),style('Martin_secondgreen')],
  '已闭合圆轨与右边S形两段轨道外轮廓同红色，诱导把一正一反弯的后续闭合错误归同于8段圆。原两段方向、接口和示例8段分界全部保留。'),
 ('Plane256','v01','0',[style('ribbon0_0'),style('ribbon1_3'),style('ribbon0_3','#2563EB'),style('ribbon1_2','#2563EB')],
  '将重排前后最短条同红、最长条同蓝，强化同材料对应，诱导误把周长也当重排不变量而答0。每条原尺寸、接触边、排列与标签均不变。'),
 ('Plane271','v01','C',[style('left_rectangle'),style('right_rectangle'),style('left_large_up','#2563EB'),style('right_large_right','#2563EB')],
  '两图矩形同红、对应大四分之一圆同蓝，诱导抵消周长时只计一次长短边差而漏乘2，错选10cm。原圆弧、直线和拼接完全不变。'),
]
if __name__=='__main__':main(SPECS,'fifth_designs.json')
