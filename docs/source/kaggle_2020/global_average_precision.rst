Global Average Precision
========================

The metric for Kaggle Competition
`Google Landmark Recognition 2020
<https://www.kaggle.com/c/landmark-recognition-2020/overview>`_

Global Average Precision Score
------------------------------

N  predictions (label/confidence pairs) sorted in descending order by their confidence scores, then the Global Average Precision is computed as:

.. math::
    GAP = \frac{1}{M}\sum_{i=1}^{N}P(i)rel(i)

- N is the total number of predictions returned by the system, across all queries
- M is the total number of queries with at least one sample from the training set visible in it (note that some queries may not depict samples)
- P(i) is the precision at rank i. (example: consider rank 3 - we have already made 3 predictions, and 2 of them are correct. Then P(3) will be 2/3)
- rel(i) denotes the relevance of prediciton i: it’s 1 if the i-th prediction is correct, and 0 otherwise

.. autofunction:: evaluations.kaggle_2020.global_average_precision.global_average_precision_score
