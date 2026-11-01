from design import main,style
SPECS=[
 ('Plane268','v03','D',[style('given_moving_body',width=3),style('given_moving_head',width=2),style('D_moving_body',width=3),style('D_moving_head',width=2)],
  '将给定移动币与错误D中保持直立的袋鼠头身轮廓同红色，诱导按同姿态匹配忽略滚动自转。四个轮廓覆盖仅改变颜色线宽，所有几何和箭头保持不变。'),
 ('Plane263','v01','5',[style('cell'+str(i),width=1.5) for i in range(5)],
  '将五个原单位格的边界同红色形成显著五格组，诱导只用面积下界25/5=5而忽略5×5不可拼性。所有格子和连接关系保持不变，无新增格线或文字。'),
]
if __name__=='__main__':main(SPECS,'third_designs.json')
