"use strict";
(() => {
  const profiles = ["quicktest1", "quicktest2"];
  const labels = {quicktest1: "Quick Test 1", quicktest2: "Quick Test 2"};
  const modes = {quicktest1: "MiniMax-M3 · nonthinking", quicktest2: "MiniMax-M3.1-Flash-Preview · low"};
  const element = (profile, name) => $(profile + "-" + name);
  let currentKey = "", sending = null;
  let localErrors = {}, outputKeys = {};
  const identity = value => JSON.stringify([value?.session_id, value?.question_id, value?.input_revision,
    value?.candidate?.candidate_id, value?.candidate?.pixel_sha256, value?.candidate?.parameter_key]);
  const result = (config, profile) => config?.jobs?.[profile] || (profile === "quicktest1" ? config?.job : null);

  function controls(ready) {
    const config = state?.quick_test, running = !!config?.running_candidate_id;
    for (const profile of profiles) {
      const job = result(config, profile), button = element(profile, "button");
      button.disabled = !ready || !!sending || running || !config?.configured;
      button.textContent = sending === profile || job?.status === "running" ? `${labels[profile]} · 测试中…` : labels[profile];
      button.title = !config?.configured ? "在项目 .env 中配置 MINIMAX_API_KEY" : running ?
        "正在等待模型返回结果" : `使用 ${modes[profile]} 回答当前候选图中的题目`;
    }
  }

  function onState(value) {
    const nextKey = identity(value);
    if (nextKey !== currentKey) { currentKey = nextKey; localErrors = {}; outputKeys = {}; }
    const config = value?.quick_test;
    for (const profile of profiles) {
      const job = result(config, profile);
      element(profile, "panel").hidden = !value?.candidate;
      element(profile, "model").textContent = modes[profile];
      element(profile, "hint").textContent = !config?.configured ? "请在项目 .env 中配置 MINIMAX_API_KEY。" :
        config.running_candidate_id && config.running_candidate_id !== value.candidate?.candidate_id ?
          "另一个候选正在测试，完成后即可测试当前图。" :
          profile === "quicktest1" ? "发送题干和当前候选图；关闭思考，直接回答，不自动判分。" :
          "发送题干和当前候选图；思考强度为 low，分别显示回答和思考，不自动判分。";
      const error = localErrors[profile] || job?.error || "";
      element(profile, "error").hidden = !error;
      element(profile, "error").textContent = error;
      const running = job?.status === "running";
      const statuses = {completed: "已完成", error: "测试失败", interrupted: "已中断"};
      let status = running ? `测试中 · ${Math.max(0, Math.floor((Date.now() - Date.parse(job.started_at)) / 1000))} 秒` : statuses[job?.status] || "尚未测试";
      if (!running && job?.elapsed_seconds !== undefined) status += ` · ${job.elapsed_seconds} 秒`;
      if (typeof job?.usage?.total_tokens === "number") status += ` · ${job.usage.total_tokens} tokens`;
      element(profile, "status").textContent = status;
      element(profile, "warning").hidden = !job?.truncated;
      const completed = job?.status === "completed";
      element(profile, "output").hidden = !completed;
      element(profile, "thinking-details").hidden = !completed || !job.thinking;
      const key = JSON.stringify([job?.run_id, job?.status, job?.answer, job?.thinking]);
      if (key !== outputKeys[profile]) {
        outputKeys[profile] = key;
        // Model output is untrusted text, never HTML or executable Markdown.
        element(profile, "answer").textContent = completed ? job.answer || "接口未返回最终回答。" : "";
        element(profile, "thinking").textContent = completed ? job.thinking || "" : "";
      }
    }
  }

  async function start(profile) {
    if (element(profile, "button").disabled) return;
    const target = identity(state);
    const body = {profile, question_id: state.question_id, candidate_id: loaded.id, context_token: state.context_token,
      pixel_sha256: loaded.pixel, parameter_key: loaded.parameter};
    sending = profile; localErrors[profile] = ""; controls(false); onState(state);
    try {
      const job = await api("/api/quick-test", body);
      if (identity(state) === target) {
        const config = state.quick_test;
        state.quick_test = {...config, jobs: {...config?.jobs, [profile]: job},
          ...(profile === "quicktest1" ? {job} : {}),
          running_candidate_id: job.status === "running" ? job.candidate_id : null,
          running_profile: job.status === "running" ? profile : null};
        onState(state);
        element(profile, "panel").scrollIntoView({behavior: "smooth", block: "nearest"});
      }
    } catch (error) {
      if (identity(state) === target) { localErrors[profile] = error.message; onState(state); }
    } finally { sending = null; window.quickTest.controls(!!loaded && connected && !busy && !$("pass").disabled); }
  }

  window.quickTest = {controls, onState};
  for (const profile of profiles) element(profile, "button").addEventListener("click", () => start(profile));
})();
