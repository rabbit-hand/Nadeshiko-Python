"""
なでしこ3互換パーサー
助詞区切りの法則に基づいた日本語構文をPythonコードに変換
"""

import re
import math
import random
import time
import sys
import os
import datetime
from nadesiko_keywords import NadesikoKeywords

class NadesikoParser:
    """なでしこ3互換のパーサー"""
    
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self._result = None  # 「それ」用の変数
        self.indent_level = 0
        self.imports = set()
        
    def parse_line(self, line):
        """一行のなでしこコードをPythonコードに変換"""
        line = line.strip()
        if not line or line.startswith('#'):
            return line
        
        # コメント処理
        if '//' in line:
            line = line.split('//')[0].strip()
        
        # 助詞で分割
        words = NadesikoKeywords.split_by_particles(line)
        
        # 基本パターンのマッチング
        python_code = self._match_patterns(line, words)
        
        return python_code if python_code else line
    
    def _match_patterns(self, original_line, words):
        """なでしこの文法パターンをマッチング"""
        
        # 表示系: 「〜を表示」「〜と言う」
        if any(word in original_line for word in ['を表示', 'を表示する', 'と言う', 'と言う']):
            content = self._extract_content(original_line, ['を表示', 'を表示する', 'と言う', 'と言う'])
            return f"print({self._translate_expression(content)})"
        
        # 代入系: 「AはB」「AとはB」「AにBを代入」
        if 'は' in original_line or 'とは' in original_line or 'に代入' in original_line:
            return self._parse_assignment(original_line)
        
        # もし文: 「もし〜ならば」
        if original_line.startswith('もし') and 'ならば' in original_line:
            condition = original_line.replace('もし', '').replace('ならば', '').strip()
            return f"if {self._parse_condition(condition)}:"
        
        # 違えば: 「違えば」
        if original_line.startswith('違えば') or original_line == '違えば':
            return "else:"
        
        # 条件分岐: 「〜ならば」
        if original_line.endswith('ならば') and not original_line.startswith('もし'):
            condition = original_line.replace('ならば', '').strip()
            return f"elif {self._parse_condition(condition)}:"
        
        # 繰り返し系
        if '繰り返す' in original_line:
            return self._parse_loop(original_line)
        
        # 間ループ: 「〜の間」
        if 'の間' in original_line:
            condition = original_line.replace('の間', '').strip()
            return f"while {self._parse_condition(condition)}:"
        
        # 回数ループ: 「〜回」「〜回繰り返す」
        if '回' in original_line:
            return self._parse_count_loop(original_line)
        
        # 反復: 「〜を反復」「〜から〜まで反復」
        if 'を反復' in original_line:
            if 'から' in original_line and 'まで' in original_line:
                # 「AからBまで反復」パターン
                match = re.match(r'(.+?)から(.+?)までを反復', original_line)
                if match:
                    start = self._translate_expression(match.group(1))
                    end = self._translate_expression(match.group(2))
                    return f"for _ in range(int({start}), int({end}) + 1):"
            iterable = original_line.replace('を反復', '').strip()
            return f"for _ in {self._translate_expression(iterable)}:"
        
        # 関数定義: 「●関数名」
        if original_line.startswith('●'):
            return self._parse_function_def(original_line)
        
        # 返す: 「〜を返す」「〜を戻る」
        if 'を返す' in original_line or 'を戻る' in original_line:
            value = original_line.replace('を返す', '').replace('を戻る', '').strip()
            return f"return {self._translate_expression(value)}"
        
        # 終了: 「終了」「終わる」
        if original_line in ['終了', '終わる']:
            return "sys.exit()"
        
        # 待つ: 「〜秒待つ」
        if '秒待つ' in original_line:
            seconds = original_line.replace('秒待つ', '').strip()
            return f"time.sleep({self._translate_expression(seconds)})"
        
        # 入力: 「〜を尋ねる」「〜を入力」
        if 'を尋ねる' in original_line or 'を入力' in original_line:
            prompt = original_line.replace('を尋ねる', '').replace('を入力', '').strip()
            return f"input({self._translate_expression(prompt)})"
        
        # 演算子を含む式の処理
        if any(op in original_line for op in ['と', 'から', 'を掛け', 'で割', '足す', '引く']):
            return self._parse_expression(original_line)
        
        # その他の式
        return self._parse_expression(original_line)
    
    def _parse_assignment(self, line):
        """代入文の解析"""
        if 'に代入' in line:
            var, value = line.split('に代入', 1)
        elif 'とは' in line:
            var, value = line.split('とは', 1)
        elif 'は' in line:
            parts = line.split('は', 1)
            if len(parts) == 2:
                var, value = parts
            else:
                return line
        else:
            return line
        
        var = var.strip()
        value = value.strip()
        
        # 特殊変数の処理
        if var == 'それ':
            var = '_result'
        
        return f"{var} = {self._parse_expression(value)}"
    
    def _parse_loop(self, line):
        """繰り返し文の解析"""
        if 'だけ繰り返す' in line:
            count = line.replace('だけ繰り返す', '').strip()
            return f"for _ in range({self._translate_expression(count)}):"
        else:
            return f"for _ in {self._translate_expression(line.replace('繰り返す', '').strip())}:"
    
    def _parse_count_loop(self, line):
        """回数ループの解析"""
        if '回繰り返す' in line:
            count = line.replace('回繰り返す', '').strip()
            return f"for _ in range({self._translate_expression(count)}):"
        elif '回' in line:
            count = line.replace('回', '').strip()
            return f"for _ in range({self._translate_expression(count)}):"
        return line
    
    def _parse_function_def(self, line):
        """関数定義の解析"""
        func_def = line[1:].strip()  # ●を削除
        
        if '（' in func_def and '）' in func_def:
            # 引数あり
            func_name = func_def.split('（')[0].strip()
            params = func_def.split('（')[1].split('）')[0].strip()
            if params:
                # 「と」で区切られた引数を処理
                if 'と' in params:
                    param_list = [p.strip() for p in params.split('と')]
                else:
                    param_list = [p.strip() for p in params.split('、')]
                return f"def {func_name}({', '.join(param_list)}):"
            else:
                return f"def {func_name}():"
        else:
            # 引数なし
            return f"def {func_def}():"
    
    def _extract_content(self, line, patterns):
        """パターンに基づいて内容を抽出"""
        for pattern in patterns:
            if pattern in line:
                return line.replace(pattern, '').strip()
        return line
    
    def _parse_expression(self, expr):
        """式を解析してPythonコードに変換"""
        if not expr:
            return ""
        
        # 演算子の処理
        expr = self._translate_operators(expr)
        
        # その他の変換処理
        return self._translate_expression(expr)
    
    def _translate_operators(self, expr):
        """演算子を変換"""
        # 正規表現でより正確にパターンマッチング
        import re
        
        # 「AとBを足す」パターン
        match = re.match(r'(.+?)と(.+?)を足す', expr)
        if match:
            return f"{match.group(1)} + {match.group(2)}"
        
        # 「AとB」パターン（足すがない場合）
        match = re.match(r'(.+?)と(.+?)$', expr)
        if match and len(expr.split('と')) == 2:
            return f"{match.group(1)} + {match.group(2)}"
        
        # 「AからBを引く」パターン
        match = re.match(r'(.+?)から(.+?)を引く', expr)
        if match:
            return f"{match.group(1)} - {match.group(2)}"
        
        # 「AからB」パターン
        match = re.match(r'(.+?)から(.+?)$', expr)
        if match and len(expr.split('から')) == 2:
            return f"{match.group(1)} - {match.group(2)}"
        
        # 「AにBを掛ける」パターン
        match = re.match(r'(.+?)に(.+?)を掛ける', expr)
        if match:
            return f"{match.group(1)} * {match.group(2)}"
        
        # 「AをBで割る」パターン
        match = re.match(r'(.+?)を(.+?)で割る', expr)
        if match:
            return f"{match.group(1)} / {match.group(2)}"
        
        # 基本的な置換（フォールバック）
        replacements = [
            ('と', ' + '),
            ('から', ' - '),
            ('を掛ける', ' * '),
            ('で割る', ' / '),
        ]
        
        for japanese, python_op in replacements:
            expr = expr.replace(japanese, python_op)
        
        return expr
    
    def _parse_condition(self, condition):
        """条件式を解析してPythonコードに変換"""
        if not condition:
            return ""
        
        # 比較演算子の処理
        condition = self._translate_comparison_operators(condition)
        
        # その他の式処理
        return self._parse_expression(condition)
    
    def _translate_comparison_operators(self, condition):
        """比較演算子を変換"""
        import re
        
        # 「AがB以上」パターン
        match = re.match(r'(.+?)が(.+?)以上', condition)
        if match:
            return f"{match.group(1)} >= {match.group(2)}"
        
        # 「AがB以下」パターン
        match = re.match(r'(.+?)が(.+?)以下', condition)
        if match:
            return f"{match.group(1)} <= {match.group(2)}"
        
        # 「AがBより大きい」パターン
        match = re.match(r'(.+?)が(.+?)より大きい', condition)
        if match:
            return f"{match.group(1)} > {match.group(2)}"
        
        # 「AがBより小さい」パターン
        match = re.match(r'(.+?)が(.+?)より小さい', condition)
        if match:
            return f"{match.group(1)} < {match.group(2)}"
        
        # 「AがBと等しい」パターン
        match = re.match(r'(.+?)が(.+?)と等しい', condition)
        if match:
            return f"{match.group(1)} == {match.group(2)}"
        
        # 「AがBと異なる」パターン
        match = re.match(r'(.+?)が(.+?)と異なる', condition)
        if match:
            return f"{match.group(1)} != {match.group(2)}"
        
        # 「AがB」パターン（単純な等価）
        match = re.match(r'(.+?)が(.+?)$', condition)
        if match and len(condition.split('が')) == 2:
            return f"{match.group(1)} == {match.group(2)}"
        
        # 基本的な置換
        replacements = [
            ('以上', '>='),
            ('以下', '<='),
            ('より大きい', '>'),
            ('より小さい', '<'),
            ('と等しい', '=='),
            ('と異なる', '!='),
            ('が', '=='),
        ]
        
        for japanese, python_op in replacements:
            condition = condition.replace(japanese, python_op)
        
        return condition
    
    def _translate_expression(self, expr):
        """式をPython式に変換"""
        if not expr:
            return ""
        
        # 特殊変数の置換
        expr = NadesikoKeywords.translate_variable(expr)
        
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
        
        # なでしこ命令の置換
        for nadesiko, python in NadesikoKeywords.NADESIKO_COMMANDS.items():
            if nadesiko in expr:
                expr = expr.replace(nadesiko, python)
                self._add_import_if_needed(python)
        
        # 基本命令の置換
        for nadesiko, python in NadesikoKeywords.BASIC_COMMANDS.items():
            expr = expr.replace(nadesiko, python)
        
        # 括弧の調整（なでしこの全角括弧を半角に）
        expr = expr.replace('（', '(').replace('）', ')')
        expr = expr.replace('［', '[').replace('］', ']')
        expr = expr.replace('｛', '{').replace('｝', '}')
        
        # 文字列リテラルの処理
        if not (expr.startswith('"') and expr.endswith('"')) and \
           not (expr.startswith("'") and expr.endswith("'")) and \
           not expr.startswith('f"') and \
           not expr.startswith("f'") and \
           not expr.isdigit() and \
           not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', expr) and \
           not any(op in expr for op in ['+', '-', '*', '/', '>', '<', '=', '!', 'and', 'or', 'not']):
            expr = f'"{expr}"'
        
        return expr.strip()
    
    def _add_import_if_needed(self, python_code):
        """必要なimportを追加"""
        if 'math.' in python_code:
            self.imports.add('import math')
        if 'random.' in python_code:
            self.imports.add('import random')
        if 'time.' in python_code:
            self.imports.add('import time')
        if 'sys.' in python_code:
            self.imports.add('import sys')
        if 'os.' in python_code:
            self.imports.add('import os')
        if 'datetime.' in python_code:
            self.imports.add('import datetime')
        if 'tkinter.' in python_code:
            self.imports.add('import tkinter')
        if 'requests.' in python_code:
            self.imports.add('import requests')
        if 'urllib.' in python_code:
            self.imports.add('import urllib.request')
    
    def parse_file(self, nadesiko_code):
        """なでしこコード全体をPythonコードに変換"""
        lines = nadesiko_code.split('\n')
        python_lines = []
        indent_stack = []
        
        # import文の追加
        for imp in sorted(self.imports):
            python_lines.append(imp)
        
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
    
    def execute(self, nadesiko_code):
        """なでしこコードを実行"""
        python_code = self.parse_file(nadesiko_code)
        print(f"変換されたPythonコード:\n{python_code}\n")
        print("実行結果:")
        
        # 実行環境の準備
        exec_globals = {
            '_result': self._result,
            'math': math,
            'random': random,
            'time': time,
            'sys': sys,
            'os': os,
            'datetime': datetime,
        }
        
        try:
            exec(python_code, exec_globals)
            self._result = exec_globals.get('_result')
        except Exception as e:
            print(f"エラー: {e}")
