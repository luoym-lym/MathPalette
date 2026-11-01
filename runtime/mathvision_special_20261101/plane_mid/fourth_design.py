from design import main,style
SPECS=[
 ('Plane222','v01','5',[style('trapezoid'),style('square','#2563EB',1.5),style('boat')],
  '大梯形瓦片与船形外框同红色、小方片蓝色，诱导只取面积下界：36÷8向上取整为5，而不检查四梯形加一方片能否实际铺满。全部单位格、轮廓和面积不变。'),
 ('Plane272','v01','5',[style('tile'+str(i),width=1.5) for i in range(4)],
  'T形原四格同红色描边，突出4格×5块=20格的面积直觉，诱导忽略棋盘黑白染色障碍而错答5。原四格灰度填充和5×4棋盘均保持原样。'),
 ('Plane228','v01','1',[style('source_'+str(i),width=2) for i in (7,8,9,13)],
  '只把原图顶部单位格的四条原边同红色，诱导固定删除这个显著格而误答只得到一种。题干仍为任意删除一格，所有格子和五个候选形状均不变，颜色不增加删除限制。'),
]
if __name__=='__main__':main(SPECS,'fourth_designs.json')
