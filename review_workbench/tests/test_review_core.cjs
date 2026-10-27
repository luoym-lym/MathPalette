const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');const path=require('node:path');
const C=require('../static/review-core.js');
test('normalization and filtering treat only terminal decisions as completed',()=>{
  assert.equal(C.status('prepared_for_user_review'),'pending');assert.equal(C.status('passed'),'passed');assert.equal(C.status('deleted'),'deleted');
  const rows=[{id:'MV0001',subject:'PlaneGeometry',status:'prepared_for_user_review',title:'Triangle'},{id:'MV0002',subject:'Analytics',status:'passed',title:'Equation'}];
  assert.deepEqual(C.filter(rows,{status:'pending',branch:'all',query:'triangle'}),[rows[0]]);
  assert.deepEqual(C.filter(rows,{status:'all',branch:'Analytics',query:''}),[rows[1]]);
  assert.deepEqual(C.compactSummary(rows),{total:2,pending:1,passed:1,deleted:0});
});
test('successor is adjacent and handles last/only item without wrapping to a completed item',()=>{
  const rows=[{id:'a'},{id:'b'},{id:'c'}];assert.equal(C.nextAfter(rows,'b',[rows[0],rows[2]]),'c');assert.equal(C.nextAfter(rows,'c',[rows[0],rows[1]]),'b');assert.equal(C.nextAfter([rows[0]],'a',[]),null);
});
test('original and candidate choice letters resolve independently and exact values are preserved',()=>{
  const e=C.evidence({answer:'C',choices:{C:'12\\sqrt{3}'},original_answer:'D',source_answer_value:'36',candidate_answer_value:'12\\sqrt{3}',provenance_data:{audit:{independently_computed_result:'12\\sqrt{3}'}}});
  assert.equal(e.originalAnswer,'D · 36');assert.equal(e.candidateAnswer,'C · 12\\sqrt{3}');assert.equal(e.derived,'12\\sqrt{3}');
});
test('nested geometry independent solution and adaptations appear as readable fields',()=>{
  const e=C.evidence({answer:'C',choices:{C:'13 m'},provenance_data:{audit:{independent_solution:{method:'sqrt(12²+5²)=13',computed_answer:'C'},adaptations:[{type:'clarification',reason:'Only the curved lateral surface is included.'}]}}});
  assert.equal(e.derived,'C · 13 m');assert.equal(e.explanation,'sqrt(12²+5²)=13');assert.match(e.adaptation,/curved lateral/);
});
test('analytic correction keeps original and verified answer distinct',()=>{
  const e=C.evidence({original_answer:'(-2,1]',provenance_data:{audit:{adaptation:'Corrected endpoint to −1.',answer_verification:{method:'Independent analytic derivation',derivation:'Right endpoint is −1.',answer:'(-2,-1]'}}}});
  assert.equal(e.originalAnswer,'(-2,1]');assert.equal(e.derived,'(-2,-1]');assert.equal(e.method,'Independent analytic derivation');assert.equal(e.explanation,'Right endpoint is −1.');assert.equal(e.adaptation,'Corrected endpoint to −1.');
});
test('separate numerical verification record includes uniquely matched choice without replacing exact answer',()=>{
  const e=C.evidence({choices:{C:'12\\sqrt{3}'},verification_data:{'answer_verification.json':{theorem_result:20.784609690826528,answer_check:{unique:true,matching_options:['C']}}}});
  assert.match(e.derived,/C · 12\\sqrt\{3\} ≈ 20.78460969/);
});
test('all pending candidates retain original text, source values, and available independent solutions',(t)=>{
  const root=path.resolve(__dirname,'../..');const index=path.join(root,'review_candidates/mathverse/index.jsonl');
  if(!fs.existsSync(index))return;
  const rows=fs.readFileSync(index,'utf8').split('\n').filter(line=>line.trim()).map(JSON.parse);
  if(!rows.length){t.skip('No pending candidates remain');return;}
  assert.equal(new Set(rows.map(row=>row.id)).size,rows.length);
  for(const row of rows){
    const provenance_data=JSON.parse(fs.readFileSync(path.join(root,row.provenance),'utf8'));
    const verification_data=JSON.parse(fs.readFileSync(path.join(root,row.verification),'utf8'));
    const e=C.evidence({...row,provenance_data,verification_data});
    assert.ok(e.originalQuestion,`${row.id}: missing source question`);assert.notEqual(e.originalAnswer,'未提供',row.id);
    if(provenance_data.audit?.independent_solution?.computed_answer!=null){assert.notEqual(e.derived,'见核验说明',row.id);}
    if(provenance_data.audit?.answer_verification?.answer!=null){assert.notEqual(e.derived,'见核验说明',row.id);}
    assert.ok(e.explanation,`${row.id}: missing verification explanation`);
  }
});
test('source and MathVision topic filters preserve unique identities and agent verification stays pending',()=>{
  const rows=[
    {id:'MV0011',branch:'PlaneGeometry',status:'pending',source_dataset:'MathVerse'},
    {id:'MVI0011',branch:'SolidGeometry',status:'agent_verified',source_dataset:'MathVision',source_category:'solid geometry'},
    {id:'MVI0013',branch:'PlaneGeometry',status:'prepared_for_user_review',source_dataset:'MathVision',source_category:'transformation_geometry'},
    {id:'MVI0021',branch:'PlaneGeometry',status:'pending',source_dataset:'MathVision',source_category:'combinatorial geometry'},
  ];
  const all={status:'pending',branch:'all',dataset:'all',category:'all',query:''};
  assert.equal(C.filter(rows,all).length,4);
  assert.deepEqual(C.filter(rows,{...all,dataset:'MathVision'}),rows.slice(1));
  assert.deepEqual(C.filter(rows,{...all,dataset:'MathVision',category:'transformation geometry'}),[rows[2]]);
  assert.deepEqual(C.filter(rows,{...all,dataset:'MathVerse',category:'solid geometry'}),[]);
  assert.deepEqual(C.filter(rows,{...all,query:'组合几何'}),[rows[3]]);
  assert.equal(C.dataset({id:'MVI0001'}),'MathVision');assert.equal(C.dataset({id:'MV0001'}),'MathVerse');
  assert.equal(C.sourceLabel(rows[2]),'MathVision · 变换几何');
  assert.deepEqual(C.compactSummary(rows),{total:4,pending:4,passed:0,deleted:0});
});
test('jump IDs never confuse MathVerse with MathVision and numeric ambiguity requires a source',()=>{
  const rows=[{id:'MV0011',source_dataset:'MathVerse'},{id:'MVI0011',source_dataset:'MathVision'},{id:'MVI0013',source_dataset:'MathVision'}];
  assert.deepEqual(C.resolveJump('11',rows),{row:null,ambiguous:true});
  assert.deepEqual(C.resolveJump('00011',rows,'MathVision'),{row:rows[1],ambiguous:false});
  assert.deepEqual(C.resolveJump('11',rows,'MathVerse'),{row:rows[0],ambiguous:false});
  assert.deepEqual(C.resolveJump('mvi11',rows),{row:rows[1],ambiguous:false});
  assert.deepEqual(C.resolveJump('mv00011',rows,'MathVision'),{row:rows[0],ambiguous:false});
  assert.deepEqual(C.resolveJump('13',rows),{row:rows[2],ambiguous:false});
  assert.deepEqual(C.resolveJump('13',rows,'MathVerse'),{row:null,ambiguous:false});
  assert.deepEqual(C.resolveJump('../MVI0011',rows),{row:null,ambiguous:false});
});
test('MathVision evidence renders source options and independent inspected facts without asserting user approval',()=>{
  const detail={id:'MVI0011',source_dataset:'MathVision',answer:'7',answer_type:'number',original_question:'How many?',original_answer:'7',original_options:['7','8'],verification_data:{verdict:'agent_verified',user_approval:false,explicit_inspected_facts:['18 minus 11 = 7; source answer agrees.']}};
  const e=C.evidence(detail);
  assert.deepEqual(e.originalOptions,['7','8']);assert.match(e.explanation,/18 minus 11/);
  assert.match(e.method,/不等于人工通过/);assert.equal(C.status(detail.verification_data.verdict),'pending');
  assert.equal(e.originalQuestion,'How many?');assert.equal(e.originalAnswer,'7');
});
test('source filter controls and original option view have matching static wiring',()=>{
  const base=path.resolve(__dirname,'../static');const html=fs.readFileSync(path.join(base,'index.html'),'utf8');const app=fs.readFileSync(path.join(base,'app.js'),'utf8');
  for(const id of ['dataset-filter','category-filter','original-choices']){assert.ok(html.includes(`id="${id}"`),id);assert.ok(app.includes(`'${id}'`),id);}
  assert.ok(app.includes("params.set('dataset'"));assert.ok(app.includes("params.set('category'"));
  assert.ok(app.includes("params.get('dataset')"));assert.ok(app.includes("params.get('category')"));
  assert.ok(app.includes('C.resolveJump('));assert.equal(app.includes('MATHVERSE ·'),false);
});
test('MathVision answer_verification, answer_review and answer_check retain explicit computed answers',()=>{
  for(const audit of [
    {answer_verification:{reasoning:'18 − 11 = 7',result:'7',verified:true}},
    {answer_verification:{verified_answer:'7',reason:'Count the remaining cubes.'}},
    {answer_review:{answer:'7',reason:'Same count from a second view.'}},
    {answer_check:{answer:'7',reasoning:'Enumeration gives 7.'}},
  ]){const e=C.evidence({answer:'7',provenance_data:{audit}});assert.equal(e.derived,'7');assert.ok(e.explanation);}
});
test('all pending MathVision entries expose source identity/options and readable verification evidence',(t)=>{
  const root=path.resolve(__dirname,'../..');const index=path.join(root,'review_candidates/mathvision/index.jsonl');
  if(!fs.existsSync(index)){t.skip('MathVision package not installed');return;}
  const rows=fs.readFileSync(index,'utf8').split('\n').filter(line=>line.trim()).map(JSON.parse);
  if(!rows.length){t.skip('No pending MathVision candidates remain');return;}
  assert.equal(new Set(rows.map(row=>row.id)).size,rows.length);
  for(const row of rows){
    const provenance_data=JSON.parse(fs.readFileSync(path.join(root,row.provenance),'utf8'));
    const verification_data=JSON.parse(fs.readFileSync(path.join(root,row.verification),'utf8'));
    const e=C.evidence({...row,provenance_data,verification_data});
    assert.equal(C.dataset(row),'MathVision',row.id);assert.equal(C.status(row.status),'pending',row.id);
    assert.equal(e.originalQuestion,provenance_data.original_record.question,row.id);
    assert.deepEqual(e.originalOptions,provenance_data.original_record.options,row.id);
    assert.notEqual(e.originalAnswer,'未提供',row.id);assert.ok(e.explanation,`${row.id}: missing readable explanation`);
    assert.ok(['solid geometry','transformation geometry','combinatorial geometry'].includes(C.category(row)),row.id);
  }
});
