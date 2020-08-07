"""Tests for jaccard_word_level_score function"""

from evaluations.text_extraction import jaccard_word_level_score


def test_1():
    """
    50% predictions true
    """
    assert jaccard_word_level_score(
        [
            "Hello, how are you?",
            "Be happy my friend",
            "It's good.",
        ],
        [
            "Hello, how are you?",
            "be happy",
            "Have a nice day!"
        ]
    ) == .5
