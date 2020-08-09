"""Row-wise micro averaged F1 score for Cornell Birdcall Identification
https://www.kaggle.com/c/birdsong-recognition/overview"""

from typing import List


def row_wise_micro_averaged_f1_score(
        y_true: List[str],
        y_pred: List[str]
) -> float:
    """
    Compute row-wise micro averaged f1 score

    Parameters
    ----------
    y_true : List[str]
        Target list of strings of a space separated birds names
    y_pred : List[str]
        Predicted list of strings of a space separated birds names

    Returns
    -------
    float
        Row-wise micro averaged F1 score

    Examples
    --------
    >>> from evaluations.kaggle_2020 import row_wise_micro_averaged_f1_score
    >>> y_true = [
    ...         'amecro',
    ...         'amecro amerob',
    ...         'nocall',
    ...     ]
    >>> y_pred = [
    ...         'amecro',
    ...         'amecro bird666',
    ...         'nocall',
    ...     ]
    >>> row_wise_micro_averaged_f1_score(y_true, y_pred)
    0.8333333333333333
    """
    n_rows = len(y_true)
    f1_score = 0.
    for true_row, predicted_row in zip(y_true, y_pred):
        f1_score += micro_f1_similarity(true_row, predicted_row) / n_rows
    return f1_score


def micro_f1_similarity(
        y_true: str,
        y_pred: str
) -> float:
    """
    Compute micro f1 similarity for 1 row

    Parameters
    ----------
    y_true : str
        True string of a space separated birds names
    y_pred : str
        Predicted string of a space separated birds names

    Returns
    -------
    float
        Micro F1 similarity

    Examples
    --------
    >>> from evaluations.kaggle_2020 import micro_f1_similarity
    >>> y_true = 'amecro amerob'
    >>> y_pred = 'amecro bird666'
    >>> micro_f1_similarity(y_true, y_pred)
    0.5
    """
    true_labels = y_true.split()
    pred_labels = y_pred.split()

    true_pos, false_pos, false_neg = 0, 0, 0

    for true_elem in true_labels:
        if true_elem in pred_labels:
            true_pos += 1
        else:
            false_neg += 1

    for pred_el in pred_labels:
        if pred_el not in true_labels:
            false_pos += 1

    f1_similarity = 2 * true_pos / (2 * true_pos + false_neg + false_pos)

    return f1_similarity
