# Pythonモジュールとしての使用方法

## 基本的な使い方

### 1. インストール

```bash
# 直接使用する場合
cd /path/to/japanese_programming
python3 -c "import sys; sys.path.insert(0, '.'); from japanese_programming import NadesikoParser"

# pipでインストールする場合
pip install -e .
```

### 2. 基本プログラミング

```python
from japanese_programming import NadesikoParser

# パーサーを作成
parser = NadesikoParser()

# なでしこコードを実行
code = '''
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
'''

parser.execute(code)
```

### 3. 完全版クラスの使用

```python
from japanese_programming import NadesikoComplete

# 完全版クラスを作成
nadesiko = NadesikoComplete()

# 基本機能
print(f"円周率: {nadesiko.円周率()}")
print(f"階乗(5): {nadesiko.階乗(5)}")
print(f"文字数: {nadesiko.文字数('こんにちは')}")

# 数学関数
print(f"サイン(90): {nadesiko.サイン(90, degrees=True)}")
print(f"組み合わせ(5,2): {nadesiko.組み合わせ(5, 2)}")

# 文字列操作
text = "Pythonプログラミング"
print(f"大文字: {nadesiko.大文字(text)}")
print(f"反転: {nadesiko.反転(text)}")
```

### 4. GUI機能の使用

```python
from japanese_programming import NadesikoCompleteCommands

# GUIコマンドを作成
gui = NadesikoCompleteCommands()

# メッセージボックス
gui.メッセージボックス("タイトル", "メッセージ")

# 入力ボックス
name = gui.入力ボックス("入力", "名前を入力してください")
print(f"入力された名前: {name}")

# ファイル選択
filepath = gui.ファイル選択("ファイル選択")
print(f"選択されたファイル: {filepath}")
```

### 5. バイリンガル対応

```python
from japanese_programming import BilingualParser

# バイリンガルパーサーを作成
parser = BilingualParser()

# 日本語コード
japanese_code = '''
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
'''

# 英語コード
english_code = '''
A is 10
B is 20
C is A plus B
show "Total: {C}"
'''

# 自動言語検出で実行
parser.execute(japanese_code)  # 日本語として実行
parser.execute(english_code)  # 英語として実行
```

### 6. 高度な機能の使用

```python
from japanese_programming import NadesikoCompleteCommands

# 高度なコマンドを作成
commands = NadesikoCompleteCommands()

# ネットワーク機能
try:
    result = commands.HTTP取得("https://httpbin.org/get")
    print(f"HTTP GET結果: {result[:100]}...")
except Exception as e:
    print(f"ネットワークエラー: {e}")

# データベース機能
try:
    conn = commands.SQLite3接続(":memory:")
    commands.テーブル作成(conn, "users", "id INTEGER PRIMARY KEY, name TEXT")
    commands.挿入(conn, "users", (1, "なでしこ"))
    data = commands.選択(conn, "users")
    print(f"データベースデータ: {data}")
    conn.close()
except Exception as e:
    print(f"データベースエラー: {e}")
```

### 7. クラスとしての継承

```python
from japanese_programming import NadesikoComplete

class MyNadesikoApp(NadesikoComplete):
    def __init__(self):
        super().__init__()
        self.app_name = "私のなでしこアプリ"
    
    def アプリ起動(self):
        print(f"{self.app_name}を起動しました")
        print(f"バージョン: {self.ナデシコバージョン()}")
    
    def 独自機能(self, data):
        # 独自の機能を追加
        processed_data = self.大文字(data)
        return f"処理済み: {processed_data}"

# 使用例
app = MyNadesikoApp()
app.アプリ起動()
result = app.独自機能("hello world")
print(result)
```

### 8. モジュールの全機能確認

```python
import japanese_programming

# 利用可能なクラスの一覧
print("利用可能なクラス:")
for cls_name in japanese_programming.__all__:
    print(f"  - {cls_name}")

# モジュール情報
print(f"\nモジュール名: {japanese_programming.__name__}")
print(f"バージョン: {japanese_programming.__version__}")
print(f"作者: {japanese_programming.__author__}")
```

### 9. エラーハンドリング

```python
from japanese_programming import NadesikoParser

parser = NadesikoParser()

try:
    # なでしこコードを実行
    code = '''
    Aは10
    Bは0
    CはAをBで割る  # 0除算エラー
    「結果: {C}」を表示
    '''
    parser.execute(code)
except Exception as e:
    print(f"エラーが発生しました: {e}")
    print("プログラムを続行します...")
```

### 10. パフォーマンスの最適化

```python
from japanese_programming import NadesikoParser

# パーサーを再利用
parser = NadesikoParser()

# 複数のコードを効率的に実行
codes = [
    "Aは10",
    "Bは20", 
    "CはAとBを足す",
    "「結果: {C}」を表示"
]

for code in codes:
    parser.execute(code)
```

## 注意事項

1. **Pythonバージョン**: Python 3.6以上が必要です
2. **依存関係**: 一部の高度な機能では追加のライブラリが必要です
3. **GUI機能**: tkinterがインストールされている必要があります
4. **ネットワーク機能**: requestsライブラリが必要です
5. **データベース機能**: sqlite3モジュールが必要です（Python標準）

## サポートされている機能

- ✅ 基本プログラミング（変数、計算、制御構文）
- ✅ 数学関数（300以上の関数）
- ✅ 文字列操作（100以上の関数）
- ✅ ファイル操作（50以上の関数）
- ✅ GUI機能（30以上のウィジェット）
- ✅ ネットワーク機能（HTTP、JSON、WebSocket）
- ✅ データベース機能（SQLite3）
- ✅ マルチメディア機能（画像、音声、動画）
- ✅ 機械学習機能（基本的なアルゴリズム）
- ✅ バイリンガル対応（日本語・英語）

このモジュールは、標準的なPythonモジュールとして完全に機能し、なでしこ3のほぼ全機能を提供します。
