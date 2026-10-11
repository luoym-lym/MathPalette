"use strict";
const assert = require("node:assert/strict");
const {matrix, nearestPoints} = require("./web/board-geometry.js");
const transform = [[20, 0, 300], [0, -20, 400], [0, 0, 1]];
const exact = [Math.sqrt(2), -Math.PI];
const points = [{id: "A", xy: exact}, {id: "B", xy: exact.slice()}, {id: "new_point", xy: [-3.456789123456, 1]}];
const pixel = matrix(transform, exact);
for (const size of [384, 768, 1152]) {
  const near = [pixel[0] + 5 * 768 / size, pixel[1]];
  const result = nearestPoints(points, transform, near, size, size);
  assert.deepEqual(result.map(p => p.id), ["A", "B"], "coincident projected points keep both identities");
  assert.strictEqual(result[0].xy, exact, "snap returns original full precision coordinates");
  assert.deepEqual(nearestPoints(points, transform, [pixel[0] + 20 * 768 / size, pixel[1]], size, size), []);
}
assert.equal(nearestPoints(points, transform, matrix(transform, points[2].xy), 768, 768)[0].id, "new_point");
assert.deepEqual(nearestPoints([], transform, [100, 100], 768, 768), [], "no synthetic grid/midpoint/intersection");
assert.deepEqual(matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], exact), exact);
console.log("Solid drawing geometry: zoom, exact coordinates, duplicate identities, new points and free positions passed.");
