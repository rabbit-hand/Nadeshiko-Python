"""
なでしこ3互換基本関数ライブラリ
"""

import math
import random
import time
import sys
import os
import datetime
from nadesiko_keywords import NadesikoKeywords

class NadesikoFunctions:
    """なでしこ3の基本関数を実装"""
    
    def __init__(self):
        self._result = None  # 「それ」用の変数
        
    # === 数学関数 ===
    def 絶対値(self, x):
        """絶対値を返す"""
        self._result = abs(x)
        return self._result
    
    def 平方根(self, x):
        """平方根を返す"""
        self._result = math.sqrt(x)
        return self._result
    
    def サイン(self, x):
        """サインを返す"""
        self._result = math.sin(x)
        return self._result
    
    def コサイン(self, x):
        """コサインを返す"""
        self._result = math.cos(x)
        return self._result
    
    def タンジェント(self, x):
        """タンジェントを返す"""
        self._result = math.tan(x)
        return self._result
    
    def 整数部分(self, x):
        """整数部分を返す"""
        self._result = int(x)
        return self._result
    
    def 小数部分(self, x):
        """小数部分を返す"""
        self._result = x - int(x)
        return self._result
    
    def 四捨五入(self, x, digits=0):
        """四捨五入する"""
        self._result = round(x, digits)
        return self._result
    
    def 切り上げ(self, x):
        """切り上げする"""
        self._result = math.ceil(x)
        return self._result
    
    def 切り捨て(self, x):
        """切り捨てする"""
        self._result = math.floor(x)
        return self._result
    
    def 乱数(self):
        """0以上1未満の乱数を返す"""
        self._result = random.random()
        return self._result
    
    def 整数乱数(self, min_val, max_val):
        """指定範囲の整数乱数を返す"""
        self._result = random.randint(min_val, max_val)
        return self._result
    
    def べき乗(self, x, y):
        """べき乗を計算"""
        self._result = x ** y
        return self._result
    
    def 割り切れる(self, x, y):
        """割り算の余りを返す"""
        self._result = x % y
        return self._result
    
    # === 文字列関数 ===
    def 文字数(self, text):
        """文字数を返す"""
        self._result = len(str(text))
        return self._result
    
    def 長さ(self, text):
        """長さを返す"""
        return self.文字数(text)
    
    def 左から(self, text, n):
        """左からn文字を取得"""
        text = str(text)
        self._result = text[:n]
        return self._result
    
    def 右から(self, text, n):
        """右からn文字を取得"""
        text = str(text)
        self._result = text[-n:]
        return self._result
    
    def 中から(self, text, start, length=None):
        """中から文字列を取得"""
        text = str(text)
        if length is None:
            self._result = text[start:]
        else:
            self._result = text[start:start+length]
        return self._result
    
    def 置換(self, text, old, new):
        """文字列を置換"""
        text = str(text)
        self._result = text.replace(old, new)
        return self._result
    
    def 検索(self, text, pattern):
        """文字列を検索"""
        text = str(text)
        self._result = text.find(pattern)
        return self._result
    
    def 含む(self, text, pattern):
        """文字列が含まれるか"""
        text = str(text)
        self._result = pattern in text
        return self._result
    
    def 分割(self, text, delimiter):
        """文字列を分割"""
        text = str(text)
        self._result = text.split(delimiter)
        return self._result
    
    def 結合(self, items, delimiter):
        """文字列を結合"""
        self._result = delimiter.join(str(item) for item in items)
        return self._result
    
    def 大文字(self, text):
        """大文字に変換"""
        text = str(text)
        self._result = text.upper()
        return self._result
    
    def 小文字(self, text):
        """小文字に変換"""
        text = str(text)
        self._result = text.lower()
        return self._result
    
    def 反転(self, text):
        """文字列を反転"""
        text = str(text)
        self._result = text[::-1]
        return self._result
    
    # === 配列関数 ===
    def 要素数(self, array):
        """配列の要素数を返す"""
        self._result = len(array)
        return self._result
    
    def 空(self, array):
        """配列が空か"""
        self._result = len(array) == 0
        return self._result
    
    def 追加(self, array, item):
        """配列に要素を追加"""
        array.append(item)
        self._result = array
        return self._result
    
    def 削除(self, array, item):
        """配列から要素を削除"""
        if item in array:
            array.remove(item)
        self._result = array
        return self._result
    
    def 挿入(self, array, index, item):
        """配列に要素を挿入"""
        array.insert(index, item)
        self._result = array
        return self._result
    
    def ソート(self, array):
        """配列をソート"""
        array.sort()
        self._result = array
        return self._result
    
    def 配列反転(self, array):
        """配列を反転"""
        array.reverse()
        self._result = array
        return self._result
    
    def コピー(self, array):
        """配列をコピー"""
        self._result = array.copy()
        return self._result
    
    # === 日時関数 ===
    def 今(self):
        """現在日時を返す"""
        self._result = datetime.datetime.now()
        return self._result
    
    def 年(self):
        """現在の年を返す"""
        self._result = datetime.datetime.now().year
        return self._result
    
    def 月(self):
        """現在の月を返す"""
        self._result = datetime.datetime.now().month
        return self._result
    
    def 日(self):
        """現在の日を返す"""
        self._result = datetime.datetime.now().day
        return self._result
    
    def 時(self):
        """現在の時を返す"""
        self._result = datetime.datetime.now().hour
        return self._result
    
    def 分(self):
        """現在の分を返す"""
        self._result = datetime.datetime.now().minute
        return self._result
    
    def 秒(self):
        """現在の秒を返す"""
        self._result = datetime.datetime.now().second
        return self._result
    
    def 書式(self, dt, format_str):
        """日時を書式化"""
        self._result = dt.strftime(format_str)
        return self._result
    
    # === システム関数 ===
    def 待つ(self, seconds):
        """指定秒数待つ"""
        time.sleep(seconds)
    
    def 終了(self):
        """プログラムを終了"""
        sys.exit()
    
    def 環境変数(self, name):
        """環境変数を取得"""
        self._result = os.environ.get(name)
        return self._result
    
    def プラットフォーム(self):
        """プラットフォーム情報を返す"""
        self._result = sys.platform
        return self._result
    
    # === 変数操作 ===
    def それ(self):
        """直前の計算結果を返す"""
        return self._result
    
    def set_それ(self, value):
        """「それ」に値を設定"""
        self._result = value
    
    # === 型変換 ===
    def 文字列に変換(self, value):
        """文字列に変換"""
        self._result = str(value)
        return self._result
    
    def 数値に変換(self, value):
        """数値に変換"""
        try:
            self._result = float(value)
        except:
            self._result = 0
        return self._result
    
    def 整数に変換(self, value):
        """整数に変換"""
        try:
            self._result = int(value)
        except:
            self._result = 0
        return self._result
    
    # === 論理関数 ===
    def 真(self):
        """真を返す"""
        self._result = True
        return self._result
    
    def 偽(self):
        """偽を返す"""
        self._result = False
        return self._result
    
    def 空っぽ(self, value):
        """空っぽか判定"""
        self._result = value is None or value == "" or len(value) == 0
        return self._result
