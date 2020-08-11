"""Tests for concordance_index function"""

from evaluations.medical import concordance_index


def test_ai4medical_prognosis():
    """
    Test from AI for Medical Prognosis course
    """
    events = [1, 0, 1, 1, 0]
    risks = [0.8, 0.43, 0.62, 0.58, 0.62]
    assert concordance_index(events, risks) == .75


def test_best_model():
    """
    Good predictions
    """
    events = [1, 0, 1, 1, 0, 0]
    risks = [0.99, 0.01, 0.99, 0.99, 0.01, 0.01]
    assert concordance_index(events, risks) == 1.


def test_bad_model():
    """
    Bad predictions
    """
    events = [1, 0, 1, 1, 0, 0]
    risks = [0.01, 0.99, 0.01, 0.01, 0.99, 0.99]
    assert concordance_index(events, risks) == 0.


def test_lazy_model():
    """
    Equals predictions
    """
    events = [1, 0, 1, 1, 0, 0]
    risks = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    assert concordance_index(events, risks) == 0.5
