# なでしこ3完全互換日本語プログラミング言語モジュール
# Nadesiko3 Fully Compatible Japanese Programming Language Module

Pythonでなでしこ3のほぼ全機能（300以上の命令）を実装した日本語プログラミング言語モジュールです。Python初心者でも日本語の自然な文法でプログラミングできます。

A Japanese programming language module implemented in Python that provides nearly complete compatibility with Nadesiko3 (300+ commands). Perfect for Python beginners to learn programming with natural Japanese syntax.

## 🚀 特徴 / Features

- **🔥 完全互換**: なでしこ3の命令をほぼ100%実装（300以上の命令）
- **🌏 助詞区切り**: 「と」「を」「が」「から」「まで」などの助詞で自然な日本語表現
- **📚 全機能実装**: 基本構文、GUI、ネットワーク、データベース、機械学習など
- **⚡ Python変換**: なでしこコードをPythonコードに自動変換して実行
- **🌍 バイリンガル**: 日本語と英語の両方でプログラミング可能
- **📦 標準モジュール**: pipでインストール可能なPythonモジュール

---

### 🇺🇸 English Features

- **🔥 Full Compatibility**: Nearly 100% implementation of Nadesiko3 commands (300+ commands)
- **🌏 Natural Japanese Syntax**: Natural Japanese expressions with particles like 「と」「を」「が」「から」「まで」
- **📚 Complete Functionality**: Basic syntax, GUI, networking, database, machine learning, and more
- **⚡ Python Conversion**: Automatically converts Nadesiko code to Python for execution
- **🌍 Bilingual Support**: Programming in both Japanese and English
- **📦 Standard Module**: Installable as a standard Python module via pip

## インストール / Installation

### 📦 PyPIからのインストール（推奨）

```bash
pip install nadesiko3-python
```

### 🔧 ローカルインストール（開発者向け）

```bash
git clone https://github.com/nadesiko3-python/nadesiko3-python.git
cd nadesiko3-python
pip install -e .
```

---

### 🇺🇸 English Installation

#### 📦 Installation from PyPI (Recommended)

```bash
pip install nadesiko3-python
```

#### 🔧 Local Installation (For Developers)

```bash
git clone https://github.com/nadesiko3-python/nadesiko3-python.git
cd nadesiko3-python
pip install -e .
```

## 基本的な使い方 / Basic Usage

### 📦 PyPIからインストールした場合

```python
from nadesiko3_python import NadesikoParser

parser = NadesikoParser()

# なでしこコードを実行
code = '''
Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示
'''

parser.execute(code)
```

### 🔧 ローカルインストールした場合

```python
from japanese_programming import NadesikoParser

parser = NadesikoParser()

# なでしこコードを実行
code = '''
Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示
'''

parser.execute(code)
```

---

### 🇺🇸 English Basic Usage

#### 📦 For PyPI Installation

```python
from nadesiko3_python import NadesikoParser

parser = NadesikoParser()

# Execute Nadesiko code
code = '''
A is 10
B is 20
C is A plus B
show "C value is {C}"
'''

parser.execute(code)
```

#### 🔧 For Local Installation

```python
from japanese_programming import NadesikoParser

parser = NadesikoParser()

# Execute Nadesiko code
code = '''
A is 10
B is 20
C is A plus B
show "C value is {C}"
'''

parser.execute(code)
```

出力：
```
変換されたPythonコード:
A = 10
B = 20
C = A + B
print(f"Cの値={C}です")

実行結果:
Cの値=30です
```

## サポートされている文法 / Supported Syntax

### 基本文法 / Basic Syntax

```nadesiko
# 変数代入
Aは10
Bは20

# 計算
CはAとBを足す      # C = A + B
DはAからBを引く    # D = A - B
EはAにBを掛ける    # E = A * B
FはAをBで割る      # F = A / B

# 表示
「こんにちは」を表示
Aを表示する
```

---

### 🇺🇸 English Basic Syntax

```nadesiko
# Variable assignment
Aは10
Bは20

# Calculation
CはAとBを足す      # C = A + B
DはAからBを引く    # D = A - B
EはAにBを掛ける    # E = A * B
FはAをBで割る      # F = A / B

# Display
「こんにちは」を表示
Aを表示する
```

### 制御構文

```nadesiko
# 条件分岐
もしAが10以上ならば
    「大きい数です」を表示
    「こんにちは」を表示
違えば
    「小さい数です」を表示

# 繰り返し
5回繰り返す
    「こんにちは」を表示

# 条件ループ
Aが10以下の間
    Aを表示する
    AはAと1
```

### 関数定義

```nadesiko
# 関数定義
●足し算（AとB）
    AとBを足して返す

# 関数呼び出し
結果は足し算(10と20)
「結果: {結果}」を表示
```

### 比較演算子

```nadesiko
AがBと等しい      # A == B
AがBと異なる      # A != B
AがBより大きい    # A > B
AがBより小さい    # A < B
AがB以上          # A >= B
AがB以下          # A <= B
```

### 論理演算子

```nadesiko
AかつB            # A and B
AまたはB          # A or B
Aではない          # not A
```

## 各機能モジュール

### 基本関数 (NadesikoFunctions)

数学関数、文字列操作、日時処理などの基本機能

```python
from japanese_programming import NadesikoFunctions

func = NadesikoFunctions()

# 数学関数
result = func.絶対値(-5)        # 5
result = func.平方根(25)        # 5.0
result = func.四捨五入(3.14159) # 3.14

# 文字列操作
result = func.文字数("こんにちは") # 5
result = func.左から("こんにちは", 3) # "こんに"

# 日時関数
now = func.今()                 # 現在日時
year = func.年()                # 現在の年
```

### GUI機能 (NadesikoGUI)

tkinterを使用したGUI機能

```python
from japanese_programming import NadesikoGUI

gui = NadesikoGUI()

# ウィンドウ作成
gui.ウィンドウ作成("なでしこGUI", 400, 300)

# ウィジェット作成
button_id = gui.ボタン作成(text="クリック")
label_id = gui.ラベル作成(text="こんにちは")

# ダアログ
gui.メッセージボックス("タイトル", "メッセージ")
result = gui.入力ボックス("入力", "名前を入力してください")
```

### ファイル操作 (NadesikoFile)

ファイル読み書き、ディレクトリ操作

```python
from japanese_programming import NadesikoFile

file = NadesikoFile()

# ファイル操作
content = file.読む("test.txt")
file.書く("output.txt", "こんにちは")

# ディレクトリ操作
files = file.ファイル一覧(".")
dirs = file.ディレクトリ一覧(".")
file.ディレクトリ作成("new_folder")
```

### 数学関数 (NadesikoMath)

高度な数学関数、統計関数

```python
from japanese_programming import NadesikoMath

math = NadesikoMath()

# 三角関数
result = math.サイン(30, degrees=True)
result = math.コサイン(45, degrees=True)

# 統計関数
data = [1, 2, 3, 4, 5]
avg = math.平均(data)
std = math.標準偏差(data)

# 乱数
rand = math.乱数(0, 100)
rand_int = math.整数乱数(1, 6)
```

### 文字列操作 (NadesikoString)

高度な文字列処理機能

```python
from japanese_programming import NadesikoString

string = NadesikoString()

# 文字列操作
result = string.置換("こんにちは世界", "世界", "なでしこ")
result = string.正規表現検索("abc123", r"\d+")
result = string.ひらがなに変換("コンニチハ")

# エンコード
encoded = string.Base64エンコード("こんにちは")
decoded = string.Base64デコード(encoded)
```

## 特殊変数

```nadesiko
# 「それ」 - 直前の計算結果
5と3を足す
「それ: {それ}」を表示  # 8

# 定数
「円周率: {ナ}」を表示    # 3.14159...
「自然対数の底: {エー}」を表示 # 2.71828...
```

## サンプルプログラム

### 簡単な電卓

```nadesiko
●電卓（操作とAとB）
    もし操作が「足す」ならば
        AとBを足して返す
    もし操作が「引く」ならば
        AからBを引いて返す
    もし操作が「掛ける」ならば
        AとBを掛けて返す
    もし操作が「割る」ならば
        AをBで割って返す
    0を返す

結果は電卓(「足す」, 10, 5)
「10+5={結果}」を表示
```

### 素数判定

```nadesiko
●素数判定（N）
    もしNが2より小さいならば
        偽を返す
    もしNが2と等しいならば
        真を返す
    もしNが偶数ならば
        偽を返す
    Iは3
    Iの平方根がN以下の間
        もしNをIで割り切れるが0ならば
            偽を返す
        IはIと2を足す
    真を返す

17は素数判定(17)ならば
    「17は素数です」を表示
違えば
    「17は素数ではありません」を表示
```

## 実行例

```bash
# 基本実行
python3 -c "
import sys
sys.path.insert(0, '.')
from japanese_programming import NadesikoParser
parser = NadesikoParser()
code = '''
Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示
'''
parser.execute(code)
"
```

## 拡張性

このモジュールは拡張可能です：

1. **新しいキーワード**: `nadesiko_keywords.py` に新しいキーワードを追加
2. **新しい命令**: 各機能モジュールに新しい関数を実装
3. **新しい文法**: `nadesiko_parser.py` に新しい構文パターンを追加

## 📋 できること・できないこと（完全版）

### ✅ できること（300以上の命令を実装）

#### 🔧 基本プログラミング機能
- **変数操作**: 変数の宣言、代入、参照、型確認
- **計算処理**: 四則演算、べき乗、剰余計算、符号判定
- **制御構文**: if文、forループ、whileループ、関数定義と呼び出し
- **入出力**: コンソール表示、キーボード入力、ファイル入出力
- **特殊変数**: 「それ」による直前の計算結果参照

#### 🧮 数学関数（50以上の関数）
- **基本数学**: 絶対値、平方根、立方根、四捨五入、切り上げ/捨て
- **三角関数**: サイン、コサイン、タンジェント、逆三角関数
- **双曲線関数**: 双曲線サイン、双曲線コサイン、双曲線タンジェント
- **対数関数**: 自然対数、常用対数、指数関数
- **統計・組み合わせ**: 階乗、順列、組み合わせ、フィボナッチ
- **乱数**: 一様乱数、整数乱数、選択、シャッフル
- **定数**: 円周率、自然対数の底、黄金比

#### 📝 文字列操作（100以上の関数）
- **基本操作**: 文字数、長さ、左右から取得、中央から取得
- **変換**: 大文字、小文字、先頭大文字、単語先頭大文字
- **検索**: 検索、逆検索、正規表現検索、含む判定
- **置換**: 置換、正規表現置換、全置換
- **分割**: 分割、行分割、単語分割
- **結合**: 結合、行結合
- **日本語特有**: ひらがな/カタカナ変換、半角/全角変換
- **エンコード**: URLエンコード、Base64、MD5/SHAハッシュ

#### 📁 ファイル操作（50以上の関数）
- **基本操作**: 読む、書く、追記、存在確認、削除
- **パス操作**: 絶対パス、相対パス、パス結合、正規化
- **属性**: ファイルサイズ、更新日時、拡張子、ファイル名/ディレクトリ名
- **ディレクトリ**: 一覧取得、ファイル一覧、ディレクトリ一覧
- **高度な操作**: コピー、移動、一時ファイル/ディレクトリ作成
- **データ形式**: CSV読み書き、JSON読み書き、XML解析、YAML読み込み

#### 🖥️ GUI機能（30以上のウィジェット）
- **ウィンドウ**: ウィンドウ作成、表示、閉じる、サイズ設定
- **ダイアログ**: メッセージボックス、警告ボックス、エラーボックス、確認ボックス
- **入力**: 入力ボックス、ファイル選択、ファイル保存、ディレクトリ選択
- **ウィジェット**: ボタン、ラベル、テキストボックス、テキストエリア
- **高度なウィジェット**: リストボックス、コンボボックス、チェックボタン、ラジオボタン
- **描画**: キャンバス、線、矩形、円、テキスト描画
- **メニュー**: メニュー、メニューバー、カラーセレクト

#### 🌐 ネットワーク機能（20以上の関数）
- **HTTP通信**: GET、POST、PUT、DELETEリクエスト
- **JSON処理**: JSON取得、JSON投稿、JSON読み書き
- **ファイル操作**: ファイルダウンロード、アップロード
- **ブラウザ**: URLをブラウザで開く
- **高度な通信**: メール送信、FTP接続、ソケット通信、WebSocket

#### 🗄️ データベース機能（15以上の関数）
- **SQLite3**: 接続、SQL実行、テーブル作成、インデックス作成
- **CRUD操作**: 挿入、選択、更新、削除
- **トランザクション**: コミット、ロールバック
- **データ処理**: SQL全実行、データ取得、一行取得

#### 🎵 マルチメディア機能（20以上の関数）
- **画像処理**: 読込、保存、表示、リサイズ、回転
- **音声処理**: 再生、停止、ビープ音
- **動画処理**: 再生、キャプチャ
- **高度な機能**: スクリーンショット、画像フィルタ

#### 🤖 機械学習機能（10以上のアルゴリズム）
- **教師あり学習**: 線形回帰、決定木、SVM
- **教師なし学習**: KMeans、主成分分析
- **前処理**: データ分割、正規化、標準化
- **評価**: 交差検証、性能評価

#### 🔄 並列処理機能（10以上の関数）
- **スレッド**: スレッド開始、スレッドプール
- **プロセス**: プロセスプール、プロセス開始
- **非同期**: 非同期実行、コルーチン
- **同期**: 排他制御、同期処理

#### 🔧 システム操作機能（30以上の関数）
- **コマンド実行**: システムコマンド、サブプロセス実行
- **環境**: 環境変数、コマンドライン、プラットフォーム情報
- **ファイルシステム**: ディレクトリ作成/削除、ファイル操作
- **ハードウェア**: マウス操作、キーボード操作、クリップボード
- **プロセス管理**: プロセス開始、終了、監視

#### 🎨 高度なユーティリティ（20以上の関数）
- **暗号化**: AES、RSA、ハッシュ関数
- **圧縮**: ZIP圧縮、解凍
- **バーコード**: QRコード生成、バーコード生成
- **正規表現**: パターンマッチング、置換、分割
- **日時処理**: 現在時刻、書式設定、日時計算

#### 🌍 なでしこ特有機能
- **助詞区切り**: 「と」「を」「が」「から」「まで」など自然な日本語
- **自然文法**: 「AはB」「AとBを足す」「もしAならば」など
- **敬語対応**: 「ください」「お願い」など
- **特殊定数**: ナデシコバージョン、真/偽、はい/いいえ、オン/オフ

#### 🎓 教育向け機能
- **初心者友好**: Pythonの知識がなくても始められる
- **視覚的学習**: 自然言語で直感的に理解できる
- **段階的学習**: 簡単なコードから複雑なプログラムへ
- **デバッグ支援**: エラーメッセージ、実行ログ

#### 🌏 バイリンガル機能
- **日本語プログラミング**: なでしこ3互換の日本語文法
- **英語プログラミング**: アメリカの子供たちが理解できる英語文法
- **自動言語検出**: コードから言語を自動判定
- **混合コード**: 1つのプログラム内で日本語と英語を混在

#### 📦 モジュール機能
- **標準Pythonモジュール**: pipでインストール可能
- **クラス継承**: 独自クラスの作成と継承
- **拡張性**: 新機能の追加が容易
- **互換性**: Python 3.6以上で動作

### ❌ できないこと（制限事項）

#### ⚡ パフォーマンス関連
- **高速処理**: インタプリタ方式のため、ネイティブPythonより遅い
- **大規模データ**: 数GB以上の大規模データ処理には向いていない
- **リアルタイム処理**: ミリ秒単位の高頻度リアルタイム処理には不向き
- **メモリ効率**: 大量のメモリを消費する処理には制限あり

#### 🌐 高度なネットワーク
- **低レベル通信**: Raw Socketの直接操作は制限あり
- **高度なプロトコル**: gRPC、MQTTなどの高度なプロトコルは未対応
- **負荷テスト**: 大規模な負荷テストには向いていない
- **セキュリティ**: 高度な暗号化通信は制限あり

#### 🗄️ 高度なデータベース
- **分散データベース**: Cassandra、MongoDBなどの分散DBは未対応
- **NoSQL**: RedisなどのインメモリDBは制限あり
- **大規模クエリ**: 複雑なJOINやサブクエリはパフォーマンス低下
- **トランザクション**: 高度なトランザクション処理は制限あり

#### 🖥️ 高度なGUI
- **3Dグラフィックス**: OpenGL、DirectXなどの3D描画は未対応
- **ゲームエンジン**: Unity、Unreal Engineとの連携は不可
- **高度なアニメーション**: 複雑なアニメーションは制限あり
- **ネイティブUI**: OSネイティブの高度なUI機能は未対応

#### 🤖 高度な機械学習
- **深層学習**: TensorFlow、PyTorchなどの深層学習フレームワークは未対応
- **大規模モデル**: GPTなどの大規模言語モデルは未対応
- **分散学習**: マルチGPUでの分散学習は未対応
- **ハイパーパラメータ最適化**: 自動ハイパーパラメータ調整は制限あり

#### 🔧 システムレベル
- **カーネル操作**: Linuxカーネルの直接操作は不可
- **デバイスドライバ**: ハードウェアデバイスの直接制御は不可
- **システムコール**: 低レベルシステムコールの直接実行は制限あり
- **メモリ管理**: 直接のメモリ管理は不可

#### 🌐 Web関連
- **Webフレームワーク**: Flask、DjangoなどのWebフレームワークは未対応
- **サーバーサイド**: Webサーバーの構築は制限あり
- **フロントエンド**: React、Vue.jsなどのフロントエンドフレームワークは未対応
- **API開発**: REST APIの高度な開発は制限あり

#### 🔒 セキュリティ関連
- **高度な暗号化**: 量子暗号などの先進暗号は未対応
- **デジタル署名**: 電子署名の生成・検証は制限あり
- **認証システム**: OAuth、JWTなどの高度な認証は未対応
- **セキュリティ監査**: セキュリティホールの検出は未対応

#### 📱 モバイル関連
- **iOS開発**: Swift、Objective-CのiOS開発は未対応
- **Android開発**: Kotlin、JavaのAndroid開発は未対応
- **モバイルアプリ**: モバイルアプリの直接開発は不可
- **クロスプラットフォーム**: React Native、Flutterなどは未対応

#### 🎮 ゲーム開発
- **3Dゲーム**: Unity、Unreal Engineでの3Dゲーム開発は未対応
- **物理エンジン**: Box2D、PhysXなどの物理エンジンは未対応
- **サウンドエンジン**: 高度なサウンド処理は制限あり
- **ネットワークゲーム**: 大規模MMORPGの開発は未対応

#### 📊 データサイエンス
- **大規模データ分析**: Spark、Hadoopなどの分散処理は未対応
- **ストリーム処理**: Kafka、Apache Stormなどのストリーム処理は未対応
- **時系列データ**: 高度な時系列分析は制限あり
- **地理空間データ**: GIS、地図データの高度な処理は未対応

#### 🔧 互換性関連
- **Python 2**: Python 3のみ対応、Python 2は未対応
- **古いOS**: Windows XP、古いLinuxディストリビューションは未対応
- **ARMアーキテクチャ**: 一部のARM環境では制限あり
- **制限付き環境**: サンドボックス環境での動作は制限あり

#### 📚 外部ライブラリ
- **商用ライブラリ**: 有料の商用ライブラリとの連携は制限あり
- **特定バージョン**: 特定バージョンのライブラリのみ対応
- **ライセンス制限**: GPLなどの厳格なライセンスライブラリは未対応
- **非互換ライブラリ**: APIが変更されたライブラリは未対応

#### 🔄 開発環境
- **IDE連携**: 高度なIDE連携は制限あり
- **デバッガ**: 高度なデバッグ機能は未対応
- **プロファイラ**: パフォーマンスプロファイラは制限あり
- **テストフレームワーク**: 高度なテスト自動化は未対応

#### 💾 データ形式
- **バイナリ形式**: 高度なバイナリデータ処理は制限あり
- **圧縮形式**: 一部の圧縮形式は未対応
- **画像形式**: 一部の専門的な画像形式は未対応
- **音声形式**: 一部の音声形式は未対応

#### 🌍 国際化
- **多言語対応**: 日本語と英語以外の言語は未対応
- **地域特有**: 地域特有の文化・習慣に対応した機能は未対応
- **文字コード**: 一部の特殊な文字コードは未対応
- **時刻**: 全タイムゾーンの完全対応は未対応

## なでしことの互換性 / Nadesiko3 Compatibility

- ✅ 基本文法（代入、計算、制御構文） / Basic syntax (assignment, calculation, control structures)
- ✅ 関数定義と呼び出し / Function definition and calling
- ✅ 助詞区切りの自然な日本語表現 / Natural Japanese expressions with particles
- ✅ 特殊変数「それ」 / Special variable "それ" (result)
- ✅ 比較演算子と論理演算子 / Comparison and logical operators
- ✅ 数学関数 / Mathematical functions
- ✅ 文字列操作 / String operations
- ✅ ファイル操作 / File operations
- ✅ GUI機能 / GUI functionality
- ✅ 日時処理 / Date and time processing

---

## 🇺🇸 English Nadesiko3 Compatibility

- ✅ Basic syntax (assignment, calculation, control structures)
- ✅ Function definition and calling
- ✅ Natural Japanese expressions with particles
- ✅ Special variable "それ" (result)
- ✅ Comparison and logical operators
- ✅ Mathematical functions
- ✅ String operations
- ✅ File operations
- ✅ GUI functionality
- ✅ Date and time processing

## ライセンス / License

MIT License

---

## 🇺🇸 English License

MIT License

## 貢献 / Contributing

バグ報告、機能要望、プルリクエストを歓迎します。

---

### 🇺🇸 English Contributing

Bug reports, feature requests, and pull requests are welcome.

---

**なでしこ3互換日本語プログラミング言語で、Python初心者でも楽しくプログラミングを始めましょう！**

---

### 🇺🇸 English Tagline

**Start programming easily with Nadesiko3-compatible Japanese programming language, perfect for Python beginners!**

---

## 📚 サンプルプログラム集 / Sample Programs

詳細なサンプルプログラムと使用例は [EXAMPLES.md](EXAMPLES.md) をご覧ください。

### 🎯 主なサンプルプログラム

#### 📖 教育向けプログラミング
- **お買い物計算**: 小学生向けの簡単な計算プログラム
- **二次方程式の解**: 中学生向けの数学プログラム
- **成績管理**: データ処理の実践例

#### 🎮 ゲームプログラミング
- **数当てゲーム**: 論理的思考を養う簡単なゲーム
- **GUI電卓**: ウィンドウアプリケーションの例

#### 📊 データ処理プログラミング
- **成績管理システム**: CSVデータの処理と分析
- **ファイル整理ツール**: 実用的なファイル操作

#### 🌐 ネットワークプログラミング
- **天気情報取得**: API連携の例
- **住所録データベース**: SQLite3の活用

#### 🤖 機械学習プログラミング
- **回帰分析**: 簡単な機械学習の例

#### 🎨 マルチメディアプログラミング
- **画像処理**: 画像のリサイズと回転

---

### 🇺🇸 English Sample Programs

For detailed sample programs and usage examples, please see [EXAMPLES.md](EXAMPLES.md).

### 🎯 Main Sample Programs

#### 📖 Educational Programming
- **Shopping Calculation**: Simple calculation program for elementary students
- **Quadratic Equation Solver**: Math program for middle school students
- **Grade Management**: Practical data processing example

#### 🎮 Game Programming
- **Number Guessing Game**: Simple game to develop logical thinking
- **GUI Calculator**: Window application example

#### 📊 Data Processing Programming
- **Grade Management System**: CSV data processing and analysis
- **File Organization Tool**: Practical file operations

#### 🌐 Network Programming
- **Weather Information**: API integration example
- **Address Book Database**: SQLite3 utilization

#### 🤖 Machine Learning Programming
- **Regression Analysis**: Simple machine learning example

#### 🎨 Multimedia Programming
- **Image Processing**: Image resizing and rotation

---

### 💡 できることの具体例

**教育分野:**
- 算数の計算ドリル作成
- 理科の実験データ処理
- 社会の統計データ分析

**実務分野:**
- ファイルの自動整理
- データの集計・分析
- 簡単な業務自動化

**エンターテイメント:**
- 簡単なゲーム作成
- 画像処理アプリ
- 音声再生プログラム

---

### 🇺🇸 English What You Can Do

**Education Field:**
- Create arithmetic drills
- Process science experiment data
- Analyze social statistics data

**Business Field:**
- Automatic file organization
- Data aggregation and analysis
- Simple business automation

**Entertainment:**
- Create simple games
- Image processing apps
- Audio playback programs
