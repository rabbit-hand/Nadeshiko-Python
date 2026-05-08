"""
なでしこ3互換文字列操作ライブラリ
"""

import re
import unicodedata
import base64
import hashlib
import urllib.parse

class NadesikoString:
    """なでしこ3の文字列操作機能を拡張実装"""
    
    def __init__(self):
        self._result = None
    
    # === 基本文字列操作 ===
    def 文字数(self, text):
        """文字数をカウント"""
        self._result = len(str(text))
        return self._result
    
    def 長さ(self, text):
        """長さを取得"""
        return self.文字数(text)
    
    def 左から(self, text, n):
        """左からn文字取得"""
        text = str(text)
        self._result = text[:n]
        return self._result
    
    def 右から(self, text, n):
        """右からn文字取得"""
        text = str(text)
        self._result = text[-n:]
        return self._result
    
    def 中から(self, text, start, length=None):
        """中から文字列取得"""
        text = str(text)
        if length is None:
            self._result = text[start:]
        else:
            self._result = text[start:start+length]
        return self._result
    
    def 置換(self, text, old, new, count=-1):
        """文字列置換"""
        text = str(text)
        self._result = text.replace(old, new, count)
        return self._result
    
    def 全置換(self, text, old, new):
        """全て置換"""
        return self.置換(text, old, new, -1)
    
    def 正規表現置換(self, text, pattern, replacement):
        """正規表現置換"""
        text = str(text)
        self._result = re.sub(pattern, replacement, text)
        return self._result
    
    def 検索(self, text, pattern, start=0):
        """文字列検索"""
        text = str(text)
        self._result = text.find(pattern, start)
        return self._result
    
    def 逆検索(self, text, pattern):
        """後ろから検索"""
        text = str(text)
        self._result = text.rfind(pattern)
        return self._result
    
    def 正規表現検索(self, text, pattern):
        """正規表現検索"""
        text = str(text)
        match = re.search(pattern, text)
        self._result = match if match else None
        return self._result
    
    def 正規表現全検索(self, text, pattern):
        """正規表現全検索"""
        text = str(text)
        self._result = re.findall(pattern, text)
        return self._result
    
    def 含む(self, text, pattern):
        """文字列が含まれるか"""
        text = str(text)
        self._result = pattern in text
        return self._result
    
    def 前から含む(self, text, pattern):
        """前方一致"""
        text = str(text)
        self._result = text.startswith(pattern)
        return self._result
    
    def 後から含む(self, text, pattern):
        """後方一致"""
        text = str(text)
        self._result = text.endswith(pattern)
        return self._result
    
    # === 分割・結合 ===
    def 分割(self, text, delimiter, maxsplit=-1):
        """文字列分割"""
        text = str(text)
        self._result = text.split(delimiter, maxsplit)
        return self._result
    
    def 行分割(self, text):
        """行に分割"""
        text = str(text)
        self._result = text.splitlines()
        return self._result
    
    def 単語分割(self, text):
        """単語に分割"""
        text = str(text)
        self._result = text.split()
        return self._result
    
    def 結合(self, items, delimiter):
        """文字列結合"""
        self._result = delimiter.join(str(item) for item in items)
        return self._result
    
    def 行結合(self, lines):
        """行を結合"""
        self._result = '\n'.join(str(line) for line in lines)
        return self._result
    
    # === 大文字・小文字 ===
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
    
    def 先頭大文字(self, text):
        """先頭を大文字に"""
        text = str(text)
        self._result = text.capitalize()
        return self._result
    
    def 単語先頭大文字(self, text):
        """単語の先頭を大文字に"""
        text = str(text)
        self._result = text.title()
        return self._result
    
    def 入れ替え(self, text):
        """大文字小文字を入れ替え"""
        text = str(text)
        self._result = text.swapcase()
        return self._result
    
    # === 反転・整列 ===
    def 反転(self, text):
        """文字列を反転"""
        text = str(text)
        self._result = text[::-1]
        return self._result
    
    def ソート(self, text):
        """文字をソート"""
        text = str(text)
        self._result = ''.join(sorted(text))
        return self._result
    
    def シャッフル(self, text):
        """文字をシャッフル"""
        import random
        text = str(text)
        chars = list(text)
        random.shuffle(chars)
        self._result = ''.join(chars)
        return self._result
    
    # === 空白操作 ===
    def 空白削除(self, text):
        """前後の空白を削除"""
        text = str(text)
        self._result = text.strip()
        return self._result
    
    def 左空白削除(self, text):
        """左の空白を削除"""
        text = str(text)
        self._result = text.lstrip()
        return self._result
    
    def 右空白削除(self, text):
        """右の空白を削除"""
        text = str(text)
        self._result = text.rstrip()
        return self._result
    
    def 空白統一(self, text):
        """連続する空白を統一"""
        text = str(text)
        self._result = ' '.join(text.split())
        return self._result
    
    def タブ削除(self, text):
        """タブを削除"""
        text = str(text)
        self._result = text.replace('\t', '')
        return self._result
    
    def 改行削除(self, text):
        """改行を削除"""
        text = str(text)
        self._result = text.replace('\n', '').replace('\r', '')
        return self._result
    
    # === 文字種変換 ===
    def ひらがなに変換(self, text):
        """ひらがなに変換"""
        text = str(text)
        # カタカナをひらがなに変換
        self._result = ''.join(
            chr(ord(ch) - 0x60) if 'ァ' <= ch <= 'ン' else ch
            for ch in text
        )
        return self._result
    
    def カタカナに変換(self, text):
        """カタカナに変換"""
        text = str(text)
        # ひらがなをカタカナに変換
        self._result = ''.join(
            chr(ord(ch) + 0x60) if 'ぁ' <= ch <= 'ん' else ch
            for ch in text
        )
        return self._result
    
    def 半角に変換(self, text):
        """半角に変換"""
        text = str(text)
        self._result = unicodedata.normalize('NFKC', text)
        return self._result
    
    def 全角に変換(self, text):
        """全角に変換"""
        text = str(text)
        self._result = unicodedata.normalize('NFKC', text)
        return self._result
    
    # === エンコード ===
    def URLエンコード(self, text):
        """URLエンコード"""
        text = str(text)
        self._result = urllib.parse.quote(text)
        return self._result
    
    def URLデコード(self, text):
        """URLデコード"""
        text = str(text)
        self._result = urllib.parse.unquote(text)
        return self._result
    
    def Base64エンコード(self, text):
        """Base64エンコード"""
        text = str(text)
        text_bytes = text.encode('utf-8')
        self._result = base64.b64encode(text_bytes).decode('utf-8')
        return self._result
    
    def Base64デコード(self, text):
        """Base64デコード"""
        text = str(text)
        try:
            text_bytes = base64.b64decode(text)
            self._result = text_bytes.decode('utf-8')
        except:
            self._result = ""
        return self._result
    
    # === ハッシュ ===
    def MD5ハッシュ(self, text):
        """MD5ハッシュ"""
        text = str(text)
        self._result = hashlib.md5(text.encode('utf-8')).hexdigest()
        return self._result
    
    def SHA1ハッシュ(self, text):
        """SHA1ハッシュ"""
        text = str(text)
        self._result = hashlib.sha1(text.encode('utf-8')).hexdigest()
        return self._result
    
    def SHA256ハッシュ(self, text):
        """SHA256ハッシュ"""
        text = str(text)
        self._result = hashlib.sha256(text.encode('utf-8')).hexdigest()
        return self._result
    
    # === 文字種判定 ===
    def 数字か(self, text):
        """数字のみか"""
        text = str(text)
        self._result = text.isdigit()
        return self._result
    
    def 文字か(self, text):
        """文字のみか"""
        text = str(text)
        self._result = text.isalpha()
        return self._result
    
    def 英数字か(self, text):
        """英数字のみか"""
        text = str(text)
        self._result = text.isalnum()
        return self._result
    
    def ひらがなか(self, text):
        """ひらがなのみか"""
        text = str(text)
        self._result = all('ぁ' <= ch <= 'ん' for ch in text)
        return self._result
    
    def カタカナか(self, text):
        """カタカナのみか"""
        text = str(text)
        self._result = all('ァ' <= ch <= 'ン' for ch in text)
        return self._result
    
    def 漢字か(self, text):
        """漢字のみか"""
        text = str(text)
        self._result = all('\u4e00' <= ch <= '\u9fff' for ch in text)
        return self._result
    
    # === 繰り返し ===
    def 繰り返す(self, text, count):
        """文字列を繰り返す"""
        text = str(text)
        self._result = text * count
        return self._result
    
    def 文字繰り返す(self, char, count):
        """文字を繰り返す"""
        char = str(char)
        self._result = char * count
        return self._result
    
    # === 挿入・削除 ===
    def 挿入(self, text, index, insert_text):
        """文字列を挿入"""
        text = str(text)
        self._result = text[:index] + insert_text + text[index:]
        return self._result
    
    def 削除(self, text, start, end=None):
        """文字列を削除"""
        text = str(text)
        if end is None:
            self._result = text[:start] + text[start+1:]
        else:
            self._result = text[:start] + text[end:]
        return self._result
    
    # === 比較 ===
    def 比較(self, text1, text2):
        """文字列を比較"""
        text1 = str(text1)
        text2 = str(text2)
        if text1 < text2:
            self._result = -1
        elif text1 > text2:
            self._result = 1
        else:
            self._result = 0
        return self._result
    
    def 類似度(self, text1, text2):
        """文字列の類似度（レーベンシュタイン距離）"""
        text1 = str(text1)
        text2 = str(text2)
        
        # レーベンシュタイン距離を計算
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        max_len = max(m, n)
        similarity = (max_len - dp[m][n]) / max_len
        self._result = similarity
        return self._result
    
    # === ユーティリティ ===
    def 引用符追加(self, text, quote='"'):
        """引用符を追加"""
        text = str(text)
        self._result = f"{quote}{text}{quote}"
        return self._result
    
    def 引用符削除(self, text, quotes='"\''):
        """引用符を削除"""
        text = str(text)
        if text and text[0] in quotes and text[-1] in quotes:
            self._result = text[1:-1]
        else:
            self._result = text
        return self._result
    
    def ゼロ埋め(self, text, width):
        """ゼロ埋め"""
        text = str(text)
        self._result = text.zfill(width)
        return self._result
    
    def 空白埋め(self, text, width):
        """空白埋め"""
        text = str(text)
        self._result = text.ljust(width)
        return self._result
    
    def 中央揃え(self, text, width, fillchar=' '):
        """中央揃え"""
        text = str(text)
        self._result = text.center(width, fillchar)
        return self._result
    
    def それ(self):
        """直前の操作結果"""
        return self._result
