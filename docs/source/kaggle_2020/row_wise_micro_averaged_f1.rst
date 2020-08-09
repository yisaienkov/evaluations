Row-Wise Micro Averaged F1
==========================

The metric for Kaggle Competition
`Cornell Birdcall Identification
<https://www.kaggle.com/c/birdsong-recognition/overview>`_

For each row we compute number of True Positives (TP), False Positives (FP) and
False Negatives (FN) predictions.

For example, if true label is "bird1 bird2", and we predict "bird2 bird3 bird4",
then we have:

- TP = 1 (bird2)
- FP = 2 (bird3, bird4)
- FN = 1 (bird1)

Then we calculate F1 score by the next formula:

.. math::
    F1\ Score = \frac{2 * TP}{2*TP + FN + FP}

At the end we compute mean by all row scores.


Row-Wise Micro Averaged F1 Score
--------------------------------

.. autofunction:: evaluations.kaggle_2020.row_wise_micro_averaged_f1.row_wise_micro_averaged_f1_score


Micro F1 Similarity
--------------------------------

.. autofunction:: evaluations.kaggle_2020.row_wise_micro_averaged_f1.micro_f1_similarity