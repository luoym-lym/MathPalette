"""Check content fitting on independent off-center 2D/3D scenes."""
from copy import deepcopy
import io
from pathlib import Path
import sys
import unittest

import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
from dataset_tools.geometry_dataset import read_json, renderer_for
from dataset_tools.geometry_layout import fit_scene, layout_metrics


class GeometryLayoutTests(unittest.TestCase):
    def verify(self,scene,branch):
        renderer=renderer_for(branch)
        original=deepcopy(scene)
        fitted,metrics=fit_scene(scene,renderer)
        self.assertEqual(scene,original)
        for field in original:
            if field!="view":
                self.assertEqual(fitted[field],original[field])
        self.assertAlmostEqual(metrics["long_side_fraction"],.86,delta=.003)
        self.assertLessEqual(max(abs(v) for v in metrics["center_offset_px"]),1)
        self.assertGreaterEqual(metrics["minimum_outer_margin_fraction"],.05)
        refitted,_=fit_scene(fitted,renderer)
        self.assertEqual(fitted,refitted)
        png,_=renderer.image_bytes(fitted)
        with Image.open(io.BytesIO(png)) as im:
            self.assertEqual(im.size,(768,768))
            self.assertEqual(im.convert("RGBA").getchannel("A").getextrema(),(255,255))
            self.assertEqual(layout_metrics(im),metrics)
        fig,_=renderer.render_scene(fitted)
        try:
            self.assertEqual([t.get_fontsize() for t in fig.axes[0].texts],[18,16])
            self.assertTrue(all(l.get_linewidth()==1 for l in fig.axes[0].lines))
        finally:
            plt.close(fig)

    def test_plane_includes_long_annotation_and_recenters_without_distortion(self):
        renderer=renderer_for("PlaneGeometry")
        scene={"scene_schema_version":"1.0.0","protocol_version":read_json(renderer.PROTOCOL_PATH)["protocol_version"],
               "id":"OffCenterPlane","source_dataset":"Custom","view":{"xlim":[-20,20],"ylim":[-20,20]},
               "points":{"A":[6,3],"B":[12,3],"C":[7,6]},
               "objects":[{"id":a+b,"type":"segment","points":[a,b]} for a,b in [("A","B"),("B","C"),("C","A")]],
               "labels":[{"id":"name_A","type":"vertex","point":"A","offset_pt":[-14,-12]},
                         {"id":"measurement","type":"text","text":"123.45 mm","anchor":[9,3],"offset_pt":[0,-20]}],
               "constraints":[{"id":"width","type":"distance","points":["A","B"],"value":6}]}
        self.verify(scene,"PlaneGeometry")

    def test_solid_preserves_projection_and_hidden_edge(self):
        renderer=renderer_for("SolidGeometry")
        camera={"kind":"orthographic","matrix":[[1,0,0],[0,1,0]],"origin":[0,0,0],
                "offset":[4,2],"toward_viewer":[0,0,1]}
        scene={"scene_schema_version":"1.0.0","protocol_version":read_json(renderer.PROTOCOL_PATH)["protocol_version"],
               "id":"OffCenterSolid","subject":"SolidGeometry","status":"test_fixture","source_dataset":"Custom",
               "source_image":"unused.png","source_note":"Independent layout fixture","world_unit":"m",
               "projection":camera,"visibility":{"mode":"frozen_intervals","projection_sha256":renderer.projection_fingerprint(camera)},
               "view":{"xlim":[-20,20],"ylim":[-20,20]},"points":{"A":[0,0,0],"B":[5,0,0],"C":[2,3,1]},
               "objects":[{"id":a+b,"type":"segment","role":"edge","points":[a,b],"visibility":visibility}
                          for a,b,visibility in [("A","B","visible"),("B","C","visible"),("C","A","hidden")]],
               "dimensions":[],
               "labels":[{"id":"name_A","type":"vertex","anchor":"A","text":"A","offset_pt":[-14,-12]},
                         {"id":"measurement","type":"text","anchor":[2.5,0,0],"text":"123.45 mm","offset_pt":[0,-20]}],
               "constraints":[]}
        self.verify(scene,"SolidGeometry")


if __name__=="__main__":
    unittest.main()
