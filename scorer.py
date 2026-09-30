"""Repeatable factual-answer scorer used by ``run_eval.py``.

Each evaluation question already declares a short expected fact in
``questions.py``.  This scorer normalizes capitalization, punctuation, and
whitespace before checking for that fact in the generated answer.  It is
intentionally simple: it makes the existing factual check reproducible while
leaving nuanced judgments, such as whether a citation truly supports a claim,
for manual review.
"""

import re


def _normalize(text: str) -> str:
    """Return comparable lowercase words with punctuation removed."""
    return " ".join(re.findall(r"[a-z0-9]+", text.casefold()))


def judge(question: str, expects: str, answer: str, results) -> bool:
    """Return whether ``answer`` contains the question's expected fact.

    ``question`` and ``results`` are accepted because ``run_eval.py`` defines
    this shared scorer interface; this check only needs ``expects`` and the
    generated ``answer``.
    """
    del question, results
    expected = _normalize(expects)
    return bool(expected) and expected in _normalize(answer)
