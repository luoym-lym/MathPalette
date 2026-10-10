"use strict";

let state = null;
let busy = false;
let imageReadyCandidateId = null;
const $ = (id) => document.getElementById(id);
const statusNames = {available: "可用", unavailable: "不可用", exhausted: "已耗尽", skipped: "已跳过"};

function element(tag, className, text) {
  const item = document.createElement(tag);
  if (className) item.className = className;
  if (text !== undefined) item.textContent = text;
  return item;
}

function setBusy(value, message = "正在生成或保存，请稍候…") {
  busy = value;
  document.querySelectorAll("[data-mutates]").forEach((button) => { button.disabled = value; });
  $("skip-reason").disabled = value;
  $("busy-message").textContent = value ? message : "";
  $("candidate-frame").setAttribute("aria-busy", String(value));
  if (!value) updateButtons();
}

function updateButtons() {
  const hasCandidate = Boolean(state?.candidate) && !state?.recovery_required;
  const visibleCandidate = hasCandidate && imageReadyCandidateId === state.candidate.candidate_id;
  $("pass").disabled = busy || !visibleCandidate;
  $("reject").disabled = busy || !visibleCandidate;
  $("skip").disabled = busy || state?.recovery_required || (!hasCandidate && !state?.error);
  $("zoom-candidate").disabled = !visibleCandidate;
  if (state) {
    const index = state.questions.findIndex((q) => q.id === state.current_question);
    $("previous").disabled = busy || index === 0;
    $("next").disabled = busy || index === state.questions.length - 1;
  }
}

function notice(message) {
  $("notice").textContent = message || "";
  $("notice").classList.toggle("hidden", !message);
}

async function request(path, payload) {
  const options = payload === undefined ? {} : {
    method: "POST", headers: {"Content-Type": "application/json", "X-Workbench-Token": state?.api_token || ""},
    body: JSON.stringify(payload),
  };
  const response = await fetch(path, {...options, cache: "no-store"});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `服务返回 ${response.status}`);
  return data;
}

async function action(path, payload, message) {
  if (busy) return;
  notice("");
  setBusy(true, message);
  try {
    const next = await request(path, payload);
    render(next);
  } catch (error) {
    // A network error can arrive after the transaction committed. Always read
    // the server's actual state instead of reusing the previous candidate.
    try { render(await request("/api/state")); } catch (_) { /* keep retry visible */ }
    notice(error.message);
    $("retry").classList.remove("hidden");
  } finally {
    setBusy(false);
  }
}

function summarize(candidate) {
  if (!candidate) return state?.plan.phase === "complete" ? "本题 A/B 配额均已完成。" : "当前没有待审核候选。";
  const p = candidate.params;
  const xy = (point) => `(${point.map((v) => Number.isInteger(v) ? v : Number(v.toFixed(4))).join(", ")})`;
  switch (candidate.operation) {
    case "A1": return p.mode === "off" ? "关闭两个方向的全部网格，保留坐标轴、刻度短线和数字。" : `网格间隔改为 2，位置 ${p.grid_positions.join(", ")}；刻度保持不变。`;
    case "A2": return "隐藏两轴全部刻度数字及独立原点 0；保留刻度短线、网格和数学文字。";
    case "A3": return `${{ellipse: "椭圆", rectangle: "矩形", triangle: "三角形"}[p.shape]} · 中心 ${xy(p.center)} · 宽 ${p.width.toFixed(3)} / 高 ${p.height.toFixed(3)} · 旋转 ${p.angle_deg.toFixed(2)}° · 无填充`;
    case "A4": return `画布、绘图区与刻度数字遮罩统一改为 ${p.background_color}，输出不透明。`;
    case "B1": case "B5": return `新增 ${p.points.length} 个点：` + p.points.map((point) => `${xy(point.xy)} ${point.filled ? "实心" : "空心"}${point.curve_id ? ` · ${point.curve_id}` : ""}`).join("；");
    case "B2": return `${{horizontal: "水平线", vertical: "竖直线", oblique: "斜线"}[p.orientation]} · ${xy(p.endpoints[0])} → ${xy(p.endpoints[1])} · ${p.linestyle === "solid" ? "实线" : "虚线"}`;
    case "B3": return `原有点 ${p.source.id} ${xy(p.source.xy)} → 原点 (0, 0) · 虚线`;
    case "B4": return `${p.source.kind === "original_point" ? "原有点" : "已验证曲线整数点"} ${xy(p.source.xy)} → ${p.projection_axis} 轴 ${xy(p.endpoints[1])} · 虚线`;
    default: return JSON.stringify(p);
  }
}

function renderQuestions() {
  const filter = $("question-filter").value;
  $("question-list").replaceChildren();
  state.questions.filter((q) => filter === "all" || (filter === "pending" && !q.complete) || (filter === "blocked" && q.blocked) || (filter === "complete" && q.complete)).forEach((q) => {
    const button = element("button", `question-button ${q.complete ? "complete" : q.blocked ? "blocked" : ""} ${q.id === state.current_question ? "active" : ""}`, q.id.slice(3));
    button.type = "button";
    button.setAttribute("aria-label", `${q.id}，A ${q.counts.A}/5，B ${q.counts.B}/5${q.blocked ? "，待处理" : ""}`);
    button.setAttribute("aria-current", q.id === state.current_question ? "true" : "false");
    button.title = `${q.id} · A ${q.counts.A}/5 · B ${q.counts.B}/5`;
    button.dataset.mutates = "";
    button.disabled = busy;
    button.addEventListener("click", () => action("/api/navigate", {question_id: q.id}, "正在恢复此题的候选…"));
    $("question-list").append(button);
  });
}

function zoom(title, url, recipe = null) {
  $("dialog-title").textContent = title;
  $("dialog-image").src = url;
  $("dialog-params").classList.toggle("hidden", !recipe);
  $("dialog-params").textContent = recipe ? JSON.stringify(recipe, null, 2) : "";
  $("image-dialog").showModal();
}

function showCandidate(candidate) {
  const image = $("candidate-image");
  if (!candidate) {
    imageReadyCandidateId = null;
    delete image.dataset.candidateId;
    image.removeAttribute("src");
    image.classList.add("hidden");
    $("candidate-empty").classList.remove("hidden");
    return;
  }
  if (image.dataset.candidateId === candidate.candidate_id && imageReadyCandidateId === candidate.candidate_id) return;
  imageReadyCandidateId = null;
  image.classList.add("hidden");
  $("candidate-empty").classList.remove("hidden");
  $("candidate-empty").replaceChildren(element("span", "empty-symbol", "◇"), element("p", "", "正在载入冻结候选图片…"));
  image.dataset.candidateId = candidate.candidate_id;
  image.onload = () => {
    if (state?.candidate?.candidate_id !== image.dataset.candidateId || !image.complete) return;
    imageReadyCandidateId = state.candidate.candidate_id;
    image.classList.remove("hidden");
    $("candidate-empty").classList.add("hidden");
    updateButtons();
  };
  image.onerror = () => {
    imageReadyCandidateId = null;
    notice("候选图片载入失败，审核按钮已禁用。请点击重试。 ");
    $("retry").classList.remove("hidden");
    updateButtons();
  };
  image.src = candidate.image_url;
}

function render(next) {
  const changedQuestion = state?.current_question !== next.current_question;
  state = next;
  $("question-id").textContent = state.current_question;
  $("question-text").textContent = state.question.question;
  $("answer-text").textContent = typeof state.question.answer === "object" ? JSON.stringify(state.question.answer) : String(state.question.answer);
  if (changedQuestion) { $("answer-details").open = false; $("skip-reason").value = ""; }
  $("original-image").src = state.original_url;
  $("a-count").replaceChildren("A 类 ", element("b", "", `${state.counts.A} / 5`));
  $("b-count").replaceChildren("B 类 ", element("b", "", `${state.counts.B} / 5`));
  const phase = state.candidate?.phase || state.plan.phase;
  $("phase").textContent = phase === "coverage" ? "覆盖类型" : phase === "fill" ? "随机补足" : "本题完成";
  $("phase").classList.toggle("fill", phase === "fill");
  $("next-slot").textContent = state.plan.slot_id ? `下一通过槽位 ${state.plan.slot_id}` : "A = 5 · B = 5";
  $("candidate-operation").textContent = state.current_operation ? `${state.current_operation} · ${state.operation_names[state.current_operation]}` : "无待审核候选";
  const candidate = state.candidate;
  showCandidate(candidate);
  if (!candidate) {
    $("candidate-empty").replaceChildren(element("span", "empty-symbol", state.plan.phase === "complete" ? "✓" : "◇"), element("p", "", state.error || (state.plan.blocked ? `${state.plan.category} 类仍有缺口，所有可用类型均已用尽或跳过。可恢复跳过类型，或导航到其他题。` : "本题 10 个槽位均已通过，可查看图片与重绘参数。")));
  }
  $("parameter-summary").textContent = summarize(candidate);
  $("parameter-json").textContent = candidate ? JSON.stringify(candidate, null, 2) : "没有候选参数";
  $("retry").classList.toggle("hidden", !state.error);
  notice(state.error);
  $("global-passed").replaceChildren(String(state.global.accepted), element("span", "", "/ 800"));
  $("global-completed").replaceChildren(String(state.global.completed_questions), element("span", "", "/ 80"));
  $("global-pending").textContent = state.global.pending_slots;
  $("slots-total").textContent = `${state.counts.A + state.counts.B} / 10`;
  $("slots").replaceChildren();
  for (const category of ["A", "B"]) {
    for (let index = 1; index <= 5; index++) {
      const slot = `${category}${String(index).padStart(2, "0")}`;
      const recipe = state.accepted.find((r) => r.slot_id === slot);
      const box = element("button", `slot ${recipe ? "passed" : ""} ${slot === state.plan.slot_id ? "next" : ""}`);
      box.type = "button";
      box.disabled = !recipe;
      box.setAttribute("aria-label", recipe ? `查看 ${slot}，${recipe.operation} 通过图与参数` : `${slot} 待审核`);
      if (recipe) {
        const thumb = element("img"); thumb.src = recipe.image_url; thumb.alt = `${slot} 通过图`; thumb.loading = "lazy";
        box.append(thumb, element("strong", "", slot), element("small", "", recipe.operation));
        box.addEventListener("click", () => zoom(`${state.current_question} / ${slot} · ${recipe.operation}`, recipe.image_url, recipe));
      } else box.append(element("span", "slot-placeholder", "·"), element("strong", "", slot), element("small", "", slot === state.plan.slot_id ? "下一槽位" : "待审核"));
      $("slots").append(box);
    }
  }
  $("operations").replaceChildren();
  $("global-coverage").replaceChildren();
  for (const [operation, info] of Object.entries(state.operations)) {
    const row = element("div", "operation-row");
    const label = element("div", "operation-name"); label.append(element("b", "", operation), element("span", "", state.operation_names[operation]));
    const status = element("span", `operation-status ${info.status}`, info.covered ? `已覆盖 · ${statusNames[info.status]}` : statusNames[info.status]);
    row.append(label, status);
    if (info.reason) { const reason = element("p", "operation-reason", info.reason); row.append(reason); }
    if (info.status === "skipped") {
      const restore = element("button", "restore-button", "恢复尝试"); restore.type = "button"; restore.dataset.mutates = ""; restore.disabled = busy;
      restore.addEventListener("click", () => action("/api/retry", {operation}, "正在恢复此类型…")); row.append(restore);
    }
    $("operations").append(row);
    const metric = element("div"); metric.append(element("span", "", operation), element("b", "", state.global.coverage[operation])); $("global-coverage").append(metric);
  }
  $("point-count").textContent = `原有点 ${state.precheck.original_point_count}`;
  $("geometry-note").textContent = state.precheck.unsupported_geometry.join("；");
  $("shortage-title").textContent = `尚未补足的大类 (${state.global.shortages.length})`;
  $("shortages").replaceChildren();
  for (const shortage of state.global.shortages) {
    const button = element("button", `shortage ${shortage.blocked ? "blocked" : ""}`, `${shortage.question_id} / ${shortage.category} · 缺 ${shortage.missing}${shortage.blocked ? " · 待处理" : ""}`);
    button.type = "button"; button.dataset.mutates = ""; button.disabled = busy;
    button.addEventListener("click", () => action("/api/navigate", {question_id: shortage.question_id}, "正在载入题目…")); $("shortages").append(button);
  }
  renderQuestions();
  updateButtons();
}

$("question-filter").addEventListener("change", () => { if (state) renderQuestions(); });
$("previous").addEventListener("click", () => { const i = state.questions.findIndex((q) => q.id === state.current_question); if (i > 0) action("/api/navigate", {question_id: state.questions[i - 1].id}, "正在恢复上一题…"); });
$("next").addEventListener("click", () => { const i = state.questions.findIndex((q) => q.id === state.current_question); if (i < 79) action("/api/navigate", {question_id: state.questions[i + 1].id}, "正在恢复下一题…"); });
$("pass").addEventListener("click", () => { if (state.candidate) action("/api/review", {candidate_id: state.candidate.candidate_id, decision: "pass"}, "正在保存展示的候选与冻结参数…"); });
$("reject").addEventListener("click", () => { if (state.candidate) action("/api/review", {candidate_id: state.candidate.candidate_id, decision: "reject"}, "正在删除候选并构造新图…"); });
$("skip").addEventListener("click", () => action("/api/skip", {candidate_id: state.candidate?.candidate_id, operation: state.current_operation, reason: $("skip-reason").value}, "正在记录跳过并继续同组审核…"));
$("retry").addEventListener("click", async () => {
  if (!state) { try { setBusy(true); render(await request("/api/state")); notice(""); } catch (e) { notice(e.message); } finally { setBusy(false); } }
  else action("/api/retry", {}, "正在恢复事务或重试生成…");
});
$("zoom-original").addEventListener("click", () => { if (state) zoom(`${state.current_question} · 原图 · 768 × 768`, state.original_url); });
$("zoom-candidate").addEventListener("click", () => { if (state?.candidate) zoom(`${state.current_question} · ${state.candidate.operation} 候选 · 768 × 768`, state.candidate.image_url, state.candidate); });
$("close-dialog").addEventListener("click", () => $("image-dialog").close());
$("image-dialog").addEventListener("click", (event) => { if (event.target === $("image-dialog")) $("image-dialog").close(); });

(async () => {
  setBusy(true, "正在恢复上次审核位置…");
  try { render(await request("/api/state")); }
  catch (error) { notice(`载入失败：${error.message}`); $("retry").classList.remove("hidden"); }
  finally { setBusy(false); }
})();
