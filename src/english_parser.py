"""
英語プログラミング言語のパーサー
アメリカの子供たちが理解できる自然な英語構文をPythonコードに変換
"""

import re
import math
import random
import time
import sys
import os
import datetime
try:
    from .english_keywords import EnglishKeywords
    from .os_commands import os_commands
    from .error_handler import error_handler
    from .performance_optimizer import performance_optimizer, measure_time, cache_result
    from .macro_system import macro_system, start_macro_recording, stop_macro_recording, play_macro, create_simple_macro
except ImportError:
    from english_keywords import EnglishKeywords
    from os_commands import os_commands
    from error_handler import error_handler
    from performance_optimizer import performance_optimizer, measure_time, cache_result
    from macro_system import macro_system, start_macro_recording, stop_macro_recording, play_macro, create_simple_macro

class EnglishParser:
    """英語プログラミング言語のパーサー"""
    
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self._result = None  # 「it」「result」用の変数
        self.indent_level = 0
        self.imports = set()
        
    def parse_line(self, line):
        """一行の英語コードをPythonコードに変換"""
        line = line.strip()
        if not line or line.startswith('#'):
            return line
        
        # コメント処理
        if '//' in line:
            line = line.split('//')[0].strip()
        
        # 基本パターンのマッチング
        python_code = self._match_english_patterns(line)
        
        # Pythonコードとして認識された場合はそのまま返す
        if python_code and python_code != line:
            return python_code
        
        # それ以外は式として処理（ただし既にPythonコードの場合はそのまま返す）
        if line.startswith(('print(', 'if ', 'else:', 'elif ', 'for ', 'while ', 'def ', 'return ', 'import ', 'from ')):
            return line
        
        return self._parse_expression(line)
    
    def _match_english_patterns(self, line):
        """英語の文法パターンをマッチング"""
        
        # 表示系: 「show ~」「print ~」「display ~」
        if any(word in line.lower() for word in ['show ', 'print ', 'display ', 'say ', 'tell ']):
            return self._parse_print_statement(line)
        
        # 関数呼び出しの処理（代入系の前）
        if '(' in line and ')' in line and not line.startswith(('if ', 'elif ', 'while ', 'for ')):
            func_match = re.match(r'(.+?)\s*=\s*(.+?)\((.+?)\)', line)
            if func_match:
                var = func_match.group(1).strip()
                func_name = func_match.group(2).strip()
                args = func_match.group(3).strip()
                if args:
                    return f"{var} = {func_name}({args})"
                else:
                    return f"{var} = {func_name}()"
        
        # 代入系: 「A is 10」「Let A be 10」「A are 10」
        if re.search(r'\b(is|are|be)\b', line) and not any(word in line.lower() for word in [' if ', ' when ', ' than ']):
            return self._parse_assignment(line)
        
        # Let代入: 「Let A be 10」
        if line.lower().startswith('let '):
            return self._parse_let_assignment(line)
        
        # if文: 「If A is greater than 10」「When A > 10」
        if line.lower().startswith('if ') or line.lower().startswith('when '):
            return self._parse_if_statement(line)
        
        # else文: 「else」「otherwise」
        if line.lower() in ['else', 'otherwise']:
            return "else:"
        
        # elif文: 「elif」「else if」
        if line.lower().startswith('elif ') or line.lower().startswith('else if '):
            return self._parse_elif_statement(line)
        
        # OSコマンド実行
        if any(word in line.lower() for word in ['command ', 'execute ', 'run ']):
            return self._parse_os_command(line)
        
        # ファイル操作
        if any(word in line.lower() for word in ['read ', 'write ', 'create ', 'delete ', 'copy ', 'move ']):
            return self._parse_file_operation(line)
        
        # ディレクトリ操作
        if any(word in line.lower() for word in ['directory ', 'folder ']):
            return self._parse_directory_operation(line)
        
        # システム情報
        if any(word in line.lower() for word in ['system info', 'os info', 'current directory']):
            return self._parse_system_info(line)
        
        # マクロ機能
        if any(word in line.lower() for word in ['macro', 'record', 'play', 'execute']):
            return self._parse_macro(line)
        
        # return文
        if any(word in line.lower() for word in ['return ', 'give back ', 'send back ']):
            return self._parse_return(line)
        
        # 条件分岐
        if line.lower().startswith('if ') and ' then' in line.lower():
            return self._parse_if(line)
        
        if line.lower().startswith('else') or line.lower() == 'else':
            return "else:"
        
        if line.lower().startswith('elif '):
            return self._parse_elif(line)
        
        # 繰り返し
        if 'repeat ' in line.lower() and ' times' in line.lower():
            return self._parse_repeat(line)
        
        if 'for ' in line.lower() and ' in ' in line.lower():
            return self._parse_for_loop(line)
        
        if 'while ' in line.lower():
            return self._parse_while_loop(line)
        
        # 関数定義
        if line.lower().startswith('function '):
            return self._parse_function_def(line)
        
        # return文: 「return value」「give back value」
        if any(word in line.lower() for word in ['return ', 'give ', 'output ']):
            return self._parse_return_statement(line)
        
        # 繰り返し系
        if any(word in line.lower() for word in ['repeat ', 'loop ', 'times']):
            return self._parse_repeat_loop(line)
        
        # whileループ: 「While condition」「Until condition」
        if line.lower().startswith('while ') or line.lower().startswith('until '):
            return self._parse_while_loop(line)
        
        # forループ: 「For each item in list」「For item in list」
        if line.lower().startswith('for ') or line.lower().startswith('each '):
            return self._parse_for_loop(line)
        
        # 関数定義: 「Function name(x, y)」「Define name with (x and y)」
        if line.lower().startswith('function ') or line.lower().startswith('define '):
            return self._parse_function_def(line)
        
        # return文: 「return value」「give back value」
        if any(word in line.lower() for word in ['return ', 'give ', 'output ']):
            return self._parse_return_statement(line)
        
        # 終了: 「stop」「end」「quit」
        if line.lower() in ['stop', 'end', 'quit', 'finish']:
            return "sys.exit()"
        
        # 待つ: 「wait 5 seconds」「sleep 5」
        if any(word in line.lower() for word in ['wait ', 'sleep ', 'pause ']):
            return self._parse_wait_statement(line)
        
        # 入力: 「ask question」「get input」
        if any(word in line.lower() for word in ['ask ', 'get ', 'read ', 'input ']):
            return self._parse_input_statement(line)
        
        # その他の式
        return self._parse_expression(line)
    
    def _parse_print_statement(self, line):
        """表示文の解析"""
        patterns = [
            (r'^show\s+(.+)$', 'show'),
            (r'^print\s+(.+)$', 'print'),
            (r'^display\s+(.+)$', 'display'),
            (r'^say\s+(.+)$', 'say'),
            (r'^tell\s+(.+)$', 'tell'),
        ]
        
        for pattern, keyword in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                content = match.group(1).strip()
                # 単純な変数名の場合は直接使用
                if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', content):
                    return f"print({content})"
                else:
                    # 式を処理
                    return f"print({content})"
        
        return line
    
    def _parse_assignment(self, line):
        """代入文の解析"""
        # 「A is 10」「A are 10」「A be 10」
        patterns = [
            r'(.+?)\s+is\s+(.+)$',
            r'(.+?)\s+are\s+(.+)$',
            r'(.+?)\s+be\s+(.+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                var, value = match.groups()
                var = var.strip()
                value = value.strip()
                
                if var.lower() in ['it']:
                    var = '_result'
                
                # 関数呼び出しの場合
                if '(' in value and ')' in value:
                    func_match = re.match(r'(.+?)\((.+?)\)', value)
                    if func_match:
                        func_name = func_match.group(1).strip()
                        args = func_match.group(2).strip()
                        if args:
                            return f"{var} = {func_name}({args})"
                        else:
                            return f"{var} = {func_name}()"
                
                return f"{var} = {self._parse_expression(value)}"
        
        return line
    
    def _parse_let_assignment(self, line):
        """Let代入文の解析"""
        # 「Let A be 10」「Let A is 10」
        patterns = [
            r'let\s+(.+?)\s+be\s+(.+)$',
            r'let\s+(.+?)\s+is\s+(.+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                var, value = match.groups()
                var = var.strip()
                value = value.strip()
                
                if var.lower() in ['it']:
                    var = '_result'
                
                return f"{var} = {self._parse_expression(value)}"
        
        return line
    
    def _parse_if_statement(self, line):
        """if文の解析"""
        # 「If A is greater than 10」「When A > 10」
        if line.lower().startswith('if '):
            condition = line[3:].strip()
        elif line.lower().startswith('when '):
            condition = line[5:].strip()
        else:
            return line
        
        return f"if {self._parse_condition(condition)}:"
    
    def _parse_elif_statement(self, line):
        """elif文の解析"""
        if line.lower().startswith('elif '):
            condition = line[5:].strip()
        elif line.lower().startswith('else if '):
            condition = line[8:].strip()
        else:
            return line
        
        return f"elif {self._parse_condition(condition)}:"
    
    def _parse_repeat_loop(self, line):
        """繰り返し文の解析"""
        # 「Repeat 5 times」「Loop 3 times」
        patterns = [
            r'(repeat|loop)\s+(\d+)\s+times$',
            r'(repeat|loop)\s+(\d+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                count = match.group(2)
                return f"for _ in range(int({count})):"
        
        return line
    
    def _parse_while_loop(self, line):
        """whileループの解析"""
        if line.lower().startswith('while '):
            condition = line[6:].strip()
            return f"while {self._parse_condition(condition)}:"
        elif line.lower().startswith('until '):
            condition = line[6:].strip()
            return f"while not ({self._parse_condition(condition)}):"
        
        return line
    
    def _parse_for_loop(self, line):
        """forループの解析"""
        # 「For each item in list」「For item in list」
        patterns = [
            r'for\s+each\s+(.+?)\s+in\s+(.+)$',
            r'for\s+(.+?)\s+in\s+(.+)$',
            r'each\s+(.+?)\s+in\s+(.+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                var, iterable = match.groups()
                var = var.strip()
                iterable = iterable.strip()
                return f"for {var} in {self._parse_expression(iterable)}:"
        
        return line
    
    def _parse_function_def(self, line):
        """関数定義の解析"""
        # 「Function name(x, y)」「Define name with (x and y)」
        patterns = [
            r'function\s+(\w+)\s*\((.+?)\)$',
            r'define\s+(\w+)\s+with\s*\((.+?)\)$',
            r'define\s+(\w+)\s*\((.+?)\)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                func_name, params = match.groups()
                func_name = func_name.strip()
                params = params.strip()
                
                if params:
                    # 「and」で区切られた引数を処理
                    if ' and ' in params:
                        param_list = [p.strip() for p in params.split(' and ')]
                    else:
                        param_list = [p.strip() for p in params.split(',')]
                    return f"def {func_name}({', '.join(param_list)}):"
                else:
                    return f"def {func_name}():"
        
        return line
    
    def _parse_return_statement(self, line):
        """return文の解析"""
        patterns = [
            r'return\s+(.+)$',
            r'give\s+(.+)$',
            r'give back\s+(.+)$',
            r'output\s+(.+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                value = match.group(1).strip()
                return f"return {self._parse_expression(value)}"
        
        # 引数なでしこのreturn
        if line.lower() in ['return', 'give', 'give back', 'output']:
            return "return"
        
        return line
    
    def _parse_wait_statement(self, line):
        """wait文の解析"""
        # 「wait 5 seconds」「sleep 5」「pause 2 seconds」
        patterns = [
            r'(wait|sleep|pause)\s+(\d+)\s+seconds?$',
            r'(wait|sleep|pause)\s+(\d+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                seconds = match.group(2)
                return f"time.sleep(int({seconds}))"
        
        return line
    
    def _parse_input_statement(self, line):
        """入力文の解析"""
        # 「ask question」「get input」「read text」
        patterns = [
            r'ask\s+(.+)$',
            r'get\s+(.+)$',
            r'read\s+(.+)$',
            r'input\s+(.+)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                prompt = match.group(1).strip()
                return f"input({self._parse_expression(prompt)})"
        
        return line
    
    def _parse_condition(self, condition):
        """条件式の解析"""
        import re
        
        # 比較演算子の変換
        condition = self._translate_comparison_operators(condition)
        
        # 論理演算子の変換
        condition = condition.replace(' and ', ' and ')
        condition = condition.replace(' or ', ' or ')
        condition = condition.replace(' not ', ' not ')
        
        return condition
    
    def _translate_comparison_operators(self, condition):
        """比較演算子を変換"""
        import re
        
        # 「A is greater than B」「A is more than B」
        patterns = [
            (r'(.+?)\s+is\s+(greater|more)\s+than\s+(.+)$', r'\1 > \3'),
            (r'(.+?)\s+is\s+(less|smaller)\s+than\s+(.+)$', r'\1 < \3'),
            (r'(.+?)\s+is\s+(equal|same)\s+to\s+(.+)$', r'\1 == \4'),
            (r'(.+?)\s+is\s+(different|not equal)\s+from\s+(.+)$', r'\1 != \4'),
            (r'(.+?)\s+is\s+(at least|greater equal)\s+(.+)$', r'\1 >= \3'),
            (r'(.+?)\s+is\s+(at most|less equal)\s+(.+)$', r'\1 <= \3'),
            (r'(.+?)\s+are\s+(greater|more)\s+than\s+(.+)$', r'\1 > \3'),
            (r'(.+?)\s+are\s+(less|smaller)\s+than\s+(.+)$', r'\1 < \3'),
            (r'(.+?)\s+are\s+(equal|same)\s+to\s+(.+)$', r'\1 == \4'),
        ]
        
        for pattern, replacement in patterns:
            match = re.match(pattern, condition, re.IGNORECASE)
            if match:
                return match.expand(replacement)
        
        # 基本的な置換
        replacements = [
            ('greater than', '>'),
            ('more than', '>'),
            ('less than', '<'),
            ('smaller than', '<'),
            ('equal to', '=='),
            ('same as', '=='),
            ('different from', '!='),
            ('not equal', '!='),
            ('at least', '>='),
            ('greater equal', '>='),
            ('at most', '<='),
            ('less equal', '<='),
        ]
        
        for english, python_op in replacements:
            condition = condition.replace(english, python_op)
        
        return condition
    
    def _parse_expression(self, expr):
        """式を解析してPythonコードに変換"""
        if not expr:
            return ""
        
        # 既にPythonコードの場合はそのまま返す
        if expr.startswith(('print(', 'if ', 'else:', 'elif ', 'for ', 'while ', 'def ', 'return ', 'import ', 'from ')):
            return expr
        
        # 演算子の処理
        expr = self._translate_arithmetic_operators(expr)
        
        # その他の変換処理
        return self._translate_expression(expr)
    
    def _translate_arithmetic_operators(self, expr):
        """算術演算子を変換"""
        import re
        
        # 「A plus B」「add A and B」
        patterns = [
            (r'^(.+?)\s+plus\s+(.+?)$', r'\1 + \2'),
            (r'^(.+?)\s+minus\s+(.+?)$', r'\1 - \2'),
            (r'^(.+?)\s+times\s+(.+?)$', r'\1 * \2'),
            (r'^(.+?)\s+multiplied by\s+(.+?)$', r'\1 * \2'),
            (r'^(.+?)\s+divided by\s+(.+?)$', r'\1 / \2'),
            (r'^add\s+(.+?)\s+and\s+(.+?)$', r'\1 + \2'),
            (r'^subtract\s+(.+?)\s+from\s+(.+?)$', r'\2 - \1'),
            (r'^multiply\s+(.+?)\s+by\s+(.+?)$', r'\1 * \2'),
            (r'^divide\s+(.+?)\s+by\s+(.+?)$', r'\1 / \2'),
        ]
        
        for pattern, replacement in patterns:
            match = re.match(pattern, expr, re.IGNORECASE)
            if match:
                groups = match.groups()
                if len(groups) == 2:
                    # 直接演算子を返す
                    if 'plus' in match.group(1).lower():
                        return f"{groups[0]} + {groups[1]}"
                    elif 'minus' in match.group(1).lower():
                        return f"{groups[0]} - {groups[1]}"
                    elif 'times' in match.group(1).lower() or 'multiplied' in match.group(1).lower():
                        return f"{groups[0]} * {groups[1]}"
                    elif 'divided' in match.group(1).lower():
                        return f"{groups[0]} / {groups[1]}"
                    else:
                        return f"{groups[0]} + {groups[1]}"
        
        # 基本的な置換
        replacements = [
            (' plus ', ' + '),
            (' minus ', ' - '),
            (' times ', ' * '),
            (' multiplied by ', ' * '),
            (' divided by ', ' / '),
        ]
        
        for english, python_op in replacements:
            expr = expr.replace(english, python_op)
        
        return expr
    
    def _translate_expression(self, expr):
        """式をPython式に変換"""
        if not expr:
            return ""
        
        # 特殊変数の置換
        expr = EnglishKeywords.translate_variable(expr)
        
        # 英語命令の置換
        for english, python in EnglishKeywords.ENGLISH_COMMANDS.items():
            if english.lower() in expr.lower():
                expr = expr.replace(english, python)
                self._add_import_if_needed(python)
        
        # 基本命令の置換
        for english, python in EnglishKeywords.BASIC_COMMANDS.items():
            expr = expr.replace(english, python)
        
        # 括弧の調整
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
    
    def parse_file(self, english_code):
        """英語コード全体をPythonコードに変換"""
        lines = english_code.split('\n')
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
            
            # 終端マーカーのチェック
            if line.strip().lower() == 'koko':
                break
            
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
    
    def execute(self, english_code):
        """英語コードを実行"""
        python_code = self.parse_file(english_code)
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
            'os_commands': os_commands,
            'macro_system': macro_system,
            'start_macro_recording': start_macro_recording,
            'stop_macro_recording': stop_macro_recording,
            'play_macro': play_macro,
            'create_simple_macro': create_simple_macro,
            'list_macros': list_macros,
        }
        
        try:
            exec(python_code, exec_globals)
            self._result = exec_globals.get('_result')
        except Exception as e:
            # エラー情報を取得
            error_info = error_handler.handle_error(e, english_code)
            
            # エラー報告を表示
            error_report = error_handler.format_error_report(error_info)
            print(error_report)
    
    def _parse_os_command(self, line):
        """OSコマンドを解析"""
        import re
        
        # コマンド実行
        if 'command ' in line.lower():
            match = re.search(r'command\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                command = match.group(1)
                return f"_result = os_commands.execute_command('{command}')[1]"
        
        if 'execute ' in line.lower():
            match = re.search(r'execute\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                command = match.group(1)
                return f"_result = os_commands.execute_command('{command}')[1]"
        
        if 'run ' in line.lower():
            match = re.search(r'run\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                command = match.group(1)
                return f"_result = os_commands.execute_command('{command}')[1]"
        
        return line
    
    def _parse_file_operation(self, line):
        """ファイル操作を解析"""
        import re
        
        # ファイル読み込み
        if 'read from ' in line.lower():
            match = re.search(r'(.+?)\s+is\s+read\s+from\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if not match:
                match = re.search(r'read\s+from\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                if len(match.groups()) == 2:
                    var, file = match.groups()
                    return f"{var} = os_commands.execute_command('type {file}')[1]"
                else:
                    file = match.group(1)
                    return f"_result = os_commands.execute_command('type {file}')[1]"
        
        # ファイル書き込み
        if 'write to ' in line.lower():
            match = re.search(r'write\s+[\"\'"](.+?)[\"\'"]\s+to\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                content, file = match.groups()
                return f"os_commands.execute_command('echo {content} > {file}')"
        
        # ファイル作成
        if 'create ' in line.lower():
            match = re.search(r'create\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                file = match.group(1)
                return f"os_commands.execute_command('touch {file}')"
        
        # ファイル削除
        if 'delete ' in line.lower():
            match = re.search(r'delete\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                file = match.group(1)
                return f"os_commands.execute_command('rm {file}')"
        
        # ファイルコピー
        if 'copy ' in line.lower():
            match = re.search(r'copy\s+[\"\'"](.+?)[\"\'"]\s+to\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                src, dst = match.groups()
                return f"os_commands.copy_file('{src}', '{dst}')"
        
        # ファイル移動
        if 'move ' in line.lower():
            match = re.search(r'move\s+[\"\'"](.+?)[\"\'"]\s+to\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                src, dst = match.groups()
                return f"os_commands.move_file('{src}', '{dst}')"
        
        return line
    
    def _parse_directory_operation(self, line):
        """ディレクトリ操作を解析"""
        import re
        
        # ディレクトリ一覧
        if 'list ' in line.lower() or 'contents ' in line.lower():
            match = re.search(r'list\s+(?:directory\s+)?[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if not match:
                match = re.search(r'contents\s+of\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                path = match.group(1)
                return f"_result = os_commands.list_directory('{path}')"
        
        # ディレクトリ作成
        if 'create ' in line.lower() and ('directory' in line.lower() or 'folder' in line.lower()):
            match = re.search(r'create\s+(?:directory|folder)\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                path = match.group(1)
                return f"os_commands.create_directory('{path}')"
        
        # ディレクトリ削除
        if 'delete ' in line.lower() and ('directory' in line.lower() or 'folder' in line.lower()):
            match = re.search(r'delete\s+(?:directory|folder)\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                path = match.group(1)
                return f"os_commands.remove_directory('{path}')"
        
        return line
    
    def _parse_system_info(self, line):
        """システム情報を解析"""
        
        # システム情報
        if 'system info' in line.lower() or 'os info' in line.lower():
            return "_result = os_commands.get_system_info()"
        
        # 現在のディレクトリ
        if 'current directory' in line.lower():
            return "_result = os_commands.get_current_directory()"
        
        return line
    
    def _parse_macro(self, line):
        """マクロ機能を解析"""
        import re
        
        # マクロ記録開始
        if 'record' in line.lower() and 'macro' in line.lower():
            match = re.search(r'record\s+macro\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                name = match.group(1)
                return f"start_macro_recording('{name}')"
        
        # マクロ記録停止
        if 'stop' in line.lower() and 'record' in line.lower():
            return "stop_macro_recording()"
        
        # マクロ再生
        if 'play' in line.lower() and 'macro' in line.lower():
            match = re.search(r'play\s+macro\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                name = match.group(1)
                return f"play_macro('{name}')"
        
        if 'execute' in line.lower() and 'macro' in line.lower():
            match = re.search(r'execute\s+macro\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                name = match.group(1)
                return f"play_macro('{name}')"
        
        # マクロ一覧
        if 'list' in line.lower() and 'macro' in line.lower():
            return "_result = macro_system.list_macros()"
        
        # マクロ作成
        if 'create' in line.lower() and 'macro' in line.lower():
            match = re.search(r'create\s+macro\s+[\"\'"](.+?)[\"\'"]', line, re.IGNORECASE)
            if match:
                name = match.group(1)
                # 簡単なマクロ作成の例
                steps = [
                    {'action': 'message', 'parameters': {'message': 'Macro started'}, 'description': 'Start message'},
                    {'action': 'wait', 'parameters': {'seconds': 1}, 'description': 'Wait 1 second'},
                    {'action': 'message', 'parameters': {'message': 'Macro ended'}, 'description': 'End message'}
                ]
                return f"create_simple_macro('{name}', 'Simple macro', {steps})"
        
        return line
