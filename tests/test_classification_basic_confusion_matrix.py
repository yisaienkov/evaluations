"""Tests for confusion_matrix_binary function"""

from evaluations.classification.basic import confusion_matrix_binary


def test_all_tp():
    """
    All tp
    """
    result = confusion_matrix_binary([1, 1, 1], [1, 1, 1])
    answer = {'tp': 3, 'tn': 0, 'fp': 0, 'fn': 0}
    assert result == answer


def test_all_tn():
    """
    All tn
    """
    result = confusion_matrix_binary([0, 0, 0], [0, 0, 0])
    answer = {'tp': 0, 'tn': 3, 'fp': 0, 'fn': 0}
    assert result == answer


def test_all_fp():
    """
    All fp
    """
    result = confusion_matrix_binary([0, 0, 0], [1, 1, 1])
    answer = {'tp': 0, 'tn': 0, 'fp': 3, 'fn': 0}
    assert result == answer


def test_all_fn():
    """
    All fn
    """
    result = confusion_matrix_binary([1, 1, 1], [0, 0, 0])
    answer = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 3}
    assert result == answer


def test_all_types():
    """
    All types
    """
    result = confusion_matrix_binary([1, 1, 0, 0], [1, 0, 0, 1])
    answer = {'tp': 1, 'tn': 1, 'fp': 1, 'fn': 1}
    assert result == answer
