"""Tests for global_average_precision_score function"""

from evaluations.kaggle_2020 import global_average_precision_score


def test_all_true():
    """
    All predictions true
    """
    y_true = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
    }
    y_pred = {
        '1': (1, 0.9),
        '2': (2, 0.4),
        '3': (3, 0.5),
        '4': (4, 0.8),
    }
    assert global_average_precision_score(y_true, y_pred) == 1.


def test_all_false():
    """
    All predictions false
    """
    y_true = {
        '1': 5,
        '2': 5,
        '3': 5,
        '4': 5,
    }
    y_pred = {
        '1': (1, 0.9),
        '2': (2, 0.4),
        '3': (3, 0.5),
        '4': (4, 0.8),
    }
    assert global_average_precision_score(y_true, y_pred) == 0.


def test_best_is_false():
    """
    Best prediction is false
    """
    y_true = {
        '1': 5,
        '2': 2,
        '3': 3,
        '4': 4,
    }
    y_pred = {
        '1': (1, 0.9),
        '2': (2, 0.4),
        '3': (3, 0.5),
        '4': (4, 0.8),
    }
    assert global_average_precision_score(y_true, y_pred) == 0.47916666666666663


def test_missing_predictions():
    """
    Only one prediction from 4
    """
    y_true = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
    }
    y_pred = {
        '2': (2, 0.4),
    }
    assert global_average_precision_score(y_true, y_pred) == .25


def test_no_targets_correct():
    """
    Test situation with no target and no prediction for this target
    """
    y_true = {
        '1': 1,
        '2': None,
        '3': None,
        '4': 4,
    }
    y_pred = {
        '1': (1, 0.4),
        '4': (4, 0.2),
    }
    assert global_average_precision_score(y_true, y_pred) == 1.


def test_no_targets_incorrect():
    """
    Test situation with no target and incorrect prediction for one target
    """
    y_true = {
        '1': 1,
        '2': None,
        '3': None,
        '4': 4,
    }
    y_pred = {
        '1': (1, 0.4),
        '2': (2, 0.8),
        '4': (4, 0.2),
    }
    assert global_average_precision_score(y_true, y_pred) == 0.5833333333333333


def test_001():
    """
    Some test 001
    """
    y_true = {
        '1': 1,
        '2': None,
        '3': None,
        '4': 4,
        'another_4': 4,
        'too_4': 4,
        'i_am_4': 4,
    }
    y_pred = {
        '1': (1, 0.4),
        '2': (2, 0.8),
        '4': (4, 0.2),
        'another_4': (4, 0.9),
        'too_4': (5, 0.7)
    }
    assert global_average_precision_score(y_true, y_pred) == 0.42000000000000004


def test_002():
    """
    Some test 002
    """
    y_true = {
        'id_001': 123,
        'id_002': None,
        'id_003': 999,
        'id_004': 123,
        'id_005': 999,
        'id_006': 888,
        'id_007': 666,
        'id_008': 666,
        'id_009': None,
        'id_010': 666,
    }
    y_pred = {
        'id_002': (123, 0.10),
        'id_001': (123, 0.15),
        'id_003': (999, 0.30),
        'id_005': (999, 0.40),
        'id_007': (555, 0.60),
        'id_008': (666, 0.70),
        'id_010': (666, 0.99),
    }
    assert global_average_precision_score(y_true, y_pred) == 0.5479166666666666
