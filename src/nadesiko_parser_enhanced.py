"""
なでしこパイソンパーサー - 超強化版
すべての機能を統合した日本語プログラミング言語パーサー
"""

import re
import math
import random
import time
import sys
import os
import datetime
import json
import csv
import statistics
import requests
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from pathlib import Path

try:
    from .nadesiko_keywords import NadesikoKeywords
except ImportError:
    from nadesiko_keywords import NadesikoKeywords

class EnhancedNadesikoParser:
    """超強化版なでしこパーサー"""
    
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self._result = None
        self.indent_level = 0
        self.imports = set()
        self.loop_count = 0
        
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
        if any(word in line for word in ['を返す', 'を戻る', 'して返す', 'と返す']):
            return self._parse_return(line)
        
        # 「それ」変数の処理
        if 'それ' in line and not line.startswith('それ'):
            line = line.replace('それ', '_result')
        
        # 表示・出力系
        if any(word in line for word in ['を表示', 'を表示する', 'と言う', 'と表示', 'を出力', 'と出力']):
            return self._parse_print(line)
        
        # 尋ねる・入力系
        if any(word in line for word in ['を尋ねる', 'と尋ねる', 'に尋ねる', 'を入力']):
            return self._parse_input(line)
        
        # 代入系（拡張）
        if any(word in line for word in ['=', 'は', 'とは', 'に代入', 'を設定', 'に設定']):
            return self._parse_assignment(line)
        
        # 条件分岐（拡張）
        if self._is_if_statement(line):
            return self._parse_if(line)
        
        if self._is_else_statement(line):
            return self._parse_else(line)
        
        if self._is_endif_statement(line):
            return self._parse_endif(line)
        
        # 繰り返し・ループ（拡張）
        if self._is_loop_statement(line):
            return self._parse_loop(line)
        
        if self._is_for_statement(line):
            return self._parse_for(line)
        
        if self._is_while_statement(line):
            return self._parse_while(line)
        
        if self._is_endloop_statement(line):
            return self._parse_endloop(line)
        
        # 関数定義（拡張）
        if line.startswith('●') or line.startswith('関数'):
            return self._parse_function_def(line)
        
        if self._is_endfunction_statement(line):
            return self._parse_endfunction(line)
        
        # ファイル操作（拡張）
        if self._is_file_operation(line):
            return self._parse_file_operation(line)
        
        # リスト・配列操作
        if self._is_list_operation(line):
            return self._parse_list_operation(line)
        
        # 辞書操作
        if self._is_dict_operation(line):
            return self._parse_dict_operation(line)
        
        # Web API操作
        if self._is_web_operation(line):
            return self._parse_web_operation(line)
        
        # GUIダイアログ
        if self._is_gui_operation(line):
            return self._parse_gui_operation(line)
        
        # 数学・統計関数
        if self._is_math_operation(line):
            return self._parse_math_operation(line)
        
        # 文字列処理（拡張）
        if self._is_string_operation(line):
            return self._parse_string_operation(line)
        
        # 日時操作（拡張）
        if self._is_datetime_operation(line):
            return self._parse_datetime_operation(line)
        
        # ランダム機能
        if self._is_random_operation(line):
            return self._parse_random_operation(line)
        
        # OSコマンド
        if line.startswith('コマンド') or line.startswith('実行'):
            return self._parse_os_command(line)
        
        # 型変換
        if self._is_type_conversion(line):
            return self._parse_type_conversion(line)
        
        # 例外処理
        if self._is_try_statement(line):
            return self._parse_try(line)
        
        if self._is_catch_statement(line):
            return self._parse_catch(line)
        
        if self._is_finally_statement(line):
            return self._parse_finally(line)
        
        # その他の式
        return self._parse_expression(line)
    
    def _process_japanese_quotes(self, line):
        """日本語引用符「」を処理"""
        def replace_quotes(match):
            content = match.group(1)
            # 変数展開を処理
            if '{' in content and '}' in content:
                return f'"{content}"'
            return f'"{content}"'
        
        return re.sub(r'「(.+?)」', replace_quotes, line)
    
    # ========== 表示・出力系 ==========
    
    def _parse_print(self, line):
        """表示文の処理（拡張版）"""
        # パターン1: 「文字列」を表示
        match = re.search(r'「(.+?)」', line)
        if match:
            content = match.group(1)
            if '{' in content and '}' in content:
                # 変数展開あり
                return f'print("{content}".format(**locals()))'
            return f'print("{content}")'
        
        # パターン2: 変数を表示
        match = re.search(r'(.+?)を表示', line)
        if match:
            var = match.group(1).strip()
            return f'print({var})'
        
        return "print('表示')"
    
    def _parse_input(self, line):
        """入力文の処理"""
        # パターン1: 「メッセージ」を尋ねる
        match = re.search(r'「(.+?)」.*を尋ねる', line)
        if match:
            message = match.group(1)
            return f'input("{message}")'
        
        # パターン2: 変数に入力
        match = re.search(r'(.+?)に尋ねる', line)
        if match:
            var = match.group(1).strip()
            return f'{var} = input()'
        
        return 'input()'
    
    # ========== 代入系 ==========
    
    def _parse_assignment(self, line):
        """代入文の処理（拡張版）"""
        # 特殊な代入パターン
        if 'に代入' in line:
            var, value = line.split('に代入', 1)
        elif 'とは' in line:
            var, value = line.split('とは', 1)
        elif 'を設定' in line:
            var, value = line.split('を設定', 1)
        elif 'に設定' in line:
            var, value = line.split('に設定', 1)
        elif '=' in line:
            var, value = line.split('=', 1)
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
        
        # 特殊値の処理
        value = self._translate_special_values(value)
        
        # 式の変換
        value = self._translate_expression(value)
        
        # リスト・辞書の初期化
        if value == '[]' or '空のリスト' in value:
            return f'{var} = []'
        if value == '{}' or '空の辞書' in value:
            return f'{var} = {{}}'
        
        return f'{var} = {value}'
    
    def _translate_special_values(self, value):
        """特殊な値を変換"""
        # 時刻・日付
        if value in ['今', '現在時刻']:
            return 'datetime.datetime.now()'
        if value in ['今日', '今日の日付']:
            return 'datetime.date.today()'
        if value == '現在の時刻':
            return 'datetime.datetime.now().time()'
        
        # 定数
        if value in ['パイ', '円周率']:
            return 'math.pi'
        if value in ['エー', '自然対数の底']:
            return 'math.e'
        if value in ['真', 'はい']:
            return 'True'
        if value in ['偽', 'いいえ']:
            return 'False'
        if value == '空':
            return 'None'
        
        return value
    
    # ========== 条件分岐 ==========
    
    def _is_if_statement(self, line):
        """条件分岐文かチェック"""
        return any(line.startswith(word) for word in ['もし', '如果', 'if']) and \
               any(word in line for word in ['ならば', 'なら', 'ら', 'then'])
    
    def _is_else_statement(self, line):
        """else文かチェック"""
        return any(line == word or line.startswith(word) for word in 
                  ['違えば', 'else', 'そうでなければ', 'それ以外'])
    
    def _is_endif_statement(self, line):
        """endif文かチェック"""
        return any(word in line for word in ['もし終わり', 'もし終了', 'endif', 'if終了'])
    
    def _parse_if(self, line):
        """if文の処理"""
        # 条件部分を抽出
        for delimiter in ['ならば', 'なら', 'ら']:
            if delimiter in line:
                condition = line.split(delimiter)[0].strip()
                # 開始語を削除
                for start_word in ['もし', '如果']:
                    if condition.startswith(start_word):
                        condition = condition[len(start_word):].strip()
                break
        else:
            condition = line.strip()
        
        # 条件式を変換
        condition = self._translate_condition(condition)
        
        return f'if {condition}:'
    
    def _parse_else(self, line):
        """else文の処理"""
        return 'else:'
    
    def _parse_endif(self, line):
        """endif文の処理"""
        # Pythonではインデントでブロックが終了するので何もしない
        return ''
    
    def _translate_condition(self, condition):
        """条件式をPythonに変換"""
        # 比較演算子の変換
        replacements = [
            (r'(.+?)が(.+?)と等しい', r'\1 == \2'),
            (r'(.+?)が(.+?)と同じ', r'\1 == \2'),
            (r'(.+?)が(.+?)と違う', r'\1 != \2'),
            (r'(.+?)が(.+?)と異なる', r'\1 != \2'),
            (r'(.+?)が(.+?)より大きい', r'\1 > \2'),
            (r'(.+?)が(.+?)より小さい', r'\1 < \2'),
            (r'(.+?)が(.+?)以上', r'\1 >= \2'),
            (r'(.+?)が(.+?)以下', r'\1 <= \2'),
            (r'(.+?)が(.+?)を含む', r'\2 in \1'),
            (r'(.+?)が(.+?)に含まれる', r'\1 in \2'),
            (r'(.+?)以上', r'\1 >='),
            (r'(.+?)以下', r'\1 <='),
            (r'(.+?)より大きい', r'> \1'),
            (r'(.+?)より小さい', r'< \1'),
        ]
        
        for pattern, replacement in replacements:
            condition = re.sub(pattern, replacement, condition)
        
        return condition
    
    # ========== ループ ==========
    
    def _is_loop_statement(self, line):
        """ループ文かチェック"""
        return any(word in line for word in ['繰り返す', 'ループ', 'loop'])
    
    def _is_for_statement(self, line):
        """for文かチェック"""
        return any(line.startswith(word) for word in ['Ｎ回', 'N回', '回数']) or \
               ('回' in line and ('繰り返す' in line or 'ループ' in line))
    
    def _is_while_statement(self, line):
        """while文かチェック"""
        return any(line.startswith(word) for word in ['まで', '間', 'while']) or \
               ('間' in line and '繰り返す' in line)
    
    def _is_endloop_statement(self, line):
        """endloop文かチェック"""
        return any(word in line for word in ['繰り返し終わり', 'ループ終了', 'endloop', 'endfor'])
    
    def _parse_loop(self, line):
        """ループ文の処理"""
        self.loop_count += 1
        return f'for _ in range(10):  # デフォルト10回繰り返し'
    
    def _parse_for(self, line):
        """for文の処理"""
        # 回数を抽出
        match = re.search(r'(\d+)', line)
        if match:
            count = match.group(1)
            return f'for i in range({count}):'
        
        # 範囲ループ
        match = re.search(r'(.+?)から(.+?)まで', line)
        if match:
            start = match.group(1).strip()
            end = match.group(2).strip()
            return f'for i in range({start}, {end}+1):'
        
        return 'for i in range(10):'
    
    def _parse_while(self, line):
        """while文の処理"""
        # 条件を抽出
        for delimiter in ['まで', '間']:
            if delimiter in line:
                condition = line.split(delimiter)[0].strip()
                condition = self._translate_condition(condition)
                return f'while {condition}:'
        
        return 'while True:'
    
    def _parse_endloop(self, line):
        """endloop文の処理"""
        return ''
    
    # ========== 関数 ==========
    
    def _parse_function_def(self, line):
        """関数定義の処理"""
        # ●関数名(引数)
        match = re.match(r'[●関数]\s*(\w+)\s*\((.*?)\)', line)
        if match:
            func_name = match.group(1)
            args = match.group(2)
            return f'def {func_name}({args}):'
        
        # 関数 関数名
        match = re.match(r'関数\s*(\w+)', line)
        if match:
            func_name = match.group(1)
            return f'def {func_name}():'
        
        return f'def function():'
    
    def _is_endfunction_statement(self, line):
        """endfunction文かチェック"""
        return any(word in line for word in ['関数終わり', '関数終了', 'endfunction', 'ここまで'])
    
    def _parse_endfunction(self, line):
        """endfunction文の処理"""
        return ''
    
    def _parse_return(self, line):
        """return文の処理"""
        for delimiter in ['を返す', 'を戻る', 'と返す']:
            if delimiter in line:
                value = line.split(delimiter)[0].strip()
                value = self._translate_expression(value)
                return f'return {value}'
        
        return 'return'
    
    # ========== ファイル操作 ==========
    
    def _is_file_operation(self, line):
        """ファイル操作かチェック"""
        return any(word in line for word in 
                  ['ファイル', '読む', '書く', '保存', '開く', '閉じる', '削除', 'コピー', '移動', 'リネーム'])
    
    def _parse_file_operation(self, line):
        """ファイル操作の処理"""
        # 読み込み
        if any(word in line for word in ['読む', '読み込む', '開く']):
            match = re.search(r'「(.+?)」', line)
            if match:
                filepath = match.group(1)
                if 'JSON' in line or 'json' in line:
                    self.imports.add('json')
                    return f'json.load(open("{filepath}", "r", encoding="utf-8"))'
                if 'CSV' in line or 'csv' in line:
                    self.imports.add('csv')
                    return f'list(csv.reader(open("{filepath}", "r", encoding="utf-8")))'
                return f'open("{filepath}", "r", encoding="utf-8").read()'
        
        # 書き込み
        if any(word in line for word in ['書く', '書き込む', '保存']):
            match_content = re.search(r'「(.+?)」', line)
            match_file = re.findall(r'「(.+?)」', line)
            if len(match_file) >= 2:
                content = match_file[0]
                filepath = match_file[1]
                if 'JSON' in line:
                    return f'json.dump({content}, open("{filepath}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)'
                return f'open("{filepath}", "w", encoding="utf-8").write({content})'
        
        return '# ファイル操作'
    
    # ========== リスト操作 ==========
    
    def _is_list_operation(self, line):
        """リスト操作かチェック"""
        return any(word in line for word in 
                  ['リスト', '配列', '追加', '削除', '挿入', 'ソート', '逆順', '検索', '長さ', '要素数'])
    
    def _parse_list_operation(self, line):
        """リスト操作の処理"""
        # 追加
        if '追加' in line:
            match = re.search(r'(.+?)に(.+?)を追加', line)
            if match:
                list_var = match.group(1).strip()
                item = match.group(2).strip()
                return f'{list_var}.append({item})'
        
        # 削除
        if '削除' in line:
            match = re.search(r'(.+?)から(.+?)を削除', line)
            if match:
                list_var = match.group(1).strip()
                item = match.group(2).strip()
                return f'{list_var}.remove({item})'
        
        # ソート
        if 'ソート' in line:
            match = re.search(r'(.+?)をソート', line)
            if match:
                list_var = match.group(1).strip()
                return f'{list_var}.sort()'
        
        # 長さ
        if any(word in line for word in ['長さ', '要素数', '個数']):
            match = re.search(r'(.+?)の(長さ|要素数|個数)', line)
            if match:
                list_var = match.group(1).strip()
                return f'len({list_var})'
        
        return '# リスト操作'
    
    # ========== 辞書操作 ==========
    
    def _is_dict_operation(self, line):
        """辞書操作かチェック"""
        return any(word in line for word in 
                  ['辞書', 'マップ', 'キー', '値', '追加', '取得', '削除'])
    
    def _parse_dict_operation(self, line):
        """辞書操作の処理"""
        # キーと値の追加
        if '追加' in line or '設定' in line:
            match = re.search(r'(.+?)に(.+?)を(.+?)として追加', line)
            if match:
                dict_var = match.group(1).strip()
                key = match.group(2).strip()
                value = match.group(3).strip()
                return f'{dict_var}[{key}] = {value}'
        
        # 値の取得
        if '取得' in line or '読む' in line:
            match = re.search(r'(.+?)から(.+?)を取得', line)
            if match:
                dict_var = match.group(1).strip()
                key = match.group(2).strip()
                return f'{dict_var}.get({key})'
        
        return '# 辞書操作'
    
    # ========== Web API操作 ==========
    
    def _is_web_operation(self, line):
        """Web操作かチェック"""
        return any(word in line for word in 
                  ['URL', 'HTTP', 'GET', 'POST', 'ダウンロード', 'アップロード', 'API', 'リクエスト', 'ウェブ'])
    
    def _parse_web_operation(self, line):
        """Web操作の処理"""
        self.imports.add('requests')
        
        # GETリクエスト
        if 'GET' in line or '取得' in line or 'ダウンロード' in line:
            match = re.search(r'「(.+?)」', line)
            if match:
                url = match.group(1)
                return f'requests.get("{url}").text'
        
        return '# Web API操作'
    
    # ========== GUI操作 ==========
    
    def _is_gui_operation(self, line):
        """GUI操作かチェック"""
        return any(word in line for word in 
                  ['ダイアログ', 'メッセージ', '尋ねる', '確認', '選択', 'ファイル選択', '保存ダイアログ'])
    
    def _parse_gui_operation(self, line):
        """GUI操作の処理"""
        # メッセージボックス
        if 'メッセージ' in line or '表示' in line:
            match = re.search(r'「(.+?)」', line)
            if match:
                message = match.group(1)
                return f'messagebox.showinfo("メッセージ", "{message}")'
        
        # 確認ダイアログ
        if '確認' in line or 'はい/いいえ' in line:
            match = re.search(r'「(.+?)」', line)
            if match:
                message = match.group(1)
                return f'messagebox.askyesno("確認", "{message}")'
        
        # ファイル選択
        if 'ファイル選択' in line or '開く' in line:
            return 'filedialog.askopenfilename()'
        
        return '# GUI操作'
    
    # ========== 数学・統計 ==========
    
    def _is_math_operation(self, line):
        """数学操作かチェック"""
        return any(word in line for word in 
                  ['平均', '最大', '最小', '合計', '標準偏差', '分散', '中央値', 'モード', '絶対値', '平方根', '累乗'])
    
    def _parse_math_operation(self, line):
        """数学操作の処理"""
        self.imports.add('statistics')
        
        # 統計関数
        if '平均' in line:
            match = re.search(r'(.+?)の平均', line)
            if match:
                data = match.group(1).strip()
                return f'statistics.mean({data})'
        
        if '最大' in line:
            match = re.search(r'(.+?)の最大', line)
            if match:
                data = match.group(1).strip()
                return f'max({data})'
        
        if '最小' in line:
            match = re.search(r'(.+?)の最小', line)
            if match:
                data = match.group(1).strip()
                return f'min({data})'
        
        if '合計' in line:
            match = re.search(r'(.+?)の合計', line)
            if match:
                data = match.group(1).strip()
                return f'sum({data})'
        
        if '標準偏差' in line:
            match = re.search(r'(.+?)の標準偏差', line)
            if match:
                data = match.group(1).strip()
                return f'statistics.stdev({data})'
        
        if '中央値' in line:
            match = re.search(r'(.+?)の中央値', line)
            if match:
                data = match.group(1).strip()
                return f'statistics.median({data})'
        
        return '# 数学・統計操作'
    
    # ========== 文字列操作 ==========
    
    def _is_string_operation(self, line):
        """文字列操作かチェック"""
        return any(word in line for word in 
                  ['置換', '分割', '結合', '検索', 'マッチ', '正規表現', '大文字', '小文字', '空白除去'])
    
    def _parse_string_operation(self, line):
        """文字列操作の処理"""
        # 置換
        if '置換' in line:
            match = re.search(r'(.+?)の(.+?)を(.+?)に置換', line)
            if match:
                text = match.group(1).strip()
                old = match.group(2).strip()
                new = match.group(3).strip()
                return f'{text}.replace({old}, {new})'
        
        # 分割
        if '分割' in line:
            match = re.search(r'(.+?)を(.+?)で分割', line)
            if match:
                text = match.group(1).strip()
                sep = match.group(2).strip()
                return f'{text}.split({sep})'
        
        # 結合
        if '結合' in line:
            match = re.search(r'(.+?)を(.+?)で結合', line)
            if match:
                items = match.group(1).strip()
                sep = match.group(2).strip()
                return f'{sep}.join({items})'
        
        return '# 文字列操作'
    
    # ========== 日時操作 ==========
    
    def _is_datetime_operation(self, line):
        """日時操作かチェック"""
        return any(word in line for word in 
                  ['日付', '時刻', '年', '月', '日', '時', '分', '秒', 'フォーマット', 'パース', 'タイムゾーン'])
    
    def _parse_datetime_operation(self, line):
        """日時操作の処理"""
        # フォーマット
        if 'フォーマット' in line:
            match = re.search(r'(.+?)を(.+?)でフォーマット', line)
            if match:
                dt = match.group(1).strip()
                fmt = match.group(2).strip()
                return f'{dt}.strftime({fmt})'
        
        # 日付の取得
        if '年' in line and 'から' not in line:
            match = re.search(r'(.+?)の年', line)
            if match:
                dt = match.group(1).strip()
                return f'{dt}.year'
        
        return '# 日時操作'
    
    # ========== ランダム ==========
    
    def _is_random_operation(self, line):
        """ランダム操作かチェック"""
        return any(word in line for word in 
                  ['乱数', 'ランダム', 'ランダム選択', 'シャッフル', '抽選', 'サイコロ'])
    
    def _parse_random_operation(self, line):
        """ランダム操作の処理"""
        # 乱数生成
        if '乱数' in line or 'ランダム' in line:
            match = re.search(r'(\d+)から(\d+)の乱数', line)
            if match:
                start = match.group(1)
                end = match.group(2)
                return f'random.randint({start}, {end})'
            
            match = re.search(r'0から(\d+)の乱数', line)
            if match:
                end = match.group(1)
                return f'random.randint(0, {end})'
        
        # ランダム選択
        if 'ランダム選択' in line or '抽選' in line:
            match = re.search(r'(.+?)からランダム選択', line)
            if match:
                items = match.group(1).strip()
                return f'random.choice({items})'
        
        # シャッフル
        if 'シャッフル' in line:
            match = re.search(r'(.+?)をシャッフル', line)
            if match:
                items = match.group(1).strip()
                return f'random.shuffle({items})'
        
        return '# ランダム操作'
    
    # ========== OSコマンド ==========
    
    def _parse_os_command(self, line):
        """OSコマンドの処理"""
        if 'コマンド' in line:
            match = re.search(r'「(.+?)」', line)
            if match:
                cmd = match.group(1)
                return f'os.system("{cmd}")'
        
        return '# OSコマンド'
    
    # ========== 型変換 ==========
    
    def _is_type_conversion(self, line):
        """型変換かチェック"""
        return any(word in line for word in 
                  ['文字列', '数値', '整数', '実数', 'リスト', '辞書', '真偽値', '変換'])
    
    def _parse_type_conversion(self, line):
        """型変換の処理"""
        # 文字列
        if '文字列' in line:
            match = re.search(r'(.+?)を文字列', line)
            if match:
                value = match.group(1).strip()
                return f'str({value})'
        
        # 数値
        if '数値' in line or '整数' in line:
            match = re.search(r'(.+?)を(数値|整数)', line)
            if match:
                value = match.group(1).strip()
                return f'int({value})'
        
        # 実数
        if '実数' in line:
            match = re.search(r'(.+?)を実数', line)
            if match:
                value = match.group(1).strip()
                return f'float({value})'
        
        # リスト
        if 'リスト' in line:
            match = re.search(r'(.+?)をリスト', line)
            if match:
                value = match.group(1).strip()
                return f'list({value})'
        
        return '# 型変換'
    
    # ========== 例外処理 ==========
    
    def _is_try_statement(self, line):
        """try文かチェック"""
        return any(line.startswith(word) for word in ['試す', 'try', '例外を試す'])
    
    def _is_catch_statement(self, line):
        """catch文かチェック"""
        return any(line.startswith(word) for word in ['例外', 'catch', 'エラー', '失敗'])
    
    def _is_finally_statement(self, line):
        """finally文かチェック"""
        return any(line.startswith(word) for word in ['最後に', 'finally', '必ず'])
    
    def _parse_try(self, line):
        """try文の処理"""
        return 'try:'
    
    def _parse_catch(self, line):
        """catch文の処理"""
        return 'except Exception as e:'
    
    def _parse_finally(self, line):
        """finally文の処理"""
        return 'finally:'
    
    # ========== 式の変換 ==========
    
    def _translate_expression(self, expr):
        """式をPythonに変換"""
        if not expr:
            return ""
        
        # 演算子の変換
        patterns = [
            (r'(.+?)と(.+?)を足す', r'\1 + \2'),
            (r'(.+?)に(.+?)を足す', r'\1 + \2'),
            (r'(.+?)から(.+?)を引く', r'\1 - \2'),
            (r'(.+?)を(.+?)で割る', r'\1 / \2'),
            (r'(.+?)に(.+?)を掛ける', r'\1 * \2'),
            (r'(.+?)の(\d+)乗', r'\1 ** \2'),
            (r'(.+?)のべき乗', r'\1 **'),
            (r'(.+?)の平方根', r'math.sqrt(\1)'),
            (r'(.+?)の絶対値', r'abs(\1)'),
            (r'(.+?)を四捨五入', r'round(\1)'),
            (r'(.+?)を切り上げ', r'math.ceil(\1)'),
            (r'(.+?)を切り捨て', r'math.floor(\1)'),
        ]
        
        for pattern, replacement in patterns:
            expr = re.sub(pattern, replacement, expr)
        
        # 特殊変数の置換
        replacements = {
            'パイ': 'math.pi',
            '円周率': 'math.pi',
            'エー': 'math.e',
            '自然対数の底': 'math.e',
            '真': 'True',
            '偽': 'False',
            'はい': 'True',
            'いいえ': 'False',
            '空': 'None',
            '未定義': 'None',
        }
        
        for jp, py in replacements.items():
            expr = expr.replace(jp, py)
        
        return expr
    
    def _parse_expression(self, line):
        """その他の式を処理"""
        return self._translate_expression(line)
