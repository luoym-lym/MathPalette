/* Local-only original review. The server owns all review and progress state. */
(() => {
  'use strict';
  const $ = (id) => document.getElementById(id);
  const storageKey = 'mathpalette.solidgeo.original-review.pending.v1';
  const state = {data: null, current: null, loading: false, writing: false,
    pending: null, readEpoch: 0, navigation: {running: false, target: null, inflight: null},
    images: {key: null, source: false, redraw: false, failures: []}, zoomKind: 'source', zoomScale: null};
  const text = (value, fallback = '未提供') => value === null || value === undefined || value === ''
    ? fallback : (typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value));
  const asList = (value) => value === null || value === undefined ? [] : Array.isArray(value) ? value : [value];
  const statusLabels = {pending: '待审核', passed: '已通过', deleted: '已删除'};
  const typeLabels = {choice: '单项选择', number: '数值', expression: '表达式', text: '文字'};
  const current = () => state.current;
  const candidates = () => state.data?.candidates || [];
  const locked = () => state.writing || Boolean(state.pending);
  const eligible = (q) => Boolean(q && (q.pass_eligible ?? q.eligible) === true);

  function notify(message, kind = 'success', retry = false) {
    $('notice').hidden = false;
    $('notice').className = `notice ${kind === 'success' ? '' : kind}`;
    $('notice-text').textContent = message;
    $('retry-button').hidden = !retry;
    $('notice-close').hidden = retry;
    $('notice').setAttribute('role', kind === 'error' ? 'alert' : 'status');
  }
  function persistPending(value) {
    state.pending = value;
    try { if (value) sessionStorage.setItem(storageKey, JSON.stringify(value)); else sessionStorage.removeItem(storageKey); }
    catch (_) { /* The in-memory request identity still protects this open tab. */ }
  }
  function restorePending() {
    try {
      const p = JSON.parse(sessionStorage.getItem(storageKey));
      if (p && ['pass', 'delete'].includes(p.action) && typeof p.payload?.candidate_id === 'string'
          && typeof p.payload?.content_sha256 === 'string' && typeof p.payload?.request_id === 'string') {
        state.pending = p;
      }
    } catch (_) { /* Unavailable or invalid browser storage is never approval. */ }
  }
  function uniqueRequestId() {
    if (globalThis.crypto?.randomUUID) return crypto.randomUUID();
    const values = new Uint32Array(4);
    if (!globalThis.crypto?.getRandomValues) throw new Error('浏览器不支持安全请求编号。请使用新版 Edge、Chrome 或 Firefox。');
    crypto.getRandomValues(values);
    return Array.from(values, (v) => v.toString(16).padStart(8, '0')).join('-');
  }
  async function api(path, payload) {
    const options = {cache: 'no-store', credentials: 'same-origin', headers: {'Accept': 'application/json'}};
    if (payload !== undefined) {
      options.method = 'POST';
      options.headers['Content-Type'] = 'application/json';
      options.headers['X-Review-Token'] = state.data?.review_token || '';
      options.body = JSON.stringify(payload);
    }
    let response;
    try { response = await fetch(path, options); }
    catch (_) { const error = new Error('无法连接本机服务。请确认启动窗口仍在运行。'); error.uncertain = payload !== undefined; throw error; }
    let body;
    try { body = await response.json(); }
    catch (_) { const error = new Error('服务返回了无法识别的响应。请检查启动窗口。'); error.uncertain = payload !== undefined; throw error; }
    if (!response.ok || body.ok === false) {
      const error = new Error(text(body.message || body.error, `请求失败（HTTP ${response.status}）`));
      error.status = response.status; error.code = body.code; error.reasons = body.reasons;
      error.uncertain = payload !== undefined && response.status >= 500;
      throw error;
    }
    return body;
  }
  function validateState(data) {
    if (!data || !Array.isArray(data.candidates) || typeof data.review_token !== 'string') {
      throw new Error('服务返回的审核状态不完整；未改变任何页面审核状态。');
    }
    const ids = new Set();
    for (const q of data.candidates) {
      if (!q || typeof q.candidate_id !== 'string' || ids.has(q.candidate_id)) throw new Error('服务返回重复或无效的候选编号。');
      ids.add(q.candidate_id);
    }
    return data;
  }
  function applyState(data, selection = null) {
    validateState(data);
    state.data = data;
    const requested = selection || data.current_candidate_id;
    state.current = data.candidates.find((q) => q.candidate_id === requested) || data.candidates[0] || null;
    render();
  }
  async function refresh({quiet = false} = {}) {
    if (state.writing || state.navigation.running) return;
    const epoch = ++state.readEpoch;
    state.loading = true; renderControls();
    if (!state.data) $('loading').hidden = false;
    try {
      const data = await api('/api/state');
      if (epoch !== state.readEpoch) return;
      state.images.key = null;
      applyState(data);
      if (state.pending) notify('有一笔审核请求的结果尚未确认。请核对并重试原请求；不会创建第二笔操作。', 'warning', true);
      else if (!quiet) notify('已读取本机服务保存的最新状态。');
    } catch (error) {
      if (epoch === state.readEpoch) notify(error.message, 'error', Boolean(state.pending));
    } finally {
      if (epoch === state.readEpoch) { state.loading = false; $('loading').hidden = true; renderControls(); }
    }
  }

  function renderMath(el) {
    if (typeof globalThis.renderMathInElement !== 'function') return;
    try {
      globalThis.renderMathInElement(el, {
        delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\[', right: '\\]', display: true},
          {left: '\\(', right: '\\)', display: false}, {left: '$', right: '$', display: false}],
        output: 'mathml', throwOnError: true, trust: false, strict: 'error', maxExpand: 1000, maxSize: 20,
        errorCallback: () => {},
      });
    } catch (_) { /* Source text remains available if math rendering is unavailable. */ }
  }
  function answerValue(id, value, fallback) {
    const el = $(id); el.textContent = text(value, fallback);
    el.classList.toggle('complex', value !== null && typeof value === 'object');
    el.classList.toggle('long', text(value, fallback).length > 90);
    el.tabIndex = text(value, fallback).length > 90 ? 0 : -1;
    renderMath(el);
  }
  function normalizedVerification(q) {
    const v = q.verification || {};
    const raw = String(v.canonical_agreement ?? v.agreement ?? v.comparison ?? v.status ?? '').toLowerCase().replace(/[ -]/g, '_');
    if (['agreement', 'agree', 'agrees', 'agreed', 'match', 'matched', 'consistent'].includes(raw)) return {kind: 'agreement', label: '一致', v};
    if (['disagreement', 'disagree', 'disagrees', 'mismatch', 'conflict', 'inconsistent'].includes(raw)) return {kind: 'disagreement', label: '不一致', v};
    return {kind: 'unknown', label: '未确定', v};
  }
  function renderProof(value) {
    const container = $('verification-proof'); container.replaceChildren();
    if (Array.isArray(value)) {
      const list = document.createElement('ol');
      for (const step of value) { const li = document.createElement('li'); li.textContent = text(step); list.append(li); }
      container.append(list);
    } else container.textContent = text(value, '暂无独立推导记录，不能将来源答案当作已验算答案。');
    renderMath(container);
  }
  function safeImageURL(raw) {
    if (!raw || typeof raw !== 'string') return null;
    try { const url = new URL(raw, location.href); return url.origin === location.origin && url.pathname.startsWith('/api/image/') ? url.href : null; }
    catch (_) { return null; }
  }
  function renderImages(q) {
    const key = `${q.candidate_id}:${q.content_sha256}:${q.source_image_url}:${q.redraw_image_url}`;
    if (state.images.key === key) return;
    state.images = {key, source: false, redraw: false, failures: []};
    for (const kind of ['source', 'redraw']) {
      const img = $(`${kind}-image`); const placeholder = $(`${kind}-placeholder`);
      const label = kind === 'source' ? '来源原图' : '规范重绘';
      const url = safeImageURL(q[`${kind}_image_url`]);
      img.onload = null; img.onerror = null; img.removeAttribute('src');
      placeholder.hidden = false; placeholder.classList.remove('error');
      placeholder.textContent = `正在加载${label}…`;
      $(`${kind}-zoom`).disabled = true;
      const failed = () => {
        if (state.images.key !== key) return;
        state.images[kind] = false;
        if (!state.images.failures.includes(kind)) state.images.failures.push(kind);
        placeholder.hidden = false; placeholder.classList.add('error');
        placeholder.textContent = `${label}${url ? '加载失败' : '尚未提供'}\n请查看下方阻塞原因或刷新状态`;
        img.removeAttribute('src'); renderControls(); renderBlockers();
      };
      if (!url) { failed(); continue; }
      img.onload = () => {
        if (state.images.key !== key || current()?.candidate_id !== q.candidate_id) return;
        if (!img.naturalWidth || !img.naturalHeight) { failed(); return; }
        state.images[kind] = true; placeholder.hidden = true; $(`${kind}-zoom`).disabled = false;
        renderControls(); renderBlockers();
      };
      img.onerror = failed;
      img.alt = `${q.candidate_id} ${label}`;
      img.src = url;
    }
  }
  function renderBlockers() {
    const q = current(); if (!q) return;
    const reasons = [...asList(q.ineligible_reasons), ...asList(q.pass_blockers)].map((r) => text(r?.message ?? r)).filter(Boolean);
    for (const kind of state.images.failures) reasons.push(`${kind === 'source' ? '来源原图' : '规范重绘图'}未能显示，不能确认当前图片。`);
    if (!eligible(q) && !reasons.length && q.status !== 'passed') reasons.push('当前候选尚未通过服务端的内容与协议检查。');
    const unique = [...new Set(reasons)];
    $('blockers-card').hidden = unique.length === 0 || q.status === 'passed';
    $('blockers-list').replaceChildren();
    for (const reason of unique) { const li = document.createElement('li'); li.textContent = reason; $('blockers-list').append(li); }
  }
  function render() {
    const rows = candidates(); const q = current();
    const passed = state.data.counts?.passed ?? rows.filter((r) => r.status === 'passed').length;
    const pending = state.data.counts?.pending ?? rows.filter((r) => r.status !== 'passed').length;
    const deleted = state.data.counts?.deleted ?? 0;
    const initialTotal = pending + passed + deleted;
    const percent = initialTotal ? Math.round(100 * (passed + deleted) / initialTotal) : 0;
    $('pending-count').textContent = pending; $('passed-count').textContent = passed; $('total-count').textContent = rows.length;
    $('progress-summary').textContent = `已审核 ${passed + deleted} / ${initialTotal} 题 · 已删除 ${deleted} 题`;
    $('progress-percent').textContent = `${percent}%`;
    $('progress-fill').style.width = `${percent}%`;
    $('progress-track').setAttribute('aria-valuenow', String(percent));
    $('progress-track').setAttribute('aria-valuetext', `${passed} 题已通过，${deleted} 题已删除，${pending} 题待审核`);
    $('position-total').textContent = rows.length;
    $('question-select').replaceChildren();
    for (const row of rows) {
      const option = document.createElement('option'); option.value = row.candidate_id;
      option.textContent = `${row.candidate_id} · ${statusLabels[row.status] || '待审核'}${row.formal_id ? ` · ${row.formal_id}` : ''}`;
      $('question-select').append(option);
    }
    const receipts = (state.data.completed_reviews || []).filter((receipt) => !receipt.action || receipt.action === 'pass');
    $('completed-reviews').hidden = receipts.length === 0;
    $('completed-reviews-list').replaceChildren();
    for (const receipt of receipts) {
      if (receipt.action && receipt.action !== 'pass') continue;
      const item = document.createElement('li');
      item.textContent = `${receipt.candidate_id} → ${receipt.formal_id || '正式题'}${receipt.at_utc ? ` · ${receipt.at_utc}` : ''}`;
      $('completed-reviews-list').append(item);
    }
    $('question-article').hidden = !q;
    $('empty-state').hidden = Boolean(q);
    $('loading').hidden = true;
    if (!q) { $('position-current').textContent = '0'; state.images.key = null; renderControls(); return; }
    $('question-select').value = q.candidate_id;
    $('position-current').textContent = rows.findIndex((r) => r.candidate_id === q.candidate_id) + 1;
    $('question-id').textContent = q.candidate_id;
    $('review-status').textContent = statusLabels[q.status] || '待审核';
    $('review-status').className = `badge ${q.status === 'passed' ? 'badge-passed' : 'badge-pending'}`;
    $('formal-id').hidden = !q.formal_id; $('formal-id').textContent = q.formal_id ? `正式题号 ${q.formal_id}` : '';
    $('source-meta').textContent = [text(q.source_dataset, '来源未标明'), q.source_key ? `来源编号 ${text(q.source_key)}` : null].filter(Boolean).join(' / ');
    $('question-text').textContent = text(q.question ?? q.query, '题干尚未提供');
    renderMath($('question-text'));
    const choices = q.choices;
    $('choices').replaceChildren();
    const entries = Array.isArray(choices) ? choices.map((item, index) => [String.fromCharCode(65 + index), item]) : choices && typeof choices === 'object' ? Object.entries(choices) : [];
    $('choices').hidden = entries.length === 0;
    for (const [letter, value] of entries) {
      const li = document.createElement('li'); const key = document.createElement('span'); const content = document.createElement('span');
      key.className = 'choice-letter'; key.textContent = letter; content.textContent = text(value); li.append(key, content); $('choices').append(li);
    }
    renderMath($('choices'));
    answerValue('source-answer', q.source_answer, '来源未提供');
    const choice = entries.find(([letter]) => letter === String(q.answer));
    answerValue('canonical-answer', choice ? `${text(q.answer)} · ${text(choice[1])}` : q.answer, '尚未确定');
    $('answer-type').textContent = `答案类型：${typeLabels[q.answer_type] || text(q.answer_type, '未提供')}`;
    answerValue('verified-answer', q.independently_verified_answer, '尚未独立确定');
    const {kind, label, v} = normalizedVerification(q);
    $('verification-status').textContent = label; $('verification-status').className = `badge badge-${kind}`;
    $('verification-answer-help').textContent = kind === 'agreement' ? '核验记录：与标准答案一致' : kind === 'disagreement' ? '核验记录：存在差异，请先核对推导' : '核验记录：结论未确定';
    $('verification-method').textContent = text(v.method, '未记录核验方法');
    renderProof(v.proof ?? v.notes);
    const evidence = {independently_expected_result: v.independently_expected_result, agreement_evidence: v.agreement_evidence, evidence: v.evidence, source_notes: q.source_notes};
    $('verification-evidence-details').hidden = !Object.values(evidence).some((value) => value !== undefined && value !== null);
    $('verification-evidence').textContent = text(evidence, '');
    const technical = {candidate_id: q.candidate_id, content_sha256: q.content_sha256, scene_contract: q.scene_contract ?? null};
    for (const key of ['protocol', 'migration', 'migration_metadata', 'provenance', 'environment', 'redraw_environment']) if (q[key] !== undefined) technical[key] = q[key];
    $('technical-content').textContent = JSON.stringify(technical, null, 2);
    renderImages(q); renderBlockers(); renderControls();
  }
  function renderControls() {
    const q = current(); const nav = state.navigation;
    const desired = nav.target || nav.inflight || q?.candidate_id;
    const index = candidates().findIndex((row) => row.candidate_id === desired);
    const mutationBlocked = locked() || state.loading || nav.running;
    const imageReady = state.images.source && state.images.redraw;
    $('previous-button').disabled = locked() || state.loading || index <= 0;
    $('next-button').disabled = locked() || state.loading || index < 0 || index >= candidates().length - 1;
    $('question-select').disabled = locked() || state.loading || !q;
    $('refresh-button').disabled = state.loading || state.writing || nav.running;
    $('pass-button').disabled = mutationBlocked || !q || q.status !== 'pending' || !eligible(q) || !imageReady;
    $('delete-button').disabled = mutationBlocked || !q || q.status !== 'pending';
    $('retry-button').disabled = state.writing || state.loading;
    $('pass-label').textContent = state.writing && state.pending?.action === 'pass' ? '正在保存…' : q?.status === 'passed' ? '已通过原题' : 'Pass · 原题通过';
    $('question-article').setAttribute('aria-busy', String(state.writing || nav.running));
    $('save-title').textContent = state.writing ? '正在等待服务端确认' : state.pending ? '上一笔操作结果待确认' : nav.running ? '正在切换题目' : state.loading ? '正在读取已保存状态' : q?.status === 'passed' ? `已收录为 ${q.formal_id || '正式题'}` : !q ? '本机审核状态' : !eligible(q) ? '此题暂不能通过' : !imageReady ? '等待两张图片完整显示' : '审核当前显示内容';
    $('save-description').textContent = state.pending ? '核对并重试会沿用同一请求编号，防止重复操作' : q?.status === 'passed' ? '通过记录与正式编号已由服务端保存' : 'Pass 确认当前原图、重绘、完整题干和标准答案，并收录为正式题';
  }

  async function navigateTo(id) {
    if (locked() || state.loading || !candidates().some((q) => q.candidate_id === id)) return;
    const nav = state.navigation; nav.target = id; renderControls();
    if (nav.running) return;
    nav.running = true; ++state.readEpoch;
    try {
      while (nav.target) {
        const target = nav.target; nav.target = null; nav.inflight = target; renderControls();
        try {
          const data = await api('/api/navigate', {candidate_id: target});
          if (!nav.target || nav.target === target) applyState(data, target);
        } catch (error) {
          nav.target = null; notify(`${error.message}\n未切换题目，请刷新状态后再试。`, 'error');
        }
      }
    } finally { nav.inflight = null; nav.running = false; renderControls(); }
  }
  function move(delta) {
    const desired = state.navigation.target || state.navigation.inflight || current()?.candidate_id;
    const index = candidates().findIndex((q) => q.candidate_id === desired);
    const target = candidates()[index + delta]; if (index >= 0 && target) navigateTo(target.candidate_id);
  }
  async function performMutation(action, retry = false) {
    if (state.writing || state.loading || state.navigation.running) return;
    const q = current();
    if (retry) { if (!state.pending) return; action = state.pending.action; }
    else {
      if (state.pending || !q || q.status !== 'pending') return;
      if (action === 'pass' && (!eligible(q) || !state.images.source || !state.images.redraw)) return;
      try {
        persistPending({action, payload: {candidate_id: q.candidate_id, content_sha256: q.content_sha256, request_id: uniqueRequestId()}});
      } catch (error) { notify(error.message, 'error'); return; }
    }
    const request = state.pending;
    state.writing = true; ++state.readEpoch; renderControls();
    $('delete-dialog').close();
    notify(`${action === 'pass' ? '正在收录' : '正在删除'} ${request.payload.candidate_id}，等待服务端确认…`, 'warning');
    try {
      const data = await api(`/api/${action}`, request.payload);
      const result = data.result;
      if (!result || result.candidate_id !== request.payload.candidate_id || result.action !== action) {
        const error = new Error('服务响应缺少对应的操作确认。结果尚未确定。'); error.uncertain = true; throw error;
      }
      validateState(data);
      if (action === 'pass') {
        const row = data.candidates.find((item) => item.candidate_id === request.payload.candidate_id);
        const receipt = (data.completed_reviews || []).find((item) => item.candidate_id === request.payload.candidate_id && item.formal_id === result.formal_id);
        if ((!row || row.status !== 'passed' || !row.formal_id) && (!receipt || !result.formal_id)) { const error = new Error('服务尚未返回完整的正式题收录记录。'); error.uncertain = true; throw error; }
      } else if (data.candidates.some((item) => item.candidate_id === request.payload.candidate_id && item.status !== 'deleted')) {
        const error = new Error('服务尚未确认候选已从队列移除。'); error.uncertain = true; throw error;
      }
      persistPending(null); applyState(data);
      const preserved = (result.preserved_shared_files?.length || 0) + (result.preserved_untracked_files?.length || 0);
      const preservationNote = preserved ? ` 已保留 ${preserved} 个共享或未纳入 Git 的文件。` : '';
      notify((action === 'pass' ? `${request.payload.candidate_id} 已通过，正式题号 ${result.formal_id || data.candidates.find((item) => item.candidate_id === request.payload.candidate_id)?.formal_id}。审核记录已保存。` : `${request.payload.candidate_id} 已从候选队列删除。`) + preservationNote);
    } catch (error) {
      if (error.uncertain || !error.status) {
        notify(`${error.message}\n操作可能已保存。请核对并重试原请求，切勿通过另一个标签页重复提交。`, 'warning', true);
      } else {
        persistPending(null);
        let message = error.message;
        if (error.status === 409) message = '此题内容或审核状态已改变，本次操作未执行。请重新查看最新内容后再决定。';
        if (error.status === 403) message = '本机服务已重启或审核令牌失效，本次操作未执行。已尝试重新读取状态。';
        notify(message + (error.reasons?.length ? `\n${error.reasons.join('\n')}` : ''), 'error');
        try { applyState(await api('/api/state')); } catch (refreshError) { notify(`${message}\n最新状态读取失败：${refreshError.message}`, 'error'); }
      }
    } finally { state.writing = false; renderControls(); }
  }

  function setZoom(kind) {
    if (!state.images[kind]) return;
    state.zoomKind = kind; state.zoomScale = null;
    $('zoom-image').src = $(`${kind}-image`).src;
    $('zoom-image').alt = `${current()?.candidate_id} ${kind === 'source' ? '来源原图' : '规范重绘'}放大图`;
    $('zoom-title').textContent = `${current()?.candidate_id} · ${kind === 'source' ? '来源原图' : '规范重绘'}`;
    for (const which of ['source', 'redraw']) {
      $(`zoom-${which}`).classList.toggle('active', which === kind);
      $(`zoom-${which}`).setAttribute('aria-pressed', String(which === kind));
      $(`zoom-${which}`).disabled = !state.images[which];
    }
    fitZoom();
  }
  function fitZoom() { state.zoomScale = null; $('zoom-image').classList.add('fit'); $('zoom-image').style.width = ''; $('zoom-image').style.height = ''; }
  function zoomBy(factor) {
    const img = $('zoom-image');
    const base = img.naturalWidth || 768;
    const width = img.getBoundingClientRect().width || base;
    state.zoomScale = Math.max(0.2, Math.min(6, (state.zoomScale ?? width / base) * factor));
    img.classList.remove('fit'); img.style.width = `${Math.round(base * state.zoomScale)}px`; img.style.height = 'auto';
  }
  function openZoom(kind) { if (!state.images[kind]) return; setZoom(kind); $('zoom-dialog').showModal(); }
  $('refresh-button').addEventListener('click', () => refresh());
  $('empty-refresh').addEventListener('click', () => refresh());
  $('previous-button').addEventListener('click', () => move(-1));
  $('next-button').addEventListener('click', () => move(1));
  $('question-select').addEventListener('change', (event) => navigateTo(event.target.value));
  $('notice-close').addEventListener('click', () => { if (!state.pending) $('notice').hidden = true; });
  $('retry-button').addEventListener('click', () => performMutation(state.pending?.action, true));
  $('pass-button').addEventListener('click', () => performMutation('pass'));
  $('delete-button').addEventListener('click', () => {
    if ($('delete-button').disabled || !current()) return;
    $('delete-dialog-description').textContent = `候选 ${current().candidate_id}：${text(current().question ?? current().query, '题干未提供')}`;
    $('delete-dialog').showModal(); $('delete-cancel').focus();
  });
  $('delete-confirm').addEventListener('click', () => performMutation('delete'));
  for (const kind of ['source', 'redraw']) {
    $(`${kind}-zoom`).addEventListener('click', () => openZoom(kind));
    $(`zoom-${kind}`).addEventListener('click', () => setZoom(kind));
  }
  $('zoom-close').addEventListener('click', () => $('zoom-dialog').close());
  $('zoom-fit').addEventListener('click', fitZoom);
  $('zoom-in').addEventListener('click', () => zoomBy(1.35));
  $('zoom-out').addEventListener('click', () => zoomBy(1 / 1.35));
  document.addEventListener('keydown', (event) => {
    const tag = event.target?.tagName?.toLowerCase();
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || ['input', 'textarea', 'select', 'button', 'summary'].includes(tag)
        || event.target?.isContentEditable || $('zoom-dialog').open || $('delete-dialog').open) return;
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') { event.preventDefault(); move(event.key === 'ArrowLeft' ? -1 : 1); }
  });
  restorePending();
  refresh({quiet: true});
})();
