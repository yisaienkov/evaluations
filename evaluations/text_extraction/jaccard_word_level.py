"""This is module for compute Jaccard indexes for texts"""

from typing import List

__all__ = [
    'jaccard_word_level_similarity',
    'jaccard_word_level_score',
]


def jaccard_word_level_score(y_true: List[str], y_pred: List[str]) -> float:
    """
    Compute word level Jaccard score

    Parameters
    ----------
    y_true : List of str
        True labels
    y_pred : List of str
        Predicted labels

    Returns
    -------
    float:
        Word level Jaccard score

    Examples
    --------
    >>> from evaluations.text_extraction import jaccard_word_level_score
    >>> jaccard_word_level_score(
    ...         [
    ...             "Hello, how are you?",
    ...             "Be happy my friend",
    ...             "It's good.",
    ...         ],
    ...         [
    ...             "Hello, how are you?",
    ...             "be happy",
    ...             "Have a nice day!"
    ...         ]
    ...     )
    0.5
    """
    score = 0.
    for i, j in zip(y_true, y_pred):
        score += jaccard_word_level_similarity(i, j) / len(y_true)
    return score


def jaccard_word_level_similarity(y_true: str, y_pred: str) -> float:
    """
    Compute word level Jaccard similarity

    Parameters
    ----------
    y_true : str
        True text
    y_pred : str
        Predicted text

    Returns
    -------
    float
        Word level Jaccard similarity

    Examples
    --------
    >>> from evaluations.text_extraction import jaccard_word_level_similarity
    >>> assert jaccard_word_level_similarity(
    ...         "Be happy my friend",
    ...         "be happy"
    ...     )
    0.5
    """
    true_set = set(y_true.lower().split())
    pred_set = set(y_pred.lower().split())
    y_intersect = true_set.intersection(pred_set)
    return len(y_intersect) / (len(true_set) + len(pred_set) - len(y_intersect))
