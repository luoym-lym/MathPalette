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

class Ana04:
    """Sampled instance from DynaMath. Values are constants."""

    def __init__(self):
        self.id = 'Ana04'
        self.source_dataset = 'DynaMath'
        self.constant_a = 2
        self.constant_b = 1
        self.constant_c = 2
        self.constant_d = 3
        self.query = 'The period of y1 is ____ that of y2. Choices: (A) larger than (B) equal to (C) smaller than'
        self.answer = 'B'
        self.answer_type = 'multiple choice'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana04.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        cos = self.constant_b * np.cos(self.constant_a * x)
        plot_curve(ax, x, cos)
        sin = self.constant_d * np.sin(self.constant_c * x)
        plot_curve(ax, x, sin)
        # y1 is the former red cosine; y2 is the former blue sine.
        label(ax, np.pi - 0.08, 1.4, "y1", ha="right", va="bottom")
        label(ax, np.pi / 4, self.constant_d + 0.4, "y2", ha="center", va="bottom")
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
