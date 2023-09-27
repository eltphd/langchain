"""Scoring evaluators.

This module contains evaluators for scoring on a 1-10 the output of models,
be they LLMs, Chains, or otherwise. This can be based on a variety of
criteria and or a reference answer.

Example:
    >>> from langchain.chat_models import ChatOpenAI
    >>> from langchain.evaluation.scoring import PairwiseStringEvalChain
    >>> llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    >>> chain = ScoreStringEvalChain.from_llm(llm=llm)
    >>> result = chain.evaluate_string_pairs(
    ...     input = "What is the chemical formula for water?",
    ...     prediction = "H2O",
    ...     reference = "The chemical formula for water is H2O.",
    ... )
    >>> print(result["text"])
    # {
    #    "score": 8,
    #    "comment": "The response accurately states "
    #    "that the chemical formula for water is H2O."
    #    "However, it does not provide an explanation of what the formula means."
    # }
"""
from langchain.evaluation.scoring.eval_chain import (
    LabeledScoreStringEvalChain,
    ScoreStringEvalChain,
)

__all__ = ["ScoreStringEvalChain", "LabeledScoreStringEvalChain"]