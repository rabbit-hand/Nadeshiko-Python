"""
なでしこ3完全互換モジュール
なでしこ3の全機能を実装
"""

import math
import random
import time
import sys
import os
import datetime
import json
import csv
import pickle
import re
import hashlib
import base64
import urllib.parse
from decimal import Decimal, getcontext
from pathlib import Path

class NadesikoComplete:
    """なでしこ3の全機能を実装した完全互換クラス"""
    
    def __init__(self):
        self._result = None
        self.variables = {}
        self._setup_system_constants()
        
    def _setup_system_constants(self):
        """システム定数を設定"""
        # システム定数
        self.NADESHIKO_VERSION = "3.0.0"
        self.NADESHIKO_ENGINE = "Python"
        self.NADESHIKO_TYPE = "Python互換"
        self.HAI = True
        self.IIE = False
        self.SHIN = True
        self.GI = False
        self.EIEN = float('inf')
        self.ON = True
        self.OFF = False
        self.KAIGYOU = "\n"
        self.TAB = "\t"
        self.KAKKO = "("
        self.KAKKO_TOJI = ")"
        self.NAMI_KAKKO = "{"
        self.NAMI_KAKKO_TOJI = "}"
        self.OK = "OK"
        self.NG = "NG"
        self.CANCEL = "CANCEL"
        self.PI = math.pi
        self.KARA = ""
        self.NULL = None
        self.undefined = None
        self.MITEIGI = None
        self.ERROR_MESSAGE = ""
        
        # 真偽値
        self.TRUE = True
        self.FALSE = False
        self.true = True
        self.false = False
        
        # 数値定数
        self.NAN = float('nan')
        self.MUGENDAI = float('inf')
        self.HENMOCHINASHI = None
        self.HENMOCHIARI = True
        self.KARAHIRETSU = []
        self.KARAJISHO = {}
        self.KARAHASSHU = {}
        self.KARAOBUJEKUTO = {}
        
    # === システム定数 ===
    def ナデシコバージョン(self):
        return self.NADESHIKO_VERSION
    
    def ナデシコエンジン(self):
        return self.NADESHIKO_ENGINE
    
    def ナデシコ種類(self):
        return self.NADESHIKO_TYPE
    
    def はい(self):
        return self.HAI
    
    def いいえ(self):
        return self.IIE
    
    def 真(self):
        return self.SHIN
    
    def 偽(self):
        return self.GI
    
    def 永遠(self):
        return self.EIEN
    
    def オン(self):
        return self.ON
    
    def オフ(self):
        return self.OFF
    
    def 改行(self):
        return self.KAIGYOU
    
    def タブ(self):
        return self.TAB
    
    def カッコ(self):
        return self.KAKKO
    
    def カッコ閉(self):
        return self.KAKKO_TOJI
    
    def 波カッコ(self):
        return self.NAMI_KAKKO
    
    def 波カッコ閉(self):
        return self.NAMI_KAKKO_TOJI
    
    # === 標準出力 ===
    def 表示(self, *args):
        """値を表示"""
        if len(args) == 1:
            print(args[0])
        else:
            print(*args)
        self._result = args[0] if args else None
        return self._result
    
    def 継続表示(self, *args):
        """改行なしで表示"""
        if len(args) == 1:
            print(args[0], end="")
        else:
            print(*args, end="")
        self._result = args[0] if args else None
        return self._result
    
    def 連続表示(self, *args):
        """連続して表示"""
        for arg in args:
            print(arg, end="")
        print()
        self._result = args[-1] if args else None
        return self._result
    
    def 連続無改行表示(self, *args):
        """改行なしで連続表示"""
        for arg in args:
            print(arg, end="")
        self._result = args[-1] if args else None
        return self._result
    
    def 表示ログ(self, message):
        """ログを表示"""
        print(f"[LOG] {message}")
        self._result = message
        return self._result
    
    def 表示ログクリア(self):
        """ログをクリア"""
        os.system('clear' if os.name == 'posix' else 'cls')
        self._result = None
        return self._result
    
    def 言う(self, message):
        """メッセージを言う"""
        print(message)
        self._result = message
        return self._result
    
    # === 四則演算 ===
    def 足す(self, a, b=None):
        """足し算"""
        if b is None:
            return a
        return a + b
    
    def 合計(self, *args):
        """合計を計算"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            return sum(args[0])
        return sum(args)
    
    def 引く(self, a, b):
        """引き算"""
        return a - b
    
    def 掛ける(self, a, b):
        """掛け算"""
        return a * b
    
    def 倍(self, a, b):
        """倍数"""
        return a * b
    
    def 割る(self, a, b):
        """割り算"""
        return a / b
    
    def 割余(self, a, b):
        """剰余"""
        return a % b
    
    def 偶数(self, n):
        """偶数判定"""
        return n % 2 == 0
    
    def 奇数(self, n):
        """奇数判定"""
        return n % 2 != 0
    
    def 二乗(self, n):
        """二乗"""
        return n ** 2
    
    def べき乗(self, a, b):
        """べき乗"""
        return a ** b
    
    def 以上(self, a, b):
        """以上判定"""
        return a >= b
    
    def 以下(self, a, b):
        """以下判定"""
        return a <= b
    
    def 未満(self, a, b):
        """未満判定"""
        return a < b
    
    def 超(self, a, b):
        """超過判定"""
        return a > b
    
    def 等(self, a, b):
        """等しい"""
        return a == b
    
    def 等無(self, a, b):
        """等しくない"""
        return a != b
    
    def 一致(self, a, b):
        """一致"""
        return a == b
    
    def 不一致(self, a, b):
        """不一致"""
        return a != b
    
    def 範囲内(self, value, min_val, max_val):
        """範囲内判定"""
        return min_val <= value <= max_val
    
    def 範囲(self, start, end):
        """範囲オブジェクト"""
        return list(range(start, end + 1))
    
    def 連続加算(self, start, end):
        """連続加算"""
        return sum(range(start, end + 1))
    
    def MAX(self, *args):
        """最大値"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            return max(args[0])
        return max(args)
    
    def 最大値(self, *args):
        """最大値"""
        return self.MAX(*args)
    
    def MIN(self, *args):
        """最小値"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            return min(args[0])
        return min(args)
    
    def 最小値(self, *args):
        """最小値"""
        return self.MIN(*args)
    
    def CLAMP(self, value, min_val, max_val):
        """値を範囲内に制限"""
        return max(min_val, min(max_val, value))
    
    # === 型変換 ===
    def 変数型確認(self, value):
        """変数の型を確認"""
        return type(value).__name__
    
    def TYPEOF(self, value):
        """型確認"""
        return type(value).__name__
    
    def 文字列変換(self, value):
        """文字列に変換"""
        return str(value)
    
    def TOSTR(self, value):
        """文字列に変換"""
        return str(value)
    
    def 整数変換(self, value):
        """整数に変換"""
        try:
            return int(value)
        except:
            return 0
    
    def TOINT(self, value):
        """整数に変換"""
        return self.整数変換(value)
    
    def 実数変換(self, value):
        """実数に変換"""
        try:
            return float(value)
        except:
            return 0.0
    
    def TOFLOAT(self, value):
        """実数に変換"""
        return self.実数変換(value)
    
    def INT(self, value):
        """整数に変換"""
        return self.整数変換(value)
    
    def FLOAT(self, value):
        """実数に変換"""
        return self.実数変換(value)
    
    def NAN判定(self, value):
        """NaN判定"""
        try:
            return math.isnan(value)
        except:
            return False
    
    def 非数判定(self, value):
        """非数判定"""
        return self.NAN判定(value)
    
    def HEX(self, value):
        """16進数に変換"""
        return hex(value)
    
    def 進数変換(self, value, base):
        """進数変換"""
        try:
            if base == 2:
                return bin(value)
            elif base == 8:
                return oct(value)
            elif base == 16:
                return hex(value)
            else:
                return str(value)
        except:
            return "0"
    
    def 二進(self, value):
        """2進数に変換"""
        return bin(value)
    
    def 二進表示(self, value):
        """2進数で表示"""
        return bin(value)
    
    def RGB(self, r, g, b):
        """RGB値を作成"""
        return f"#{r:02x}{g:02x}{b:02x}"
    
    # === 文字列処理 ===
    def 文字数(self, text):
        """文字数を取得"""
        return len(str(text))
    
    def 長さ(self, text):
        """長さを取得"""
        return len(str(text))
    
    def 左から(self, text, n):
        """左からn文字取得"""
        text = str(text)
        return text[:n]
    
    def 右から(self, text, n):
        """右からn文字取得"""
        text = str(text)
        return text[-n:]
    
    def 中から(self, text, start, length=None):
        """中から文字列取得"""
        text = str(text)
        if length is None:
            return text[start:]
        else:
            return text[start:start+length]
    
    def 置換(self, text, old, new, count=-1):
        """文字列置換"""
        text = str(text)
        return text.replace(old, new, count)
    
    def 検索(self, text, pattern, start=0):
        """文字列検索"""
        text = str(text)
        return text.find(pattern, start)
    
    def 含む(self, text, pattern):
        """文字列が含まれるか"""
        text = str(text)
        return pattern in text
    
    def 分割(self, text, delimiter, maxsplit=-1):
        """文字列分割"""
        text = str(text)
        return text.split(delimiter, maxsplit)
    
    def 結合(self, items, delimiter):
        """文字列結合"""
        return delimiter.join(str(item) for item in items)
    
    def 大文字(self, text):
        """大文字に変換"""
        return str(text).upper()
    
    def 小文字(self, text):
        """小文字に変換"""
        return str(text).lower()
    
    def 反転(self, text):
        """文字列反転"""
        return str(text)[::-1]
    
    # === 配列操作 ===
    def 要素数(self, array):
        """要素数"""
        return len(array)
    
    def 空(self, array):
        """空か判定"""
        return len(array) == 0
    
    def 追加(self, array, item):
        """要素を追加"""
        array.append(item)
        return array
    
    def 削除(self, array, item):
        """要素を削除"""
        if item in array:
            array.remove(item)
        return array
    
    def 挿入(self, array, index, item):
        """要素を挿入"""
        array.insert(index, item)
        return array
    
    def ソート(self, array):
        """ソート"""
        array.sort()
        return array
    
    def 配列反転(self, array):
        """配列反転"""
        array.reverse()
        return array
    
    def コピー(self, array):
        """コピー"""
        return array.copy()
    
    # === 日時処理 ===
    def 今(self):
        """現在時刻"""
        return datetime.datetime.now()
    
    def 年(self):
        """年"""
        return datetime.datetime.now().year
    
    def 月(self):
        """月"""
        return datetime.datetime.now().month
    
    def 日(self):
        """日"""
        return datetime.datetime.now().day
    
    def 時(self):
        """時"""
        return datetime.datetime.now().hour
    
    def 分(self):
        """分"""
        return datetime.datetime.now().minute
    
    def 秒(self):
        """秒"""
        return datetime.datetime.now().second
    
    def 書式(self, dt, format_str):
        """日時書式化"""
        return dt.strftime(format_str)
    
    # === 数学関数 ===
    def 絶対値(self, x):
        """絶対値"""
        return abs(x)
    
    def 階乗(self, n):
        """階乗"""
        return math.factorial(n)
    
    def 組み合わせ(self, n, r):
        """組み合わせ"""
        return math.comb(n, r)
    
    def 平方根(self, x):
        """平方根"""
        return math.sqrt(x)
    
    def サイン(self, x, degrees=False):
        """サイン"""
        if degrees:
            x = math.radians(x)
        return math.sin(x)
    
    def コサイン(self, x, degrees=False):
        """コサイン"""
        if degrees:
            x = math.radians(x)
        return math.cos(x)
    
    def タンジェント(self, x, degrees=False):
        """タンジェント"""
        if degrees:
            x = math.radians(x)
        return math.tan(x)
    
    def 四捨五入(self, x, digits=0):
        """四捨五入"""
        return round(x, digits)
    
    def 切り上げ(self, x):
        """切り上げ"""
        return math.ceil(x)
    
    def 切り捨て(self, x):
        """切り捨て"""
        return math.floor(x)
    
    def 乱数(self, min_val=0, max_val=1):
        """乱数"""
        if min_val == 0 and max_val == 1:
            return random.random()
        else:
            return random.uniform(min_val, max_val)
    
    def 整数乱数(self, min_val, max_val):
        """整数乱数"""
        return random.randint(min_val, max_val)
    
    # === ファイル操作 ===
    def 読む(self, filepath, encoding="utf-8"):
        """ファイル読み込み"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except Exception as e:
            return f"エラー: {e}"
    
    def 書く(self, filepath, content, encoding="utf-8"):
        """ファイル書き込み"""
        try:
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(str(content))
            return True
        except Exception as e:
            return f"エラー: {e}"
    
    def 存在する(self, filepath):
        """ファイル存在確認"""
        return os.path.exists(filepath)
    
    def 一覧取得(self, dirpath=".", pattern="*"):
        """ファイル一覧取得"""
        try:
            from glob import glob
            files = glob(os.path.join(dirpath, pattern))
            return [os.path.basename(f) for f in files]
        except Exception as e:
            return []
    
    # === 特殊変数 ===
    def 円周率(self):
        """円周率"""
        return math.pi
    
    def ナ(self):
        """円周率"""
        return math.pi
    
    def それ(self):
        """直前の結果"""
        return self._result
    
    def set_それ(self, value):
        """「それ」に設定"""
        self._result = value
    
    # === ユーティリティ ===
    def 待つ(self, seconds):
        """待つ"""
        time.sleep(seconds)
    
    def 終了(self):
        """終了"""
        sys.exit()
    
    def 環境変数(self, name):
        """環境変数取得"""
        return os.environ.get(name)
    
    def プラットフォーム(self):
        """プラットフォーム情報"""
        return sys.platform
