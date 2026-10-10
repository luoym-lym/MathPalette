"""Record explicit user approval of a frozen MathPalette question.

Candidate preparation and agent visual inspection never imply approval.
Only invoke approve after the user explicitly passes the named question.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
from dataset_tools.geometry_dataset import read_json,write_json

REGISTRY_PATH=ROOT/"imports/mathverse_vision_dominant/question_user_reviews.json"
BRANCHES={"Analytics","PlaneGeometry","SolidGeometry"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_registry():
    if REGISTRY_PATH.exists():
        return read_json(REGISTRY_PATH)
    return {"schema_version":"1.0.0","policy":"explicit_user_approval","approvals":{}}


def content_fingerprint(branch,qid):
    if branch not in BRANCHES:
        raise ValueError(f"Unknown question branch: {branch}")
    if branch=="Analytics":
        base=ROOT/"Analytics/fine_grained_dataset"
        rows=[json.loads(line) for line in (base/"dataset.jsonl").read_text(encoding="utf-8").splitlines() if line]
        row=next((r for r in rows if r["id"]==qid),None)
        if row is None:
            raise ValueError(f"Missing Analytics candidate: {qid}")
        paths={"png":base/row["image"],
               "question_script":base/"dataset_generator/dataset_generator"/f"function_plot{int(qid[3:]):02d}.py",
               "protocol":base/"dataset_generator/protocol.json",
               "renderer":base/"dataset_generator/common_renderer.py"}
        provenance_path=base/"provenance/MathVerse"/f"{qid}.json"
        source_dataset="DynaMath"
        if provenance_path.exists():
            provenance=read_json(provenance_path)
            source_dataset=provenance["source_dataset"]
            paths.update(provenance=provenance_path,source_image=base/provenance["preserved_source_copy"],
                         coordinate_renderer=base/"dataset_generator/mathverse_renderer.py")
        payload={"id":qid,"branch":branch,"source_dataset":source_dataset,
                 "question":row["question"],"answer":row["answer"],
                 "files":{key:{"path":p.relative_to(ROOT).as_posix(),"sha256":sha(p)} for key,p in paths.items()}}
        digest=hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,allow_nan=False).encode()).hexdigest()
        return {"sha256":digest,"content":payload}
    scene_path=ROOT/branch/"dataset_generator/scenes"/f"{qid}.json"
    scene=read_json(scene_path)
    if scene["id"]!=qid:
        raise ValueError("Scene identity mismatch")
    paths={"scene":scene_path,"protocol":ROOT/branch/"dataset_generator/protocol.json",
           "png":ROOT/branch/"image"/f"{qid}.png","svg":ROOT/branch/"image"/f"{qid}.svg",
           "source_image":(scene_path.parent/scene["source_image"]).resolve()}
    payload={"id":qid,"branch":branch,"source_dataset":scene["source_dataset"],
             "source_key":scene["provenance"]["source_key"],"question":scene["query"],
             "answer":scene["answer"],"files":{key:{"path":p.relative_to(ROOT).as_posix(),"sha256":sha(p)}
                                               for key,p in paths.items()}}
    digest=hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,allow_nan=False).encode()).hexdigest()
    return {"sha256":digest,"content":payload}


def approval_state(approval,current_sha256):
    if not approval:
        return "pending_user_review"
    return "registered" if approval["content_sha256"]==current_sha256 else "needs_reapproval"


def registration_for(branch,qid,registry=None):
    registry=registry if registry is not None else read_registry()
    approval=registry["approvals"].get(qid)
    fingerprint=content_fingerprint(branch,qid)
    status=approval_state(approval,fingerprint["sha256"])
    return {"status":status,"user_pass":status=="registered", "reviewer":"user" if approval else None,
            "approved_at_utc":approval["approved_at_utc"] if approval else None,
            "content_sha256":fingerprint["sha256"],
            "approved_content_sha256":approval["content_sha256"] if approval else None}


def approve(branch,qid,instruction):
    if not instruction.strip():
        raise ValueError("Record the user's explicit approval instruction")
    fingerprint=content_fingerprint(branch,qid)
    report_path=(ROOT/"imports/mathverse_vision_dominant/results/analytics"/f"{qid}_redraw_report.json" if branch=="Analytics"
                 else ROOT/branch/"dataset_generator/reports"/f"{qid}_redraw_report.json")
    report=read_json(report_path) if report_path.exists() else None
    if report is None and branch!="Analytics":
        raise ValueError("Geometry preparation report is missing")
    if report and not (report.get("determinism_and_base_replay_verified") if branch=="Analytics"
                       else report["all_constraints_passed"] and report["determinism_verified"]):
        raise ValueError("Geometry preparation checks must pass before registration")
    if report and report["visual_review"]["status"]!="inspected":
        raise ValueError("Agent visual inspection is missing")
    for key,item in (report["inputs"].items() if report else []):
        path,expected=(item["path"],item["sha256"]) if isinstance(item,dict) else (key,item)
        if sha(ROOT/path)!=expected:
            raise ValueError(f"Stale report input: {path}")
    if report and report["output_png_sha256"]!=fingerprint["content"]["files"]["png"]["sha256"]:
        raise ValueError("The approved image must match the prepared report")
    if report and branch!="Analytics" and report["output_svg_sha256"]!=fingerprint["content"]["files"]["svg"]["sha256"]:
        raise ValueError("The SVG must match the prepared report")
    registry=read_registry()
    previous=registry["approvals"].get(qid)
    if previous and previous["content_sha256"]==fingerprint["sha256"]:
        return previous
    approval={"id":qid,"branch":branch,"reviewer":"user","instruction":instruction,
              "approved_at_utc":datetime.now(timezone.utc).isoformat(),
              "content_sha256":fingerprint["sha256"],"content":fingerprint["content"]}
    if previous:
        approval["previous_approvals"]=[*previous.get("previous_approvals",[]),
                                        {k:v for k,v in previous.items() if k!="previous_approvals"}]
    registry["approvals"][qid]=approval
    write_json(REGISTRY_PATH,registry)
    return approval


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("branch",choices=sorted(BRANCHES))
    parser.add_argument("qid")
    parser.add_argument("--instruction",required=True)
    args=parser.parse_args()
    approval=approve(args.branch,args.qid,args.instruction)
    print(json.dumps({k:approval[k] for k in ["id","branch","approved_at_utc","content_sha256"]},indent=2))
