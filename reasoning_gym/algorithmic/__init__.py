"""
Algorithmic tasks for training reasoning capabilities:
- Text processing
- Counting
- Sorting
- Pattern matching
"""

from .base_conversion import BaseConversionConfig, BaseConversionDataset
from .binary_matrix import BinaryMatrixConfig, BinaryMatrixDataset
from .caesar_cipher import CaesarCipherConfig, CaesarCipherDataset
from .group_anagrams import GroupAnagramsConfig, GroupAnagramsDataset
from .isomorphic_strings import IsomorphicStringsConfig, IsomorphicStringsDataset
from .letter_counting import LetterCountingConfig, LetterCountingDataset
from .letter_jumble import LetterJumbleConfig, LetterJumbleDataset
from .manipulate_matrix import ManipulateMatrixConfig, ManipulateMatrixDataset
from .number_filtering import NumberFilteringConfig, NumberFilteringDataset
from .number_sorting import NumberSortingConfig, NumberSortingDataset
from .palindrome_generation import PalindromeConfig, PalindromeDataset
from .ransom_note import RansomNoteConfig, RansomNoteDataset
from .rotate_matrix import RotateMatrixConfig, RotateMatrixDataset
from .sentence_reordering import SentenceReorderingConfig, SentenceReorderingDataset
from .spell_backward import SpellBackwardConfig, SpellBackwardDataset
from .spiral_matrix import SpiralMatrixConfig, SpiralMatrixDataset
from .word_ladder import WordLadderConfig, WordLadderDataset
from .word_sequence_reversal import WordSequenceReversalConfig, WordSequenceReversalDataset
from .word_sorting import TextTransformation, WordSortingConfig, WordSortingDataset

__all__ = [
    "SpellBackwardConfig",
    "SpellBackwardDataset",
    "BaseConversionConfig",
    "BaseConversionDataset",
    "CaesarCipherConfig",
    "CaesarCipherDataset",
    "LetterCountingConfig",
    "LetterCountingDataset",
    "LetterJumbleConfig",
    "LetterJumbleDataset",
    "NumberFilteringConfig",
    "NumberFilteringDataset",
    "NumberSortingConfig",
    "NumberSortingDataset",
    "SentenceReorderingConfig",
    "SentenceReorderingDataset",
    "WordSequenceReversalConfig",
    "WordSequenceReversalDataset",
    "WordSortingConfig",
    "WordSortingDataset",
    "TextTransformation",
    "WordLadderConfig",
    "WordLadderDataset",
    "PalindromeConfig",
    "PalindromeDataset",
    "GroupAnagramsConfig",
    "GroupAnagramsDataset",
    "SpiralMatrixConfig",
    "SpiralMatrixDataset",
    "RansomNoteConfig",
    "RansomNoteDataset",
    "IsomorphicStringsConfig",
    "IsomorphicStringsDataset",
    "RotateMatrixConfig",
    "RotateMatrixDataset",
    "ManipulateMatrixConfig",
    "ManipulateMatrixDataset",
    "BinaryMatrixConfig",
    "BinaryMatrixDataset",
]
