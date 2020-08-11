"""Tests for row_wise_micro_averaged_f1 functions"""

from evaluations.kaggle_2020 import row_wise_micro_averaged_f1_score
from evaluations.kaggle_2020 import micro_f1_similarity


def test_micro_f1_similarity_all_true():
    """
    All predictions true
    """
    y_true = 'bird1 bird2 bird3 bird4'
    y_pred = 'bird1 bird2 bird3 bird4'
    assert micro_f1_similarity(y_true, y_pred) == 1.


def test_micro_f1_similarity_no_true():
    """
    All predictions false
    """
    y_true = 'bird1 bird2 bird3 bird4'
    y_pred = 'bird6 bird7'
    assert micro_f1_similarity(y_true, y_pred) == 0.


def test_micro_f1_similarity_half_true():
    """
    Half predictions true
    """
    y_true = 'bird1 bird2 bird3 bird4'
    y_pred = 'bird2 bird3 bird6 bird7'
    assert micro_f1_similarity(y_true, y_pred) == 0.5


def test_micro_f1_similarity_one_true():
    """
    One predictions true
    """
    y_true = 'bird1 bird2 bird3 bird4 bird5 bird6'
    y_pred = 'bird1'
    assert round(micro_f1_similarity(y_true, y_pred), 3) == 0.286


def test_micro_f1_similarity_one_true_rest_false():
    """
    One predictions true rest fp
    """
    y_true = 'bird1'
    y_pred = 'bird1 bird2 bird3 bird4 bird5 bird6'
    assert round(micro_f1_similarity(y_true, y_pred), 3) == 0.286


def test_all_true():
    """
    All predictions true
    """
    y_true = [
        'bird1 bird2 bird3 bird4',
        'bird2 bird3',
        'bird2',
    ]
    y_pred = [
        'bird1 bird2 bird3 bird4',
        'bird2 bird3',
        'bird2',
    ]
    assert row_wise_micro_averaged_f1_score(y_true, y_pred) == 1.


def test_all_false():
    """
    All predictions false
    """
    y_true = [
        'bird1 bird2 bird3 bird4',
        'bird2 bird3',
        'bird2',
    ]
    y_pred = [
        'bird5',
        'bird5 bird6',
        'bird7',
    ]
    assert row_wise_micro_averaged_f1_score(y_true, y_pred) == 0.


def test_001():
    """
    Some test 001
    """
    y_true = [
        'bird1 bird2 bird3 bird4',
        'bird1 bird2 bird3 bird4',
        'bird1 bird2 bird3 bird4',
    ]
    y_pred = [
        'bird1 bird2 bird3 bird4',
        'bird6 bird7',
        'bird2 bird3 bird6 bird7',
    ]
    assert row_wise_micro_averaged_f1_score(y_true, y_pred) == 0.5


def test_002():
    """
    Some test 002
    """
    y_true = [
        'bird1 bird2 bird3 bird4 bird5 bird6',
        'bird1',
        'bird1 bird2 bird3 bird4',
    ]
    y_pred = [
        'bird1',
        'bird1 bird2 bird3 bird4 bird5 bird6',
        'bird4 bird5 bird6',
    ]
    assert round(row_wise_micro_averaged_f1_score(y_true, y_pred), 3) == 0.286


def test_003():
    """
    Some test 003
    """
    y_true = [
        'amecro',
        'amecro amerob',
        'nocall',
    ]
    y_pred = [
        'amecro',
        'amecro bird666',
        'nocall',
    ]
    assert round(row_wise_micro_averaged_f1_score(y_true, y_pred), 3) == 0.833
