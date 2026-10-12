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
test('all packaged candidates retain original text, source values, and available independent solutions',()=>{
  const root=path.resolve(__dirname,'../..');const index=path.join(root,'review_candidates/mathverse/index.jsonl');
  if(!fs.existsSync(index))return;
  const rows=fs.readFileSync(index,'utf8').trim().split('\n').map(JSON.parse);assert.equal(rows.length,731);
  let structured=0,analytic=0;
  for(const row of rows){
    const provenance_data=JSON.parse(fs.readFileSync(path.join(root,row.provenance),'utf8'));
    const verification_data=JSON.parse(fs.readFileSync(path.join(root,row.verification),'utf8'));
    const e=C.evidence({...row,provenance_data,verification_data});
    assert.ok(e.originalQuestion,`${row.id}: missing source question`);assert.notEqual(e.originalAnswer,'未提供',row.id);
    if(provenance_data.audit?.independent_solution?.computed_answer!=null){assert.notEqual(e.derived,'见核验说明',row.id);structured++;}
    if(provenance_data.audit?.answer_verification?.answer!=null){assert.notEqual(e.derived,'见核验说明',row.id);analytic++;}
    assert.ok(e.explanation,`${row.id}: missing verification explanation`);
  }
  assert.ok(structured>100);assert.ok(analytic>100);
});
