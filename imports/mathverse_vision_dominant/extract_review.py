"""Extract the local MathVerse review export without executing its HTML scripts."""
from __future__ import annotations

import base64
from collections import Counter
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
IMPORT_ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "wrong_review_vision_dominant.html"


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.parts.append("\n")


def plain(fragment):
    parser = TextParser()
    parser.feed(fragment)
    return "".join(parser.parts).strip()


def extract():
    raw = SOURCE.read_bytes()
    document = raw.decode("utf-8")
    cards = re.findall(r'<article\b([^>]*)>(.*?)</article>', document, re.S)
    records = []
    for attrs, card in cards:
        key = re.search(r'\bid="(s\d+)"', attrs).group(1)
        badge = plain(re.search(r'<span class="badge subfield">(.*?)</span>', card, re.S).group(1))
        subject, subfield = badge.split(" / ", 1)
        sample, problem = map(int, re.search(r'Sample (\d+) \(Problem (\d+)\)', card).groups())
        sections = {}
        for section in ("question", "gold", "response"):
            match = re.search(r'<div class="' + section + r'">.*?<div class="math">(.*?)</div>', card, re.S)
            if match is None:
                raise ValueError(f"Missing {section}: {key}")
            sections[section] = plain(match.group(1))
        mime, encoded = re.search(r'<img\b[^>]*src="data:(image/[^;]+);base64,([^"]+)"', card, re.S).groups()
        data = base64.b64decode(encoded, validate=True)
        with Image.open(io.BytesIO(data)) as image:
            image.load()
            size = list(image.size)
            extension = {"PNG": "png", "JPEG": "jpg"}[image.format]
        relative_image = f"sources/{key}.{extension}"
        destination = IMPORT_ROOT / relative_image
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and destination.read_bytes() != data:
            raise ValueError(f"Existing source changed: {key}")
        destination.write_bytes(data)
        if sample != int(key[1:]):
            raise ValueError(f"Sample ID mismatch: {key}")
        records.append({
            "source_key": key, "sample_id": sample, "problem_id": problem,
            "source_dataset": "MathVerse", "source_split": "testmini", "source_version": "Vision Dominant",
            "source_subject": subject, "source_subfield": subfield,
            "question": sections["question"], "source_answer": sections["gold"],
            "previous_model_response": sections["response"],
            "source_image": relative_image, "source_image_mime": mime, "source_image_size": size,
            "source_image_sha256": hashlib.sha256(data).hexdigest(),
            "source_html": "../../wrong_review_vision_dominant.html", "source_html_sha256": hashlib.sha256(raw).hexdigest()})
    if not records or len({r["source_key"] for r in records}) != len(records):
        raise ValueError("Empty review export or duplicate source keys.")
    (IMPORT_ROOT / "source_manifest.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(records), "subjects": dict(Counter(r["source_subject"] for r in records)),
                      "subfields": dict(Counter(r["source_subfield"] for r in records))}, ensure_ascii=False, indent=2))
    for r in records:
        print(f"{r['source_key']} | {r['source_subject']} / {r['source_subfield']} | {r['question'][:95].replace(chr(10), ' ')} | GT={r['source_answer']}")
    return records


if __name__ == "__main__":
    extract()
