"""Tests for accuracy function"""

from evaluations.classification.basic import accuracy


def test_accuracy_all_true():
    """
    All predictions true
    """
    assert accuracy([1, 1, 0, 0], [1, 1, 0, 0]) == 1.


def test_accuracy_half_true():
    """
    50% predictions true
    """
    assert accuracy([1, 1, 0, 0], [1, 0, 1, 0]) == .5


def test_accuracy_no_true():
    """
    No true predictions
    """
    assert accuracy([1, 1, 0, 0], [0, 0, 1, 1]) == 0.
