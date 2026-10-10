"""Audit the centered-layout migration and build full-page before/after reviews."""
from __future__ import annotations

from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps
from matplotlib.font_manager import findfont

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from dataset_tools.geometry_dataset import read_json, write_json, renderer_for
from dataset_tools.geometry_layout import layout_metrics

REVIEW = ROOT/"imports/mathverse_vision_dominant/layout_upgrade_20261010"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_display_only(before, after, allowed, description):
    assert len(before) == len(after), description
    for old, new in zip(before, after):
        assert {k:v for k,v in old.items() if k not in allowed} == {
            k:v for k,v in new.items() if k not in allowed}, description


def inspect_label_collisions(scene, renderer):
    """Return conservative box/path collisions for an independent visual review."""
    import matplotlib.pyplot as plt
    fig, _ = renderer.render_scene(scene)
    try:
        ax = fig.axes[0]
        canvas = fig.canvas.get_renderer()
        results = []
        texts = [(text, text.get_window_extent(canvas).padded(.5)) for text in ax.texts]
        annotation_names=[item["id"]+"_text" for item in scene.get("dimensions",[])]+[item["id"] for item in scene["labels"]]
        names={id(text):text.get_gid() or name for (text,_),name in zip(texts,annotation_names)}
        protocol=read_json(renderer.PROTOCOL_PATH)
        vertices={item["id"] for item in scene["labels"] if item["type"]=="vertex"}
        assert all(text.get_fontsize()==protocol["font"]["vertex_size_pt" if names[id(text)] in vertices else "size_pt"] for text,_ in texts)
        for i, (text, box) in enumerate(texts):
            crossed = []
            for edge in [*ax.lines, *ax.patches]:
                if edge.get_path().transformed(edge.get_transform()).intersects_bbox(box, filled=False):
                    crossed.append(edge.get_gid() or type(edge).__name__)
            # Some inherited scenes contain redundant, coincident records of the
            # same vertex name. They are one visible annotation, not two labels
            # competing for different space; retain those source records.
            def coincident(other):
                return (text.get_text()==other.get_text() and tuple(text.xy)==tuple(other.xy)
                        and tuple(text.get_position())==tuple(other.get_position()))
            overlap = [names[id(other)] for other, other_box in texts[:i]
                       if box.overlaps(other_box) and not coincident(other)]
            if crossed or overlap:
                results.append({"label":names[id(text)], "edges":crossed, "other_labels":overlap})
        return results
    finally:
        plt.close(fig)


def build_reviews(records):
    font = ImageFont.truetype(findfont("DejaVu Sans"), 20)
    for branch in ("PlaneGeometry", "SolidGeometry"):
        rows = [r for r in records if r["branch"] == branch]
        for start in range(0,len(rows),4):
            sheet = Image.new("RGB",(1200,1600),"white")
            draw = ImageDraw.Draw(sheet)
            for row, record in enumerate(rows[start:start+4]):
                qid = record["id"]
                draw.text((15,row*400+6),f"{qid} BEFORE / CENTERED 18 pt vertex",font=font,fill="black")
                for col, path in enumerate((REVIEW/"before"/branch/"image"/f"{qid}.png",
                                            ROOT/branch/"image"/f"{qid}.png")):
                    with Image.open(path) as im:
                        tile=ImageOps.contain(im.convert("RGB"),(570,365))
                        sheet.paste(tile,(col*600+(600-tile.width)//2,row*400+30))
            sheet.save(REVIEW/f"{branch}_{start//4+1:02d}.png")
    cards=[]
    for record in records:
        branch,qid=record["branch"],record["id"]
        cards.append(f'<article data-branch="{branch}" id="{qid}"><h2>{qid}</h2><div class="pair">'
                     f'<figure><a href="before/{branch}/image/{qid}.png"><img loading="lazy" src="before/{branch}/image/{qid}.png"></a><figcaption>调整前</figcaption></figure>'
                     f'<figure><a href="../../../{branch}/image/{qid}.png"><img loading="lazy" src="../../../{branch}/image/{qid}.png"></a><figcaption>新版 · 点名18 pt · 完整图示居中</figcaption></figure></div></article>')
    document='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>几何构图协议 · 调整前后</title>
<style>body{font:16px/1.5 system-ui;background:#f4f5f7;color:#17202b;margin:0}header,main{max-width:1200px;margin:24px auto;padding:0 18px}article{background:white;padding:18px;margin:22px 0;border-radius:8px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:15px}figure{margin:0}img{width:100%;display:block}figcaption{text-align:center}select,input{font:inherit;padding:6px}article[hidden]{display:none}h2{margin-top:0}@media(max-width:700px){.pair{grid-template-columns:1fr}}</style>
<header><h1>平面与立体几何 · 构图调整前后</h1><p>61题 · 768×768 · 点名18 pt · 数值和单位16 pt · 线宽1 pt · 最长边约占86% · 至少5%边距。图形保持比例，三维投影与显隐关系保留。</p><label>题型 <select id="branch"><option value="all">全部</option><option>PlaneGeometry</option><option>SolidGeometry</option></select></label> <input id="search" placeholder="题号"><p><a href="validation.json">核对记录</a> · <a href="../redraw_review.html">来源图、题干与答案核验</a></p></header><main>'''+''.join(cards)+'''</main><script>function filter(){const b=document.querySelector('#branch').value,q=document.querySelector('#search').value.toLowerCase();document.querySelectorAll('article').forEach(c=>c.hidden=(b!=='all'&&c.dataset.branch!==b)||!c.id.toLowerCase().includes(q))}document.querySelector('#branch').addEventListener('input',filter);document.querySelector('#search').addEventListener('input',filter);</script></html>'''
    (REVIEW/"layout_review.html").write_text(document,encoding="utf-8")


def main():
    manifest=read_json(REVIEW/"before_manifest.json")
    records=[]
    for branch, baseline in manifest["branches"].items():
        protocol=read_json(ROOT/branch/"dataset_generator/protocol.json")
        renderer=renderer_for(branch)
        previous_protocol=read_json(REVIEW/"before"/branch/"dataset_generator/protocol.json")
        assert protocol["stroke"]==previous_protocol["stroke"], branch+" stroke changed"
        for old_row in baseline:
            qid=old_row["id"]
            relative=Path(branch)/"dataset_generator/scenes"/f"{qid}.json"
            before=read_json(REVIEW/"before"/relative)
            current=read_json(ROOT/relative)
            assert {k:v for k,v in before.items() if k not in {"view","labels","dimensions","protocol_version"}}=={
                k:v for k,v in current.items() if k not in {"view","labels","dimensions","protocol_version"}}, qid+" geometry/source/answer changed"
            check_display_only(before["labels"],current["labels"],{"offset_pt","radius_pt"},qid+" label binding changed")
            check_display_only(before.get("dimensions",[]),current.get("dimensions",[]),{"offset_pt","label_offset_pt"},qid+" dimension binding changed")
            assert current["protocol_version"]==protocol["protocol_version"], qid
            assert current["view"]["layout"]["method"]=="frozen_content_fit", qid
            assert abs((current["view"]["xlim"][1]-current["view"]["xlim"][0])-(current["view"]["ylim"][1]-current["view"]["ylim"][0]))<1e-9,qid
            source=ROOT/branch/"originals"/f"{qid}.png"
            report=read_json(ROOT/branch/"dataset_generator/reports"/f"{qid}_redraw_report.json")
            assert digest(source)==report["inputs"]["source_image"]["sha256"],qid
            for name,item in report["inputs"].items():
                assert digest(ROOT/item["path"])==item["sha256"],f"{qid} stale report input {name}"
            assert report["all_constraints_passed"] and report["determinism_verified"],qid
            assert report["visual_review"]["status"]=="inspected",qid+" not visually inspected"
            with Image.open(ROOT/report["output_png"]) as image:
                assert image.size==(768,768) and image.convert("RGBA").getchannel("A").getextrema()==(255,255),qid
                metrics=layout_metrics(image)
            assert abs(metrics["long_side_fraction"]-protocol["view"]["target_long_side_fraction"])<=protocol["view"]["occupancy_tolerance_fraction"],qid
            assert max(abs(v) for v in metrics["center_offset_px"])<=protocol["view"]["center_tolerance_px"],qid
            assert metrics["minimum_outer_margin_fraction"]>=protocol["view"]["minimum_outer_margin_fraction"],qid
            assert digest(ROOT/report["output_png"])==report["output_png_sha256"]==report["visual_review"]["image_sha256"],qid
            assert digest(ROOT/report["output_svg"])==report["output_svg_sha256"],qid
            records.append({"id":qid,"branch":branch,"before_long_side_fraction":old_row["long_side_fraction"],
                            **metrics,"protocol_version":protocol["protocol_version"],
                            "geometry_projection_visibility_preserved":True,"source_question_answer_preserved":True,
                            "determinism_verified":True,"visual_review":"inspected",
                            "display_adjusted_labels":[n["id"] for o,n in zip(before["labels"],current["labels"]) if o!=n],
                            "conservative_label_collisions":inspect_label_collisions(current,renderer)})
        dataset_relative=(Path(branch)/"dataset.jsonl").as_posix()
        before_rows=[json.loads(line) for line in (REVIEW/"before"/dataset_relative).read_text(encoding="utf-8").splitlines() if line]
        paths=[ROOT/dataset_relative,ROOT/branch/"pending_dataset.jsonl"]
        retained=[json.loads(line) for path in paths if path.exists() for line in path.read_text(encoding="utf-8").splitlines() if line]
        assert len(retained)==len(before_rows) and {r["id"]:r for r in retained}=={r["id"]:r for r in before_rows},branch+" source records lost or changed"
    plane01=read_json(ROOT/"PlaneGeometry/dataset_generator/scenes/Plane01.json")
    assert "BE" not in {o["id"] for o in plane01["objects"]} and "BC" in {o["id"] for o in plane01["objects"]}
    assert next(l for l in plane01["labels"] if l["id"]=="label_D")["offset_pt"][1]<0
    summary={"question_count":len(records),"branch_counts":dict(Counter(r["branch"] for r in records)),
             "point_font_pt":18,"value_font_pt":16,"stroke_width_pt":1,"target_long_side_fraction":.86,
             "minimum_outer_margin_fraction":.05,"all_geometry_projection_visibility_preserved":True,
             "all_source_questions_answers_preserved":True,"all_reports_current_and_deterministic":True,
             "all_images_visually_inspected":True,"Plane01_user_corrections_preserved":True,
             "occupancy_by_branch":{b:{"before_average":sum(r["before_long_side_fraction"] for r in records if r["branch"]==b)/len(v),
                "after_average":sum(r["long_side_fraction"] for r in records if r["branch"]==b)/len(v)} for b,v in manifest["branches"].items()},
             "label_collision_candidates":sum(bool(r["conservative_label_collisions"]) for r in records),"questions":records}
    write_json(REVIEW/"validation.json",summary)
    build_reviews(records)
    print(json.dumps({k:v for k,v in summary.items() if k!="questions"},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
