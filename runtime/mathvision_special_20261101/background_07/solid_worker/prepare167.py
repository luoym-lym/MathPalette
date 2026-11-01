from design_tools import *
q='Solid167'
s=AD.scenes[q]
p=s['points']
fold_x=p['p52'][0]; fold_y=p['p49'][1]
top=np.array([p[x][:2] for x in ['p49','p50','p51']])
left=np.array([p[x][:2] for x in ['p52','p53','p54']])
def reflect(a,axis,c):
    b=a.copy();b[:,axis]=2*c-b[:,axis];return b
families=[]
for name,t,axis,c,other,oc in [('top_fold_triangle',top,1,fold_y,0,fold_x),('left_fold_triangle',left,0,fold_x,1,fold_y)]:
    diamond=np.vstack((t,reflect(t,axis,c)))
    bounds=diamond.max(0)-diamond.min(0)
    mirror=reflect(diamond,other,oc)
    assert np.isclose(np.linalg.norm(t[1]-t[0]),np.linalg.norm(t[2]-t[1]))
    families.append({'name':name,'triangle_flat_xy':t.tolist(),'diamond_unique_vertices':np.unique(diamond,axis=0).tolist(),'second_diamond_unique_vertices':np.unique(mirror,axis=0).tolist(),'extent_xy':bounds.tolist(),'long_axis':'vertical' if bounds[1]>bounds[0] else 'horizontal','centres':[diamond.mean(0).tolist(),mirror.mean(0).tolist()]})
proof={'question_id':q,'formal_answer':'C','fold_axes_flat_xy':{'vertical':fold_x,'horizontal':fold_y},'method':'Reflect each equilateral notch over its own fold to form a 60/120 degree rhombus, then reflect the rhombus over the other perpendicular fold.','families':families,'unique_choice_elimination':{'A':'Left-fold notch creates two horizontal rhombi at top/bottom; A instead has vertical rhombi there.','B':'Equilateral triangles yield 60/120 degree rhombi, not four right-angled squares.','C':'Exactly two horizontal rhombi on vertical centreline plus two vertical rhombi on horizontal centreline.','D':'Top-fold notch creates two vertical rhombi at left/right; D incorrectly makes them horizontal.','E':'E adds a central fifth hole absent from either cut; both cut families are away from the intersection of fold axes.'},'human_semantics':'Only existing notch and existing option hole edges are recolored. No edge, boundary, cut, piece or partition is added. Color is appearance correspondence, not an extra equality or a changed cut instruction.'}
math_path=TASK/q/'fold_math_audit.json';write(math_path,proof)
actions=[style('line14',RED,2,interval(q,'line14',.7,.9)),style('line14',BLUE,2,interval(q,'line14',.3,.5)),style('line21',RED),style('line24',RED),style('line22',BLUE),style('line23',BLUE)]
roles=['Red actual left-fold triangular notch sides identify the family that really produces horizontal diamonds on top/bottom.','Blue actual top-fold triangular notch sides identify the family that really produces vertical diamonds on left/right.','Red A top diamond falsely binds the left-fold notch to a vertical diamond, inducing failure to rotate notch orientation through unfolding.','Red A bottom diamond is the second reflection-mate of that same false family; retains original closed hole contour.','Blue A left diamond supplies the true perpendicular-family partner, making a structured source-to-output comparison.','Blue A right diamond completes the same true reflection pair.']
mechanism='Two perpendicular folded-notch families map by red/blue to A hole pairs, falsely preserving vertical diamond orientation for the left-fold notch while correctly retaining the top-fold family. Original cuts, long-axis distinctions and five choice labels remain unchanged.'
out=save_candidate(q,'orthogonal_notch_family_binding','A',actions,roles,mechanism,proof,math_path)
print(out)
