"""
日本語・英語バイリンガルプログラミング言語パーサー
なでしこ3互換の日本語と、アメリカの子供たちが理解できる英語の両方をサポート
"""

import re
from nadesiko_parser import NadesikoParser
from english_parser import EnglishParser
from nadesiko_keywords import NadesikoKeywords
from english_keywords import EnglishKeywords

class BilingualParser:
    """日本語・英語バイリンガルプログラミング言語のパーサー"""
    
    def __init__(self):
        self.nadesiko_parser = NadesikoParser()
        self.english_parser = EnglishParser()
        self.language_mode = 'auto'  # 'auto', 'japanese', 'english'
        
    def detect_language(self, code):
        """コードの言語を自動検出"""
        lines = code.split('\n')
        japanese_count = 0
        english_count = 0
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # 日本語の特徴を検出
            if any(char in line for char in ['は', 'を', 'が', 'の', 'に', 'へ', 'で', 'から', 'まで', 'と', 'や', 'など']):
                japanese_count += 1
            
            # 英語の特徴を検出
            if any(word in line.lower() for word in ['is', 'are', 'be', 'let', 'show', 'print', 'if', 'when', 'for', 'while']):
                english_count += 1
            
            # なでしこ特有の表現
            if any(pattern in line for pattern in ['ならば', '違えば', '繰り返す', '●']):
                japanese_count += 2
            
            # 英語特有の表現
            if any(pattern in line.lower() for pattern in ['times', 'than', 'each', 'function', 'define']):
                english_count += 2
        
        if japanese_count > english_count:
            return 'japanese'
        elif english_count > japanese_count:
            return 'english'
        else:
            return 'japanese'  # デフォルトは日本語
    
    def parse_line(self, line):
        """一行のコードを解析"""
        if self.language_mode == 'auto':
            # 行単位で言語を判定
            if self._is_japanese_line(line):
                return self.nadesiko_parser.parse_line(line)
            else:
                return self.english_parser.parse_line(line)
        elif self.language_mode == 'japanese':
            return self.nadesiko_parser.parse_line(line)
        elif self.language_mode == 'english':
            return self.english_parser.parse_line(line)
        else:
            return line
    
    def _is_japanese_line(self, line):
        """行が日本語かどうかを判定"""
        line = line.strip()
        if not line:
            return True
        
        # 日本語のひらがな、カタカナ、漢字を含むか
        japanese_chars = set('ひらがなカタカナ漢字０１２３４５６７８９')
        has_japanese = any(char in japanese_chars for char in line)
        
        # 日本語の助詞を含むか
        particles = ['は', 'を', 'が', 'の', 'に', 'へ', 'で', 'から', 'まで', 'と', 'や']
        has_particle = any(particle in line for particle in particles)
        
        # なでしこ特有の表現
        nadesiko_patterns = ['ならば', '違えば', '繰り返す', '反復', '●', 'を表示', 'を足す', 'から引く']
        has_nadesiko = any(pattern in line for pattern in nadesiko_patterns)
        
        # 英語の単語が少ない場合
        english_words = ['is', 'are', 'be', 'let', 'show', 'print', 'if', 'when', 'for', 'while', 'times', 'than']
        english_count = sum(1 for word in english_words if word in line.lower())
        
        return has_japanese or has_particle or has_nadesiko or english_count == 0
    
    def parse_file(self, code):
        """コード全体を解析"""
        # 言語モードの決定
        if self.language_mode == 'auto':
            detected_lang = self.detect_language(code)
        else:
            detected_lang = self.language_mode
        
        # 対応するパーサーで処理
        if detected_lang == 'japanese':
            return self.nadesiko_parser.parse_file(code)
        else:
            return self.english_parser.parse_file(code)
    
    def execute(self, code):
        """コードを実行"""
        # 言語モードの決定
        if self.language_mode == 'auto':
            detected_lang = self.detect_language(code)
            lang_name = '日本語' if detected_lang == 'japanese' else '英語'
        else:
            detected_lang = self.language_mode
            lang_name = '日本語' if detected_lang == 'japanese' else '英語'
        
        print(f"検出された言語: {lang_name}")
        
        # 対応するパーサーで実行
        if detected_lang == 'japanese':
            return self.nadesiko_parser.execute(code)
        else:
            return self.english_parser.execute(code)
    
    def set_language_mode(self, mode):
        """言語モードを設定"""
        if mode in ['auto', 'japanese', 'english']:
            self.language_mode = mode
        else:
            raise ValueError("言語モードは 'auto', 'japanese', 'english' のいずれかである必要があります")
    
    def get_supported_keywords(self):
        """サポートされているキーワードの一覧を取得"""
        return {
            'japanese': {
                'basic': list(NadesikoKeywords.BASIC_COMMANDS.keys()),
                'nadesiko': list(NadesikoKeywords.NADESIKO_COMMANDS.keys()),
                'variables': list(NadesikoKeywords.SPECIAL_VARIABLES.keys())
            },
            'english': {
                'basic': list(EnglishKeywords.BASIC_COMMANDS.keys()),
                'english': list(EnglishKeywords.ENGLISH_COMMANDS.keys()),
                'variables': list(EnglishKeywords.SPECIAL_VARIABLES.keys())
            }
        }
    
    def translate_code(self, code, target_lang):
        """コードを別の言語に翻訳"""
        current_lang = self.detect_language(code)
        
        if current_lang == target_lang:
            return code
        
        # 一度Pythonに変換してから、ターゲット言語の文法で再構築
        if current_lang == 'japanese':
            python_code = self.nadesiko_parser.parse_file(code)
        else:
            python_code = self.english_parser.parse_file(code)
        
        # Pythonコードをターゲット言語に変換（簡易実装）
        if target_lang == 'japanese':
            return self._python_to_japanese(python_code)
        else:
            return self._python_to_english(python_code)
    
    def _python_to_japanese(self, python_code):
        """Pythonコードを日本語に変換（簡易実装）"""
        translations = {
            'print(': '「',
            '=': 'は',
            '+': 'と足す',
            '-': 'から引く',
            '*': 'を掛ける',
            '/': 'で割る',
            'if ': 'もし',
            'else:': '違えば',
            'for ': '繰り返す',
            'while ': 'の間',
            'def ': '●',
            'return ': '返す',
        }
        
        result = python_code
        for python, japanese in translations.items():
            result = result.replace(python, japanese)
        
        return result
    
    def _python_to_english(self, python_code):
        """Pythonコードを英語に変換（簡易実装）"""
        translations = {
            'print(': 'show ',
            '=': 'is',
            '+': 'plus',
            '-': 'minus',
            '*': 'times',
            '/': 'divided by',
            'if ': 'if ',
            'else:': 'else',
            'for ': 'for ',
            'while ': 'while ',
            'def ': 'function ',
            'return ': 'return ',
        }
        
        result = python_code
        for python, english in translations.items():
            result = result.replace(python, english)
        
        return result
