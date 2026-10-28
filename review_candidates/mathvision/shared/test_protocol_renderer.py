"""Independent figure and source-adaptation checks; no candidate fixtures."""
import ast, unittest
if __package__:
    from . import protocol_renderer as r
else:
    import protocol_renderer as r
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class ProtocolTests(unittest.TestCase):
    def setUp(self):
        self.protocol=r.read(r.machine_protocol('PlaneGeometry'))
    def tearDown(self):plt.close('all')
    def test_opaque_hollow_point_and_semantic_fill(self):
        fig,ax=plt.subplots();line=ax.plot([0],[0],marker='o',mfc='white')[0];line.set_gid('p')
        fill=Polygon([[0,0],[1,0],[0,1]],facecolor='red',edgecolor='black');fill.set_gid('region');ax.add_patch(fill)
        scene={'objects':[{'id':'p','type':'point','filled':False},{'id':'region','type':'polygon'}],'labels':[]}
        review={'semantic_fills':[{'object_ids':['region'],'reason':'independent region fixture','color':'preserve'}]}
        records=r.normalize(fig,scene,review,self.protocol)
        self.assertEqual(line.get_markerfacecolor(),'white');self.assertEqual(line.get_markersize(),6)
        self.assertAlmostEqual(fill.get_facecolor()[0],.2126);self.assertEqual(fill.get_linewidth(),1)
        self.assertEqual(records[0]['marker_size_pt'],6)
    def test_semantic_face_alpha_never_fades_outline_or_white_hole(self):
        fig,ax=plt.subplots()
        region=Polygon([[0,0],[1,0],[0,1]],facecolor='gray',edgecolor='black',alpha=.3);region.set_gid('region');ax.add_patch(region)
        hole=Polygon([[0,0],[.1,0],[0,.1]],facecolor='white',edgecolor='black');hole.set_gid('hole');ax.add_patch(hole)
        scene={'objects':[{'id':'region','type':'polygon'},{'id':'hole','type':'polygon'}],'labels':[]}
        review={'semantic_fills':[{'object_ids':['region'],'reason':'distinct region fixture'},{'object_ids':['hole'],'reason':'opaque white cutout fixture','color':'#FFFFFF'}]}
        r.normalize(fig,scene,review,self.protocol)
        self.assertIsNone(region.get_alpha())
        self.assertEqual(region.get_edgecolor(),(0.,0.,0.,1.))
        self.assertEqual(region.get_facecolor()[3],self.protocol['fill']['semantic_alpha'])
        self.assertEqual(hole.get_facecolor(),(1.,1.,1.,1.))
        self.assertEqual(hole.get_edgecolor(),(0.,0.,0.,1.))

    def test_unapproved_fill_removed_and_unknown_decision_rejected(self):
        fig,ax=plt.subplots();patch=Polygon([[0,0],[1,0],[0,1]],facecolor='red');ax.add_patch(patch)
        r.normalize(fig,{'objects':[],'labels':[]},{},self.protocol)
        self.assertEqual(patch.get_facecolor()[3],0)
        with self.assertRaises(ValueError):r.decisions({'semantic_fills':[{'object_ids':['x']}]},'semantic_fills')
    def test_adaptation_keeps_geometry_postprocessing(self):
        source="""def render():
    fig, ax = build()
    ax.plot([0,1],[0,1])
    postprocess_geometry(fig)
    fig.savefig('never.png')
    return 'bytes'
"""
        tree=r.ExposeFigure().visit(ast.parse(source));ast.fix_missing_locations(tree)
        code=ast.unparse(tree)
        self.assertLess(code.index('postprocess_geometry'),code.index('return (fig'))
        self.assertNotIn('savefig',code)
if __name__=='__main__':unittest.main()
