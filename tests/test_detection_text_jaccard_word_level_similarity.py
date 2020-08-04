"""Tests for jaccard_word_level_similarity function"""

from evaluations.detection.text import jaccard_word_level_similarity


def test_all_true():
    """
    100% similarity
    """
    assert jaccard_word_level_similarity(
        "Hello, how are you?",
        "Hello, how are you?"
    ) == 1.


def test_half_true():
    """
    50% similarity
    """
    assert jaccard_word_level_similarity(
        "Be happy my friend",
        "be happy"
    ) == 0.5


def test_no_true():
    """
    No similarity
    """
    assert jaccard_word_level_similarity(
        "It's good.",
        "Have a nice day!"
    ) == 0.
