"""
なでしこ3パイソンパーサー - 最終完成版
日本語自然言語をPythonコードに変換
"""

import re
import math
import random
import time
import sys
import os
import datetime
from src.nadesiko_keywords import NadesikoKeywords

class NadesikoParser:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self._result = None
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
        
        # 日本語引用符の処理
        line = self._process_japanese_quotes(line)
        
        # 返す処理
        if 'を返す' in line or 'を戻る' in line or 'して返す' in line:
            return self._parse_return(line)
        
        # 「それ」変数の処理
        if 'それ' in line:
            line = line.replace('それ', '_result')
        
        # 表示系
        if any(word in line for word in ['を表示', 'を表示する', 'と言う']):
            return self._parse_print(line)
        
        # 代入系
        if 'は' in line or 'とは' in line or 'に代入' in line:
            return self._parse_assignment(line)
        
        # 条件分岐
        if line.startswith('もし') and 'ならば' in line:
            return self._parse_if(line)
        
        if line.startswith('違えば') or line == '違えば':
            return "else:"
        
        # 繰り返し
        if '繰り返す' in line:
            return self._parse_loop(line)
        
        if '回' in line:
            return self._parse_count_loop(line)
        
        # 関数定義
        if line.startswith('●'):
            return self._parse_function_def(line)
        
        # その他の式
        if any(op in line for op in ['+', '-', '*', '/', '=', '>', '<']):
            return f"_result = {self._translate_expression(line)}"
        
        return line
    
    def _process_japanese_quotes(self, line):
        """日本語引用符を処理"""
        import re
        if '「' in line and '」' in line:
            line = re.sub(r'「([^」]+?)」', r'"\1"', line)
        return line
    
    def _parse_return(self, line):
        """戻り値の処理"""
        if 'して返す' in line:
            value = line.replace('して返す', '').strip()
            if 'と' in value and ('を足す' in value or 'を足' in value):
                if value.endswith('を足す'):
                    core_value = value[:-3]
                    if 'と' in core_value:
                        parts = core_value.split('と')
                        if len(parts) == 2:
                            left = parts[0].strip()
                            right = parts[1].strip()
                            return f"return {left} + {right}"
                else:
                    processed_value = value.replace('と', ' + ').replace('を足', '')
                    return f"return {processed_value}"
            else:
                processed_value = value.replace('と', ' + ').replace('を足す', '').replace('を引く', ' - ')
                return f"return {processed_value}"
        else:
            value = line.replace('を返す', '').replace('を戻る', '').strip()
            return f"return {value}"
    
    def _parse_print(self, line):
        """表示文の処理"""
        content = self._extract_content(line, ['を表示', 'を表示する', 'と言う'])
        if '{' in content and '}' in content:
            return f"print(f{content})"
        else:
            return f"print({content})"
    
    def _parse_assignment(self, line):
        """代入文の処理"""
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
        
        if var == 'それ':
            var = '_result'
        
        # 関数呼び出しの場合
        if '(' in value and ')' in value:
            func_match = re.match(r'(.+?)\((.+?)\)', value)
            if func_match:
                func_name = func_match.group(1).strip()
                args = func_match.group(2).strip()
                if args:
                    if 'と' in args:
                        arg_list = [arg.strip() for arg in args.split('と')]
                        processed_args = ', '.join(arg_list)
                        return f"{var} = {func_name}({processed_args})"
                    else:
                        return f"{var} = {func_name}({args})"
                else:
                    return f"{var} = {func_name}()"
        
        return f"{var} = {self._translate_expression(value)}"
    
    def _parse_if(self, line):
        """if文の処理"""
        condition = line.replace('もし', '').replace('ならば', '').strip()
        return f"if {self._parse_condition(condition)}:"
    
    def _parse_condition(self, condition):
        """条件式の処理"""
        # 比較演算子の変換
        patterns = [
            (r'(.+?)が(.+?)以上', r'\1 >= \2'),
            (r'(.+?)が(.+?)以下', r'\1 <= \2'),
            (r'(.+?)が(.+?)より大きい', r'\1 > \2'),
            (r'(.+?)が(.+?)より小さい', r'\1 < \2'),
            (r'(.+?)が(.+?)と等しい', r'\1 == \2'),
            (r'(.+?)が(.+?)と異なる', r'\1 != \2'),
            (r'(.+?)が(.+?)で割り切れる', r'\1 % \2 == 0'),
            (r'(.+?)が偶数', r'\1 % 2 == 0'),
            (r'(.+?)が奇数', r'\1 % 2 == 1'),
            (r'(.+?)の平方根が(.+?)以下', r'math.sqrt(\1) <= \2'),
        ]
        
        for pattern, replacement in patterns:
            match = re.match(pattern, condition)
            if match:
                return match.expand(replacement)
        
        return self._translate_expression(condition)
    
    def _parse_loop(self, line):
        """繰り返し文の処理"""
        if 'だけ繰り返す' in line:
            count = line.replace('だけ繰り返す', '').strip()
            return f"for _ in range({count}):"
        elif 'の間' in line:
            condition = line.replace('の間', '').strip()
            return f"while {self._parse_condition(condition)}:"
        else:
            return f"for _ in {self._translate_expression(line.replace('繰り返す', '').strip())}:"
    
    def _parse_count_loop(self, line):
        """回数ループの処理"""
        if '回繰り返す' in line:
            count = line.replace('回繰り返す', '').strip()
            return f"for _ in range({count}):"
        elif '回' in line:
            count = line.replace('回', '').strip()
            return f"for _ in range({count}):"
        return line
    
    def _parse_function_def(self, line):
        """関数定義の処理"""
        func_def = line[1:].strip()
        
        if '（' in func_def and '）' in func_def:
            func_name = func_def.split('（')[0].strip()
            params = func_def.split('（')[1].split('）')[0].strip()
            if params:
                if 'と' in params:
                    param_list = [p.strip() for p in params.split('と')]
                else:
                    param_list = [p.strip() for p in params.split('、')]
                return f"def {func_name}({', '.join(param_list)}):"
            else:
                return f"def {func_name}():"
        else:
            return f"def {func_def}():"
    
    def _extract_content(self, line, patterns):
        """内容を抽出"""
        for pattern in patterns:
            if pattern in line:
                return line.replace(pattern, '').strip()
        return line
    
    def _translate_expression(self, expr):
        """式を変換"""
        if not expr:
            return ""
        
        # 演算子の変換
        expr = self._translate_operators(expr)
        
        # 特殊な変数の置換
        replacements = {
            '真': 'True',
            '偽': 'False',
            'パイ': 'math.pi',
            '円周率': 'math.pi',
        }
        
        for jp, py in replacements.items():
            expr = expr.replace(jp, py)
        
        return expr
    
    def _translate_operators(self, expr):
        """演算子を変換"""
        patterns = [
            (r'(.+?)と(.+?)を足す', r'\1 + \2'),
            (r'(.+?)から(.+?)を引く', r'\1 - \2'),
            (r'(.+?)に(.+?)を掛ける', r'\1 * \2'),
            (r'(.+?)を(.+?)で割る', r'\1 / \2'),
            (r'(.+?)を(.+?)で割って返す', r'\1 / \2'),
            (r'(.+?)と(.+?)を掛けて返す', r'\1 * \2'),
            (r'(.+?)から(.+?)を引いて返す', r'\1 - \2'),
            (r'(.+?)の平方根', r'math.sqrt(\1)'),
            (r'(.+?)の文字数', r'len(\1)'),
            (r'左から\((.+?),\s*(.+?)\)', r'\1[:\2]'),
            (r'(.+?)の絶対値', r'abs(\1)'),
        ]
        
        for pattern, replacement in patterns:
            match = re.match(pattern, expr)
            if match:
                return match.expand(replacement)
        
        return expr
    
    def parse_file(self, nadesiko_code):
        """ファイル全体を解析"""
        lines = nadesiko_code.split('\n')
        python_lines = []
        indent_stack = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 元の行のインデントを取得
            original_line = line
            leading_spaces = len(original_line) - len(original_line.lstrip())
            line = line.strip()
            
            python_line = self.parse_line(line)
            
            if python_line.endswith(':'):
                indent_stack.append(leading_spaces)
                python_lines.append(' ' * leading_spaces + python_line)
            elif python_line.startswith('else:') or python_line.startswith('elif '):
                if indent_stack:
                    current_indent = indent_stack[-1]
                python_lines.append(' ' * current_indent + python_line)
            else:
                if indent_stack and leading_spaces <= indent_stack[-1]:
                    while indent_stack and leading_spaces <= indent_stack[-1]:
                        indent_stack.pop()
                
                current_indent = len(indent_stack) * 4
                python_lines.append(' ' * current_indent + python_line)
        
        # 関数定義のインデントを修正
        result_lines = []
        for i, line in enumerate(python_lines):
            if line.strip().startswith('def '):
                # 次の行のインデントを確認
                if i + 1 < len(python_lines):
                    next_line = python_lines[i + 1]
                    if next_line.strip() and not next_line.startswith('    '):
                        # 次の行をインデント
                        python_lines[i + 1] = '    ' + next_line.strip()
            result_lines.append(line)
        
        return '\n'.join(result_lines)
    
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
