"""The module for text detection tasks"""

from .jaccard_word_level import jaccard_word_level_similarity
from .jaccard_word_level import jaccard_word_level_score

__all__ = [
    'jaccard_word_level_similarity',
    'jaccard_word_level_score',
]
