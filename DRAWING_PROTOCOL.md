# MathPalette drawing protocol 2.1

Each `MathPalette_Dataset/questions/<ID>.py` defines one class named after the question. `draw(output_path=None, *, variant=None)` draws the original; `variant="C01"` calls the same class's `draw_C01()` method. Importing a question does not create files.

Construction is explicit Python. Coordinates, sampled curves, projection matrices, visibility fragments, and label offsets remain in the question class. No source-specific renderer, image replay, JSON scene, or workbench is required.

## Shared tools

`MathPalette_Dataset/drawing.py` provides three configurations: `ANALYTICS`, `PLANE`, and `SOLID`.

| Tool | Purpose |
| --- | --- |
| `Canvas(protocol, xlim=..., ylim=...)` | Fixed canvas, square viewport, isolated style settings |
| `line(points, **style)` | Segments, polylines, sampled curves, segment collections |
| `point(points, filled=True, **style)` | Filled or open points |
| `path(vertices, codes, **style)` | Vector paths, including Bezier curves |
| `circle(center, radius)` / `arc(center, radius, start, end)` | Circles and degree-based arcs |
| `fill(points, **style)` | Polygon and region fills |
| `text(text, xy, offset_pt=..., vertex=False)` | Text and fixed point offsets |
| `project(xyz)` | A frozen rank-two 2-by-3 parallel projection |
| `save(path)` | Opaque PNG or SVG output |

```python
from MathPalette_Dataset.drawing import Canvas, PLANE

class Example:
    def draw(self, output_path):
        with Canvas(PLANE, xlim=(-2, 6), ylim=(-2, 6)) as canvas:
            points = [(0, 0), (4, 0), (1, 3)]
            canvas.line([*points, points[0]], id="triangle")
            canvas.text("A", points[0], offset_pt=(0, -12), vertex=True)
            return canvas.save(output_path)
```

PNG output is 768 by 768 pixels at 100 dpi, with an opaque white background and equal coordinate scaling. Autoscaling and tight cropping are disabled. Analytics shows coordinate axes by default; Plane and Solid hide them. Frozen appearance overrides remain explicit in each question.

Plane constructions preserve the stated geometric relations. Solid constructions preserve geometry, projection, and visible/hidden fragments separately; projection does not perform automatic hidden-surface removal. Page offsets and projected distances do not replace spatial measurements.

Temporary output goes to `.runtime/reproduced/` unless a path is supplied. `save()` rejects output inside the formal dataset directory. The saved formal PNGs use the current code as their reference; there is no legacy grayscale tolerance or compatibility renderer.

Question text, answers, choices, or mathematical construction changes still require user confirmation. Rendering a figure does not approve a question or create a Pass/Collect record. If approved drawing changes are published, regenerate the affected PNGs and synchronize the image references, metadata hashes, and `SHA256SUMS`.
