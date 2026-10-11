"use strict";
// Editing produces the existing declarative C plugin. Canvas is only an input
// surface; the authoritative preview and every saved PNG come from Matplotlib.
(() => {
  const dialog = $("board-dialog"), canvas = $("board-canvas"), ctx = canvas.getContext("2d");
  const clone = value => JSON.parse(JSON.stringify(value));
  let scene = null, base = null, plugin = null, original = null, picture = null;
  let tool = "point", selected = "", hovered = "", cursor = null, rawCursor = null, start = null;
  let undo = [], redo = [], revision = 0, preview = null, timer = null, rendering = false;
  let saving = false, conflict = false, opening = 0, ctrl = false, shift = false;
  let changed = false, storageWarning = false, snapped = [];
  let pointColor = "#DC2626", lineColor = "#2563EB";
  const open = () => dialog.open;
  const key = qid => `mathpalette-solid-c-board-v1:${qid}`;
  const blank = qid => ({plugin_schema_version: "1.0.0", question_id: qid, category: "C",
    operation: "C_manual", description: "", intent: "", params: {actions: []}});
  const fromState = current => current.candidate ? {...blank(current.question_id),
    description: current.candidate.description, intent: current.candidate.intent,
    params: clone(current.candidate.params)} : blank(current.question_id);

  function message(text, error = false) {
    $("board-message").textContent = text;
    $("board-message").dataset.error = String(error);
  }
  function persist() {
    if (!plugin || !base) return;
    try { localStorage.setItem(key(base.question_id), JSON.stringify({plugin, input_revision: base.input_revision, candidate_id: base.candidate?.candidate_id || null})); }
    catch { storageWarning = true; }
  }
  function forget() {
    try { localStorage.removeItem(key(base.question_id)); } catch { /* Optional browser cache. */ }
  }
  function controlsBoard() {
    const editable = !!scene && !saving && !conflict;
    const ready = editable && !!preview && preview.revision === revision && !start && !rendering;
    $("board-pass").disabled = $("board-submit").disabled = !ready;
    $("close-board").disabled = saving;
    $("board-reload").disabled = saving;
    $("board-undo").disabled = !editable || !undo.length;
    $("board-redo").disabled = !editable || !redo.length;
    $("board-clear").disabled = !editable || !plugin?.params.actions.length;
    $("board-description").disabled = !editable;
    $("board-target").disabled = !editable;
    document.querySelectorAll("[data-board-tool]").forEach(b => { b.disabled = !editable; b.setAttribute("aria-pressed", String(b.dataset.boardTool === tool)); });
    const style = currentStyle(selected);
    document.querySelectorAll("[data-board-color]").forEach(b => {
      b.disabled = !editable || !selected;
      b.setAttribute("aria-pressed", String(b.dataset.boardColor === style?.color));
    });
    document.querySelectorAll("[data-board-add-color]").forEach(b => {
      b.disabled = !editable;
      b.setAttribute("aria-pressed", String(b.dataset.boardAddColor === (tool === "point" ? pointColor : lineColor)));
    });
    for (const id of ["board-point-start", "board-point-end", "board-connect-points"]) $(id).disabled = !editable;
    for (const name of ["dashed", "solid"]) {
      $("board-" + name).disabled = !editable || !selected;
      $("board-" + name).setAttribute("aria-pressed", String(style?.linestyle === name));
    }
    $("board-restore-curve").disabled = !editable || !selected;
    $("board-conflict").hidden = !conflict;
    $("board-save-hint").textContent = saving ? "正在保存图片与插件参数…" : storageWarning ?
      "浏览器草稿缓存不可用；返回前请提交候选。" : "草稿在本浏览器暂存；Pass 才收集。青色选中轮廓与指针不保存。";
  }
  function currentStyle(id) {
    if (!id || !scene) return null;
    const target = scene.targets.find(t => t.id === id);
    if (!target) return null;
    let style = {color: target.color, linestyle: target.linestyle, linewidth_pt: target.linewidth_pt};
    for (const a of plugin.params.actions) if (a.type === "set_object_style" && a.target === id) style = {...style, ...a};
    return style;
  }
  function actionsList() {
    $("board-action-count").textContent = plugin.params.actions.length;
    $("board-actions").replaceChildren(...plugin.params.actions.map((action, index) => {
      const li = document.createElement("li"), remove = document.createElement("button");
      li.append(document.createTextNode(actionSummary(action)));
      remove.textContent = "删除"; remove.disabled = saving || conflict;
      remove.setAttribute("aria-label", `删除第 ${index + 1} 个标记`);
      remove.addEventListener("click", () => edit(() => plugin.params.actions.splice(index, 1)));
      li.append(remove); return li;
    }));
  }
  function edit(change) {
    if (!scene || saving || conflict) return;
    const before = clone(plugin);
    change();
    if (JSON.stringify(before) === JSON.stringify(plugin)) return;
    undo.push(before); redo = []; changed = true;
    updated();
  }
  function updated() {
    revision++; preview = null;
    $("board-description").value = plugin.description;
    actionsList(); refreshPointChoices(); persist(); controlsBoard(); draw();
    clearTimeout(timer);
    if (!plugin.params.actions.length) {
      picture = original; draw(); message("在图中添加点、线或选择曲线修改样式。");
    } else {
      message("正在生成最新预览…");
      timer = setTimeout(renderPreview, 200);
    }
  }
  function history(direction) {
    if (saving || conflict) return;
    const source = direction === "undo" ? undo : redo, destination = direction === "undo" ? redo : undo;
    if (!source.length) return;
    destination.push(clone(plugin)); plugin = source.pop(); start = null; changed = true; updated();
  }
  async function renderPreview() {
    if (!open() || !scene || rendering || saving || conflict || !plugin.params.actions.length) return;
    rendering = true; const at = revision, session = opening;
    controlsBoard();
    try {
      const result = await api("/api/drawing-preview", {plugin: clone(plugin), context_token: base.context_token, replace: base.candidate?.candidate_id || null});
      const img = new Image(); img.src = result.image_url; await img.decode();
      if (!open() || at !== revision || session !== opening || conflict) return;
      if (img.naturalWidth !== 768 || img.naturalHeight !== 768) throw new Error("预览尺寸无效。");
      picture = img; preview = {...result, revision: at};
      message("预览已更新，可以继续标注或点击 Pass 收集。"); draw();
    } catch (error) {
      if (open() && at === revision && session === opening) {
        if (["stale_context", "stale_candidate", "pending_candidate", "invalid_session"].includes(error.code)) conflict = true;
        message(error.message, true);
      }
    } finally {
      rendering = false; controlsBoard();
      if (open() && (at !== revision || session !== opening)) renderPreview();
    }
  }
  const matrix = SolidBoardGeometry.matrix;
  function pointPool() {
    return [...scene.snap_points, ...plugin.params.actions.filter(a => a.type === "add_point")
      .map(a => ({id: a.id, label: a.id, xy: a.xy, source: "annotation"}))];
  }
  function refreshPointChoices() {
    if (!scene) return;
    const points = pointPool();
    for (const id of ["board-point-start", "board-point-end"]) {
      const select = $(id), previous = select.value;
      select.replaceChildren(new Option("选择几何点", ""), ...points.map(p =>
        new Option(`${p.label} [${p.id}]${p.source === "annotation" ? " · 新增" : ""}`, `${p.source}:${p.id}`)));
      if ([...select.options].some(o => o.value === previous)) select.value = previous;
    }
  }
  function nearestPoints(pixel, threshold) {
    const rect = canvas.getBoundingClientRect();
    return SolidBoardGeometry.nearestPoints(pointPool(), scene.data_to_pixel, pixel,
      rect.width, rect.height, threshold);
  }
  function dataPoint(pixel) {
    let p = matrix(scene.pixel_to_data, pixel);
    snapped = ctrl || $("board-snap").checked ? nearestPoints(pixel, 12) : [];
    if (snapped.length) return snapped[0].xy.slice();
    if (tool === "line" && start && shift) {
      if (Math.abs(p[0] - start[0]) >= Math.abs(p[1] - start[1])) p[1] = start[1]; else p[0] = start[0];
    }
    return p;
  }
  function inside(pixel) {
    const [l, t, r, b] = scene.plot_bounds;
    return pixel[0] >= l && pixel[0] <= r && pixel[1] >= t && pixel[1] <= b;
  }
  function distance(p, a, b) {
    const dx = b[0] - a[0], dy = b[1] - a[1], length = dx * dx + dy * dy;
    const u = length ? Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / length)) : 0;
    return Math.hypot(p[0] - a[0] - u * dx, p[1] - a[1] - u * dy);
  }
  function hit(pixel) {
    const threshold = 8 * canvas.width / canvas.clientWidth;
    let best = threshold, id = "";
    for (const target of scene.targets) for (const path of target.paths) for (let i = 1; i < path.length; i++) {
      const d = distance(pixel, path[i - 1], path[i]);
      if (d < best) { best = d; id = target.id; }
    }
    return id;
  }
  function trace(id) {
    const target = scene.targets.find(t => t.id === id);
    if (!target) return;
    ctx.beginPath();
    for (const path of target.paths) path.forEach((p, i) => i ? ctx.lineTo(...p) : ctx.moveTo(...p));
    ctx.strokeStyle = "#06B6D4"; ctx.lineWidth = 4; ctx.globalAlpha = 0.45; ctx.stroke(); ctx.globalAlpha = 1;
  }
  function draw() {
    ctx.clearRect(0, 0, 768, 768);
    if (picture) ctx.drawImage(picture, 0, 0, 768, 768);
    if (!scene) return;
    ctx.save(); const [l, t, r, b] = scene.plot_bounds;
    ctx.beginPath(); ctx.rect(l, t, r - l, b - t); ctx.clip();
    if (tool === "curve") { trace(selected); if (hovered !== selected) trace(hovered); }
    if (start) {
      const a = matrix(scene.data_to_pixel, start);
      ctx.fillStyle = "#2563EB"; ctx.beginPath(); ctx.arc(...a, 4, 0, Math.PI * 2); ctx.fill();
      if (cursor) {
        ctx.beginPath(); ctx.moveTo(...a); ctx.lineTo(...matrix(scene.data_to_pixel, cursor));
        ctx.strokeStyle = "#2563EB"; ctx.lineWidth = 100 / 72; ctx.setLineDash([3.7 * 100 / 72, 1.6 * 100 / 72]); ctx.stroke(); ctx.setLineDash([]);
      }
    }
    if (cursor && tool !== "curve") {
      const [x, y] = matrix(scene.data_to_pixel, cursor);
      ctx.strokeStyle = snapped.length ? "#059669" : "#64748B"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(x - 9, y); ctx.lineTo(x + 9, y); ctx.moveTo(x, y - 9); ctx.lineTo(x, y + 9); ctx.stroke();
      ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.stroke();
    }
    ctx.restore();
  }
  function updateCursor() {
    if (!scene) return;
    cursor = rawCursor && inside(rawCursor) ? dataPoint(rawCursor) : null;
    hovered = tool === "curve" && cursor ? hit(rawCursor) : "";
    $("board-coordinates").textContent = cursor ? `x ${cursor[0].toFixed(4)} · y ${cursor[1].toFixed(4)}${snapped.length ? " · 吸附 " + snapped.map(p => p.label + " [" + p.id + "]").join(" / ") : ""}` : "移动指针查看坐标";
    $("board-selected").textContent = hovered || selected;
    draw();
  }
  function setTool(value) {
    tool = value; start = null; hovered = "";
    $("board-curve-controls").hidden = tool !== "curve";
    $("board-add-colors").hidden = tool === "curve";
    $("board-point-connect").hidden = tool !== "line";
    $("board-tool-help").textContent = {point: "单击放置实心点；Ctrl 吸附已有顶点、命名点与新增点。", line: "点击两个位置或拖动；Ctrl 精确吸附，Shift 仅约束画面水平 / 竖直。也可选择下方两个点连接。", curve: "选择原棱线或轮廓后改色或切换实虚线；改色保留每个片段的原线型。"}[tool];
    controlsBoard(); updateCursor();
  }
  function selectCurve(id) { selected = id; $("board-target").value = id; controlsBoard(); updateCursor(); }
  function restyle(change) {
    const style = currentStyle(selected);
    if (!style) return;
    const target = selected;
    edit(() => {
      const previous = plugin.params.actions.filter(a => a.type === "set_object_style" && a.target === target)
        .reduce((result, a) => ({...result, ...a}), {});
      plugin.params.actions = plugin.params.actions.filter(a => !(a.type === "set_object_style" && a.target === target));
      plugin.params.actions.push({type: "set_object_style", target, ...previous, ...change});
    });
  }
  function id(prefix) {
    const used = new Set([...base.objects.map(o => o.id), ...plugin.params.actions.map(a => a.id)]);
    let n = 1; while (used.has(`${prefix}_${n}`)) n++;
    return `${prefix}_${n}`;
  }
  function lineTo(end) {
    if (!start || (start[0] === end[0] && start[1] === end[1])) { message("请选择不同的终点。", true); return; }
    const a = start; start = null;
    edit(() => plugin.params.actions.push({...clone(scene.presets.line), color: lineColor, id: id("board_line"), endpoints: [a, end]}));
  }
  let press = null;
  canvas.addEventListener("pointerdown", e => {
    if (!scene || saving || conflict || e.button !== 0) return;
    canvas.focus({preventScroll: true}); pointer(e);
    if (!cursor) return;
    press = {pixel: rawCursor.slice(), first: !start};
    if (tool === "line" && !start) { start = cursor.slice(); controlsBoard(); draw(); }
    canvas.setPointerCapture(e.pointerId);
  });
  function pointer(e) {
    const rect = canvas.getBoundingClientRect();
    rawCursor = [(e.clientX - rect.left - canvas.clientLeft) * 768 / canvas.clientWidth,
      (e.clientY - rect.top - canvas.clientTop) * 768 / canvas.clientHeight];
    ctrl = e.ctrlKey; shift = e.shiftKey; updateCursor();
  }
  canvas.addEventListener("pointermove", pointer);
  canvas.addEventListener("pointerleave", () => { if (!press) { rawCursor = null; updateCursor(); } });
  canvas.addEventListener("pointercancel", () => { press = null; start = null; controlsBoard(); draw(); });
  canvas.addEventListener("pointerup", e => {
    if (!press) return;
    const down = press; press = null; pointer(e);
    if (canvas.hasPointerCapture(e.pointerId)) canvas.releasePointerCapture(e.pointerId);
    if (saving || conflict || !cursor) return;
    if (tool === "point") {
      const xy = cursor.slice(); edit(() => plugin.params.actions.push({...clone(scene.presets.point), color: pointColor, id: id("board_point"), xy}));
    } else if (tool === "curve") selectCurve(hit(rawCursor));
    else if (!down.first || Math.hypot(rawCursor[0] - down.pixel[0], rawCursor[1] - down.pixel[1]) > 5) lineTo(cursor.slice());
    else message("已选起点，点击终点完成辅助线；Esc 取消。");
  });

  async function loadBoard(useDraft = true) {
    const session = ++opening;
    clearTimeout(timer); scene = null; base = clone(state); conflict = false; saving = false;
    plugin = fromState(base); original = picture = preview = null; revision++; changed = false;
    undo = []; redo = []; selected = hovered = ""; cursor = rawCursor = start = null;
    ctrl = shift = false;
    $("board-title").textContent = `${base.question_id} · 手动画板`;
    $("board-question-text").textContent = base.question;
    $("board-answer").textContent = typeof base.answer === "string" ? base.answer : JSON.stringify(base.answer, null, 2);
    $("board-description").value = plugin.description;
    message("正在载入原图与可选曲线…"); controlsBoard(); draw();
    if (!open()) dialog.showModal();
    try {
      const image = new Image(); image.src = base.original_image_url;
      const [geometry] = await Promise.all([api(`/api/drawing-scene/${base.question_id}`), image.decode()]);
      if (!open() || session !== opening) return;
      scene = geometry; original = picture = image;
      const options = [new Option("点击图中的原对象", ""), ...scene.targets.map(t => new Option(t.id, t.id))];
      $("board-target").replaceChildren(...options);
      let restored = false;
      if (useDraft) try {
        const saved = JSON.parse(localStorage.getItem(key(base.question_id)) || "null");
        if (saved?.plugin?.question_id === base.question_id && saved.input_revision === base.input_revision && saved.candidate_id === (base.candidate?.candidate_id || null)) {
          plugin = saved.plugin; restored = true; changed = true;
        }
      } catch { /* Ignore an invalid browser cache; server schema validation is authoritative. */ }
      setTool(tool); updated();
      if (restored) $("board-save-hint").textContent = "已恢复本浏览器暂存草稿。";
    } catch (error) { if (session === opening) { message(error.message, true); controlsBoard(); } }
  }
  async function save(collect) {
    if ($(collect ? "board-pass" : "board-submit").disabled) return;
    const shown = preview; saving = true; busy = true; epoch++; controls(); controlsBoard(); actionsList();
    let submitted = false;
    try {
      const result = await api("/api/drawing-submit", {plugin: shown.plugin, context_token: base.context_token,
        replace: base.candidate?.candidate_id || null, pixel_sha256: shown.pixel_sha256, parameter_key: shown.parameter_key});
      submitted = true;
      if (result.state.candidate?.candidate_id !== result.candidate.candidate_id) throw new Error("候选在提交后发生变化；请返回工作台检查最新候选。");
      if (collect) await api("/api/review", {question_id: base.question_id, candidate_id: result.candidate.candidate_id,
        decision: "pass", context_token: result.state.context_token, pixel_sha256: shown.pixel_sha256, parameter_key: shown.parameter_key, note: ""});
      forget(); dialog.close(); opening++; clearTimeout(timer);
      actionError = ""; render(await api("/api/state"));
    } catch (error) {
      message(error.message + (submitted ? " 候选已生成；返回工作台可继续审核。" : ""), true);
      if (submitted || ["stale_context", "stale_candidate", "pending_candidate", "invalid_session"].includes(error.code)) conflict = true;
      actionError = error.message;
    } finally { saving = false; busy = false; controlsBoard(); controls(); actionsList(); }
  }
  function closeBoard() {
    if (saving) return;
    persist(); clearTimeout(timer); opening++; dialog.close();
  }
  $("open-board").addEventListener("click", () => loadBoard());
  $("close-board").addEventListener("click", closeBoard);
  dialog.addEventListener("cancel", e => { e.preventDefault(); if (start || selected) { start = null; selectCurve(""); controlsBoard(); draw(); } else closeBoard(); });
  $("board-reload").addEventListener("click", () => {
    if (changed && !window.confirm("载入最新候选将替换当前画板草稿，是否继续？")) return;
    forget(); loadBoard(false);
  });
  document.querySelectorAll("[data-board-tool]").forEach(b => b.addEventListener("click", () => setTool(b.dataset.boardTool)));
  document.querySelectorAll("[data-board-color]").forEach(b => b.addEventListener("click", () => restyle({color: b.dataset.boardColor})));
  document.querySelectorAll("[data-board-add-color]").forEach(b => b.addEventListener("click", () => {
    if (tool === "point") pointColor = b.dataset.boardAddColor; else lineColor = b.dataset.boardAddColor;
    controlsBoard();
  }));
  $("board-connect-points").addEventListener("click", () => {
    const points = pointPool(), resolve = value => points.find(p => `${p.source}:${p.id}` === value);
    const a = resolve($("board-point-start").value), b = resolve($("board-point-end").value);
    if (!a || !b) { message("请选择起点和终点。", true); return; }
    start = a.xy.slice(); lineTo(b.xy.slice());
  });
  $("board-dashed").addEventListener("click", () => restyle({linestyle: "dashed"}));
  $("board-solid").addEventListener("click", () => restyle({linestyle: "solid"}));
  $("board-target").addEventListener("change", e => selectCurve(e.target.value));
  $("board-restore-curve").addEventListener("click", () => edit(() => { plugin.params.actions = plugin.params.actions.filter(a => !(a.type === "set_object_style" && a.target === selected)); }));
  $("board-undo").addEventListener("click", () => history("undo"));
  $("board-redo").addEventListener("click", () => history("redo"));
  $("board-clear").addEventListener("click", () => { start = null; edit(() => { plugin.params.actions = []; }); });
  $("board-snap").addEventListener("change", updateCursor);
  $("board-description").addEventListener("change", e => edit(() => { plugin.description = e.target.value; }));
  $("board-pass").addEventListener("click", () => save(true));
  $("board-submit").addEventListener("click", () => save(false));
  window.addEventListener("keydown", e => {
    if (!open()) return;
    ctrl = e.ctrlKey; shift = e.shiftKey; updateCursor();
    if (e.target.matches("input, textarea, select")) return;
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "z") { e.preventDefault(); history(e.shiftKey ? "redo" : "undo"); }
    else if (!e.ctrlKey && !e.metaKey && ["1", "2", "3"].includes(e.key)) setTool({1: "point", 2: "line", 3: "curve"}[e.key]);
  });
  window.addEventListener("keyup", e => { if (open()) { ctrl = e.ctrlKey; shift = e.shiftKey; updateCursor(); } });
  window.addEventListener("blur", () => { ctrl = shift = false; if (open()) { persist(); updateCursor(); } });
  window.addEventListener("beforeunload", () => { if (open()) persist(); });
  window.drawingBoard = {onState(next) {
    if (!open() || saving || !base) return;
    if (next.context_token !== base.context_token) { conflict = true; clearTimeout(timer); controlsBoard(); actionsList(); }
  }};
})();
