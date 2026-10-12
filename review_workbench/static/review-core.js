/* Pure review helpers. No DOM, network or decisions. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.ReviewCore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const status = value => ['passed', 'deleted'].includes(value) ? value : 'pending';
  const branch = row => row.branch || row.subject || '';
  const branchLabel = value => ({PlaneGeometry:'平面几何',SolidGeometry:'立体几何',Analytics:'函数 / 解析'}[value] || value || '未分类');
  const string = value => value == null ? '' : typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value);
  const filter = (rows, settings) => {
    const query = (settings.query || '').trim().toLowerCase();
    return rows.filter(row => (settings.status === 'all' || status(row.status) === settings.status) &&
      (settings.branch === 'all' || branch(row) === settings.branch) &&
      (!query || [row.id,row.title,row.question,row.source_key,row.legacy_id,row.source_problem_index].some(value => string(value).toLowerCase().includes(query))));
  };
  function nextAfter(rows, id, available) {
    const index = rows.findIndex(row => row.id === id);
    const ids = new Set(available.map(row => row.id));
    for (let i = index + 1; i < rows.length; i++) if (ids.has(rows[i].id) && rows[i].id !== id) return rows[i].id;
    for (let i = Math.min(index - 1, rows.length - 1); i >= 0; i--) if (ids.has(rows[i].id) && rows[i].id !== id) return rows[i].id;
    return available.find(row => row.id !== id)?.id || null;
  }
  function evidence(detail) {
    const provenance = detail.provenance_data || {};
    const audit = provenance.audit || {};
    const check = audit.secondary_answer_check || {};
    const consistency = detail.answer_consistency || {};
    const verification = detail.verification_data || {};
    const independent = typeof audit.independent_solution === 'object' && audit.independent_solution ? audit.independent_solution : {};
    const answerVerification = typeof audit.answer_verification === 'object' && audit.answer_verification ? audit.answer_verification : {};
    const numericVerification = verification['answer_verification.json'] || {};
    const calculation = answerVerification.calculation || {};
    const calculationText = calculation.formula ? `${calculation.formula} = ${string(calculation.unrounded_value)}${calculation.unit ? ' ' + calculation.unit : ''}${calculation.rounding_decimal_places != null ? `; rounded to ${calculation.rounding_decimal_places} decimal places` : ''}.` : '';
    const originalAnswer = detail.original_answer ?? detail.source_answer ?? provenance.source?.original_answer ?? audit.source_answer ?? audit.original_answer;
    const originalValue = detail.source_answer_value;
    const candidateValue = detail.candidate_answer_value ?? detail.choices?.[string(detail.answer)];
    const derived = detail.verified_answer ?? audit.independently_computed_result ?? check.independent_derivation_value ?? independent.computed_answer ?? answerVerification.answer ?? answerVerification.canonical_answer ?? calculation.answer ?? audit.computed_answer ?? audit.verified_answer ?? numericVerification.theorem_result;
    let derivedText = derived == null ? '见核验说明' : string(derived);
    if (detail.choices?.[derivedText]) derivedText += ` · ${string(detail.choices[derivedText])}`;
    else if (numericVerification.answer_check?.unique && numericVerification.answer_check.matching_options?.length === 1) {
      const letter = numericVerification.answer_check.matching_options[0];
      derivedText = `${letter} · ${string(detail.choices?.[letter] ?? derivedText)}${typeof derived === 'number' ? ` ≈ ${Number(derived.toPrecision(10))}` : ''}`;
    }
    const explanation = detail.verification_explanation || (typeof audit.independent_solution === 'string' ? audit.independent_solution : independent.method || independent.derivation) || answerVerification.derivation || calculationText || audit.independent_derivation || audit.derivation || audit.verification_reason || numericVerification.method || '';
    const adaptations = Array.isArray(audit.adaptations) ? audit.adaptations.map(item => typeof item === 'string' ? item : item.reason || item.note || string(item)).join('\n') : '';
    const adaptation = detail.adaptation_notes || audit.adaptation_reason || audit.adaptation_notes || audit.correction_reason || (typeof audit.adaptation === 'string' ? audit.adaptation : audit.adaptation?.reason) || adaptations;
    return {
      originalAnswer: originalAnswer == null ? '未提供' : string(originalAnswer) + (originalValue != null && string(originalValue) !== string(originalAnswer) ? ` · ${string(originalValue)}` : ''),
      candidateAnswer: string(detail.answer) + (candidateValue != null && string(candidateValue) !== string(detail.answer) ? ` · ${string(candidateValue)}` : ''),
      derived: derivedText,
      originalQuestion: detail.original_question ?? detail.source_question ?? provenance.source?.original_question ?? audit.source_question ?? audit.original_question ?? '',
      consistency: typeof consistency === 'string' ? consistency : consistency.status || 'unknown',
      reason: typeof consistency === 'object' ? consistency.reason || '' : '',
      method: answerVerification.method || answerVerification.status || (typeof audit.answer_verification === 'string' ? audit.answer_verification : '') || check.method || numericVerification.method || '',
      explanation: string(explanation),
      adaptation: string(adaptation) || (detail.differences?.question_changed || detail.differences?.answer_changed ? '题干或答案与来源记录有变化。请核对下方原始题目和核验记录。' : '未记录实质性题干或答案改编。图片按原题重新绘制。'),
      record: {answer_consistency:consistency, differences:detail.differences || {}, audit, verification}
    };
  }
  function compactSummary(rows, supplied) {
    const counts = {total:rows.length,pending:0,passed:0,deleted:0};
    rows.forEach(row => counts[status(row.status)]++);
    return {...counts,...supplied};
  }
  return {status,branch,branchLabel,string,filter,nextAfter,evidence,compactSummary};
});
