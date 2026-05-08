"""
日本語プログラミング言語のキーワード定義
"""

class JapaneseKeywords:
    """日本語プログラミング言語のキーワードと対応するPythonコードを管理"""
    
    # 基本キーワードのマッピング
    KEYWORD_MAP = {
        # 制御構文
        'もし': 'if',
        'ならば': ':',
        'そうでなければ': 'else',
        '条件の間': 'while',
        'だけ繰り返す': 'for',
        '繰り返す': 'for',
        
        # 関数
        '関数': 'def',
        'を返す': 'return',
        '返す': 'return',
        
        # 入出力
        '表示する': 'print',
        '読み込む': 'input',
        
        # 演算子
        'と': '+',
        'から': '-',
        'を掛ける': '*',
        'で割る': '/',
        'よりも大きい': '>',
        'よりも小さい': '<',
        'と等しい': '==',
        'と異なる': '!=',
        
        # 論理演算子
        'かつ': 'and',
        'または': 'or',
        'ではない': 'not',
        
        # データ型
        'リスト': 'list',
        '辞書': 'dict',
        '文字列': 'str',
        '整数': 'int',
        '実数': 'float',
    }
    
    # 特殊構文パターン
    PATTERNS = {
        'variable_declaration': r'(.+?)は(.+?)$',
        'if_statement': r'もし(.+?)ならば(.+?)$',
        'else_statement': r'そうでなければ(.+?)$',
        'while_loop': r'(.+?)の間(.+?)$',
        'for_loop': r'(.+?)だけ繰り返す(.+?)$',
        'function_def': r'関数(.+?)は\((.*?)\)を返す(.+?)$',
        'print_statement': r'(.+?)を表示する$',
        'comparison': r'(.+?)(よりも大きい|よりも小さい|と等しい|と異なる)(.+?)$',
    }
    
    @classmethod
    def translate_keyword(cls, japanese_word):
        """日本語キーワードをPythonキーワードに変換"""
        return cls.KEYWORD_MAP.get(japanese_word, japanese_word)
    
    @classmethod
    def is_keyword(cls, word):
        """単語がキーワードかどうかを判定"""
        return word in cls.KEYWORD_MAP
