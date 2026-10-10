"""Frozen analytic-geometry questions.

Each class is one sampled instance. Numbers in __init__ are constants from
that sample. draw() does not choose parameters.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

_ROOT = Path(__file__).resolve().parents[1]
_DATASET_ROOT = _ROOT.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from common_renderer import (  # noqa: E402
    add_styled_patch,
    aux_hline,
    aux_vline,
    build_expression,
    domain_linspace,
    figure_label,
    fill_polygon,
    fill_region,
    finalize,
    label,
    open_canvas,
    plot_curve,
    scatter_points,
    slope_segments,
)

class Ana01:
    """Sampled instance of source question Q47. Values are constants."""

    def __init__(self):
        self.id = 'Ana01'
        self.source_id = 'Q47'
        self.a = 1
        self.b = 1
        self.c = -2
        self.d = -4
        self.e = 2
        self.query = 'What is the limit of the function as x approaches 1 from the left side?'
        self.answer = 0
        self.answer_type = 'float'
        self.subject = 'analytic geometry'
        self.level = 'undergraduate'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana01.png."""
        fig, ax = open_canvas()
        x1 = domain_linspace(-10, 1, 200, endpoint=True)
        x2 = domain_linspace(1, 10, 200, endpoint=True)
        f1 = self.a * x1 ** 2 + self.b * x1 + self.c
        f2 = self.d * x2 + self.e
        plot_curve(ax, x1, f1)
        plot_curve(ax, x2, f2)
        scatter_points(ax, 1, self.a + self.b + self.c, open_marker=True)
        scatter_points(ax, 1, self.d + self.e)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
