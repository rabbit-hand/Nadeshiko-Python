"""
なでしこ3互換日本語プログラミング言語モジュール
Pythonでなでしこの全機能を実装
"""

__version__ = "2.0.0"
__author__ = "Nadesiko Compatible Module"

from src.parser import JapaneseParser
from src.keywords import JapaneseKeywords

__all__ = [
    'JapaneseParser',
    'JapaneseKeywords'
]
