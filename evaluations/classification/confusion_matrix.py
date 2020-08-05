"""The module for compute confusion matrix' components"""

from typing import List, Dict

__all__ = [
    'confusion_matrix_binary'
]


def confusion_matrix_binary(
        y_true: List[int],
        y_pred: List[int]
) -> Dict[str, int]:
    """
    Compute tp, tn, fp, fn

    Parameters
    ----------
    y_true : list of ints
        True labels
    y_pred : list os ints
        Predicted labels

    Returns
    -------
    Dict[str, int]
        Dictionary with number of samples of tp, tn, fp, fn

    Examples
    --------
    >>> from evaluations.classification.basic import confusion_matrix_binary
    >>> confusion_matrix_binary([1, 1, 0, 0], [1, 0, 0, 1])
    {'tp': 1, 'tn': 1, 'fp': 1, 'fn': 1}
    """
    true_pos, true_neg, false_pos, false_neg = 0, 0, 0, 0
    for el_true, el_pred in zip(y_true, y_pred):
        if el_true and el_pred:
            true_pos += 1
        elif not el_true and not el_pred:
            true_neg += 1
        elif el_true and not el_pred:
            false_neg += 1
        elif not el_true and el_pred:
            false_pos += 1

    return {'tp': true_pos, 'tn': true_neg, 'fp': false_pos, 'fn': false_neg}
