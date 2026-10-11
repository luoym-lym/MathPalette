"use strict";
const $ = id => document.getElementById(id);
let state = null, connected = false, busy = false, polling = false, epoch = 0;
let displayKey = "", navKey = "", loaded = null, originalLoaded = false, actionError = "";
const statusNames = {waiting: "等待提交", generating: "生成中", pending: "待审核", error: "操作失败", completed: "全部完成"};

async function api(path, body) {
  const response = await fetch(path, body === undefined ? {cache: "no-store"} : {
    method: "POST", headers: {"Content-Type": "application/json", "X-Review-Token": state?.review_token || ""}, body: JSON.stringify(body)
  });
  const value = await response.json();
  if (!response.ok) { const error = new Error(value.error || `HTTP ${response.status}`); error.code = value.code; throw error; }
  return value;
}

function controls() {
  const hasQuestion = !!state?.question_id;
  $("open-board").disabled = !hasQuestion || !connected || busy || !originalLoaded;
  $("collect-question").disabled = !hasQuestion || !connected || busy || !state.accepted.length || !!state.candidate || state.status === "generating" || $("board-dialog").open;
  const ready = connected && !busy && state?.candidate?.status === "pending" && originalLoaded &&
    loaded?.id === state.candidate.candidate_id && loaded?.pixel === state.candidate.pixel_sha256 && loaded?.parameter === state.candidate.parameter_key;
  $("pass").disabled = $("reject").disabled = !ready;
  window.quickTest?.controls(ready);
  $("reject-note").disabled = busy || !state?.candidate;
  $("original-zoom").disabled = !originalLoaded;
  $("candidate-zoom").disabled = !loaded;
  const index = state ? state.questions.findIndex(q => q.id === state.question_id) : -1;
  $("previous").disabled = busy || !connected || index <= 0;
  $("next").disabled = busy || !connected || index < 0 || index >= state.questions.length - 1;
  document.querySelectorAll(".question-item").forEach(button => button.disabled = busy || !connected);
  document.querySelectorAll(".reopen-question").forEach(button => button.disabled = busy || !connected);
  document.querySelectorAll(".delete-accepted, .cancel-delete").forEach(button => {
    button.disabled = busy || !connected || state?.status === "generating" || $("board-dialog").open;
  });
  $("review-hint").textContent = busy ? "正在保存，请稍候…" : ready ? "Pass 收集当前图；No Pass 删除候选并保留反馈。" :
    state?.candidate ? "等待原图与候选图完成载入…" : "收到候选并完成载入后可审核。";
}

function errors() {
  const message = actionError || state?.error || (!connected ? "连接中断，正在重连工作台…" : "");
  $("error").hidden = !message;
  $("error").textContent = message;
}

function listQuestions() {
  const key = JSON.stringify([state.questions, state.completed_questions, state.question_id, busy, connected, $("search").value]);
  if (key === navKey) return;
  navKey = key;
  $("question-list").replaceChildren();
  const filter = $("search").value.trim().toLowerCase();
  state.questions.filter(q => q.id.toLowerCase().includes(filter)).forEach(q => {
    const button = document.createElement("button");
    button.className = "question-item" + (q.id === state.question_id ? " active" : "");
    button.setAttribute("aria-label", `选择 ${q.id}，已收集 ${q.accepted_count} 张${q.has_pending ? "，有待审候选" : ""}`);
    if (q.id === state.question_id) button.setAttribute("aria-current", "page");
    const label = document.createElement("span"); label.textContent = q.id; button.append(label);
    if (q.has_pending) { const dot = document.createElement("span"); dot.className = "dot"; button.append(dot); }
    const count = document.createElement("span"); count.className = "count"; count.textContent = `${q.accepted_count} 张`; button.append(count);
    button.addEventListener("click", () => navigate(q.id));
    $("question-list").append(button);
  });
  const completed = state.completed_questions || [];
  $("toggle-completed").textContent = `已完成 ${completed.length} 道 · ${$("completed-list").hidden ? "查看" : "收起"}`;
  $("toggle-completed").disabled = !connected || busy || completed.length === 0;
  $("toggle-completed").setAttribute("aria-expanded", String(!$("completed-list").hidden));
  const completedList = $("completed-list");
  completedList.replaceChildren();
  completed.filter(q => q.id.toLowerCase().includes(filter)).forEach(q => {
    const row = document.createElement("div"); row.className = "question-item completed-item";
    const label = document.createElement("span"); label.textContent = `${q.id} · ${q.accepted_count} 张`;
    const button = document.createElement("button"); button.className = "reopen-question";
    button.textContent = "重新打开"; button.disabled = busy || !connected;
    button.setAttribute("aria-label", `重新打开 ${q.id}`);
    button.addEventListener("click", () => reopenQuestion(q.id));
    row.append(label, button); completedList.append(row);
  });
}

function actionSummary(action) {
  if (action.type === "add_point") return `点 ${action.id}：(${action.xy.join(", ")})，${action.filled ? "实心" : "空心"}，${action.color}，${action.size_pt2} pt²`;
  if (action.type === "add_line") return `线段 ${action.id}：(${action.endpoints[0].join(", ")}) → (${action.endpoints[1].join(", ")})，${action.linestyle === "dashed" ? "虚线" : "实线"}，${action.color}，${action.linewidth_pt} pt`;
  if (action.type === "set_object_style") return `原对象 ${action.target}：${action.color || "保留颜色"}，${action.linestyle ? (action.linestyle === "dashed" ? "虚线" : "实线") : "保留各片段原线型"}`;
  return `未知操作：${action.type}`;
}

function zoom(url, title) {
  $("zoom-title").textContent = title;
  $("zoom-image").src = url;
  $("zoom-image").alt = title;
  $("zoom-dialog").showModal();
}

function render(next) {
  const previous = state;
  state = next; connected = true;
  $("question-total").textContent = `待标注 ${state.questions.length} 道`;
  $("question-id").textContent = state.question_id || "全部收集完成";
  const hasQuestion = !!state.question_id;
  $("all-collected").hidden = hasQuestion;
  document.querySelectorAll("main > .question-panel, main > .comparison, main > .review-bar, main > .object-panel, main > .collection").forEach(element => element.hidden = !hasQuestion);
  $("question-text").textContent = state.question;
  $("answer").textContent = typeof state.answer === "string" ? state.answer : JSON.stringify(state.answer, null, 2);
  $("total-count").textContent = `已完成 ${state.collected_total} 题 · 已保存 ${state.accepted_total} 张`;
  $("status").textContent = statusNames[state.status] || state.status;
  $("status").className = `status status-${state.status}`;
  if (previous?.question_id !== state.question_id || previous?.input_revision !== state.input_revision || previous?.session_id !== state.session_id) {
    originalLoaded = false;
    $("original-image").onload = () => { originalLoaded = $("original-image").naturalWidth === 768; controls(); };
    $("original-image").onerror = () => { originalLoaded = false; actionError = "原图载入失败。"; errors(); controls(); };
    if (state.original_image_url) $("original-image").src = state.original_image_url;
    else $("original-image").removeAttribute("src");
    renderObjects();
  }
  const key = JSON.stringify([state.question_id, state.candidate?.candidate_id, state.accepted.map(r => r.candidate_id)]);
  if (key !== displayKey) {
    displayKey = key;
    loaded = null;
    $("reject-note").value = "";
    const candidate = state.candidate;
    $("candidate-zoom").hidden = !candidate;
    $("waiting").hidden = !!candidate;
    $("candidate-info").hidden = !candidate;
    $("candidate-count").textContent = candidate ? "待人工审核" : "等待提交";
    $("candidate-id").textContent = candidate ? `ID · ${candidate.candidate_id}` : "没有待审候选";
    if (candidate) {
      const expected = candidate.candidate_id;
      $("candidate-image").onload = () => {
        if (state.candidate?.candidate_id === expected && $("candidate-image").naturalWidth === 768) {
          loaded = {id: expected, pixel: candidate.pixel_sha256, parameter: candidate.parameter_key};
          $("candidate-frame").dataset.loadedCandidate = expected;
          controls();
        }
      };
      $("candidate-image").onerror = () => { loaded = null; actionError = "候选图载入失败，请等待更新或检查服务。"; errors(); controls(); };
      $("candidate-image").src = candidate.image_url;
      $("description").textContent = candidate.description || "未填写描述";
      $("intent").textContent = candidate.intent ? `意图：${candidate.intent}` : "";
      $("action-summary").replaceChildren(...candidate.params.actions.map(action => {
        const li = document.createElement("li"); li.textContent = actionSummary(action); return li;
      }));
      $("candidate-params").textContent = JSON.stringify(candidate.params, null, 2);
    } else {
      $("candidate-image").removeAttribute("src");
      delete $("candidate-frame").dataset.loadedCandidate;
    }
    renderAccepted();
  }
  if (state.status === "generating" && !state.candidate) {
    $("waiting").querySelector("strong").textContent = "正在生成候选…";
  } else {
    $("waiting").querySelector("strong").textContent = "等待 agent 提交方案";
  }
  listQuestions(); errors(); controls();
  window.drawingBoard?.onState(state);
  window.quickTest?.onState(state);
}

function renderObjects() {
  $("objects").replaceChildren();
  state.objects.filter(obj => obj.styleable).forEach(obj => {
    const row = document.createElement("div"); row.className = "object-row";
    const id = document.createElement("code"); id.textContent = obj.id;
    const expression = document.createElement("span"); expression.className = "expression";
    expression.textContent = `${obj.kind} · 冻结场景对象 ${obj.id}`;
    const button = document.createElement("button"); button.textContent = "高亮参考";
    button.setAttribute("aria-label", `高亮 ${obj.id}`);
    button.addEventListener("click", async () => {
      const qid = state.question_id;
      button.disabled = true;
      try { const ref = await api("/api/highlight", {question_id: qid, object_id: obj.id}); zoom(ref.image_url, `仅供参考 · ${qid} / ${obj.id}`); }
      catch (error) { actionError = error.message; errors(); }
      finally { button.disabled = false; }
    });
    row.append(id, expression, button); $("objects").append(row);
  });
}

function renderAccepted() {
  $("accepted-count").textContent = state.accepted.length;
  $("accepted-list").replaceChildren();
  if (!state.accepted.length) {
    const empty = document.createElement("p"); empty.className = "empty-collection";
    empty.textContent = "本题尚未收集 C 图。通过一张候选后，图片与冻结参数会显示在这里。";
    $("accepted-list").append(empty); return;
  }
  state.accepted.forEach(recipe => {
    const card = document.createElement("article"); card.className = "accepted-card";
    const button = document.createElement("button"); button.className = "image-button";
    button.setAttribute("aria-label", `放大已收集 ${recipe.slot_id}`);
    const image = document.createElement("img"); image.src = recipe.image_url; image.alt = `${state.question_id} ${recipe.slot_id}`;
    button.append(image); button.addEventListener("click", () => zoom(recipe.image_url, `${recipe.question_id} · ${recipe.slot_id} · 已收集`));
    const caption = document.createElement("div"); caption.className = "accepted-caption";
    const title = document.createElement("strong"); title.textContent = recipe.slot_id;
    const heading = document.createElement("div"); heading.className = "accepted-heading";
    const remove = document.createElement("button"); remove.className = "delete-accepted";
    remove.textContent = "删除"; remove.setAttribute("aria-label", `删除 ${recipe.question_id} ${recipe.slot_id}`);
    const confirmation = document.createElement("div"); confirmation.className = "delete-confirmation"; confirmation.hidden = true;
    const hint = document.createElement("p"); hint.textContent = "删除这张变体？剩余变体会按顺序重新编号。";
    const yes = document.createElement("button"); yes.className = "delete-accepted"; yes.textContent = "确认删除";
    yes.setAttribute("aria-label", `确认删除 ${recipe.question_id} ${recipe.slot_id}`);
    const cancel = document.createElement("button"); cancel.className = "cancel-delete"; cancel.textContent = "取消";
    remove.addEventListener("click", () => { confirmation.hidden = false; remove.hidden = true; controls(); });
    cancel.addEventListener("click", () => { confirmation.hidden = true; remove.hidden = false; });
    yes.addEventListener("click", () => deleteAccepted(recipe));
    confirmation.append(hint, yes, cancel); heading.append(title, remove);
    const description = document.createElement("p"); description.textContent = recipe.description;
    const details = document.createElement("details"), summary = document.createElement("summary"), pre = document.createElement("pre");
    summary.textContent = "插件参数"; pre.textContent = JSON.stringify(recipe, null, 2); details.append(summary, pre);
    caption.append(heading, description, details, confirmation); card.append(button, caption); $("accepted-list").append(card);
  });
}

async function deleteAccepted(recipe) {
  if (busy || !connected || state?.status === "generating" || $("board-dialog").open) return;
  const body = {question_id: recipe.question_id, candidate_id: recipe.candidate_id, slot_id: recipe.slot_id,
    context_token: state.context_token, pixel_sha256: recipe.pixel_sha256, parameter_key: recipe.parameter_key};
  busy = true; epoch++; actionError = ""; controls();
  try { render(await api("/api/delete-accepted", body)); }
  catch (error) { actionError = error.message; errors(); }
  finally { busy = false; controls(); }
}

async function navigate(qid) {
  if (busy || qid === state?.question_id) return;
  busy = true; epoch++; actionError = ""; controls();
  try { render(await api("/api/navigate", {question_id: qid})); }
  catch (error) { actionError = error.message; errors(); }
  finally { busy = false; controls(); }
}

async function review(decision) {
  if (busy || !loaded || $("pass").disabled) return;
  const body = {question_id: state.question_id, candidate_id: loaded.id, decision, context_token: state.context_token,
    pixel_sha256: loaded.pixel, parameter_key: loaded.parameter, note: decision === "reject" ? $("reject-note").value : ""};
  busy = true; epoch++; actionError = ""; controls();
  try { await api("/api/review", body); render(await api("/api/state")); }
  catch (error) { actionError = error.message; errors(); }
  finally { busy = false; controls(); }
}

async function collectQuestion() {
  if ($("collect-question").disabled) return;
  const body = {question_id: state.question_id, context_token: state.context_token};
  busy = true; epoch++; actionError = ""; controls();
  try { render(await api("/api/collect", body)); }
  catch (error) { actionError = error.message; errors(); }
  finally { busy = false; controls(); }
}

async function reopenQuestion(qid) {
  if (busy || !connected) return;
  busy = true; epoch++; actionError = ""; controls(); listQuestions();
  try { render(await api("/api/reopen", {question_id: qid, context_token: state.context_token})); }
  catch (error) { actionError = error.message; errors(); }
  finally { busy = false; controls(); listQuestions(); }
}

async function refresh() {
  if (polling || busy) return;
  polling = true; const startEpoch = epoch;
  try { const next = await api("/api/state"); if (startEpoch === epoch && !busy) render(next); }
  catch (error) { if (startEpoch === epoch) { connected = false; errors(); controls(); } }
  finally { polling = false; }
}

$("previous").addEventListener("click", () => navigate(state.questions[state.questions.findIndex(q => q.id === state.question_id) - 1].id));
$("next").addEventListener("click", () => navigate(state.questions[state.questions.findIndex(q => q.id === state.question_id) + 1].id));
$("search").addEventListener("input", () => { if (state) { listQuestions(); controls(); } });
$("pass").addEventListener("click", () => review("pass"));
$("reject").addEventListener("click", () => review("reject"));
$("collect-question").addEventListener("click", collectQuestion);
$("toggle-completed").addEventListener("click", () => {
  $("completed-list").hidden = !$("completed-list").hidden;
  navKey = ""; listQuestions();
});
$("original-zoom").addEventListener("click", () => zoom(state.original_image_url, `${state.question_id} · 原图`));
$("candidate-zoom").addEventListener("click", () => { if (loaded) zoom(state.candidate.image_url, `${state.question_id} · 当前候选`); });
$("close-zoom").addEventListener("click", () => $("zoom-dialog").close());
$("close-prompt").addEventListener("click", () => $("prompt-dialog").close());
$("prompt-button").addEventListener("click", async () => {
  try {
    const response = await fetch("/api/prompt");
    if (!response.ok) throw new Error("提示词载入失败。");
    $("prompt-text").value = await response.text(); $("prompt-dialog").showModal();
  } catch (error) { actionError = error.message; errors(); }
});
$("copy-prompt").addEventListener("click", async () => {
  try { await navigator.clipboard.writeText($("prompt-text").value); $("copy-prompt").textContent = "已复制"; }
  catch { $("prompt-text").select(); $("copy-prompt").textContent = "已选中，请按 Ctrl+C"; }
});
async function pollLoop() { await refresh(); setTimeout(pollLoop, state?.poll_interval_ms || 1000); }
pollLoop();
