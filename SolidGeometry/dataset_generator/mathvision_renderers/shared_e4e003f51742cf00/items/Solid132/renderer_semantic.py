"""Deterministic 3D geometry -> frozen parallel projection -> 2D diagram.

Visibility is authored explicitly, not inferred by a general hidden-surface engine.
Importing this module never renders or writes an output file.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from PIL import Image

PROTOCOL_PATH = Path(__file__).resolve().parents[4] / "SolidGeometry/dataset_generator/protocol.json"
BRANCH_ROOT = Path(__file__).resolve().parents[4] / "SolidGeometry"
ROLES = {"edge", "silhouette", "section", "auxiliary", "region", "given_point"}


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def invalid(value):
        raise ValueError(f"Non-finite JSON number: {value}")

    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      object_pairs_hook=pairs, parse_constant=invalid)


def projection_fingerprint(projection):
    data = json.dumps(projection, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def finite(value, shape, name):
    result = np.asarray(value, dtype=float)
    if result.shape != shape or not np.isfinite(result).all():
        raise ValueError(f"Expected finite {shape} coordinates: {name}")
    return result


def positive(value, name):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"Expected a positive finite number: {name}")
    return value


def unit(vector):
    length = float(np.linalg.norm(vector))
    if not math.isfinite(length) or length <= 1e-12:
        raise ValueError("Degenerate direction or coincident endpoints.")
    return vector / length


def point(scene, reference):
    value = scene["points"][reference] if isinstance(reference, str) else reference
    return finite(value, (3,), str(reference))


def segment(scene, references):
    if len(references) != 2:
        raise ValueError("A segment requires exactly two endpoints.")
    a, b = [point(scene, ref) for ref in references]
    unit(b - a)
    return a, b


def project(scene, xyz):
    camera = scene["projection"]
    return ((np.asarray(xyz) - camera["origin"]) @ np.asarray(camera["matrix"]).T
            + camera["offset"])


def circle_frame(scene, item):
    center = point(scene, item["center"])
    u = finite(item["u"], (3,), item["id"] + ".u")
    v = finite(item["v"], (3,), item["id"] + ".v")
    if not np.allclose(np.array([u, v]) @ np.array([u, v]).T,
                       np.eye(2), rtol=0, atol=1e-10):
        raise ValueError(f"Circle axes must be orthonormal: {item['id']}")
    return center, u, v, positive(item["radius"], item["id"] + ".radius")


def circle_point(frame, degrees):
    center, u, v, radius = frame
    angle = math.radians(degrees)
    return center + radius * (math.cos(angle) * u + math.sin(angle) * v)


def arc_parts(scene, item):
    center, u, v, radius = circle_frame(scene, item)
    for interval in item["intervals"]:
        angles = np.radians(np.linspace(interval["start_deg"], interval["end_deg"],
                                        interval["samples"]))
        xyz = center + radius * (np.cos(angles)[:, None] * u + np.sin(angles)[:, None] * v)
        yield interval, project(scene, xyz)


def plane_residual(points):
    xyz = np.asarray(points)
    centered = xyz - xyz.mean(axis=0)
    _, singular, axes = np.linalg.svd(centered, full_matrices=True)
    if len(singular) < 2 or singular[1] <= 1e-12:
        raise ValueError("A plane requires non-collinear points.")
    return float(np.max(np.abs(centered @ axes[-1])))


def dimension_text(item):
    return item.get("text") or f"{item['value']:.{item['decimals']}f} {item['unit']}".rstrip()


def dimension_geometry(scene, item, units_per_pt):
    """Bind true 3D endpoints to a perpendicular offset in the projected page."""
    a, b = project(scene, [point(scene, ref) for ref in item["points"]])
    shift = finite(item["offset_pt"], (2,), item["id"]) * units_per_pt
    direction = unit(b - a)
    if np.linalg.norm(shift) <= 1e-12 or abs(float(np.dot(shift, direction))) > 1e-8 * np.linalg.norm(shift):
        raise ValueError(f"Distance range offset must be nonzero and perpendicular in projection: {item['id']}")
    return a, b, a + shift, b + shift


def validate_scene(scene, protocol=None):
    protocol = protocol or read_json(PROTOCOL_PATH)
    if (scene.get("scene_schema_version") != "1.0.0"
            or scene.get("protocol_version") != protocol["protocol_version"]):
        raise ValueError("Scene and redraw protocol versions do not match.")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", scene.get("id", "")):
        raise ValueError("Scene requires a safe, stable ID.")
    for field in ("source_dataset", "source_image", "source_note", "world_unit", "status"):
        if not scene.get(field):
            raise ValueError(f"Missing scene metadata: {field}")
    if scene.get("subject") != "SolidGeometry":
        raise ValueError("Expected subject SolidGeometry.")
    if scene["status"] == "redraw_example" and (scene.get("query") is not None or scene.get("answer") is not None):
        raise ValueError("An image-only example cannot invent a question or answer.")
    for name in scene["points"]:
        point(scene, name)

    tol = protocol["validation"]
    absolute, relative = tol["length_absolute_tolerance"], tol["relative_tolerance"]
    projection_tol = tol["projection_tolerance"]
    camera = scene["projection"]
    if camera["kind"] not in protocol["projection"]["supported"]:
        raise ValueError(f"Unsupported projection: {camera['kind']}")
    matrix = finite(camera["matrix"], (2, 3), "projection.matrix")
    finite(camera["origin"], (3,), "projection.origin")
    finite(camera["offset"], (2,), "projection.offset")
    if np.linalg.matrix_rank(matrix, tol=projection_tol) != 2:
        raise ValueError("Degenerate projection matrix.")
    if camera["kind"] == "orthographic" and not np.allclose(matrix @ matrix.T, np.eye(2), atol=projection_tol, rtol=0):
        raise ValueError("Orthographic projection rows must be orthonormal.")
    toward = unit(finite(camera["toward_viewer"], (3,), "projection.toward_viewer"))
    if np.linalg.norm(matrix @ toward) > projection_tol:
        raise ValueError("View direction must lie in the projection kernel.")
    visibility = scene["visibility"]
    if visibility["mode"] != "frozen_intervals":
        raise ValueError("Only explicitly frozen visibility is supported.")
    if visibility["projection_sha256"] != projection_fingerprint(camera):
        raise ValueError("Visibility is stale: revalidate it against the changed projection.")

    limits = finite([scene["view"]["xlim"], scene["view"]["ylim"]], (2, 2), "view")
    spans = limits[:, 1] - limits[:, 0]
    if (spans <= 0).any() or not math.isclose(*spans, abs_tol=1e-10, rel_tol=1e-10):
        raise ValueError("The frozen viewport must be square with increasing limits.")
    groups = [scene[key] for key in ("objects", "dimensions", "labels", "constraints")]
    ids = [item["id"] for group in groups for item in group]
    if len(ids) != len(set(ids)):
        raise ValueError("Object, dimension, label and constraint IDs must be unique.")
    objects = {item["id"]: item for item in scene["objects"]}
    checks = [{"id": "projection_and_visibility", "type": "projection", "passed": True,
               "projection_sha256": projection_fingerprint(camera), "automatic_occlusion": False}]

    def in_view(xy, name):
        xy = np.asarray(xy)
        if not np.isfinite(xy).all() or (xy < limits[:, 0] - absolute).any() or (xy > limits[:, 1] + absolute).any():
            raise ValueError(f"Projected object exceeds frozen view: {name}")

    def line_visibility(value):
        if value not in ("visible", "hidden"):
            raise ValueError(f"Unsupported visibility: {value}")

    for item in scene["objects"]:
        kind = item["type"]
        if item.get("role") not in ROLES:
            raise ValueError(f"Missing or unsupported semantic role: {item['id']}")
        if kind == "circular_arc":
            frame = circle_frame(scene, item)
            start, end = finite(item["domain_deg"], (2,), item["id"] + ".domain")
            if not 0 < end - start <= 360 or not item["intervals"]:
                raise ValueError("An arc needs a positive domain of at most 360 degrees.")
            previous = float(start)
            max_error = 0.0
            radius_px = (frame[3] * np.linalg.norm(matrix @ np.array(frame[1:3]).T, 2)
                         * protocol["output"]["width_px"] * protocol["figure"]["axes_position"][2] / spans[0])
            for interval in item["intervals"]:
                low, high = finite([interval["start_deg"], interval["end_deg"]], (2,), "arc interval")
                if abs(low - previous) > projection_tol or high <= low or high > end + projection_tol:
                    raise ValueError(f"Arc intervals must cover the domain without gaps or overlaps: {item['id']}")
                line_visibility(interval["visibility"])
                count = interval["samples"]
                if type(count) is not int or not 2 <= count <= 100000:
                    raise ValueError("Arc sample count must be a frozen integer >= 2.")
                error = radius_px * (1 - math.cos(math.radians(high - low) / (count - 1) / 2))
                max_error = max(max_error, error)
                for boundary, angle in (("start_point", low), ("end_point", high)):
                    if boundary in interval and not np.allclose(circle_point(frame, angle), point(scene, interval[boundary]),
                                                               atol=absolute, rtol=relative):
                        raise ValueError(f"Arc boundary disagrees with its 3D point: {item['id']}.{boundary}")
                previous = float(high)
            if abs(previous - end) > projection_tol:
                raise ValueError(f"Arc intervals do not cover the domain: {item['id']}")
            if max_error > tol["curve_max_chord_error_px"]:
                raise ValueError(f"Arc sampling is too coarse: {item['id']}")
            for _, xy in arc_parts(scene, item):
                in_view(xy, item["id"])
            checks.append({"id": item["id"], "type": "arc_sampling", "max_chord_error_px": max_error, "passed": True})
        elif kind in ("segment", "polyline", "face"):
            names = item["points"]
            if len(names) < (3 if kind == "face" else 2):
                raise ValueError(f"Too few vertices: {item['id']}")
            xyz = np.array([point(scene, name) for name in names])
            if kind == "segment":
                segment(scene, names)
            xy = project(scene, xyz)
            if kind == "face":
                if plane_residual(xyz) > absolute or not item.get("semantic_fill_reason"):
                    raise ValueError("A filled face requires coplanar vertices and a semantic reason.")
                if item.get("visibility") != "visible":
                    raise ValueError("Only explicitly visible face fills may be drawn.")
            else:
                line_visibility(item["visibility"])
                if (np.linalg.norm(np.diff(xy, axis=0), axis=1) <= projection_tol).any():
                    raise ValueError(f"A drawn edge collapses under this projection: {item['id']}")
            in_view(xy, item["id"])
        elif kind == "point":
            if item.get("visibility") != "visible":
                raise ValueError("A point marker must be explicitly visible.")
            in_view(project(scene, point(scene, item["point"])), item["id"])
        else:
            raise ValueError(f"Unsupported object: {kind}")
        if "linestyle" in item and (item["role"] != "auxiliary" or item["linestyle"] not in ("solid", "dashed")):
            raise ValueError("Only auxiliary objects may explicitly select a semantic linestyle.")

    for item in scene["constraints"]:
        kind = item["type"]
        if not item.get("basis"):
            raise ValueError("Constraints must distinguish source evidence from construction.")
        if kind == "distance":
            a, b = segment(scene, item["points"])
            measured = float(np.linalg.norm(b - a))
            passed = math.isclose(measured, positive(item["value"], item["id"]), rel_tol=relative, abs_tol=absolute)
        elif kind in ("parallel", "perpendicular", "equal_length"):
            a, b = segment(scene, item["segments"][0])
            c, d = segment(scene, item["segments"][1])
            u, v = unit(b - a), unit(d - c)
            if kind == "parallel":
                measured = float(np.linalg.norm(np.cross(u, v)))
                passed = measured <= relative
            elif kind == "perpendicular":
                measured = abs(float(np.dot(u, v)))
                passed = measured <= relative
            else:
                measured = [float(np.linalg.norm(b - a)), float(np.linalg.norm(d - c))]
                passed = math.isclose(*measured, rel_tol=relative, abs_tol=absolute)
        elif kind == "collinear":
            a, b, c = [point(scene, ref) for ref in item["points"]]
            measured = float(np.linalg.norm(np.cross(b - a, unit(c - a))))
            passed = measured <= absolute + relative * np.linalg.norm(c - a)
        elif kind == "coplanar":
            measured = plane_residual([point(scene, ref) for ref in item["points"]])
            passed = measured <= absolute
        elif kind in ("on_circle", "projected_tangent"):
            arc = objects[item["circle"]]
            if arc["type"] != "circular_arc":
                raise ValueError("A circle constraint must reference a circular arc.")
            center, u, v, radius = circle_frame(scene, arc)
            radial = point(scene, item["point"]) - center
            normal = np.cross(u, v)
            on_circle = (abs(np.dot(radial, normal)) <= absolute
                         and math.isclose(float(np.linalg.norm(radial)), radius, abs_tol=absolute, rel_tol=relative))
            if kind == "on_circle":
                measured = float(np.linalg.norm(radial))
                passed = on_circle
            else:
                a, b = segment(scene, item["segment"])
                t = unit(matrix @ np.cross(normal, radial))
                direction = unit(matrix @ (b - a))
                measured = abs(float(t[0] * direction[1] - t[1] * direction[0]))
                at_endpoint = any(np.allclose(point(scene, item["point"]), p, atol=absolute, rtol=relative) for p in (a, b))
                passed = on_circle and at_endpoint and measured <= relative
        elif kind == "angle":
            a, vertex, b = [point(scene, ref) for ref in item["points"]]
            measured = math.degrees(math.acos(float(np.clip(np.dot(unit(a - vertex), unit(b - vertex)), -1, 1))))
            target = float(item["degrees"])
            passed = math.isfinite(target) and 0 <= target <= 180 and abs(measured - target) <= tol["angle_absolute_tolerance_deg"]
        else:
            raise ValueError(f"Unsupported constraint: {kind}")
        checks.append({"id": item["id"], "type": kind, "basis": item["basis"], "measured": measured, "passed": bool(passed)})
        if not passed:
            raise ValueError(f"Geometry constraint failed: {item['id']} ({measured})")

    for item in scene["dimensions"]:
        if item["type"] != "distance" or item["unit"] != scene["world_unit"]:
            raise ValueError("Dimensions require world-space distance and matching units.")
        a, b = segment(scene, item["points"])
        measured = float(np.linalg.norm(b - a))
        if not math.isclose(measured, positive(item["value"], item["id"]), rel_tol=relative, abs_tol=absolute):
            raise ValueError(f"Dimension disagrees with 3D geometry: {item['id']}")
        if type(item["decimals"]) is not int or not 0 <= item["decimals"] <= 8:
            raise ValueError("Dimension decimal precision must be frozen.")
        dimension_geometry(scene, item, 1.0)
        finite(item["label_offset_pt"], (2,), item["id"])
        if "text" in item and (not isinstance(item["text"], str) or not item["text"].strip()):
            raise ValueError("Dimension label override must be nonempty text.")
        if not item.get("basis"):
            raise ValueError("Dimension interpretation needs source evidence.")
        checks.append({"id": item["id"], "type": "dimension", "text": dimension_text(item),
                       "measured_world_length": measured, "unit": item["unit"], "basis": item["basis"],
                       "style": "Plane02_parallel_dashed", "points": item["points"],
                       "projected_perpendicular_connections": True, "passed": True})
    for item in scene["labels"]:
        if item["type"] not in ("vertex", "text") or not item.get("text"):
            raise ValueError(f"Unsupported or empty label: {item['id']}")
        point(scene, item["anchor"])
        finite(item["offset_pt"], (2,), item["id"])
    return checks


def render_settings(protocol):
    return {"font.family": protocol["font"]["family"], "font.size": protocol["font"]["size_pt"],
            "svg.fonttype": protocol["font"]["svg_fonttype"], "svg.hashsalt": "MathPalette.SolidGeometry.1",
            "lines.scale_dashes": False, "path.simplify": False,
            "savefig.bbox": None, "savefig.transparent": False}


def render_scene(scene, protocol=None, *, check_layout=True):
    protocol = protocol or read_json(PROTOCOL_PATH)
    checks = validate_scene(scene, protocol)
    font, stroke = protocol["font"], protocol["stroke"]
    with matplotlib.rc_context(render_settings(protocol)):
        fig = plt.figure(figsize=protocol["figure"]["figsize_in"], dpi=protocol["figure"]["dpi"],
                         facecolor=protocol["output"]["background"])
        try:
            ax = fig.add_axes(protocol["figure"]["axes_position"])
            ax.set(xlim=scene["view"]["xlim"], ylim=scene["view"]["ylim"], aspect="equal")
            ax.set_autoscale_on(False)
            ax.set_axis_off()
            fig.canvas.draw()
            units_per_pt = np.ptp(scene["view"]["xlim"]) / ax.bbox.width * fig.dpi / 72
            artists, lines, texts = [], [], []

            def line(xy, name, visibility="visible", auxiliary=False, linewidth=None, dash_pattern=None, dimension=False):
                pattern = (stroke["hidden_dash_pattern_pt"] if visibility == "hidden"
                           else stroke["auxiliary_dash_pattern_pt"])
                pattern = dash_pattern or pattern
                dashed = visibility == "hidden" or auxiliary
                artist = ax.plot(*np.asarray(xy).T, color=stroke["color"],
                                 linewidth=linewidth or stroke["linewidth_pt"],
                                 linestyle=(0, pattern) if dashed else "solid",
                                 solid_capstyle=stroke["capstyle"], dash_capstyle=stroke["dash_capstyle"],
                                 antialiased=stroke["antialiased"], clip_on=False,
                                 zorder=2 if visibility == "hidden" else 3)[0]
                if dimension:
                    artist.set_gid(name)
                artists.append((name, artist))
                lines.append(artist)

            def label(text, xy, offset, name, ha="center", va="center", italic=False):
                artist = ax.annotate(text, xy=xy, xytext=offset, textcoords="offset points",
                                     fontfamily=font["family"],
                                     fontsize=font["vertex_size_pt"] if italic else font["size_pt"],
                                     fontstyle=font["vertex_style"] if italic else font["value_style"],
                                     color=font["color"], ha=ha, va=va, zorder=5, clip_on=False)
                artists.append((name, artist))
                texts.append((name, artist))

            for item in scene["objects"]:
                kind = item["type"]
                auxiliary = item["role"] == "auxiliary" and item.get("linestyle", "solid") == "dashed"
                if kind == "circular_arc":
                    for interval, xy in arc_parts(scene, item):
                        line(xy, item["id"], interval["visibility"], auxiliary)
                elif kind in ("segment", "polyline"):
                    line(project(scene, [point(scene, ref) for ref in item["points"]]),
                         item["id"], item["visibility"], auxiliary)
                elif kind == "face":
                    shape = Polygon(project(scene, [point(scene, ref) for ref in item["points"]]),
                                    closed=True, facecolor=semantic_color(scene, item, protocol),
                                    edgecolor="none", alpha=protocol["fill"]["semantic_alpha"], zorder=1)
                    ax.add_patch(shape)
                    artists.append((item["id"], shape))
                elif kind == "point":
                    xy = project(scene, point(scene, item["point"]))
                    # Line2D has a finite window extent, unlike a scatter collection.
                    artist = ax.plot(*xy, marker="o", linestyle="none",
                                     markersize=math.sqrt(protocol["point"]["area_pt2"]),
                                     markerfacecolor=protocol["point"]["filled_facecolor"],
                                     markeredgecolor=stroke["color"],
                                     markeredgewidth=protocol["point"]["edge_linewidth_pt"], zorder=4)[0]
                    artists.append((item["id"], artist))

            connection_keys = set()
            for item in scene["dimensions"]:
                a, b, p, q = dimension_geometry(scene, item, units_per_pt)
                line([p, q], item["id"] + "_range", auxiliary=True,
                     linewidth=protocol["dimension"]["linewidth_pt"],
                     dash_pattern=protocol["dimension"]["range_dash_pattern_pt"], dimension=True)
                for suffix, xy in (("_start", [a, p]), ("_end", [b, q])):
                    key = tuple(sorted(tuple(np.round(endpoint, 12)) for endpoint in xy))
                    if key not in connection_keys:
                        line(xy, item["id"] + suffix, linewidth=protocol["dimension"]["linewidth_pt"], dimension=True)
                        connection_keys.add(key)
                label(dimension_text(item), (p + q) / 2, item["label_offset_pt"], item["id"] + "_text",
                      item.get("ha", "center"), item.get("va", "center"))
            for item in scene["labels"]:
                label(item["text"], project(scene, point(scene, item["anchor"])), item["offset_pt"],
                      item["id"], item.get("ha", "center"), item.get("va", "center"), item["type"] == "vertex")

            fig.canvas.draw()
            if check_layout:
                renderer = fig.canvas.get_renderer()
                padding = stroke["linewidth_pt"] * fig.dpi / 72 / 2
                margin_fraction = protocol["view"]["minimum_outer_margin_fraction"]
                for name, artist in artists:
                    box = artist.get_window_extent(renderer).padded(padding)
                    if not (ax.bbox.contains(box.x0, box.y0) and ax.bbox.contains(box.x1, box.y1)):
                        raise ValueError(f"Object or label violates the {margin_fraction:.0%} outer margin: {name}")
                boxes = []
                for name, artist in texts:
                    box = artist.get_window_extent(renderer).padded(1)
                    if any(box.overlaps(other) for other in boxes):
                        raise ValueError(f"Text labels overlap: {name}")
                    for edge in lines:
                        path = edge.get_path().transformed(edge.get_transform())
                        if path.intersects_bbox(box, filled=False):
                            raise ValueError(f"Text label overlaps a diagram line: {name}")
                    boxes.append(box)
                checks.append({"id": "layout", "type": "layout", "outer_margin_fraction": margin_fraction,
                               "label_line_overlap": False, "label_label_overlap": False, "passed": True})
            return fig, checks
        except Exception:
            plt.close(fig)
            raise


def image_bytes(scene, vector=False):
    protocol = read_json(PROTOCOL_PATH)
    fig, checks = render_scene(scene, protocol)
    try:
        buffer = io.BytesIO()
        with matplotlib.rc_context(render_settings(protocol)):
            fig.savefig(buffer, format="svg" if vector else "png", dpi=protocol["figure"]["dpi"],
                        facecolor=protocol["output"]["background"], transparent=False, bbox_inches=None,
                        pad_inches=0, metadata={"Date": None, "Creator": "MathPalette SolidGeometry 1.0.0"}
                        if vector else {"Software": "MathPalette SolidGeometry 1.0.0"})
        data = buffer.getvalue()
        if not vector:
            with Image.open(io.BytesIO(data)) as image:
                if image.size != (protocol["output"]["width_px"], protocol["output"]["height_px"]):
                    raise ValueError("Expected a 768 x 768 PNG.")
                if image.convert("RGBA").getextrema()[3] != (255, 255):
                    raise ValueError("Expected fully opaque pixels.")
        return data, checks
    finally:
        plt.close(fig)


def draw(scene_path, output_path=None):
    scene_path = Path(scene_path).resolve()
    scene = read_json(scene_path)
    validate_scene(scene)
    target = (Path(output_path) if output_path else BRANCH_ROOT / "reproduced" / f"{scene['id']}.png").resolve()
    protected = {scene_path, (scene_path.parent / scene["source_image"]).resolve(),
                 PROTOCOL_PATH.resolve(), Path(__file__).resolve()}
    if target in protected:
        raise ValueError("A redraw cannot overwrite its source or frozen inputs.")
    if target.suffix.lower() not in (".png", ".svg"):
        raise ValueError("The output must be PNG or SVG.")
    data, checks = image_bytes(scene, vector=target.suffix.lower() == ".svg")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return {"image_path": str(target), "constraints": checks}


def semantic_color(scene, item, protocol):
    key = item.get("semantic_material")
    if key is None:
        return protocol["fill"]["semantic_facecolor"]
    spec = scene.get("semantic_materials", {})
    if not spec.get("source_evidence") or not spec.get("normalization_authority"):
        raise ValueError("Semantic material extension needs source evidence and authority")
    palette = spec.get("palette", {})
    if key not in palette:
        raise ValueError("Unknown semantic material class")
    value = palette[key]
    if not isinstance(value, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise ValueError("Semantic material must use explicit grayscale hex")
    rgb = [int(value[i:i+2], 16) for i in (1,3,5)]
    if len(set(rgb)) != 1:
        raise ValueError("Only grayscale source material fills allowed")
    if len(set(v.lower() for v in palette.values())) != len(palette):
        raise ValueError("Distinct material classes must not merge")
    return value
