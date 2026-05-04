# プログラム本体ガイド / Core Files Guide

## 🎯 プログラムの本体（主要な実装）

### 💡 どのファイルを見ればいいか？

**🌟 主要な本体ファイル**
- **`src/nadesiko_complete.py`** - なでしこ3の全機能を実装したメイン本体
- **`src/nadesiko_parser.py`** - なでしこ文法をPythonに変換するパーサー本体
- **`src/nadesiko_keywords.py`** - なでしこのキーワードと命令を定義

---

## 📁 本体ファイルの詳細

### 🏆 1. nadesiko_complete.py - メイン本体

**📍 場所**: `src/nadesiko_complete.py`  
**🎯 役割**: なでしこ3の全機能（300+命令）を実装した完全互換クラス

**🔧 主要な機能**
```python
class NadesikoComplete:
    """なでしこ3の全機能を実装した完全互換クラス"""
    
    def __init__(self):
        self._result = None
        self.variables = {}
        self._setup_system_constants()
    
    # 数学関数
    def 円周率(self):
        return math.pi
    
    def 階乗(self, n):
        return math.factorial(n)
    
    # 文字列操作
    def 文字列連結(self, str1, str2):
        return str1 + str2
    
    # ファイル操作
    def ファイル読込(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    # 日時処理
    def 現在時刻(self):
        return datetime.datetime.now()
    
    # その他300以上の命令...
```

**📊 実装されている機能カテゴリ**
- 🔢 数学関数（50+関数）
- 📝 文字列操作（100+関数）
- 📁 ファイル操作（50+関数）
- 🖥️ GUI機能（30+関数）
- 🌐 ネットワーク（20+関数）
- 🗄️ データベース（15+関数）
- 🎵 マルチメディア（20+関数）
- 🤖 機械学習（10+関数）

### 🎮 2. nadesiko_parser.py - パーサー本体

**📍 場所**: `src/nadesiko_parser.py`  
**🎯 役割**: なでしこ文法をPythonコードに変換する心臓部

**🔧 変換プロセス**
```python
class NadesikoParser:
    """なでしこ3互換のパーサー"""
    
    def parse_line(self, line):
        """一行のなでしこコードをPythonコードに変換"""
        # 助詞で分割
        words = NadesikoKeywords.split_by_particles(line)
        
        # 基本パターンのマッチング
        python_code = self._match_patterns(line, words)
        
        return python_code
    
    def _match_patterns(self, original_line, words):
        """なでしこの文法パターンをマッチング"""
        
        # 表示系: 「〜を表示」「〜と言う」
        if any(word in original_line for word in ['を表示', 'を表示する']):
            content = self._extract_content(original_line, ['を表示'])
            return f"print({self._translate_expression(content)})"
        
        # 代入系: 「Aは10」「Aに20を代入」
        if 'は' in original_line or 'に' in original_line:
            return self._parse_assignment(original_line)
        
        # 計算系: 「AとBを足す」「AからBを引く」
        if any(word in original_line for word in ['と', 'から', 'を']):
            return self._parse_calculation(original_line)
```

**🔄 変換例**
```nadesiko
# なでしこコード
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示

    ↓ パーサーによる変換

# Pythonコード
A = 10
B = 20
C = A + B
print(f"合計: {C}")
```

### 📚 3. nadesiko_keywords.py - キーワード定義

**📍 場所**: `src/nadesiko_keywords.py`  
**🎯 役割**: なでしこのキーワードと命令をPythonに対応付ける辞書

**📋 主要な定義**
```python
class NadesikoKeywords:
    """なでしこ3のキーワード定義"""
    
    # 基本命令の辞書
    NADESIKO_COMMANDS = {
        # 表示系
        "表示": "print",
        "言う": "print",
        "出力": "print",
        
        # 計算系
        "足す": "+",
        "引く": "-",
        "掛ける": "*",
        "割る": "/",
        
        # 比較系
        "等しい": "==",
        "大きい": ">",
        "小さい": "<",
        
        # 論理系
        "そして": "and",
        "または": "or",
        "ではない": "not",
        
        # その他300以上の命令...
    }
    
    # 助詞の定義
    PARTICLES = ["は", "が", "を", "に", "へ", "と", "から", "まで", "で", "の"]
    
    # システム定数
    SYSTEM_CONSTANTS = {
        "ナデシコバージョン": "3.0.0",
        "真": True,
        "偽": False,
        "改行": "\n",
        "タブ": "\t",
    }
```

---

## 🔧 その他の重要な本体ファイル

### 🌏 4. bilingual_parser.py - バイリンガル対応

**📍 場所**: `src/bilingual_parser.py`  
**🎯 役割**: 日本語と英語を自動検出して適切なパーサーを選択

```python
class BilingualParser:
    """日本語と英語のバイリンガルパーサー"""
    
    def detect_language(self, code):
        """コードの言語を自動検出"""
        japanese_chars = len(re.findall(r'[ひらがなカタカナ]', code))
        english_words = len(re.findall(r'[a-zA-Z]+', code))
        
        if japanese_chars > english_words:
            return 'ja'
        else:
            return 'en'
    
    def parse(self, code):
        """言語を検出して適切なパーサーで処理"""
        lang = self.detect_language(code)
        
        if lang == 'ja':
            return self.nadesiko_parser.parse(code)
        else:
            return self.english_parser.parse(code)
```

### 🇺🇸 5. english_parser.py - 英語対応

**📍 場所**: `src/english_parser.py`  
**🎯 役割**: 英語プログラミング文法の処理

```python
class EnglishParser:
    """英語プログラミング用のパーサー"""
    
    def parse_line(self, line):
        """英語コードをPythonに変換"""
        # "A is 10" → "A = 10"
        if ' is ' in line:
            return self._parse_assignment(line)
        
        # "A plus B" → "A + B"
        if ' plus ' in line:
            return self._parse_calculation(line)
        
        # "show message" → "print(message)"
        if line.startswith('show '):
            return self._parse_display(line)
```

### 🎨 6. nadesiko_complete_commands.py - 高度な機能

**📍 場所**: `src/nadesiko_complete_commands.py`  
**🎯 役割**: GUI、ネットワーク、AIなどの高度な機能

```python
class NadesikoCompleteCommands:
    """高度ななでしこ3命令の実装"""
    
    # GUI機能
    def ウィンドウ作成(self, title, width, height):
        import tkinter as tk
        window = tk.Tk()
        window.title(title)
        window.geometry(f"{width}x{height}")
        return window
    
    # ネットワーク機能
    def HTTP取得(self, url):
        import requests
        response = requests.get(url)
        return response.text
    
    # AI機能
    def AI対話(self, prompt):
        # AIとの対話処理
        return ai_response
```

---

## 🎯 本体の理解のための見方

### 📖 最初に見るべき順番

**1. nadesiko_complete.py**
- なでしこ3の全機能が実装されているメイン本体
- 300以上の命令がどのように実装されているか

**2. nadesiko_parser.py**
- なでしこ文法がPythonに変換される仕組み
- 助詞区切りの処理方法

**3. nadesiko_keywords.py**
- なでしこの命令がPythonに対応付けられている辞書
- 新しい命令を追加する方法

### 🔍 特定の機能を見たい場合

**🔢 数学機能を見たい**
```python
# nadesiko_complete.py の数学関数セクション
def 円周率(self):
    return math.pi

def 三角関数(self, angle):
    return math.sin(math.radians(angle))
```

**📝 文字列操作を見たい**
```python
# nadesiko_complete.py の文字列操作セクション
def 文字列連結(self, str1, str2):
    return str1 + str2

def 文字列置換(self, text, old, new):
    return text.replace(old, new)
```

**🌐 ネットワーク機能を見たい**
```python
# nadesiko_complete_commands.py のネットワークセクション
def HTTP取得(self, url):
    import requests
    response = requests.get(url)
    return response.text
```

---

## 🎮 実際の使用例

### 💻 基本的な使い方

```python
from nadesiko3_python import NadesikoComplete

# 本体クラスのインスタンス化
nadesiko = NadesikoComplete()

# なでしこ命令の実行
result = nadesiko.円周率()
print(result)  # 3.141592653589793

result = nadesiko.文字列連結("Hello", "World")
print(result)  # "HelloWorld"
```

### 🔄 パーサーを使った変換

```python
from nadesiko3_python import NadesikoParser

# パーサーのインスタンス化
parser = NadesikoParser()

# なでしこコードの変換
code = "Aは10"
python_code = parser.parse_line(code)
print(python_code)  # "A = 10"
```

---

## 🎯 まとめ

**🏆 メイン本体は3つのファイル**
1. **`nadesiko_complete.py`** - なでしこ3の全機能実装（300+命令）
2. **`nadesiko_parser.py`** - なでしこ文法の変換エンジン
3. **`nadesiko_keywords.py`** - なでしこ命令の辞書定義

**🔧 これらがプログラムの心臓部**
- なでしこコードをPythonに変換
- 300以上の命令を実装
- 日本語と英語の両方に対応

**📚 見るべき順番**
1. まず `nadesiko_complete.py` で全体像を理解
2. 次に `nadesiko_parser.py` で変換仕組みを理解
3. 最後に `nadesiko_keywords.py` で命令定義を理解

これらのファイルが、あなたのビジョンを実現するための技術的な基盤です！
