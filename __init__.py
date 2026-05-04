"""
なでしこ3互換日本語プログラミング言語モジュール
Pythonでなでしこの全機能を実装
"""

__version__ = "2.0.0"
__author__ = "Nadesiko Compatible Module"

from .nadesiko_parser import NadesikoParser
from .nadesiko_keywords import NadesikoKeywords
from .nadesiko_functions import NadesikoFunctions
from .nadesiko_gui import NadesikoGUI
from .nadesiko_file import NadesikoFile
from .nadesiko_math import NadesikoMath
from .nadesiko_string import NadesikoString
from .english_parser import EnglishParser
from .english_keywords import EnglishKeywords
from .bilingual_parser import BilingualParser
from .nadesiko_complete import NadesikoComplete
from .nadesiko_complete_commands import NadesikoCompleteCommands

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
    'NadesikoCompleteCommands'
]
