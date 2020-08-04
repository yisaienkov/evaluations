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
    y_pred : str

    Returns
    -------
    float
        Word level Jaccard similarity
    """
    true_set = set(y_true.lower().split())
    pred_set = set(y_pred.lower().split())
    y_intersect = true_set.intersection(pred_set)
    return len(y_intersect) / (len(true_set) + len(pred_set) - len(y_intersect))
