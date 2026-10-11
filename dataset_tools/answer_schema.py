"""Canonical answer categories and explicit letter-to-option mappings."""
from __future__ import annotations

import math
import re

ANSWER_TYPES = frozenset({'choice', 'number', 'expression', 'text'})


def extract_choices(question):
    """Read the existing Choices: A:... or Choices: (A)... notation verbatim."""
    heading = re.search(r'\bchoices?\s*:\s*', question, flags=re.IGNORECASE)
    if heading is None:
        return {}
    tail = question[heading.end():].strip()
    if tail.endswith(r'\]'):
        tail = tail[:-2].rstrip()
    labels = list(re.finditer(r'^\s*([A-Z])\s*:', tail, flags=re.MULTILINE))
    if not labels:
        labels = list(re.finditer(r'\(([A-Z])\)', tail))
    if len(labels) < 2 or tail[:labels[0].start()].strip():
        raise ValueError('Cannot parse the question options unambiguously')
    letters = [label.group(1) for label in labels]
    if letters != [chr(ord('A') + i) for i in range(len(letters))]:
        raise ValueError('Choice letters must be consecutive and unique, beginning with A')
    choices = {label.group(1): tail[label.end():labels[i + 1].start() if i + 1 < len(labels) else None].strip()
               for i, label in enumerate(labels)}
    if not all(choices.values()):
        raise ValueError('Every choice requires its option text')
    return choices


def option_letter(answer, choices, *, answer_is_option_text):
    """Never confuse option text such as 'a' with a pre-existing letter answer."""
    if answer_is_option_text:
        matches = [letter for letter, value in choices.items() if value == answer]
        if len(matches) != 1:
            raise ValueError('The accepted answer must match exactly one option')
        return matches[0]
    if not isinstance(answer, str) or answer not in choices:
        raise ValueError('The accepted choice answer is not a valid option letter')
    return answer


def validate_answer(row):
    qid = row.get('id', '<unknown>')
    kind, answer = row.get('answer_type'), row.get('answer')
    if kind not in ANSWER_TYPES:
        raise ValueError(f'{qid}: unsupported answer_type {kind!r}')
    if not isinstance(row.get('question'), str) or not row['question'].strip():
        raise ValueError(f'{qid}: question must be nonempty text')
    if (type(answer) not in (str, int, float) or
            isinstance(answer, str) and not answer.strip() or
            isinstance(answer, float) and not math.isfinite(answer)):
        raise ValueError(f'{qid}: answer must be nonempty text or a finite number')
    parsed = extract_choices(row['question'])
    if kind == 'choice':
        if not parsed or row.get('choices') != parsed:
            raise ValueError(f'{qid}: choices must match the options in the question')
        if not isinstance(answer, str) or answer not in parsed:
            raise ValueError(f'{qid}: choice answers must contain only one option letter')
    elif parsed or 'choices' in row:
        raise ValueError(f'{qid}: a question with options must use answer_type="choice"')
    elif kind in ('expression', 'text') and not isinstance(answer, str):
        raise ValueError(f'{qid}: {kind} answers must be text')
