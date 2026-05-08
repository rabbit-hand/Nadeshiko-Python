"""
なでしこ3互換日本語プログラミング言語モジュール
Pythonでなでしこの全機能を実装
"""

__version__ = "2.0.0"
__author__ = "Nadesiko Compatible Module"

from src.nadesiko_parser import NadesikoParser
from src.nadesiko_keywords import NadesikoKeywords
from src.nadesiko_functions import NadesikoFunctions
from src.nadesiko_gui import NadesikoGUI
from src.nadesiko_file import NadesikoFile
from src.nadesiko_math import NadesikoMath
from src.nadesiko_string import NadesikoString
from src.english_parser import EnglishParser
from src.english_keywords import EnglishKeywords
from src.bilingual_parser import BilingualParser
from src.nadesiko_complete import NadesikoComplete
from src.nadesiko_complete_commands import NadesikoCompleteCommands
from src.parser import JapaneseParser
from src.keywords import JapaneseKeywords

__all__ = [
    'NadesikoParser', 
    'NadesikoKeywords', 
    'NadesikoFunctions',
    'NadesikoGUI',
    'NadesikoFile', 
    'NadesikoMath',
    'NadesikoString',
    'EnglishParser',
    'EnglishKeywords',
    'BilingualParser',
    'NadesikoComplete',
    'NadesikoCompleteCommands',
    'JapaneseParser',
    'JapaneseKeywords'
]
