"use strict";
// Pure coordinate helpers shared by the drawing board and offline tests.
(() => {
  const matrix = (m, p) => [m[0][0] * p[0] + m[0][1] * p[1] + m[0][2],
    m[1][0] * p[0] + m[1][1] * p[1] + m[1][2]];
  function nearest(pixel, points, forward, screenScale, threshold = 10) {
    let best = threshold, chosen = null;
    for (const point of points) {
      const p = matrix(forward, point.xy);
      const distance = Math.hypot(p[0] - pixel[0], p[1] - pixel[1]) * screenScale;
      if (distance <= best) { best = distance; chosen = point; }
    }
    if (!chosen) return null;
    const position = matrix(forward, chosen.xy);
    const ids = points.filter(point => {
      const p = matrix(forward, point.xy);
      return Math.hypot(p[0] - position[0], p[1] - position[1]) < 1e-7;
    }).map(point => point.id);
    return {xy: chosen.xy.slice(), ids};
  }
  function locate(pixel, scene, points, screenScale, snap, start, shift) {
    const target = snap ? nearest(pixel, points, scene.data_to_pixel, screenScale) : null;
    const xy = target ? target.xy.slice() : matrix(scene.pixel_to_data, pixel);
    if (!target && start && shift) {
      if (Math.abs(xy[0] - start[0]) >= Math.abs(xy[1] - start[1])) xy[1] = start[1];
      else xy[0] = start[0];
    }
    return {xy, target};
  }
  const api = {matrix, nearest, locate};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else globalThis.MathPaletteGeometryInput = api;
})();
