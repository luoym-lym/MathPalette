"use strict";
// Coordinates stay in the frozen 2-D projection. Screen distance only chooses
// a nearby point; the result is that point's original full-precision xy.
const SolidBoardGeometry = (() => {
  function matrix(m, p) {
    return [m[0][0] * p[0] + m[0][1] * p[1] + m[0][2],
      m[1][0] * p[0] + m[1][1] * p[1] + m[1][2]];
  }
  function nearestPoints(points, transform, pixel, width, height, threshold = 12) {
    let best = threshold, found = [], location = null;
    for (const point of points) {
      const p = matrix(transform, point.xy);
      const d = Math.hypot((p[0] - pixel[0]) * width / 768, (p[1] - pixel[1]) * height / 768);
      if (d < best - 1e-7) { best = d; found = [point]; location = p; }
      else if (found.length && Math.abs(d - best) < 1e-7 && Math.hypot(p[0] - location[0], p[1] - location[1]) < 1e-7) found.push(point);
    }
    return found;
  }
  return {matrix, nearestPoints};
})();
if (typeof module !== "undefined" && module.exports) module.exports = SolidBoardGeometry;
