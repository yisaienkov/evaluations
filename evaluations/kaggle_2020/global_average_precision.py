"""Global Average Precision for Google Landmark Recognition 2020
https://www.kaggle.com/c/landmark-recognition-2020/overview"""

from typing import Dict, Tuple, Any


def global_average_precision_score(
        y_true: Dict[Any, Any],
        y_pred: Dict[Any, Tuple[Any, float]]
) -> float:
    """
    Compute Global Average Precision score (GAP)

    Parameters
    ----------
    y_true : Dict[Any, Any]
        Dictionary with query ids and true ids for query samples
    y_pred : Dict[Any, Tuple[Any, float]]
        Dictionary with query ids and predictions (predicted id, confidence
        level)

    Returns
    -------
    float
        GAP score

    Examples
    --------
    >>> from evaluations.kaggle_2020 import global_average_precision_score
    >>> y_true = {
    ...         'id_001': 123,
    ...         'id_002': None,
    ...         'id_003': 999,
    ...         'id_004': 123,
    ...         'id_005': 999,
    ...         'id_006': 888,
    ...         'id_007': 666,
    ...         'id_008': 666,
    ...         'id_009': None,
    ...         'id_010': 666,
    ...     }
    >>> y_pred = {
    ...         'id_001': (123, 0.15),
    ...         'id_002': (123, 0.10),
    ...         'id_003': (999, 0.30),
    ...         'id_005': (999, 0.40),
    ...         'id_007': (555, 0.60),
    ...         'id_008': (666, 0.70),
    ...         'id_010': (666, 0.99),
    ...     }
    >>> global_average_precision_score(y_true, y_pred)
    0.5479166666666666
    """
    indexes = list(y_pred.keys())
    indexes.sort(
        key=lambda x: -y_pred[x][1],
    )
    queries_with_target = len([i for i in y_true.values() if i is not None])
    correct_predictions = 0
    total_score = 0.
    for i, k in enumerate(indexes, 1):
        relevance_of_prediction_i = 0
        if y_true[k] == y_pred[k][0]:
            correct_predictions += 1
            relevance_of_prediction_i = 1
        precision_at_rank_i = correct_predictions / i
        total_score += precision_at_rank_i * relevance_of_prediction_i

    return 1 / queries_with_target * total_score
