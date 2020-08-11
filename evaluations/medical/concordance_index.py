"""This is module for compute the Concordance index"""

from typing import List

__all__ = [
    'concordance_index'
]


def concordance_index(
        events: List[int],
        risks: List[float]
) -> float:
    """
    Compute Concordance index (C-index)

    The concordance index is a value between 0 and 1 where:

    - 1.0 - all risk scores for happened events higher than for unhappened,
    - 0.0 - all risk scores for unhappened events higher than for happened,
    - 0.5 - random risk scores.

    The formula is:

    .. math::
        C\\mbox{-}Index = \\frac{n\\_concordant\\_pairs +
        0.5 * n\\_risk\\_ties}{n\\_permissible\\_pairs}

    where:

    - n_concordant_pairs - number of permissible pairs where the score is
      bigger for the event with label 1 than 0
    - n_risk_ties - number of permissible pairs with equal scores
    - n_permissible_pairs - number of pairs with different events

    Parameters
    ----------
    events : List[int]
        If the some event happened - 1 or not happened - 0
    risks : List[int]
        Risks scores for each event

    Returns
    -------
    float
        Concordance index

    Examples
    --------
    >>> from evaluations.medical import concordance_index
    >>> events = [1, 0, 1, 1, 0]
    >>> risks = [0.8, 0.43, 0.62, 0.58, 0.62]
    >>> concordance_index(events, risks)
    0.75
    """
    n_permissible_pairs = 0
    n_concordant_pairs = 0
    n_risk_ties = 0
    for i in range(len(events) - 1):
        for j in range(i + 1, len(events)):
            if events[i] == events[j]:
                continue
            n_permissible_pairs += 1
            if events[i] and risks[i] > risks[j]:
                n_concordant_pairs += 1
            elif events[j] and risks[j] > risks[i]:
                n_concordant_pairs += 1
            elif risks[i] == risks[j]:
                n_risk_ties += 1

    return (n_concordant_pairs + 0.5 * n_risk_ties) / n_permissible_pairs
