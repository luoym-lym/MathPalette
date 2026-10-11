"use strict";
const assert = require("node:assert/strict");
const {locate, matrix} = require("./web/geometry-input.js");
const scene = {data_to_pixel: [[20, 0, 100], [0, -20, 700], [0, 0, 1]],
  pixel_to_data: [[.05, 0, -5], [0, -.05, 35], [0, 0, 1]]};
const exact = [Math.sqrt(2), Math.PI];
const points = [{id: "A", xy: exact}, {id: "coincident_A", xy: exact.slice()},
  {id: "board_point_1", xy: [4.125, 3.3333333333333335]}];
for (const scale of [.25, .5, 1, 2]) {
  const pixel = matrix(scene.data_to_pixel, exact);
  const result = locate([pixel[0] + 4 / scale, pixel[1]], scene, points, scale, true, [0, 0], true);
  assert.deepEqual(result.xy, exact, "snap must keep all coordinate precision and override Shift");
  assert.deepEqual(result.target.ids, ["A", "coincident_A"]);
}
const freePixel = [500.1, 400.2];
const free = locate(freePixel, scene, points, 1, true, null, false);
assert.equal(free.target, null, "no distant point jumps");
assert.deepEqual(free.xy, matrix(scene.pixel_to_data, freePixel));
const pixel = matrix(scene.data_to_pixel, exact);
assert.equal(locate(pixel, scene, points, 1, false, null, false).target, null, "Ctrl release allows free positioning");
assert.deepEqual(locate(matrix(scene.data_to_pixel, points[2].xy), scene, points, 1, true, null, false).xy, points[2].xy);
const shift = locate(freePixel, scene, points, 1, false, [0, 0], true);
assert.equal(shift.xy[1], 0);
console.log("Geometry input: exact original/new points, coincident identities, four scales, free placement, Shift passed.");
