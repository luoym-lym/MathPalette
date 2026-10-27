/* Browser regression tests use an entirely synthetic API. They cannot alter a candidate. */
const {test,before,after}=require('node:test');
const assert=require('node:assert/strict');
const {chromium}=require('playwright');
const http=require('node:http');
const fs=require('node:fs');
const path=require('node:path');
const C=require('../static/review-core.js');
let server,browser,base;
const staticRoot=path.resolve(__dirname,'../static');
const screenshotRoot=path.resolve(__dirname,'../../.runtime/frontend-qa');
before(async()=>{
  fs.mkdirSync(screenshotRoot,{recursive:true});
  server=http.createServer((req,res)=>{
    const requestPath=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
    const relative=requestPath==='/'?'index.html':requestPath.replace(/^\/static\//,'');
    const file=path.resolve(staticRoot,relative);
    if(!file.startsWith(staticRoot+path.sep)){res.writeHead(403).end();return;}
    fs.readFile(file,(error,data)=>{if(error){res.writeHead(404).end();return;}res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':'text/html');res.end(data);});
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));base=`http://127.0.0.1:${server.address().port}`;
  browser=await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',args:['--no-sandbox']});
});
after(async()=>{await browser?.close();await new Promise(resolve=>server?.close(resolve));});
const wait=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function fixture(options={}){
  const context=await browser.newContext({viewport:options.viewport||{width:1440,height:1040}});
  const page=await context.newPage();const posts=[],errors=[];let failures=options.failures||0;
  const rows=options.rows?.map(row=>({...row}))||Array.from({length:options.count??731},(_,i)=>({id:`MV${String(i+1).padStart(4,'0')}`,branch:i%3===0?'PlaneGeometry':i%3===1?'SolidGeometry':'Analytics',status:'pending',title:`Triangle question ${i+1}`}));
  const summary=()=>({total:rows.length,pending:rows.filter(r=>r.status==='pending').length,passed:rows.filter(r=>r.status==='passed').length,deleted:rows.filter(r=>r.status==='deleted').length});
  page.on('pageerror',error=>errors.push(error.message));
  await context.route('**/api/**',async route=>{
    const url=new URL(route.request().url()),parts=url.pathname.split('/').filter(Boolean);const id=parts[2];
    const reply=(body,status=200)=>route.fulfill({status,contentType:'application/json',body:JSON.stringify(body)});
    if(parts.length===2){await reply({candidates:rows,summary:summary()});return;}
    const row=rows.find(r=>r.id===id);if(!row){await reply({error:'not found'},404);return;}
    if(parts[3]==='image'){
      if(options.imageError){await route.fulfill({status:500,body:'broken'});return;}
      await route.fulfill({contentType:'image/svg+xml',body:`<svg xmlns="http://www.w3.org/2000/svg" width="700" height="500" viewBox="0 0 700 500"><rect width="700" height="500" fill="white"/><path d="M100 400 L350 90 L600 400 Z M220 245 L480 245" fill="none" stroke="#263f33" stroke-width="4"/><text x="333" y="65" font-size="28">A</text><text x="70" y="430" font-size="28">B</text><text x="610" y="430" font-size="28">C</text><text x="170" y="242" font-size="24">D</text><text x="490" y="242" font-size="24">E</text><text x="175" y="380" font-size="23">60°</text><text x="329" y="169" font-size="23">80°</text></svg>`});return;
    }
    if(route.request().method()==='POST'){
      const body=route.request().postDataJSON();posts.push({id,action:parts[3],body,header:route.request().headers()['x-review-workbench']});
      if(options.actionDelay)await wait(options.actionDelay);
      if(failures>0){failures--;await reply({error:{code:options.failureCode||'temporary',message:'模拟保存失败，请重试。'}},options.failureStatus||500);return;}
      row.status=parts[3]==='pass'?'passed':'deleted';row.formal_id=parts[3]==='pass'?'Plane72':undefined;
      await reply({ok:true,id,status:row.status,formal_id:row.formal_id,summary:summary()});return;
    }
    if(options.detailDelay?.[id])await wait(options.detailDelay[id]);
    if(row.status!=='pending'){await reply({...row,history:true,decided_at_utc:'2026-10-11T12:00:00Z',images:{}});return;}
    await reply({...row,fingerprint:`fp-${id}`,question:options.injection||'As shown in the figure, DE is parallel to BC. Find angle CED.\nChoices:\nA:40°\nB:60°\nC:120°\nD:140°',answer:'D',choices:{A:'40°',B:'60°',C:'120°',D:'140°'},answer_type:'choice',original_question:'As shown in the figure, DE is parallel to BC. Find angle CED.',original_answer:'D',candidate_answer_value:'140°',source_answer_value:'140°',answer_consistency:{status:'consistent',reason:'The original and candidate answer values agree.'},provenance_data:{audit:{independently_computed_result:140,independent_solution:'Angle C = 180 − 80 − 60 = 40°. Angle CED = 180 − 40 = 140°.',answer_verification:'independently_derived'}},images:{source:`/api/candidates/${id}/image/source`,redraw:`/api/candidates/${id}/image/redraw`}});
  });
  await page.goto(base);await page.locator('#candidate-id').filter({hasText:options.initialId||'MV0001'}).waitFor();
  return {page,context,posts,errors,rows,close:()=>context.close()};
}
async function ready(page,id='MV0001'){await page.waitForFunction(id=>document.querySelector('#candidate-id').textContent===id&&!document.querySelector('#pass').disabled,id);}

test('core helpers preserve answer semantics and select an adjacent remaining item',()=>{
  assert.equal(C.status('prepared_for_user_review'),'pending');
  assert.equal(C.evidence({answer:'D',choices:{D:'140°'},original_answer:'D',source_answer_value:'140°',provenance_data:{audit:{independently_computed_result:140}}}).derived,'140');
  assert.equal(C.evidence({answer:'A',choices:{A:'2/3'}}).candidateAnswer,'A · 2/3');
  assert.equal(C.nextAfter([{id:'a'},{id:'b'},{id:'c'}],'b',[{id:'a'},{id:'c'}]),'c');
  assert.equal(C.nextAfter([{id:'a'}],'a',[]),null);
});
test('731 rows stay bounded, only current images are fetched, math/source answers remain visible',async()=>{
  const f=await fixture();try{await ready(f.page);assert.equal(await f.page.locator('.candidate-row').count(),40);assert.equal(await f.page.locator('#detail-content img[src]').count(),2);assert.match(await f.page.locator('#original-answer').innerText(),/D.*140/);assert.equal(await f.page.locator('#verified-answer').innerText(),'140');assert.equal(await f.page.locator('#total-count').innerText(),'731');await f.page.screenshot({path:path.join(screenshotRoot,'frontend-desktop.png'),fullPage:true});assert.deepEqual(f.errors,[]);}finally{await f.close();}
});
test('double click sends one request and shows immediate busy state before next candidate',async()=>{
  const f=await fixture({count:3,actionDelay:450});try{await ready(f.page);await f.page.locator('#pass').dblclick({delay:5,force:true});assert.equal(f.posts.length,1);assert.match(await f.page.locator('#review-title').innerText(),/正在收录/);assert.equal(await f.page.locator('#delete').isDisabled(),true);await ready(f.page,'MV0002');assert.equal(f.posts[0].header,'1');assert.equal(await f.page.locator('#passed-count').innerText(),'1');assert.deepEqual(f.errors,[]);}finally{await f.close();}
});
test('Delete cancel and Escape issue no request; confirmed Delete advances once',async()=>{
  const f=await fixture({count:2});try{await ready(f.page);await f.page.locator('#delete').click();assert.equal(await f.page.locator('#cancel-delete').evaluate(el=>el===document.activeElement),true);await f.page.keyboard.press('Escape');assert.equal(f.posts.length,0);await f.page.locator('#delete').click();await f.page.locator('#cancel-delete').click();assert.equal(f.posts.length,0);await f.page.locator('#delete').click();await f.page.locator('#confirm-delete').click();await ready(f.page,'MV0002');assert.equal(f.posts.length,1);assert.equal(f.posts[0].action,'delete');}finally{await f.close();}
});
test('failed Pass stays on the same item; explicit retry reuses fingerprint and request id',async()=>{
  const f=await fixture({count:3,failures:1});try{await ready(f.page);await f.page.locator('#pass').click();await f.page.locator('#notice.error').waitFor();assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0001');assert.equal(await f.page.locator('#pass').isDisabled(),true);await f.page.locator('#retry-action').click();await ready(f.page,'MV0002');assert.equal(f.posts.length,2);assert.deepEqual(f.posts[0].body,f.posts[1].body);}finally{await f.close();}
});
test('unconfirmed retry survives reload and uses the same idempotency key',async()=>{
  const f=await fixture({count:3,failures:1});try{await ready(f.page);await f.page.locator('#pass').click();await f.page.locator('#notice.error').waitFor();await f.page.reload();await f.page.locator('#retry-action:not([hidden])').waitFor();await f.page.waitForFunction(()=>!document.querySelector('#retry-action').disabled);await f.page.locator('#retry-action').click();await ready(f.page,'MV0002');assert.deepEqual(f.posts[0].body,f.posts[1].body);}finally{await f.close();}
});
test('navigation during save is preserved; an old operation cannot advance another item',async()=>{
  const f=await fixture({count:4,actionDelay:650});try{await ready(f.page);await f.page.locator('#pass').click();await f.page.locator('#next').click();await f.page.waitForFunction(()=>document.querySelector('#candidate-id').textContent==='MV0002');assert.equal(await f.page.locator('#pass').isDisabled(),true);await ready(f.page,'MV0002');assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0002');assert.equal(f.posts.length,1);}finally{await f.close();}
});
test('navigate away and back during save cannot re-enable an already accepted candidate',async()=>{
  const f=await fixture({count:3,actionDelay:550});try{await ready(f.page);await f.page.locator('#pass').click();await f.page.locator('#next').click();await f.page.locator('#previous').click();await f.page.waitForFunction(()=>document.querySelector('#passed-count').textContent==='1');assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0001');assert.equal(await f.page.locator('#pass').isDisabled(),true);assert.match(await f.page.locator('#candidate-status').innerText(),/已通过/);}finally{await f.close();}
});
test('late detail cannot replace a newer selection; URL Back restores selected candidate',async()=>{
  const f=await fixture({count:4,detailDelay:{MV0002:400}});try{await ready(f.page);await f.page.locator('#next').click();await f.page.locator('#next').click();await ready(f.page,'MV0003');await wait(500);assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0003');await f.page.goBack();await ready(f.page,'MV0002');await f.page.reload();await ready(f.page,'MV0002');}finally{await f.close();}
});
test('last pending item produces a usable empty state; completed history survives refresh',async()=>{
  const f=await fixture({count:1});try{await ready(f.page);await f.page.locator('#pass').click();await f.page.locator('#empty-state:not([hidden])').waitFor();assert.equal(await f.page.locator('#pass').isDisabled(),true);await f.page.locator('#clear-filters').click();await f.page.locator('#history-panel:not([hidden])').waitFor();assert.match(await f.page.locator('#history-title').innerText(),/Plane72/);await f.page.reload();await f.page.locator('#history-panel:not([hidden])').waitFor();assert.equal(f.posts.length,1);}finally{await f.close();}
});
test('text input focus prevents arrow navigation; zoom closes without changing history',async()=>{
  const f=await fixture({count:3});try{await ready(f.page);await f.page.locator('#search').focus();await f.page.keyboard.press('ArrowRight');assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0001');const url=f.page.url();await f.page.locator('#source-zoom').click();await f.page.locator('#zoom-in').click();assert.equal(await f.page.locator('#zoom-viewport').getAttribute('class'),'zoom-viewport is-zoomed');await f.page.keyboard.press('Escape');assert.equal(f.page.url(),url);assert.equal(await f.page.locator('#source-zoom').evaluate(el=>el===document.activeElement),true);}finally{await f.close();}
});
test('external text cannot create executable markup, and failed image blocks approval',async()=>{
  const f=await fixture({count:1,injection:'<img src=x onerror="window.PWNED=1"> $\\frac{2}{3}$',imageError:true});try{await f.page.locator('#detail-content:not([hidden])').waitFor();await f.page.waitForFunction(()=>document.querySelector('.image-placeholder.failed'));assert.equal(await f.page.locator('#pass').isDisabled(),true);assert.equal(await f.page.evaluate(()=>window.PWNED),undefined);assert.equal(await f.page.locator('#question-text img').count(),0);assert.equal(await f.page.locator('#question-text math').count(),1);assert.equal(f.posts.length,0);}finally{await f.close();}
});
test('mobile stays within viewport and keeps both full images and decision controls available',async()=>{
  const f=await fixture({count:3,viewport:{width:390,height:844}});try{await ready(f.page);assert.equal(await f.page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth),true);assert.equal(await f.page.locator('#pass').isVisible(),true);assert.equal(await f.page.locator('#source-image').evaluate(el=>getComputedStyle(el).objectFit),'contain');await f.page.screenshot({path:path.join(screenshotRoot,'frontend-mobile.png'),fullPage:true});assert.deepEqual(f.errors,[]);}finally{await f.close();}
});

const mixedRows=()=>[
  {id:'MV0001',branch:'PlaneGeometry',source_dataset:'MathVerse',status:'pending',title:'Legacy source'},
  {id:'MVI0001',branch:'SolidGeometry',source_dataset:'MathVision',source_category:'solid geometry',status:'pending',title:'Cubes'},
  {id:'MVI0002',branch:'PlaneGeometry',source_dataset:'MathVision',source_category:'transformation geometry',status:'pending',title:'Reflection'},
  {id:'MVI0003',branch:'PlaneGeometry',source_dataset:'MathVision',source_category:'combinatorial geometry',status:'pending',title:'Tiling'},
];
test('dataset/topic filters survive Back, Forward and reload and never issue decisions',async()=>{
  const f=await fixture({rows:mixedRows()});try{
    await ready(f.page);await f.page.locator('#dataset-filter').selectOption('MathVision');await ready(f.page,'MVI0001');
    assert.equal(await f.page.locator('#list-count').innerText(),'3 道题');assert.match(await f.page.locator('#candidate-meta').innerText(),/MathVision · 立体几何/);
    await f.page.locator('#category-filter').selectOption('transformation geometry');await ready(f.page,'MVI0002');
    assert.equal(await f.page.locator('#list-count').innerText(),'1 道题');
    await f.page.goBack();await ready(f.page,'MVI0001');assert.equal(await f.page.locator('#category-filter').inputValue(),'all');
    await f.page.goForward();await ready(f.page,'MVI0002');await f.page.reload();await ready(f.page,'MVI0002');
    assert.equal(await f.page.locator('#dataset-filter').inputValue(),'MathVision');assert.equal(await f.page.locator('#category-filter').inputValue(),'transformation geometry');
    await f.page.locator('#dataset-filter').selectOption('MathVerse');await ready(f.page,'MV0001');
    assert.equal(await f.page.locator('#category-filter').isDisabled(),true);assert.equal(await f.page.locator('#category-filter').inputValue(),'all');
    assert.equal(f.posts.length,0);assert.deepEqual(f.errors,[]);
  }finally{await f.close();}
});
test('bare duplicate source ID is ambiguous until a dataset is chosen; explicit jump resets incompatible filters',async()=>{
  const f=await fixture({rows:mixedRows()});try{
    await ready(f.page);await f.page.locator('#jump-id').fill('1');await f.page.locator('#jump-form button').click();
    await f.page.locator('#notice.error').waitFor();assert.match(await f.page.locator('#notice-text').innerText(),/同时属于 MathVerse 和 MathVision/);assert.equal(await f.page.locator('#candidate-id').innerText(),'MV0001');
    await f.page.locator('#dataset-filter').selectOption('MathVision');await ready(f.page,'MVI0001');
    await f.page.locator('#jump-id').fill('2');await f.page.locator('#jump-form button').click();await ready(f.page,'MVI0002');
    await f.page.locator('#jump-id').fill('MV1');await f.page.locator('#jump-form button').click();await ready(f.page,'MV0001');
    assert.equal(await f.page.locator('#dataset-filter').inputValue(),'MathVerse');assert.equal(f.posts.length,0);assert.deepEqual(f.errors,[]);
  }finally{await f.close();}
});
test('MathVision decision uses MVI identity without changing same-number MathVerse row',async()=>{
  const f=await fixture({rows:mixedRows()});try{
    await ready(f.page);await f.page.locator('#dataset-filter').selectOption('MathVision');await ready(f.page,'MVI0001');
    await f.page.locator('#delete').click();await f.page.locator('#cancel-delete').click();assert.equal(f.posts.length,0);
    await f.page.locator('#pass').click();await ready(f.page,'MVI0002');
    assert.equal(f.posts.length,1);assert.equal(f.posts[0].id,'MVI0001');assert.equal(f.rows.find(row=>row.id==='MV0001').status,'pending');
    assert.equal(await f.page.locator('#passed-count').innerText(),'1');assert.deepEqual(f.errors,[]);
  }finally{await f.close();}
});
