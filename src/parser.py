"""
日本語プログラミング言語のパーサー
日本語構文をPythonコードに変換する
"""

import re
from keywords import JapaneseKeywords

class JapaneseParser:
    """日本語プログラミング言語のパーサー"""
    
    def __init__(self):
        self.indent_level = 0
        self.python_code = []
        
    def parse_line(self, line):
        """一行の日本語コードをPythonコードに変換"""
        line = line.strip()
        if not line or line.startswith('#'):
            return line
        
        # 関数定義: 「関数名は(引数)を返す」 - 最初にチェック
        if line.startswith('関数') and 'を返す' in line:
            # より正確な正規表現でマッチング
            match = re.match(r'関数(.+?)は\((.*?)\)を返す$', line)
            if match:
                func_name = match.group(1).strip()
                params = match.group(2).strip()
                # パラメータ内の「と」を「,」に変換
                params = params.replace('と', ', ')
                return f"def {func_name}({params}):"
        
        # print文: 「値を表示する」
        if line.endswith('を表示する'):
            value = line.replace('を表示する', '').strip()
            return f"print({self._translate_expression(value)})"
        
        # input文: 「読み込む」
        if line.endswith('を読み込む'):
            prompt = line.replace('を読み込む', '').strip()
            return f"input({self._translate_expression(prompt)})"
        
        # 変数宣言: 「変数名は値」
        if 'は' in line and not any(keyword in line for keyword in ['ならば', 'の間', 'だけ', 'を返す']):
            # より正確なマッチング
            match = re.match(r'(.+?)は(.+)$', line)
            if match:
                var_name = match.group(1).strip()
                value = match.group(2).strip()
                return f"{var_name} = {self._translate_expression(value)}"
        
        # if文: 「もし条件ならば」
        if line.startswith('もし') and 'ならば' in line:
            condition = line.replace('もし', '').replace('ならば', '').strip()
            python_condition = self._translate_expression(condition)
            return f"if {python_condition}:"
        
        # else文: 「そうでなければ」
        if line.startswith('そうでなければ'):
            return "else:"
        
        # whileループ: 「条件の間」
        if 'の間' in line:
            # より正確なマッチング
            match = re.match(r'(.+?)の間$', line)
            if match:
                condition = match.group(1).strip()
                python_condition = self._translate_expression(condition)
                return f"while {python_condition}:"
        
        # forループ: 「回数だけ繰り返す」
        if 'だけ繰り返す' in line:
            match = re.match(r'(.+?)だけ繰り返す$', line)
            if match:
                count = match.group(1)
                return f"for _ in range({self._translate_expression(count)}):"
        
        # return文: 「返す 値」
        if line.startswith('返す') or line.endswith('を返す'):
            if line.startswith('返す'):
                value = line.replace('返す', '').strip()
            else:
                value = line.replace('を返す', '').strip()
            return f"return {self._translate_expression(value)}"
        
        # その他の式
        return self._translate_expression(line)
    
    def _translate_expression(self, expr):
        """式をPythonコードに変換"""
        if not expr:
            return ""
        
        # 日本語の特殊関数呼び出しを処理
        # 〜の長さ -> len(〜)
        if 'の長さ' in expr:
            expr = re.sub(r'([^\s]+)の長さ', r'len(\1)', expr)
        
        # 〜の平方根 -> math.sqrt(〜)
        if 'の平方根' in expr:
            expr = re.sub(r'([^\s]+)の平方根', r'math.sqrt(\1)', expr)
        
        # 〜の絶対値 -> abs(〜)
        if 'の絶対値' in expr:
            expr = re.sub(r'([^\s]+)の絶対値', r'abs(\1)', expr)
        
        # 日本語引用符の処理（先に行う）
        if expr.startswith('「') and expr.endswith('」'):
            content = expr[1:-1]  # 「と」を削除
            # f文字列の処理
            if '{' in content and '}' in content:
                expr = f'f"{content}"'
            else:
                expr = f'"{content}"'
        elif expr.startswith('「') or expr.endswith('」'):
            # 片方だけの場合は通常の文字列として処理
            expr = expr.replace('「', '"').replace('」', '"')
        
        # 関数呼び出し内の「と」を「,」に変換（関数名(引数)パターン）
        import re
        # より単純なパターンで関数呼び出しを検出
        func_match = re.match(r'([^()]+?)\((.*?)\)', expr)
        if func_match:
            func_name = func_match.group(1).strip()
            params = func_match.group(2).strip()
            # 数値間の「と」を「, 」に変換
            params = re.sub(r'(\d+)と(\d+)', r'\1, \2', params)
            # 変数間の「と」も「, 」に変換
            params = re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)と([a-zA-Z_][a-zA-Z0-9_]*)', r'\1, \2', params)
            # 日本語引用符で囲まれた文字列を処理
            params = re.sub(r'「([^」]+)」', r'"\1"', params)
            expr = f"{func_name}({params})"
        
        # 比較演算子の置換（先に行う）
        expr = expr.replace('よりも大きい', ' > ')
        expr = expr.replace('よりも小さい', ' < ')
        expr = expr.replace('と等しい', ' == ')
        expr = expr.replace('と異なる', ' != ')
        
        # 「が」の置換は比較演算子としてのみ使用
        # 文字列内や関数内では置換しない
        if not (expr.startswith('"') and expr.endswith('"')) and not (expr.startswith("'") and expr.endswith("'")):
            # 特定のパターンでのみ「が」を「==」に置換
            import re
            expr = re.sub(r'(\w+)が(\w+)', r'\1 == \2', expr)
        
        # 論理演算子の置換
        expr = expr.replace('かつ', ' and ')
        expr = expr.replace('または', ' or ')
        expr = expr.replace('ではない', ' not ')
        
        # 算術演算子の置換（文字列内は除外）
        if not (expr.startswith('"') and expr.endswith('"')) and not (expr.startswith("'") and expr.endswith("'")):
            expr = expr.replace('と', ' + ')
        expr = expr.replace('から', ' - ')
        expr = expr.replace('を掛ける', ' * ')
        expr = expr.replace('で割る', ' / ')
        
        # キーワードの置換
        for japanese, python in JapaneseKeywords.KEYWORD_MAP.items():
            expr = expr.replace(japanese, python)
        
        return expr.strip()
    
    def parse_file(self, japanese_code):
        """日本語コード全体をPythonコードに変換"""
        lines = japanese_code.split('\n')
        python_lines = []
        indent_stack = []
        
        for line in lines:
            original_line = line
            line = line.rstrip()
            
            if not line.strip():
                python_lines.append('')
                continue
            
            # インデントの処理
            current_indent = len(line) - len(line.lstrip())
            line = line.strip()
            
            # Pythonコードに変換
            python_line = self.parse_line(line)
            
            # インデント調整
            if python_line.endswith(':'):
                indent_stack.append(current_indent)
                python_lines.append(' ' * current_indent + python_line)
            elif python_line.startswith('else:') or python_line.startswith('elif '):
                if indent_stack:
                    current_indent = indent_stack[-1]
                python_lines.append(' ' * current_indent + python_line)
            else:
                if indent_stack and current_indent <= indent_stack[-1]:
                    while indent_stack and current_indent <= indent_stack[-1]:
                        indent_stack.pop()
                
                actual_indent = len(indent_stack) * 4
                python_lines.append(' ' * actual_indent + python_line)
        
        return '\n'.join(python_lines)
    
    def execute(self, japanese_code):
        """日本語コードを実行"""
        python_code = self.parse_file(japanese_code)
        print(f"変換されたPythonコード:\n{python_code}\n")
        print("実行結果:")
        exec(python_code, globals())
