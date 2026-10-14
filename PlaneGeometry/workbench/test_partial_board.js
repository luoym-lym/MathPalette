"use strict";
// Exercise the real controller's pointer and form events with a minimal DOM.
// No browser, server, review records or formal outputs are modified by this test.
const fs = require("node:fs"), vm = require("node:vm"), assert = require("node:assert/strict"), path = require("node:path");
const web = path.join(__dirname, "web"), html = fs.readFileSync(path.join(web, "index.html"), "utf8");
class Element {
  constructor(attrs = "") {
    this.events = {}; this.children = []; this.dataset = {}; this.value = ""; this.disabled = false;
    this.clientWidth = this.clientHeight = this.width = this.height = 768; this.clientLeft = this.clientTop = 0;
    for (const [, key, value] of attrs.matchAll(/([\w-]+)="([^"]*)"/g)) {
      if (key.startsWith("data-")) this.dataset[key.slice(5).replace(/-([a-z])/g, (_, c) => c.toUpperCase())] = value;
      else this[key] = value;
    }
  }
  addEventListener(name, callback) { (this.events[name] ||= []).push(callback); }
  async fire(name, event = {}) { for (const cb of this.events[name] || []) await cb({target: this, preventDefault() {}, ...event}); }
  setAttribute(key, value) { this[key] = value; }
  replaceChildren(...children) { this.children = children; }
  get options() { return this.children; }
  append(...children) { this.children.push(...children); }
  getContext() { return new Proxy({}, {get: (o, p) => o[p] || (() => {}), set: (o, p, v) => (o[p] = v, true)}); }
  getBoundingClientRect() { return {left: 0, top: 0}; }
  focus() {} setPointerCapture() {} hasPointerCapture() { return false; }
  showModal() { this.open = true; } close() { this.open = false; }
}
const all = [...html.matchAll(/<\w+\b([^>]*)>/g)].map(m => new Element(m[1]));
const $ = id => { const found = all.find(e => e.id === id); assert.ok(found, `missing HTML control: ${id}`); return found; };
const selector = s => all.filter(e => {
  const attr = /^\[data-([\w-]+)\]$/.exec(s);
  return attr && attr[1].replace(/-([a-z])/g, (_, c) => c.toUpperCase()) in e.dataset;
});
const storage = new Map(), timers = new Map(); let timer = 0;
const geometry = {width:768,height:768,plot_bounds:[20,20,748,748],
  data_to_pixel:[[1,0,0],[0,1,0],[0,0,1]], pixel_to_data:[[1,0,0],[0,1,0],[0,0,1]],
  xlim:[0,768],ylim:[0,768],snap_points:[],presets:{point:{type:"add_point"},line:{type:"add_line"}},
  targets:[{id:"line",kind:"polyline",paths:[[[100,100],[600,100],[600,600],[100,600],[100,100]]],color:"#000000",linestyle:"solid",linewidth_pt:1,
    partial_paths:[{id:"p0",sha256:"a".repeat(64),closed:true,samples:[[100,100,0],[600,100,.25],[600,600,.5],[100,600,.75],[100,100,1]]}]}]};
const sandbox = {console, $, Math, JSON, setTimeout(cb) { timers.set(++timer,cb); return timer; }, clearTimeout(id) { timers.delete(id); },
  document:{querySelectorAll:selector,createElement:() => new Element(),createTextNode:text => ({textContent:text})},
  window:new Element(), localStorage:{setItem:(k,v) => storage.set(k,v),getItem:k => storage.get(k),removeItem:k => storage.delete(k)},
  Image:class {constructor() {this.naturalWidth=this.naturalHeight=768;} async decode() {}},
  Option:class extends Element {constructor(text,value) {super();this.textContent=text;this.value=value;}},
  state:{question_id:"Fixture01",question:"TEMPORARY SOFTWARE TEST FIXTURE",answer:"test",objects:[{id:"line"}],input_revision:"test",context_token:"test",original_image_url:"test.png"},
  actionSummary:a => a.type, controls() {}, render() {}, busy:false, epoch:0, actionError:"",
  async api(url,body) {
    if (url.startsWith("/api/drawing-scene/")) return geometry;
    if (url==="/api/drawing-preview") return {plugin:body.plugin,image_url:"preview.png",pixel_sha256:"test",parameter_key:"test"};
    throw new Error("Unexpected endpoint: " + url);
  }};
const context = vm.createContext(sandbox);
for (const file of [fs.existsSync(path.join(web,"geometry-input.js")) ? "geometry-input.js" : "board-geometry.js", "partial-selection.js", "drawing-board.js"]) vm.runInContext(fs.readFileSync(path.join(web,file),"utf8"),context,{filename:file});
const button = (dataset,value) => all.find(e => e.dataset[dataset] === value);
const click = async (x,y) => {
  await $("board-canvas").fire("pointerdown",{button:0,clientX:x,clientY:y,pointerId:1});
  await $("board-canvas").fire("pointerup",{button:0,clientX:x,clientY:y,pointerId:1});
};
const plugin = () => JSON.parse([...storage.values()][0]).plugin;
const change = async (id,value) => { $(id).value=value; await $(id).fire("change"); };
const drag = async (a,b,cancel=false) => {
  await $("board-canvas").fire("pointerdown",{button:0,clientX:a[0],clientY:a[1],pointerId:1});
  await $("board-canvas").fire("pointermove",{clientX:b[0],clientY:b[1],pointerId:1});
  await $("board-canvas").fire(cancel ? "pointercancel" : "pointerup",{button:0,clientX:b[0],clientY:b[1],pointerId:1});
};
(async () => {
  await $("open-board").fire("click");
  await button("boardTool","curve").fire("click");
  await change("board-target","line"); await change("board-style-scope","partial");
  assert.equal(button("boardColor","#DC2626").disabled,true);
  await click(200,100); await click(500,100);
  assert.equal(button("boardColor","#DC2626").disabled,false);
  await button("boardColor","#DC2626").fire("click");
  assert.equal(plugin().params.actions.length,1);
  assert.equal(plugin().params.actions[0].interval.start,.05);
  assert.equal(plugin().params.actions[0].interval.end,.2);
  await drag([200,100],[250,100]);
  assert.equal(plugin().params.actions[0].interval.start,.075);
  await drag([250,100],[500,100]); // Degenerate drag is cancelled.
  assert.equal(plugin().params.actions[0].interval.start,.075);
  await drag([250,100],[350,100],true);
  assert.equal(plugin().params.actions[0].interval.start,.075);
  await $("board-other-range").fire("click"); assert.equal(plugin().params.actions[0].interval.wrap,true);
  await $("board-new-range").fire("click"); await click(600,200); await click(600,500);
  await button("boardColor","#2563EB").fire("click"); await change("board-width","2");
  assert.equal(plugin().params.actions.length,2); assert.equal(plugin().params.actions[1].linewidth_pt,2);
  await $("board-undo").fire("click"); assert.equal(plugin().params.actions[1].linewidth_pt,undefined);
  await $("board-redo").fire("click"); assert.equal(plugin().params.actions[1].linewidth_pt,2);
  const edit = $("board-actions").children[0].children.find(e => e.textContent === "编辑区间");
  await edit.fire("click"); await $("board-restore-curve").fire("click"); assert.equal(plugin().params.actions.length,1);
  await $("close-board").fire("click"); await $("open-board").fire("click"); assert.equal(plugin().params.actions.length,1);
  await button("boardTool","curve").fire("click"); await change("board-target","line"); await change("board-style-scope","whole");
  await $("board-restore-curve").fire("click"); assert.equal(plugin().params.actions.length,0);
  console.log("board controller: selection, drag/cancel, complement, multiple ranges, width, undo/redo, edit/delete, draft restore passed");
})().catch(error => {console.error(error);process.exitCode=1;});
