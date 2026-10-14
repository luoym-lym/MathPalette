"use strict";
// Shared by the two geometry workbenches. Parameters refer to source vector
// segments; pixels are used only for hit-testing, never saved in the plugin.
((root) => {
  const pointAt = (path, u) => {
    const samples = path.samples;
    for (let i = 1; i < samples.length; i++) if (u <= samples[i][2]) {
      const a = samples[i - 1], b = samples[i], t = (u - a[2]) / (b[2] - a[2]);
      return [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]), u];
    }
    return samples.at(-1).slice();
  };
  function project(path, pixel) {
    let best = null;
    for (let i = 1; i < path.samples.length; i++) {
      const a = path.samples[i - 1], b = path.samples[i];
      const dx = b[0] - a[0], dy = b[1] - a[1], d2 = dx * dx + dy * dy;
      const t = d2 ? Math.max(0, Math.min(1, ((pixel[0] - a[0]) * dx + (pixel[1] - a[1]) * dy) / d2)) : 0;
      const p = [a[0] + t * dx, a[1] + t * dy];
      const distance = Math.hypot(pixel[0] - p[0], pixel[1] - p[1]);
      if (!best || distance < best.distance) best = {path_id: path.id, u: a[2] + t * (b[2] - a[2]), pixel: p, distance};
    }
    return best;
  }
  function nearest(paths, pixel, threshold, lockedPath = null, snapPoints = []) {
    let best = null;
    for (const path of paths) {
      if (lockedPath !== null && path.id !== lockedPath) continue;
      const hit = project(path, pixel);
      if (hit && hit.distance <= threshold && (!best || hit.distance < best.distance)) best = hit;
    }
    if (!best) return null;
    const path = paths.find(p => p.id === best.path_id);
    // Only snap to points actually on this path, including its two endpoints.
    const candidates = [...snapPoints.map(p => ({pixel: p.pixel, id: p.id})),
      {pixel: path.samples[0], id: "路径起点"}, {pixel: path.samples.at(-1), id: "路径终点"}];
    let snapDistance = threshold;
    for (const point of candidates) {
      const d = Math.hypot(point.pixel[0] - pixel[0], point.pixel[1] - pixel[1]);
      if (d > snapDistance) continue;
      const hit = project(path, point.pixel);
      if (hit && hit.distance < 0.15) { best = {...hit, snap: point.id}; snapDistance = d; }
    }
    return best;
  }
  function interval(path, points, wrap = false) {
    if (points.length !== 2 || points.some(p => p.path_id !== path.id)) return null;
    const start = Math.min(points[0].u, points[1].u), end = Math.max(points[0].u, points[1].u);
    if (end - start < 1e-9 || wrap && (!path.closed || end - start >= 1)) return null;
    return {path_id: path.id, path_sha256: path.sha256, start, end, wrap};
  }
  function traces(path, range) {
    const ranges = range.wrap ? [[0, range.start], [range.end, 1]] : [[range.start, range.end]];
    return ranges.filter(([a, b]) => b > a).map(([a, b]) => [pointAt(path, a),
      ...path.samples.filter(p => p[2] > a && p[2] < b), pointAt(path, b)]);
  }
  const api = {pointAt, nearest, interval, traces};
  if (typeof module !== "undefined") module.exports = api;
  root.MathPalettePartialSelection = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
