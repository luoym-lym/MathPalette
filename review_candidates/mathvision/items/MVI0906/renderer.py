"""Deterministic code-native plane geometry scenes, with semantic validation."""
from __future__ import annotations

import io
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Polygon
import numpy as np
from PIL import Image

PROTOCOL_PATH = Path(__file__).resolve().parents[4]/"PlaneGeometry/dataset_generator/protocol.json"


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


def point(scene, value):
    xy = scene["points"][value] if isinstance(value, str) else value
    xy = np.asarray(xy, dtype=float)
    if xy.shape != (2,) or not np.isfinite(xy).all():
        raise ValueError(f"Invalid point: {value!r}")
    return xy


def unit(vector):
    norm = float(np.linalg.norm(vector))
    if norm <= 1e-12:
        raise ValueError("A direction requires distinct points.")
    return vector / norm


def cross(a, b):
    return float(a[0] * b[1] - a[1] * b[0])


def angle_geometry(scene, names, reflex=False):
    if len(names) != 3:
        raise ValueError("An angle requires [ray_point, vertex, ray_point].")
    first, vertex, last = [point(scene, name) for name in names]
    u, v = unit(first - vertex), unit(last - vertex)
    value = math.degrees(math.acos(float(np.clip(np.dot(u, v), -1, 1))))
    if np.linalg.norm(u + v) < 1e-12:
        bisector = np.array([-u[1], u[0]])
    else:
        bisector = unit(u + v)
    a, b = [math.degrees(math.atan2(w[1], w[0])) % 360 for w in (u, v)]
    if (b - a) % 360 > 180:
        a, b = b, a
    sweep = (b - a) % 360
    if reflex:
        return vertex, -bisector, 360 - value, b, b + 360 - sweep
    return vertex, bisector, value, a, a + sweep


def segment(scene, names):
    if len(names) != 2:
        raise ValueError("A segment requires two point references.")
    a, b = [point(scene, name) for name in names]
    unit(b - a)
    return a, b


def angle_spec(item):
    """Numeric/symbolic labels and callout labels can bind to the same rays."""
    names = item.get("points") if item["type"] in ("angle", "angle_arc") else item.get("angle_points")
    return names, item.get("reflex", False)


def same_angle(scene, first, second, protocol):
    """Compare rays, not point IDs; collinear endpoints denote the same angle."""
    names_a, reflex_a = angle_spec(first)
    names_b, reflex_b = angle_spec(second)
    if reflex_a != reflex_b:
        return False
    a, vertex_a, b = [point(scene, name) for name in names_a]
    c, vertex_b, d = [point(scene, name) for name in names_b]
    if not np.allclose(vertex_a, vertex_b, rtol=0,
                       atol=protocol["validation"]["length_absolute_tolerance"]):
        return False
    ray_tol = math.radians(protocol["validation"]["angle_absolute_tolerance_deg"])
    u, v, w, z = [unit(ray) for ray in (a-vertex_a, b-vertex_a, c-vertex_b, d-vertex_b)]
    equal = lambda x, y: np.allclose(x, y, rtol=0, atol=ray_tol)
    return bool((equal(u, w) and equal(v, z)) or (equal(u, z) and equal(v, w)))


def validate_angle_annotations(scene, protocol):
    arcs = [item for item in scene["objects"] if item["type"] == "angle_arc"]
    by_id = {item["id"]: item for item in arcs}
    for index, arc in enumerate(arcs):
        angle_geometry(scene, *angle_spec(arc))
        radius = arc.get("radius_pt", protocol["markers"]["angle_arc_radius_pt"])
        if not math.isfinite(radius) or radius <= 0:
            raise ValueError(f"Angle arc requires a positive finite radius: {arc['id']}")
        if arc.get("count", 1) != 1:
            raise ValueError(f"An angle must have exactly one arc: {arc['id']}")
        for previous in arcs[:index]:
            if same_angle(scene, arc, previous, protocol):
                raise ValueError(f"Duplicate arcs for the same angle: {previous['id']}, {arc['id']}")
    checks = []
    for label in scene["labels"]:
        names, reflex = angle_spec(label)
        if names is None:
            text = label.get("text", "")
            if label.get("role") == "arc_measure":
                # Circular arc measures do not introduce a central angle or new rays.
                if len(label.get("arc_points", [])) != 2 or "center" not in label:
                    raise ValueError(f"An arc-measure label requires center and endpoints: {label['id']}")
                center = point(scene, label["center"])
                for endpoint in label["arc_points"]:
                    unit(point(scene, endpoint) - center)
                continue
            if label["type"] == "angle" or any(mark in text for mark in ("\N{DEGREE SIGN}", "\\circ", "\N{GREEK SMALL LETTER THETA}")):
                raise ValueError(f"An angle label requires explicit rays and one arc: {label['id']}")
            continue
        angle_geometry(scene, names, reflex)
        arc = by_id.get(label.get("arc_id"))
        if arc is None:
            raise ValueError(f"An angle label requires exactly one bound angle arc: {label['id']}")
        if not same_angle(scene, label, arc, protocol):
            raise ValueError(f"Angle label and arc refer to different rays: {label['id']}")
        if label["type"] == "angle" and "degrees" not in label and not label.get("text"):
            raise ValueError(f"An angle label requires a value or symbol: {label['id']}")
        checks.append({"id": f"arc_binding_{label['id']}", "type": "angle_annotation",
                       "label_id": label["id"], "arc_id": arc["id"], "measured": 1, "passed": True})
    return checks


def segments_intersect(scene, first, second, tolerance):
    a, b = segment(scene, first)
    c, d = segment(scene, second)
    r, s = b - a, d - c
    denominator = cross(r, s)
    scale = max(float(np.linalg.norm(r) * np.linalg.norm(s)), 1)
    if abs(denominator) <= tolerance * scale:
        if abs(cross(c - a, r)) > tolerance * max(float(np.linalg.norm(r)), 1):
            return False
        low, high = sorted((float(np.dot(c - a, r) / np.dot(r, r)),
                            float(np.dot(d - a, r) / np.dot(r, r))))
        return high >= -tolerance and low <= 1 + tolerance
    t, u = cross(c - a, s) / denominator, cross(c - a, r) / denominator
    return -tolerance <= t <= 1 + tolerance and -tolerance <= u <= 1 + tolerance


def validate_scene(scene, protocol=None):
    protocol = protocol or read_json(PROTOCOL_PATH)
    if (scene.get("scene_schema_version") != "1.0.0" or
            scene.get("protocol_version") != protocol["protocol_version"]):
        raise ValueError("Scene and redraw protocol versions do not match.")
    if not scene.get("source_dataset"):
        raise ValueError("A scene requires its actual source_dataset.")
    for name in scene["points"]:
        point(scene, name)
    limits = np.asarray([scene["view"]["xlim"], scene["view"]["ylim"]], dtype=float)
    if limits.shape != (2, 2) or not np.isfinite(limits).all() or (np.diff(limits) <= 0).any():
        raise ValueError("The view requires finite, increasing limits.")
    spans = limits[:, 1] - limits[:, 0]
    if not math.isclose(*spans, rel_tol=1e-10, abs_tol=1e-10):
        raise ValueError("The frozen viewport must be square.")
    for name in scene["points"]:
        xy = point(scene, name)
        if (xy < limits[:, 0]).any() or (xy > limits[:, 1]).any():
            raise ValueError(f"Point outside viewport: {name}")
    ids = [item["id"] for item in scene["objects"] + scene["labels"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Object and label IDs must be unique.")
    tol = protocol["validation"]
    angle_tol = tol["angle_absolute_tolerance_deg"]
    abs_tol, rel_tol = tol["length_absolute_tolerance"], tol["relative_tolerance"]
    checks = []
    for item in scene.get("constraints", []):
        kind = item["type"]
        measured = None
        if kind == "angle":
            measured = angle_geometry(scene, item["points"], item.get("reflex", False))[2]
            passed = abs(measured - item["degrees"]) <= angle_tol
        elif kind == "distance":
            a, b = segment(scene, item["points"])
            measured = float(np.linalg.norm(b - a))
            passed = math.isclose(measured, item["value"], abs_tol=abs_tol, rel_tol=rel_tol)
        elif kind in ("collinear", "between"):
            a, b, c = [point(scene, name) for name in item["points"]]
            axis = c - a
            axis_unit = unit(axis)
            measured = abs(cross(b - a, axis_unit))
            passed = measured <= abs_tol + rel_tol * float(np.linalg.norm(axis))
            if kind == "between":
                t = float(np.dot(b - a, axis) / np.dot(axis, axis))
                passed = passed and -rel_tol <= t <= 1 + rel_tol
        elif kind in ("parallel", "perpendicular", "equal_length", "intersection"):
            a, b = segment(scene, item["segments"][0])
            c, d = segment(scene, item["segments"][1])
            u, v = unit(b - a), unit(d - c)
            if kind == "parallel":
                measured = abs(cross(u, v))
                passed = measured <= rel_tol
            elif kind == "perpendicular":
                measured = abs(float(np.dot(u, v)))
                passed = measured <= rel_tol
            elif kind == "equal_length":
                measured = [float(np.linalg.norm(b - a)), float(np.linalg.norm(d - c))]
                passed = math.isclose(*measured, abs_tol=abs_tol, rel_tol=rel_tol)
            else:
                measured = segments_intersect(scene, *item["segments"], rel_tol)
                passed = measured == item["intersects"]
        elif kind == "on_circle":
            measured = float(np.linalg.norm(point(scene, item["point"]) - point(scene, item["center"])))
            passed = math.isclose(measured, item["radius"], abs_tol=abs_tol, rel_tol=rel_tol)
        else:
            raise ValueError(f"Unsupported constraint: {kind}")
        checks.append({"id": item["id"], "type": kind, "measured": measured, "passed": bool(passed)})
        if not passed:
            raise ValueError(f"Geometry constraint failed: {item['id']} ({measured})")
    for item in scene["labels"]:
        if item["type"] == "angle" and "degrees" in item:
            measured = angle_geometry(scene, item["points"], item.get("reflex", False))[2]
            if abs(measured - item["degrees"]) > angle_tol:
                raise ValueError(f"Angle label disagrees with geometry: {item['id']}")
    checks.extend(validate_angle_annotations(scene, protocol))
    return checks


def render_scene(scene, protocol=None, *, check_layout=True):
    """Return a figure and measured constraints; callers own figure cleanup."""
    protocol = protocol or read_json(PROTOCOL_PATH)
    checks = validate_scene(scene, protocol)
    font, stroke = protocol["font"], protocol["stroke"]
    settings = {"font.family": font["family"], "font.size": font["size_pt"],
                "svg.fonttype": font["svg_fonttype"], "svg.hashsalt": "MathPalette.PlaneGeometry.1",
                "lines.scale_dashes": False, "path.simplify": False}
    with matplotlib.rc_context(settings):
        fig = plt.figure(figsize=protocol["figure"]["figsize_in"], dpi=protocol["figure"]["dpi"],
                         facecolor=protocol["output"]["background"])
        ax = fig.add_axes(protocol["figure"]["axes_position"])
        ax.set_xlim(scene["view"]["xlim"])
        ax.set_ylim(scene["view"]["ylim"])
        ax.set_aspect("equal", adjustable="box")
        ax.set_autoscale_on(False)
        ax.set_axis_off()
        fig.canvas.draw()
        unit_per_pt = (scene["view"]["xlim"][1] - scene["view"]["xlim"][0]) / ax.bbox.width * fig.dpi / 72
        labels = []

        def line(a, b, linestyle="solid", zorder=None):
            return ax.plot(*np.array([a, b]).T, color=stroke["color"],
                           linewidth=stroke["linewidth_pt"], linestyle=linestyle,
                           solid_capstyle=stroke["capstyle"], antialiased=stroke["antialiased"],
                           zorder=zorder or stroke["zorder"])[0]

        try:
            for item in scene["objects"]:
                kind = item["type"]
                style = item.get("linestyle", "solid")
                if style not in ("solid", "dashed"):
                    raise ValueError(f"Unsupported semantic linestyle: {style}")
                style = "solid" if style == "solid" else (0, protocol["auxiliary_line"]["dash_pattern_pt"])
                if kind == "segment":
                    a, b = segment(scene, item["points"])
                    line(a, b, style)
                elif kind in ("circle", "arc"):
                    center = point(scene, item["center"])
                    radius = float(item["radius"])
                    if not math.isfinite(radius) or radius <= 0:
                        raise ValueError("A circle/arc requires a positive finite radius.")
                    if kind == "circle":
                        shape = Circle(center, radius, fill=bool(item.get("semantic_color")))
                    else:
                        shape = Arc(center, 2 * radius, 2 * radius,
                                    theta1=item["start_deg"], theta2=item["end_deg"])
                    shape.set(color=stroke["color"], linewidth=stroke["linewidth_pt"],
                              linestyle=style, zorder=stroke["zorder"])
                    if item.get("semantic_color"):
                        shape.set_facecolor(item["semantic_color"])
                        shape.set_edgecolor("#000000")
                    ax.add_patch(shape)
                    if kind == "circle":
                        if (center - radius < np.array([ax.get_xlim()[0], ax.get_ylim()[0]])).any() or (
                                center + radius > np.array([ax.get_xlim()[1], ax.get_ylim()[1]])).any():
                            raise ValueError(f"Circle bounds exceed view: {item['id']}")
                    else:
                        # An arc may occupy only a small part of its full circle.
                        # Check the actual transformed Arc path against the viewport.
                        fig.canvas.draw()
                        bounds = shape.get_window_extent(fig.canvas.get_renderer())
                        view = ax.bbox
                        if (bounds.x0 < view.x0 or bounds.x1 > view.x1 or
                                bounds.y0 < view.y0 or bounds.y1 > view.y1):
                            raise ValueError(f"Arc bounds exceed view: {item['id']}")
                elif kind == "polygon":
                    vertices = [point(scene, name) for name in item["points"]]
                    if len(vertices) < 3:
                        raise ValueError("A polygon requires at least three vertices.")
                    fill = item.get("semantic_fill", False)
                    shape = Polygon(vertices, closed=True, edgecolor=item.get("edge_color", stroke["color"]),
                                    facecolor=item.get("semantic_color", protocol["fill"]["semantic_facecolor"]) if fill else "none",
                                    linewidth=stroke["linewidth_pt"], linestyle=style, zorder=1 if fill else 2)
                    if fill:
                        # Use a separate fill so the mathematical outline remains opaque.
                        shape.set_edgecolor("none")
                        shape.set_alpha(1 if item.get("semantic_color") else protocol["fill"]["semantic_alpha"])
                        ax.add_patch(shape)
                        ax.add_patch(Polygon(vertices, closed=True, fill=False, edgecolor=item.get("edge_color", stroke["color"]),
                                             linewidth=stroke["linewidth_pt"], linestyle=style, zorder=2))
                    else:
                        ax.add_patch(shape)
                elif kind == "point":
                    xy = point(scene, item["point"])
                    p = protocol["point"]
                    ax.scatter(*xy, s=p["area_pt2"], facecolor=p["filled_facecolor"] if item.get("filled", True) else p["open_facecolor"],
                               edgecolor=p["edgecolor"], linewidths=p["edge_linewidth_pt"], zorder=p["zorder"])
                elif kind in ("angle_arc", "right_angle"):
                    vertex, _, value, start, end = angle_geometry(scene, item["points"], item.get("reflex", False))
                    if kind == "angle_arc":
                        radius = item.get("radius_pt", protocol["markers"]["angle_arc_radius_pt"]) * unit_per_pt
                        shape = Arc(vertex, 2 * radius, 2 * radius, theta1=start, theta2=end,
                                    color=stroke["color"], linewidth=protocol["markers"]["linewidth_pt"], zorder=3)
                        shape.set_gid(item["id"])
                        ax.add_patch(shape)
                    else:
                        if abs(value - 90) > protocol["validation"]["angle_absolute_tolerance_deg"]:
                            raise ValueError("A right-angle marker requires a true right angle.")
                        first, _, last = [point(scene, name) for name in item["points"]]
                        size = item.get("size_pt", protocol["markers"]["right_angle_side_pt"]) * unit_per_pt
                        u, v = unit(first - vertex) * size, unit(last - vertex) * size
                        line(vertex + u, vertex + u + v, zorder=3)
                        line(vertex + u + v, vertex + v, zorder=3)
                elif kind in ("equal_tick", "parallel_mark"):
                    a, b = segment(scene, item["points"])
                    u = unit(b - a)
                    v = np.array([-u[1], u[0]])
                    middle = a + item.get("position", 0.5) * (b - a)
                    count = item.get("count", 1)
                    if type(count) is not int or not 1 <= count <= 4:
                        raise ValueError("A relation marker requires 1 to 4 strokes/arrows.")
                    gap = protocol["markers"]["tick_gap_pt"] * unit_per_pt
                    for i in range(count):
                        center = middle + (i - (count - 1) / 2) * gap * u
                        if kind == "equal_tick":
                            size = protocol["markers"]["tick_length_pt"] * unit_per_pt / 2
                            line(center - size * v, center + size * v, zorder=3)
                        else:
                            size = protocol["markers"]["parallel_arrow_size_pt"] * unit_per_pt
                            line(center - size * u + size * v / 2, center, zorder=3)
                            line(center - size * u - size * v / 2, center, zorder=3)
                else:
                    raise ValueError(f"Unsupported object: {kind}")

            for item in scene["labels"]:
                kind = item["type"]
                if kind == "vertex":
                    xy = point(scene, item["point"])
                    text = item.get("text", item["point"])
                    offset = item.get("offset_pt", protocol["labels"]["default_vertex_offset_pt"])
                    fontstyle = font["vertex_style"]
                elif kind == "angle":
                    xy, bisector, _, _, _ = angle_geometry(scene, item["points"], item.get("reflex", False))
                    radius = item.get("radius_pt", protocol["labels"]["default_angle_radius_pt"])
                    offset = (bisector * radius + np.asarray(item.get("offset_pt", [0, 0]), dtype=float)).tolist()
                    text = item.get("text") or f"{item['degrees']:g}\N{DEGREE SIGN}"
                    fontstyle = font["value_style"]
                elif kind == "text":
                    xy, offset = point(scene, item["anchor"]), item.get("offset_pt", [0, 0])
                    text, fontstyle = item["text"], font["value_style"]
                else:
                    raise ValueError(f"Unsupported label: {kind}")
                artist = ax.annotate(text, xy=xy, xytext=offset, textcoords="offset points",
                                     fontfamily=font["family"],
                                     fontsize=font["vertex_size_pt"] if kind == "vertex" else font["size_pt"],
                                     fontstyle=fontstyle,
                                     color=font["color"], ha=item.get("ha", "center"), va=item.get("va", "center"),
                                     zorder=protocol["labels"]["zorder"], clip_on=False)
                artist.set_gid(item["id"])
                labels.append((item["id"], artist))
            fig.canvas.draw()
            if check_layout:
                for name, artist in labels:
                    box = artist.get_window_extent(fig.canvas.get_renderer())
                    if not (fig.bbox.contains(box.x0, box.y0) and fig.bbox.contains(box.x1, box.y1)):
                        raise ValueError(f"Label exceeds output canvas: {name}")
            return fig, checks
        except Exception:
            plt.close(fig)
            raise


def image_bytes(scene, vector=False):
    protocol = read_json(PROTOCOL_PATH)
    fig, checks = render_scene(scene, protocol)
    try:
        buffer = io.BytesIO()
        with matplotlib.rc_context({"svg.fonttype": "path", "svg.hashsalt": "MathPalette.PlaneGeometry.1",
                                    "savefig.bbox": None, "savefig.transparent": False}):
            fig.savefig(buffer, format="svg" if vector else "png", dpi=protocol["figure"]["dpi"],
                        facecolor=protocol["output"]["background"], transparent=False, bbox_inches=None,
                        pad_inches=0, metadata={"Date": None} if vector else {"Software": f"MathPalette PlaneGeometry {protocol['protocol_version']}"})
        data = buffer.getvalue()
        if not vector:
            with Image.open(io.BytesIO(data)) as image:
                if image.size != (protocol["output"]["width_px"], protocol["output"]["height_px"]) or image.convert("RGBA").getextrema()[3] != (255, 255):
                    raise ValueError("Expected an opaque 768 x 768 PNG.")
        return data, checks
    finally:
        plt.close(fig)


def draw(scene_path, output_path=None):
    scene_path = Path(scene_path).resolve()
    target = Path(output_path).resolve() if output_path else scene_path.with_name("redrawn.png")
    if target == scene_path or target == scene_path.parent / read_json(scene_path)["source_image"]:
        raise ValueError("A redraw cannot overwrite its scene or source image.")
    if target.suffix.lower() not in (".png", ".svg"):
        raise ValueError("The output must be PNG or SVG.")
    data, checks = image_bytes(read_json(scene_path), vector=target.suffix.lower() == ".svg")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return {"image_path": str(target), "constraints": checks}
