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


class Ana10:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana10'
        self.source_id = 'custom_10'
        self.query = 'Find the largest interval on which the function f(x) is strictly decreasing. Please answer in the format [a, b].'
        self.answer = '[-2, 2]'
        self.answer_type = 'text'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana10.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-5, 5, 300, endpoint=True)
        y = 0.25 * (x ** 3 - 12 * x)
        plot_curve(ax, x, y)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
