(function () {
  'use strict';
  const C = window.ReviewCore;
  const $ = id => document.getElementById(id);
  const PAGE_SIZE = 40;
  const ATTEMPT_KEY = 'mathpalette.mathverse.review.attempts.v1';
  const SYNC_KEY = 'mathpalette.mathverse.review.changed.v1';
  const state = {rows:[],summary:{},selected:null,detail:null,detailReady:false,images:{source:false,redraw:false},filter:{status:'pending',branch:'all',dataset:'all',category:'all',query:''},page:0,generation:0,listGeneration:0,detailController:null,operation:null,attempts:{},noticeCallback:null,deleteTarget:null,zoom:1};
  try { state.attempts = JSON.parse(sessionStorage.getItem(ATTEMPT_KEY) || '{}'); } catch (_) { /* Optional persistence only. */ }
  const saveAttempts = () => { try { sessionStorage.setItem(ATTEMPT_KEY,JSON.stringify(state.attempts)); } catch (_) {} };
  const filtered = () => C.filter(state.rows,state.filter);
  const statusLabel = value => ({pending:'待审核',passed:'已通过',deleted:'已删除'}[C.status(value)]);
  const safeUrl = value => { if(typeof value!=='string'||!value)return null;try {const u = new URL(value,location.origin);return u.origin === location.origin && ['http:','https:'].includes(u.protocol) ? u.href : null;} catch (_) {return null;} };
  const uniqueId = () => window.crypto?.randomUUID?.() || `review-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  function setText(id,value) { $(id).textContent = C.string(value); }
  function showNotice(message,type='success',label=null,callback=null) {
    setText('notice-text',message);$('notice').className = `notice ${type === 'error' ? 'error' : ''}`;$('notice').hidden = false;
    $('notice-action').hidden = !label;setText('notice-action',label || '');state.noticeCallback = callback;
  }
  function mathText(element,value,whole=false) {
    const text = C.string(value); element.textContent = text;
    const options = {output:'mathml',throwOnError:true,trust:false,strict:'error',maxExpand:1000,maxSize:20};
    try {
      if (whole && !/\$|\\\(|\\\[/.test(text) && /\\(?:frac|sqrt|pi|theta|cdot|times|sin|cos|tan|left|right|begin|angle|circ|mathrm|text)|[_^][{\w]/.test(text)) window.katex?.render(text,element,options);
      else window.renderMathInElement?.(element,{...options,delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false},{left:'$',right:'$',display:false}]});
    } catch (_) { element.textContent = text; }
  }
  class ApiError extends Error { constructor(message,status,code) {super(message);this.status=status;this.code=code;} }
  async function request(url,options={},timeout=150000) {
    const controller = new AbortController();
    const outer = options.signal;
    const abort = () => controller.abort();
    if (outer?.aborted) controller.abort(); else outer?.addEventListener('abort',abort,{once:true});
    const timer = setTimeout(abort,timeout);
    try {
      const response = await fetch(url,{...options,signal:controller.signal,cache:'no-store',credentials:'same-origin'});
      let payload;
      try { payload = await response.json(); } catch (_) { throw new ApiError('服务器返回了无法读取的结果，请刷新检查进度。',response.status,'invalid_response'); }
      if (!response.ok || payload.ok === false) {
        const error = payload.error;
        throw new ApiError(typeof error === 'string' ? error : error?.message || payload.message || `请求未完成（${response.status}）`,response.status,error?.code || payload.code);
      }
      return payload;
    } finally { clearTimeout(timer);outer?.removeEventListener('abort',abort); }
  }
  function renderSummary() {
    const summary = C.compactSummary(state.rows,state.summary);
    for (const key of ['pending','passed','deleted','total']) setText(`${key}-count`,summary[key]);
    const done = Number(summary.passed) + Number(summary.deleted);
    const percentage = summary.total ? Math.round(done/summary.total*100) : 0;
    $('progress-fill').style.width = `${Math.min(100,percentage)}%`;
    setText('progress-label',`${done} / ${summary.total} 已审核`);setText('progress-percent',`${percentage}%`);
  }
  function renderList(reveal=false) {
    const rows = filtered();
    if (reveal) {const i=rows.findIndex(row=>row.id===state.selected);if(i>=0)state.page=Math.floor(i/PAGE_SIZE);}
    const pageCount = Math.max(1,Math.ceil(rows.length/PAGE_SIZE));state.page = Math.min(state.page,pageCount-1);
    const fragment = document.createDocumentFragment();
    rows.slice(state.page*PAGE_SIZE,(state.page+1)*PAGE_SIZE).forEach(row => {
      const button=document.createElement('button');button.type='button';button.className='candidate-row';button.dataset.id=row.id;
      button.setAttribute('aria-current',String(row.id===state.selected));button.setAttribute('aria-label',`${row.id} ${C.sourceLabel(row)} ${statusLabel(row.status)}`);
      const dot=document.createElement('span');dot.className=`row-dot ${C.status(row.status)}`;dot.setAttribute('aria-hidden','true');
      const copy=document.createElement('span');copy.className='row-copy';const title=document.createElement('span');title.className='row-title';title.textContent=row.id;
      const subtitle=document.createElement('span');subtitle.className='row-subtitle';subtitle.textContent=C.sourceLabel(row);
      const status=document.createElement('span');status.className='row-status';status.textContent=statusLabel(row.status);
      copy.append(title,subtitle);button.append(dot,copy,status);button.addEventListener('click',()=>select(row.id));fragment.append(button);
    });
    if (!rows.length) {const empty=document.createElement('p');empty.className='list-empty';empty.textContent='没有符合筛选条件的题目。';fragment.append(empty);}
    $('candidate-list').replaceChildren(fragment);setText('list-count',`${rows.length} 道题`);setText('page-label',`${state.page+1} / ${pageCount} 页`);
    $('page-prev').disabled=state.page<=0;$('page-next').disabled=state.page>=pageCount-1;renderNavigation();
  }
  function renderNavigation() {
    const rows=filtered(),index=rows.findIndex(row=>row.id===state.selected);
    setText('position-label',index>=0?`${index+1} / ${rows.length}`:'筛选外题目');$('previous').disabled=index<=0;$('next').disabled=index<0||index>=rows.length-1;
  }
  function writeLocation(replace=false) {
    const params=new URLSearchParams();if(state.selected)params.set('id',state.selected);
    if(state.filter.status!=='pending')params.set('status',state.filter.status);
    if(state.filter.branch!=='all')params.set('branch',state.filter.branch);
    if(state.filter.dataset!=='all')params.set('dataset',state.filter.dataset);
    if(state.filter.category!=='all')params.set('category',state.filter.category);
    if(state.filter.query)params.set('q',state.filter.query);
    const url=`${location.pathname}${params.size?'?'+params.toString():''}`;
    if(url!==location.pathname+location.search)history[replace?'replaceState':'pushState']({},'',url);
  }
  function readLocation() {
    const params=new URLSearchParams(location.search);
    state.filter.status=['pending','passed','deleted','all'].includes(params.get('status'))?params.get('status'):'pending';
    state.filter.branch=['PlaneGeometry','SolidGeometry','Analytics','all'].includes(params.get('branch'))?params.get('branch'):'all';
    state.filter.dataset=['MathVerse','MathVision','all'].includes(params.get('dataset'))?params.get('dataset'):'all';
    state.filter.category=['solid geometry','transformation geometry','combinatorial geometry','all'].includes(params.get('category'))?params.get('category'):'all';
    if(state.filter.dataset==='MathVerse')state.filter.category='all';
    state.filter.query=params.get('q')||'';
    syncFilterControls();
    return params.get('id');
  }
  async function loadList({initial=false,keep=true}={}) {
    const token=++state.listGeneration;$('refresh').disabled=true;
    try {
      const result=await request('/api/candidates');if(token!==state.listGeneration)return;
      const rows=result.candidates||result.items||[];
      if(!Array.isArray(rows))throw new Error('候选清单格式不正确。');
      const byId=new Map(rows.map(row=>[row.id,{...row,status:C.status(row.status)}]));
      for(const row of result.history||[])if(!byId.has(row.id))byId.set(row.id,{...row,status:C.status(row.status)});
      state.rows=[...byId.values()].sort((a,b)=>a.id.localeCompare(b.id,undefined,{numeric:true}));state.summary=result.summary||{};
      $('connection-error').hidden=true;renderSummary();renderList(true);
      for(const [id,attempt] of Object.entries(state.attempts)) {const row=byId.get(id);if(row&&C.status(row.status)!=='pending')delete state.attempts[id];}saveAttempts();
      const desired=initial?readLocation():state.selected;
      const target=keep&&desired&&byId.has(desired)?desired:filtered()[0]?.id;
      await select(target||null,{history:!initial,replace:initial,focus:false});
    } catch(error) {
      if(token!==state.listGeneration)return;
      $('connection-error').textContent=`无法读取审核进度：${error.name==='AbortError'?'连接超时，请确认本地服务正在运行。':error.message}`;$('connection-error').hidden=false;
      if(!state.rows.length){$('loading-panel').hidden=true;setText('candidate-id','连接未完成');setText('candidate-status','请重试');}
    } finally {if(token===state.listGeneration)$('refresh').disabled=false;}
  }
  function clearImages() {
    for(const kind of ['source','redraw']) {const img=$(`${kind}-image`);img.onload=null;img.onerror=null;img.removeAttribute('src');img.hidden=true;$(`${kind}-placeholder`).hidden=false;$(`${kind}-placeholder`).className='image-placeholder';setText(`${kind}-placeholder`,'正在载入图片…');$(`${kind}-image-button`).disabled=true;$(`${kind}-zoom`).disabled=true;state.images[kind]=false;}
  }
  async function select(id,{history:changeHistory=true,replace=false,focus=false}={}) {
    const generation=++state.generation;state.detailController?.abort();state.detailController=new AbortController();state.selected=id;state.detail=null;state.detailReady=false;
    if($('delete-dialog').open)$('delete-dialog').close();state.deleteTarget=null;
    if($('zoom-dialog').open)$('zoom-dialog').close();
    clearImages();$('history-panel').hidden=true;$('detail-content').hidden=true;$('detail-error').hidden=true;$('loading-panel').hidden=!id;$('candidate-view').hidden=!id;$('empty-state').hidden=!!id;$('candidate-view').setAttribute('aria-busy',String(!!id));
    renderList(true);if(changeHistory||replace)writeLocation(replace);
    if(!id){setText('empty-title',state.filter.query||state.filter.branch!=='all'||state.filter.dataset!=='all'||state.filter.category!=='all'||state.filter.status!=='pending'?'没有符合条件的题目':'当前列表已审核完成');renderActions();return;}
    const row=state.rows.find(row=>row.id===id);setText('candidate-id',id);setText('candidate-meta',C.sourceLabel(row||{}));setBadge(row?.status);renderActions();
    if(focus)$('candidate-id').focus({preventScroll:true});
    try {
      const result=await request(`/api/candidates/${encodeURIComponent(id)}`,{signal:state.detailController.signal});
      if(generation!==state.generation||id!==state.selected)return;
      state.detail=result.candidate?{...result.candidate,...result}:result;state.detail.id=id;state.detail.status=C.status(state.detail.status??row?.status);
      if(row)row.status=state.detail.status;
      state.detailReady=true;$('loading-panel').hidden=true;$('detail-content').hidden=false;$('candidate-view').setAttribute('aria-busy','false');renderDetail(state.detail,generation);renderList();renderActions();
      let attempt=state.attempts[id];
      if(attempt&&attempt.fingerprint!==state.detail.fingerprint&&state.detail.status==='pending'){delete state.attempts[id];saveAttempts();attempt=null;showNotice('题目内容已更新，请重新核对图片、题干和答案后再审核。','error');renderActions();}
      if(attempt&&state.detail.status==='pending'&&!state.operation)showNotice(`上次 ${attempt.action==='pass'?'Pass':'Delete'} 的结果尚未确认。核对当前状态后，可用原请求安全重试。`,'error','重试上次操作',()=>retryAttempt());
    } catch(error) {
      if(generation!==state.generation||id!==state.selected)return;
      $('loading-panel').hidden=true;$('candidate-view').setAttribute('aria-busy','false');
      if(row&&C.status(row.status)!=='pending'&&error.status===404){state.detail={...row,status:C.status(row.status)};state.detailReady=true;setBadge(row.status);setText('detail-error-text','这道题已完成审核，原候选已归档。');$('detail-error').hidden=false;$('retry-detail').hidden=true;}
      else {setText('detail-error-text',`当前题目载入失败：${error.name==='AbortError'?'连接超时，请重试。':error.message}`);$('detail-error').hidden=false;$('retry-detail').hidden=false;}
      renderActions();
    }
  }
  function setBadge(value) {const normalized=C.status(value);setText('candidate-status',statusLabel(normalized));$('candidate-status').className=`badge ${normalized}`;}
  function renderDetail(detail,generation) {
    setText('candidate-meta',`${C.sourceLabel(detail)}${detail.source_key?' · '+detail.source_key:''}`);
    if(detail.history || (!detail.question && C.status(detail.status)!=='pending')) {
      $('detail-content').hidden=true;$('history-panel').hidden=false;setBadge(detail.status);
      setText('history-title',detail.status==='passed'?`已通过${detail.formal_id?' · '+detail.formal_id:''}`:'候选题已删除');
      setText('history-copy',detail.status==='passed'?'题目已正式收录。审核记录已保存，刷新页面不会重复收录。':'这道候选的原图、重绘图及专属材料已删除。这里仅展示审核操作记录。');
      setText('history-time',detail.decided_at_utc?`审核时间：${new Date(detail.decided_at_utc).toLocaleString()}`:'');return;
    }
    const e=C.evidence(detail);setBadge(detail.status);
    const choices=detail.choices&&typeof detail.choices==='object'?detail.choices:{};
    const question=C.string(detail.question);
    // Keep the source verbatim below; separate candidate options only when the standard Choices block is present.
    const body=Object.keys(choices).length?question.replace(/\n\s*Choices\s*:[\s\S]*$/i,''):question;
    mathText($('question-text'),body);$('choices').replaceChildren();
    for(const [key,value] of Object.entries(choices)) {const li=document.createElement('li');if(C.string(detail.answer).trim()===key)li.className='answer-choice';const label=document.createElement('span');label.className='choice-key';label.textContent=key;const content=document.createElement('span');mathText(content,value,true);li.append(label,content);$('choices').append(li);}
    $('choices').hidden=!Object.keys(choices).length;mathText($('answer'),e.candidateAnswer,true);setText('answer-type',({choice:'单项选择',number:'数值',expression:'表达式',text:'文本'}[detail.answer_type]||detail.answer_type||'答案'));
    mathText($('original-question'),e.originalQuestion||'未提供原始题干');setText('question-change-label',detail.differences?.question_changed?'题干有调整':'来源记录');
    $('original-choices').replaceChildren();$('original-choices').hidden=!e.originalOptions.length;
    e.originalOptions.forEach((value,index)=>{const li=document.createElement('li');const label=document.createElement('span');label.className='choice-key';label.textContent=String.fromCharCode(65+index);const content=document.createElement('span');mathText(content,value,true);li.append(label,content);$('original-choices').append(li);});
    mathText($('original-answer'),e.originalAnswer,true);mathText($('verified-answer'),e.derived,true);
    const labels={consistent:'原答案与候选一致',corrected:'已修正来源答案',needs_manual_confirmation:'请重点核对',unknown:'核验信息待确认'};
    setText('consistency-badge',labels[e.consistency]||'请重点核对');$('consistency-badge').className=`small-badge ${e.consistency==='consistent'?'good':'warning'}`;
    const methodLabel=({independently_derived:'独立推导',independently_verified:'独立计算核验',independent_answer_checks_passed:'独立答案检查通过'}[e.method]||C.string(e.method));
    const reasonLabel=({'Resolved answers agree, or provenance explicitly records a representation-only answer normalization.':'已比较选项所代表的答案；来源答案与候选答案一致，或仅作表达形式归一化。','Explicit correction recorded in provenance.':'已记录对来源答案的明确修正，请核对下方依据。'}[e.reason]||e.reason);
    setText('verification-status',[reasonLabel,methodLabel?`核验方法：${methodLabel}`:''].filter(Boolean).join('\n')||'未提供明确的独立答案核验结论，请人工确认。');
    mathText($('verification-explanation'),e.explanation||'请展开原始核验记录，查看计算依据与适用限制。');mathText($('adaptation-notes'),e.adaptation);
    setText('evidence-text',JSON.stringify(e.record,null,2));
    for(const kind of ['source','redraw']) {
      const url=safeUrl(detail.images?.[kind]);const image=$(`${kind}-image`);const placeholder=$(`${kind}-placeholder`);
      if(!url){setText(`${kind}-placeholder`,detail.status==='pending'?'没有可用图片，暂不能审核':'审核已完成，候选图片已归档');placeholder.classList.add('failed');continue;}
      image.onload=()=>{if(generation!==state.generation)return;state.images[kind]=true;image.hidden=false;placeholder.hidden=true;$(`${kind}-image-button`).disabled=false;$(`${kind}-zoom`).disabled=false;setText(`${kind}-dimensions`,`${image.naturalWidth} × ${image.naturalHeight}`);renderActions();};
      image.onerror=()=>{if(generation!==state.generation)return;state.images[kind]=false;placeholder.hidden=false;placeholder.classList.add('failed');setText(`${kind}-placeholder`,'图片载入失败。请重新载入本题。');renderActions();};
      image.src=url;
    }
  }
  function renderActions() {
    const detail=state.detail,pending=detail&&C.status(detail.status)==='pending';
    const ready=state.detailReady&&pending&&detail.fingerprint&&state.images.source&&state.images.redraw;
    const attempt=state.attempts[state.selected];const busy=!!state.operation;
    // After an uncertain response, preserve the exact decision and idempotency key; do not issue a conflicting decision.
    $('pass').disabled=!ready||busy||!!attempt;$('delete').disabled=!ready||busy||!!attempt;
    $('retry-action').hidden=!attempt||!pending;$('retry-action').disabled=!ready||busy||attempt?.fingerprint!==detail?.fingerprint;
    $('review-state-dot').className=`state-dot${busy?' busy':attempt?' error':''}`;
    setText('pass',busy&&state.operation.action==='pass'?'正在收录…':'Pass · 通过并收录 →');setText('delete',busy&&state.operation.action==='delete'?'正在删除…':'Delete · 删除');
    if(busy){setText('review-title',`正在${state.operation.action==='pass'?'收录':'删除'} ${state.operation.id}`);setText('review-hint','正在保存审核记录；可浏览其他题目，请勿重复提交。');}
    else if(!state.selected){setText('review-title','当前没有待审核题目');setText('review-hint','筛选全部，可查看已经完成的审核记录。');}
    else if(detail&&!pending){setText('review-title',`${state.selected} · ${statusLabel(detail.status)}${detail.formal_id?' · '+detail.formal_id:''}`);setText('review-hint','审核结果已保存，可继续浏览其他题目。');}
    else if(attempt){setText('review-title','上次操作的结果需要确认');setText('review-hint',attempt.fingerprint!==detail?.fingerprint?'内容已改变，请刷新进度确认最新状态。':'显式重试会使用同一个请求编号，不重复收录。');}
    else if(!state.detailReady){setText('review-title','等待题目载入');setText('review-hint','详情载入完成后才能审核。');}
    else if(!ready){setText('review-title','等待两张图片完整载入');setText('review-hint','如图片载入失败，点击「刷新进度」重新读取。');}
    else {setText('review-title',`审核 ${state.selected}`);setText('review-hint','Pass 收录为正式题；Delete 删除当前候选。');}
  }
  function openDelete() {
    if($('delete').disabled)return;state.deleteTarget={id:state.selected,fingerprint:state.detail.fingerprint,generation:state.generation};
    setText('delete-copy',`${state.selected} · ${C.sourceLabel(state.detail)}`);$('delete-dialog').showModal();$('cancel-delete').focus();
  }
  function retryAttempt() {
    const attempt=state.attempts[state.selected];
    if(!attempt||state.operation||!state.detailReady||attempt.fingerprint!==state.detail?.fingerprint)return;
    if(attempt.action==='delete') {state.deleteTarget={...attempt,generation:state.generation,retry:true};setText('delete-copy',`重试删除 ${attempt.id}。使用原请求编号核对结果，不会重复操作。`);$('delete-dialog').showModal();$('cancel-delete').focus();}
    else decide('pass',attempt);
  }
  async function decide(action,retry=null) {
    const detail=state.detail;
    if(state.operation||!detail||C.status(detail.status)!=='pending'||!state.detailReady||!state.images.source||!state.images.redraw)return;
    if(!retry&&state.attempts[state.selected])return;
    const attempt=retry||{id:state.selected,fingerprint:detail.fingerprint,action,request_id:uniqueId()};
    if(attempt.id!==state.selected||attempt.fingerprint!==detail.fingerprint)return;
    const generation=state.generation;const before=filtered().slice();
    state.operation=attempt;state.attempts[attempt.id]=attempt;saveAttempts();state.listGeneration++;$('refresh').disabled=true;renderActions();
    showNotice(`正在${action==='pass'?'收录':'删除'} ${attempt.id}，审核记录正在保存。`);
    try {
      const result=await request(`/api/candidates/${encodeURIComponent(attempt.id)}/${action}`,{method:'POST',headers:{'Content-Type':'application/json','X-Review-Workbench':'1'},body:JSON.stringify({fingerprint:attempt.fingerprint,request_id:attempt.request_id})},240000);
      const nextStatus=result.status|| (action==='pass'?'passed':'deleted');
      const row=state.rows.find(row=>row.id===attempt.id);if(row){row.status=C.status(nextStatus);row.formal_id=result.formal_id||row.formal_id;}
      if(result.summary)state.summary=result.summary;else state.summary=C.compactSummary(state.rows);
      delete state.attempts[attempt.id];saveAttempts();state.operation=null;
      if(state.selected===attempt.id&&state.detail){state.detail.status=C.status(nextStatus);state.detail.formal_id=result.formal_id;setBadge(nextStatus);}
      renderSummary();renderList();
      try {localStorage.setItem(SYNC_KEY,JSON.stringify({id:attempt.id,at:Date.now()}));} catch (_) {}
      showNotice(action==='pass'?`${attempt.id} 已通过${result.formal_id?'，正式题号 '+result.formal_id:''}。`:`${attempt.id} 已删除，审核历史已保存。`);
      if(state.selected===attempt.id&&state.generation===generation) {
        const candidates=filtered().filter(row=>C.status(row.status)==='pending');
        const next=C.nextAfter(before,attempt.id,candidates);
        if(next)await select(next,{replace:true,focus:true});
        else if(state.filter.status==='pending')await select(null,{replace:true});
        else await select(attempt.id,{replace:true});
      }
    } catch(error) {
      state.operation=null;
      const conflict=error.status===409||error.status===410;
      if(conflict){delete state.attempts[attempt.id];saveAttempts();}
      const message=error.name==='AbortError'?'等待结果超时，服务器可能仍在处理。请刷新确认，或安全重试相同请求。':error.message;
      showNotice(`${attempt.id} ${action==='pass'?'Pass':'Delete'} 未确认成功：${message}`,'error',state.selected===attempt.id?(conflict?'重新载入':'重试上次操作'):'返回该题',()=>state.selected===attempt.id?(conflict?loadList():retryAttempt()):select(attempt.id));
      // A failed request never advances or changes the candidate's saved status.
      if(conflict&&state.selected===attempt.id){state.detailReady=false;}
    } finally {state.operation=null;$('refresh').disabled=false;renderActions();}
  }
  function openZoom(kind) {
    if(!state.images[kind])return;const source=$(`${kind}-image`);$('zoom-image').src=source.src;$('zoom-image').alt=`${state.selected} ${kind==='source'?'原始图片':'重绘图片'}`;
    setText('zoom-title',`${state.selected} · ${kind==='source'?'原始图片':'重绘图片'}`);setText('zoom-size',`${source.naturalWidth} × ${source.naturalHeight}`);state.zoom=1;updateZoom();$('zoom-dialog').showModal();$('close-zoom').focus();
  }
  function updateZoom() {const image=$('zoom-image'),viewport=$('zoom-viewport');viewport.classList.toggle('is-zoomed',state.zoom>1);image.style.width=state.zoom>1?`${state.zoom*100}%`:'';setText('zoom-fit',state.zoom===1?'适应窗口':`${Math.round(state.zoom*100)}% · 复位`);$('zoom-out').disabled=state.zoom<=1;$('zoom-in').disabled=state.zoom>=4;}
  function move(step) {const rows=filtered(),index=rows.findIndex(row=>row.id===state.selected);if(index>=0&&rows[index+step])select(rows[index+step].id,{focus:true});}
  function syncFilterControls() {
    $('status-filter').value=state.filter.status;$('branch-filter').value=state.filter.branch;$('dataset-filter').value=state.filter.dataset;$('category-filter').value=state.filter.category;$('category-filter').disabled=state.filter.dataset==='MathVerse';$('search').value=state.filter.query;
  }
  function applyFilters() {state.filter={status:$('status-filter').value,branch:$('branch-filter').value,dataset:$('dataset-filter').value,category:$('category-filter').value,query:$('search').value};if(state.filter.dataset==='MathVerse')state.filter.category='all';syncFilterControls();state.page=0;const rows=filtered();select(rows.some(row=>row.id===state.selected)?state.selected:rows[0]?.id||null);}
  $('refresh').addEventListener('click',()=>{if(!state.operation)loadList();});
  $('notice-dismiss').addEventListener('click',()=>{$('notice').hidden=true;});$('notice-action').addEventListener('click',()=>state.noticeCallback?.());
  $('previous').addEventListener('click',()=>move(-1));$('next').addEventListener('click',()=>move(1));
  $('page-prev').addEventListener('click',()=>{state.page--;renderList();});$('page-next').addEventListener('click',()=>{state.page++;renderList();});
  for(const id of ['status-filter','branch-filter','dataset-filter','category-filter'])$(id).addEventListener('change',applyFilters);
  let searchTimer; $('search').addEventListener('input',()=>{clearTimeout(searchTimer);searchTimer=setTimeout(applyFilters,180);});
  $('jump-form').addEventListener('submit',event=>{event.preventDefault();const raw=$('jump-id').value.trim();const {row,ambiguous}=C.resolveJump(raw,state.rows,state.filter.dataset);if(!row){showNotice(ambiguous?`题号 ${raw} 同时属于 MathVerse 和 MathVision，请输入完整编号 MV… / MVI…，或先选择题目来源。`:`未找到题号 ${raw||'（空）'}，请输入完整候选题号，例如 MV0001 或 MVI0011。`,'error');return;}if(!filtered().some(item=>item.id===row.id)){state.filter={status:'all',branch:'all',dataset:C.dataset(row)||'all',category:'all',query:''};syncFilterControls();}select(row.id,{focus:true});});
  $('clear-filters').addEventListener('click',()=>{state.filter={status:'all',branch:'all',dataset:'all',category:'all',query:''};syncFilterControls();applyFilters();});
  $('retry-detail').addEventListener('click',()=>select(state.selected,{history:false}));
  $('pass').addEventListener('click',()=>{if(!$('pass').disabled)decide('pass');});$('delete').addEventListener('click',openDelete);$('retry-action').addEventListener('click',retryAttempt);
  $('cancel-delete').addEventListener('click',()=>{$('delete-dialog').close();state.deleteTarget=null;});
  $('confirm-delete').addEventListener('click',()=>{const target=state.deleteTarget;$('delete-dialog').close();state.deleteTarget=null;if(target&&target.id===state.selected&&target.fingerprint===state.detail?.fingerprint&&target.generation===state.generation)decide('delete',target.retry?state.attempts[target.id]:null);});
  $('delete-dialog').addEventListener('close',()=>{state.deleteTarget=null;});
  for(const kind of ['source','redraw'])for(const suffix of ['zoom','image-button'])$(`${kind}-${suffix}`).addEventListener('click',()=>openZoom(kind));
  $('close-zoom').addEventListener('click',()=>{$('zoom-dialog').close();$('zoom-image').removeAttribute('src');});
  $('zoom-dialog').addEventListener('close',()=>{$('zoom-image').removeAttribute('src');});
  $('zoom-in').addEventListener('click',()=>{state.zoom=Math.min(4,state.zoom+.5);updateZoom();});$('zoom-out').addEventListener('click',()=>{state.zoom=Math.max(1,state.zoom-.5);updateZoom();});$('zoom-fit').addEventListener('click',()=>{state.zoom=1;updateZoom();});
  document.addEventListener('keydown',event=>{if(event.defaultPrevented||event.ctrlKey||event.metaKey||event.altKey||event.shiftKey||event.repeat||document.querySelector('dialog[open]')||event.target.closest('input,textarea,select,button,a,summary,[contenteditable="true"]'))return;if(event.key==='ArrowLeft'){event.preventDefault();move(-1);}if(event.key==='ArrowRight'){event.preventDefault();move(1);}});
  window.addEventListener('popstate',()=>{const desired=readLocation();select(desired&&state.rows.some(row=>row.id===desired)?desired:filtered()[0]?.id||null,{history:false});});
  window.addEventListener('storage',event=>{if(event.key===SYNC_KEY&&!state.operation)loadList();});
  window.addEventListener('beforeunload',event=>{if(state.operation){event.preventDefault();event.returnValue='';}});
  readLocation();loadList({initial:true});
})();
