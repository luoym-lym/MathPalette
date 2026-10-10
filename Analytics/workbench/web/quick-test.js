"use strict";
(() => {
  let currentKey = "", sending = false, localError = "", outputKey = "";
  const identity = value => JSON.stringify([value?.session_id, value?.question_id, value?.input_revision,
    value?.candidate?.candidate_id, value?.candidate?.pixel_sha256, value?.candidate?.parameter_key]);

  function controls(ready) {
    const config = state?.quick_test;
    const job = config?.job;
    const running = !!config?.running_candidate_id;
    const button = $("quick-test-button");
    button.disabled = !ready || sending || running || !config?.configured;
    button.textContent = sending || job?.status === "running" ? "测试中…" : job ? "再次 Quick Test" : "Quick Test";
    button.title = !config?.configured ? "在项目 .env 中配置 MINIMAX_API_KEY" : running ? "正在等待 MiniMax 返回结果" : "使用 MiniMax-M3 回答当前候选图中的题目";
  }

  function onState(value) {
    const nextKey = identity(value);
    if (nextKey !== currentKey) { currentKey = nextKey; localError = ""; outputKey = ""; }
    const config = value?.quick_test, job = config?.job;
    $("quick-test-panel").hidden = !value?.candidate;
    $("quick-test-model").textContent = config?.model || "MiniMax-M3";
    $("quick-test-hint").textContent = !config?.configured ? "请在项目 .env 中配置 MINIMAX_API_KEY。" :
      config.running_candidate_id && config.running_candidate_id !== value.candidate?.candidate_id ?
        "另一个候选正在测试，完成后即可测试当前图。" : "发送题干和当前候选图，查看模型回答；已关闭思考，不自动判分。";
    const error = localError || job?.error || "";
    $("quick-test-error").hidden = !error;
    $("quick-test-error").textContent = error;
    const running = job?.status === "running";
    const labels = {completed: "已完成", error: "测试失败", interrupted: "已中断"};
    let status = running ? `测试中 · ${Math.max(0, Math.floor((Date.now() - Date.parse(job.started_at)) / 1000))} 秒` : labels[job?.status] || "尚未测试";
    if (!running && job?.elapsed_seconds !== undefined) status += ` · ${job.elapsed_seconds} 秒`;
    if (typeof job?.usage?.total_tokens === "number") status += ` · ${job.usage.total_tokens} tokens`;
    $("quick-test-status").textContent = status;
    $("quick-test-warning").hidden = !job?.truncated;
    const completed = job?.status === "completed";
    $("quick-test-output").hidden = !completed;
    $("quick-test-thinking-details").hidden = !completed || !job.thinking;
    const key = JSON.stringify([job?.run_id, job?.status, job?.answer, job?.thinking]);
    if (key !== outputKey) {
      outputKey = key;
      // Model output is untrusted text, never HTML or executable Markdown.
      $("quick-test-answer").textContent = completed ? job.answer || "接口未返回最终回答。" : "";
      $("quick-test-thinking").textContent = completed ? job.thinking || "" : "";
    }
  }

  async function start() {
    if ($("quick-test-button").disabled) return;
    const target = identity(state);
    const body = {question_id: state.question_id, candidate_id: loaded.id, context_token: state.context_token,
      pixel_sha256: loaded.pixel, parameter_key: loaded.parameter};
    sending = true; localError = ""; controls(false); onState(state);
    try {
      const job = await api("/api/quick-test", body);
      if (identity(state) === target) {
        state.quick_test = {...state.quick_test, job, running_candidate_id: job.status === "running" ? job.candidate_id : null};
        onState(state);
        $("quick-test-panel").scrollIntoView({behavior: "smooth", block: "nearest"});
      }
    } catch (error) {
      if (identity(state) === target) { localError = error.message; onState(state); }
    } finally { sending = false; window.quickTest.controls(!!loaded && connected && !busy && !$("pass").disabled); }
  }

  window.quickTest = {controls, onState};
  $("quick-test-button").addEventListener("click", start);
})();
