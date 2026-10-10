"""Exercise explicit approval and invalidation against isolated frozen assets."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
from dataset_tools import geometry_review as review


class GeometryReviewTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root=Path(self.directory.name)
        for field,value in [("ROOT",self.root),("REGISTRY_PATH",self.root/"user_reviews.json")]:
            p=patch.object(review,field,value);p.start();self.addCleanup(p.stop)
        for qid in ["Plane01","Plane02"]:
            base=self.root/"PlaneGeometry"
            files={"dataset_generator/scenes/"+qid+".json":json.dumps({
                "id":qid,"source_dataset":"Synthetic","source_image":"../../originals/"+qid+".png",
                "provenance":{"source_key":qid},"query":"A synthetic question","answer":"1"}),
                "dataset_generator/protocol.json":"{}",
                "image/"+qid+".png":"frozen PNG fixture",
                "image/"+qid+".svg":"frozen SVG fixture",
                "originals/"+qid+".png":"original fixture"}
            for relative,value in files.items():
                path=base/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(value,encoding="utf-8")
            fingerprint=review.content_fingerprint("PlaneGeometry",qid)
            prepared={"all_constraints_passed":True,"determinism_verified":True,
                      "visual_review":{"status":"inspected","user_pass":False},
                      "inputs":fingerprint["content"]["files"],
                      "output_png_sha256":fingerprint["content"]["files"]["png"]["sha256"],
                      "output_svg_sha256":fingerprint["content"]["files"]["svg"]["sha256"]}
            path=base/"dataset_generator/reports"/(qid+"_redraw_report.json")
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(prepared),encoding="utf-8")

    def test_agent_checks_do_not_approve_other_questions(self):
        self.assertFalse(review.registration_for("PlaneGeometry","Plane01")["user_pass"])
        approved=review.approve("PlaneGeometry","Plane01","Plane01 approved by the user")
        self.assertTrue(review.registration_for("PlaneGeometry","Plane01")["user_pass"])
        self.assertFalse(review.registration_for("PlaneGeometry","Plane02")["user_pass"])
        self.assertEqual(review.approve("PlaneGeometry","Plane01","repeated same instruction"),approved)

    def test_modified_asset_revokes_current_pass_and_cannot_reuse_old_report(self):
        review.approve("PlaneGeometry","Plane01","Plane01 approved by the user")
        (self.root/"PlaneGeometry/image/Plane01.png").write_text("changed drawing",encoding="utf-8")
        state=review.registration_for("PlaneGeometry","Plane01")
        self.assertEqual(state["status"],"needs_reapproval")
        self.assertFalse(state["user_pass"])
        with self.assertRaisesRegex(ValueError,"Stale report input"):
            review.approve("PlaneGeometry","Plane01","user approves new content")


if __name__=="__main__":
    unittest.main()
