"""
英語プログラミング言語のキーワード定義
アメリカの子供たちが理解できる自然な英語表現
"""

class EnglishKeywords:
    """英語プログラミング言語のキーワードと対応するPythonコードを管理"""
    
    # 基本キーワードのマッピング
    BASIC_COMMANDS = {
        # 変数代入
        'is': '=',
        'are': '=',
        'be': '=',
        'let': '=',
        'make': '=',
        'set': '=',
        'assign': '=',
        
        # 表示・入力
        'show': 'print',
        'print': 'print',
        'display': 'print',
        'say': 'print',
        'tell': 'print',
        'ask': 'input',
        'get': 'input',
        'read': 'input',
        'input': 'input',
        
        # 計算
        'plus': '+',
        'add': '+',
        'and': '+',  # 文脈により判断
        'minus': '-',
        'subtract': '-',
        'from': '-',
        'times': '*',
        'multiply': '*',
        'by': '*',  # 文脈により判断
        'divided': '/',
        'divide': '/',
        'by': '/',  # 文脈により判断
        'mod': '%',
        'remainder': '%',
        
        # 比較
        'equals': '==',
        'equal': '==',
        'is': '==',  # 文脈により判断
        'are': '==',  # 文脈により判断
        'same': '==',
        'as': '==',
        'not': '!=',
        'different': '!=',
        'greater': '>',
        'more': '>',
        'than': '>',  # 文脈により判断
        'less': '<',
        'smaller': '<',
        'than': '<',  # 文脈により判断
        'greater_equal': '>=',
        'more_equal': '>=',
        'at_least': '>=',
        'less_equal': '<=',
        'at_most': '<=',
        
        # 論理
        'and': 'and',
        'or': 'or',
        'not': 'not',
        
        # 制御構文
        'if': 'if',
        'when': 'if',
        'else': 'else',
        'otherwise': 'else',
        'elif': 'elif',
        'repeat': 'for',
        'loop': 'for',
        'times': 'range',
        'while': 'while',
        'until': 'while',
        'for': 'for',
        'each': 'for',
        'in': 'in',
        'continue': 'continue',
        'break': 'break',
        'stop': 'break',
        'exit': 'break',
        
        # 関数
        'function': 'def',
        'define': 'def',
        'create': 'def',
        'return': 'return',
        'give': 'return',
        'output': 'return',
        'end': 'return',
        
        # データ型
        'list': 'list',
        'array': 'list',
        'dictionary': 'dict',
        'map': 'dict',
        'hash': 'dict',
        'string': 'str',
        'text': 'str',
        'number': 'int',
        'integer': 'int',
        'float': 'float',
        'decimal': 'float',
        'boolean': 'bool',
        'true': 'True',
        'false': 'False',
        
        # システム
        'wait': 'time.sleep',
        'sleep': 'time.sleep',
        'pause': 'time.sleep',
        'stop': 'sys.exit',
        'end': 'sys.exit',
        'quit': 'sys.exit',
        'finish': 'return',
    }
    
    # 英語特有の命令
    ENGLISH_COMMANDS = {
        # 数学
        'absolute': 'abs',
        'sqrt': 'math.sqrt',
        'square_root': 'math.sqrt',
        'sin': 'math.sin',
        'cos': 'math.cos',
        'tan': 'math.tan',
        'int': 'int',
        'decimal_part': 'lambda x: x - int(x)',
        'fraction': 'lambda x: x - int(x)',
        'round': 'round',
        'ceil': 'math.ceil',
        'ceiling': 'math.ceil',
        'floor': 'math.floor',
        'random': 'random.random',
        'rand': 'random.randint',
        'random_int': 'random.randint',
        'power': '**',
        'exponent': '**',
        
        # 文字列操作
        'length': 'len',
        'size': 'len',
        'count': 'len',
        'left': 'str[:]',
        'right': 'str[-:]',
        'middle': 'str[:]',
        'substring': 'str[:]',
        'replace': 'str.replace',
        'find': 'str.find',
        'search': 'str.find',
        'contains': 'in',
        'include': 'in',
        'has': 'in',
        'split': 'str.split',
        'join': 'str.join',
        'upper': 'str.upper',
        'lower': 'str.lower',
        'reverse': 'str[::-1]',
        'uppercase': 'str.upper',
        'lowercase': 'str.lower',
        
        # 配列操作
        'elements': 'len',
        'items': 'len',
        'empty': 'len() == 0',
        'append': 'append',
        'add': 'append',
        'remove': 'remove',
        'delete': 'remove',
        'insert': 'insert',
        'sort': 'sort',
        'order': 'sort',
        'reverse': 'reverse',
        'copy': 'copy',
        'clone': 'copy',
        
        # ファイル操作
        'read_file': 'open().read()',
        'write_file': 'open().write()',
        'exists': 'os.path.exists',
        'create': 'open().close()',
        'delete': 'os.remove',
        'list': 'os.listdir',
        'current_directory': 'os.getcwd',
        'change_directory': 'os.chdir',
        
        # 日時
        'now': 'datetime.datetime.now()',
        'today': 'datetime.datetime.now()',
        'year': 'datetime.datetime.now().year',
        'month': 'datetime.datetime.now().month',
        'day': 'datetime.datetime.now().day',
        'hour': 'datetime.datetime.now().hour',
        'minute': 'datetime.datetime.now().minute',
        'second': 'datetime.datetime.now().second',
        'format': 'datetime.datetime.strftime',
        
        # GUI関連
        'message_box': 'tkinter.messagebox.showinfo',
        'input_box': 'tkinter.simpledialog.askstring',
        'button': 'tkinter.Button',
        'label': 'tkinter.Label',
        'textbox': 'tkinter.Entry',
        'window': 'tkinter.Tk',
        'canvas': 'tkinter.Canvas',
        
        # ネットワーク
        'http_get': 'requests.get',
        'http_post': 'requests.post',
        'download': 'requests.download',
        'open_url': 'urllib.request.urlopen',
        
        # システム
        'run': 'os.system',
        'execute': 'os.system',
        'environment': 'os.environ',
        'command_line': 'sys.argv',
        'platform': 'sys.platform',
    }
    
    # 特殊変数
    SPECIAL_VARIABLES = {
        'it': '_result',      # 直前の計算結果
        'result': '_result',  # 直前の計算結果
        'pi': 'math.pi',      # 円周率
        'e': 'math.e',        # 自然対数の底
        'null': 'None',       # 空っぽ
        'nothing': 'None',    # 空っぽ
        'true': 'True',       # 真
        'false': 'False',      # 偽
        'yes': 'True',        # 真
        'no': 'False',        # 偽
        'on': 'True',         # 真
        'off': 'False',       # 偽
    }
    
    # 文法パターン
    PATTERNS = {
        'variable_assignment': r'(.+?)\s+(is|are|be)\s+(.+)$',
        'let_assignment': r'let\s+(.+?)\s+(be|is)\s+(.+)$',
        'if_statement': r'(if|when)\s+(.+?)\s+(then)?$',
        'else_statement': r'(else|otherwise)$',
        'repeat_times': r'(repeat|loop)\s+(\d+)\s+times$',
        'while_loop': r'(while|until)\s+(.+)$',
        'for_loop': r'(for|each)\s+(.+?)\s+in\s+(.+)$',
        'function_def': r'(function|define)\s+(.+?)\s*\((.+?)\)',
        'print_statement': r'(show|print|display|say|tell)\s+(.+)$',
        'comparison': r'(.+?)\s+(is|are)\s+(.+?)\s+(greater|less|equal|different)\s+than\s+(.+)$',
        'arithmetic': r'(.+?)\s+(plus|minus|times|divided by)\s+(.+)$',
    }
    
    @classmethod
    def translate_command(cls, english_word):
        """英語キーワードをPythonキーワードに変換"""
        return cls.BASIC_COMMANDS.get(english_word, english_word)
    
    @classmethod
    def translate_english_command(cls, command):
        """英語特有命令をPythonに変換"""
        return cls.ENGLISH_COMMANDS.get(command, command)
    
    @classmethod
    def translate_variable(cls, var):
        """特殊変数をPython変数に変換"""
        return cls.SPECIAL_VARIABLES.get(var.lower(), var)
    
    @classmethod
    def is_keyword(cls, word):
        """単語がキーワードかどうかを判定"""
        return word.lower() in cls.BASIC_COMMANDS or word.lower() in cls.ENGLISH_COMMANDS
    
    @classmethod
    def is_special_variable(cls, word):
        """単語が特殊変数かどうかを判定"""
        return word.lower() in cls.SPECIAL_VARIABLES
    
    @classmethod
    def split_by_words(cls, text):
        """英語テキストを単語に分割"""
        import re
        # 単語と演算子を分割
        words = re.findall(r'\w+|[+\-*/=<>!]+|"[^"]*"|\'[^\']*\'|\(|\)|\[|\]|\{|\}', text)
        return words
