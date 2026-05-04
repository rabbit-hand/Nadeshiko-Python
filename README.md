# なでしこパイソン V7.0 / Nadesiko Python V7.0 🌍

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/nadesiko3-python/nadesiko3-python.svg)](https://github.com/nadesiko3-python/nadesiko3-python/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/nadesiko3-python/nadesiko3-python.svg)](https://github.com/nadesiko3-python/nadesiko3-python/network)
[![Version](https://img.shields.io/badge/version-7.0.0-orange.svg)](CHANGELOG.md)

## 🚀 世界を変えるアップデート - World-Changing Update

日本語・英語自然言語プログラミングをPythonで実現する革命的教育プラットフォーム / Revolutionary educational platform for Japanese-English natural language programming in Python

**🆕 V7.0で新登場**: AIパワー、ビジュアルプログラミング、リアルタイム協働、クラウド同期、モバイル対応！

---

## 📋 仕様概要

### 🎯 **プロジェクト概要**
なでしこパイソンは、なでしこV1の「ビジュアルGUIデザイン」とV3の「自然言語プログラミング」の魅力を合体させ、さらに進化させた統合開発環境です。日本語や英語などの自然言語でプログラミングしながら、マウスで直感的にGUIをデザインできる、初心者から上級者まであらゆるレベルのユーザーに対応した4つの主要機能を提供します。

### 🌟 **V1とV3の合体が生んだ4つの機能**
| 機能名 | V1要素 | V3要素 | 合体して生まれた新機能 |
|--------|--------|--------|----------------------|
| 積み木GUIアプリケーション | 積み木操作感覚 | 自然言語プログラミング | V1の直感性とV3の日本語コーディング |
| GUIデザイナー | マウスGUI設計 | Pythonコード生成 | V1のデザイン感覚を現代で進化 |
| モジュールライブラリ | コンポーネント指向 | 自然言語実行 | V1の部品概念とV3の実行環境 |
| コマンドラインパーサー | テキストベース | 日本語構文 | V1のシンプルさとV3の表現力 |

---

## 🧱 積み木GUIアプリケーション

### 📖 **機能仕様**
- **目的**: なでしこV1の積み木感覚とV3の自然言語プログラミングを融合した学習支援
- **対象**: プログラミング初心者、子供、教育者
- **特徴**: V1の直感的操作とV3の日本語プログラミングを合体させた新しい学習体験
- **言語**: 日本語・英語バイリンガル対応

### ⚙️ **技術仕様**
- **フレームワーク**: Tkinterベース
- **アーキテクチャ**: イベント駆動型GUI
- **常駐機能**: タスクトレイアイコンによるバックグラウンド実行

### 🎮 **操作仕様**
1. **起動**: `python start_gui.py`
2. **言語切替**: ツールバーから日本語/英語を選択
3. **プログラミング**: 左側パレットのブロックをクリック
4. **実行**: ▶ボタンでプログラムを実行
5. **保存**: 💾ボタンでプログラムを保存

### 🧩 **ブロック種別**
| カテゴリ | ブロック数 | 主な機能 |
|---------|-----------|----------|
| 基本 | 5種類 | 変数宣言、表示、代入 |
| 数学 | 4種類 | 四則演算 |
| 制御 | 3種類 | 条件分岐、繰り返し |
| 関数 | 2種類 | 関数定義、戻り値 |

### 📊 **対応言語仕様**
#### 🇯🇵 日本語モード
```
変数名は値
AとBを足す
もし条件ならば
回数繰り返す
```

#### 🇺🇸 英語モード
```
variable is value
A plus B
if condition
repeat count times
```

---

## 🎨 GUIデザイナー

### 📖 **機能仕様**
- **目的**: なでしこV1の直感的GUIデザイン体験を現代で再現
- **対象**: GUI開発者、アプリケーションデザイナー、なでしこV1ユーザー
- **特徴**: V1のマウス操作感覚を継承しつつ、Pythonコード自動生成でさらに進化
- **出力**: 実行可能なPythonコード

### ⚙️ **技術仕様**
- **エンジン**: Tkinter Canvasベース
- **部品管理**: オブジェクト指向設計
- **データ形式**: JSONによる設計保存

### 🎮 **操作仕様**
1. **起動**: `python start_gui_designer.py`
2. **部品配置**: 左側パレットから選択しキャンバス上でクリック
3. **編集**: ドラッグで移動、ハンドルでリサイズ
4. **プロパティ**: 右側パネルで詳細設定
5. **コード生成**: 💻ボタンでPythonコードを生成

### 🧩 **対応部品一覧**
| 部品名 | クラス | 主なプロパティ |
|--------|--------|----------------|
| ボタン | tk.Button | text, bg, fg, command |
| ラベル | tk.Label | text, bg, fg, font |
| 入力欄 | tk.Entry | text, bg, fg, font |
| テキスト | tk.Text | text, bg, fg, wrap |
| フレーム | tk.Frame | bg, relief, bd |
| キャンバス | tk.Canvas | bg, highlightthickness |
| リスト | tk.Listbox | bg, fg, font |
| コンボ | ttk.Combobox | values, state |
| チェック | tk.Checkbutton | text, bg, fg |
| ラジオ | tk.Radiobutton | text, bg, fg, value |
| スケール | tk.Scale | from_, to, orient |
| スピン | tk.Spinbox | from_, to, text |

### 🎨 **デザイン機能**
- **グリッド**: 20px間隔のグリッド線表示
- **スナップ**: グリッドへの自動位置合わせ
- **リサイズ**: 8方向ハンドルによる精密調整
- **レイヤー**: 前面・背面移動機能
- **コンテキストメニュー**: 右クリックによる高速操作

---

## 📦 モジュールライブラリ

### 📖 **機能仕様**
- **目的**: 既存Pythonアプリケーションへの自然言語機能統合
- **対象**: Web開発者、データサイエンティスト、アプリ開発者
- **提供形式**: Pythonモジュール

### ⚙️ **技術仕様**
- **モジュール名**: `src.nadesiko_gui_module`
- **スレッド対応**: マルチスレッド実行
- **エラーハンドリング**: 例外処理とロギング

### 🎮 **API仕様**
#### 基本API
```python
from src.nadesiko_gui_module import start_gui, execute_nadesiko_code

# GUI起動
start_gui(language="japanese", show_window=True)

# コード実行
result = execute_nadesiko_code("Aは10\n「{A}」を表示")
```

#### 高度API
```python
from src.nadesiko_gui_module import gui_context, with_gui

# コンテキストマネージャ
with gui_context() as gui:
    result = gui.execute_code("「こんにちは！」を表示")

# デコレータ
@with_gui(language="english")
def my_function():
    return execute_nadesiko_code("show 'Hello!'")
```

### 🔧 **応用例**
- **Webアプリ連携**: Flask/Djangoとの統合
- **データ分析**: pandas/matplotlibとの連携
- **自動化ツール**: GUI付きスクリプト実行

---

## ⌨️ コマンドラインパーサー

### 📖 **機能仕様**
- **目的**: テキストベースの自然言語プログラミング
- **対象**: 上級者、自動化開発者、スクリプト作成者
- **実行方式**: 直接コード実行

### ⚙️ **技術仕様**
- **パーサー**: 正規表現ベースの構文解析
- **変換方式**: なでしこ構文 → Pythonコード
- **実行環境**: Pythonインタプリタ

### 🎮 **使用仕様**
```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()
code = """
Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示
"""
parser.execute(code)
```

### 📊 **対応構文**
| 構文種別 | 日本語例 | 英語例 | Python相当 |
|---------|----------|----------|------------|
| 変数宣言 | Aは10 | A is 10 | A = 10 |
| 表示 | 「内容」を表示 | show "content" | print("content") |
| 条件分岐 | もしA>10ならば | if A > 10 | if A > 10: |
| 繰り返し | 5回繰り返す | repeat 5 times | for _ in range(5): |
| 関数定義 | ●関数名（引数） | function name(params) | def name(params): |
| **終端マーカー** | **ここ** | **koko** | **コードブロック終了** |
| **OSコマンド** | **コマンド「〜」** | **command "〜"** | **OSコマンド実行** |
| **ファイル操作** | **「〜」を読む** | **read from "〜"** | **ファイル読み込み** |
| **システム情報** | **システム情報** | **system info** | **システム情報取得** |

### 🎯 **終端マーカー機能**

コードブロックの終わりを明示的に指定できます。終端マーカー以降のコードは実行されません。

#### 🇯🇵 **日本語版**
```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

code = """
Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示
ここ
Dは30
# この行は実行されない
"""

parser.execute(code)
# 出力: 結果: 30
```

#### 🇺🇸 **英語版**
```python
from src.english_parser import EnglishParser

parser = EnglishParser()

code = """
A is 10
B is 20
C is A plus B
show "Result: {C}"
koko
D is 30
# This line will not be executed
"""

parser.execute(code)
# 出力: Result: {C}
```

#### ✅ **特徴**
- **日本語版**: 「ここ」でコードブロックを終了
- **英語版**: 「koko」（大文字小文字区別なし）でコードブロックを終了
- **柔軟性**: 終端マーカー以降のコードは無視される
- **デバッグ**: 部分的なコード実行に便利

### 💻 **OSコマンド機能**

Windows、Mac、Linuxすべてで動作するOSコマンド実行機能です。

#### 🇯🇵 **日本語版**
```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

# コマンド実行
code = """
コマンド「echo Hello World」を表示
システム情報を表示
現在のディレクトリを表示
"""

parser.execute(code)
```

#### 🇺🇸 **英語版**
```python
from src.english_parser import EnglishParser

parser = EnglishParser()

# コマンド実行
code = """
command "echo Hello World"
system info
current directory
"""

parser.execute(code)
```

#### 📁 **ファイル操作機能**
```python
# 日本語版
「test.txt」を作る
「test.txt」を削除
「test.txt」を「backup.txt」にコピー
「data.txt」を読む

# 英語版
create "test.txt"
delete "test.txt"
copy "test.txt" to "backup.txt"
read from "data.txt"
```

#### 🎯 **OSコマンドの特徴**
- **🌍 クロスプラットフォーム**: Windows、Mac、Linuxすべてで動作
- **🔒 セキュリティ**: 安全なコマンドのみ実行可能
- **🔄 自動変換**: OSごとのコマンド違いを自動吸収
- **📝 自然言語**: 日本語・英語で直感的に操作

---

## 📝 **マクロ機能詳細**

### 🎯 **マクロとは？**

マクロは、一連の操作を記録して自動実行する機能です。定型業務や繰り返し作業を簡単に自動化できます。

### 🚀 **できること**

#### ✅ **基本機能**
- **操作記録**: なでしこコードの実行を記録
- **自動再生**: 記録した操作を自動実行
- **一覧管理**: 作成したマクロの一覧表示
- **名前付け**: マクロに分かりやすい名前を設定
- **説明追加**: マクロに説明文を追加

#### ✅ **高度機能**
- **条件分岐**: 条件に応じた実行
- **ループ処理**: 繰り返し実行
- **変数操作**: 動的な値の使用
- **ファイル操作**: ファイルの読み書き
- **システム連携**: OSコマンドの実行

#### ✅ **管理機能**
- **保存・読込**: マクロをファイルに保存
- **検索**: キーワードでマクロを検索
- **カテゴリ分類**: マクロをカテゴリで整理
- **タグ付け**: マクロにタグを付与
- **バージョン管理**: 更新履歴の記録

### 🚫 **できないこと**

#### ⚠️ **技術的制限**
- **GUI操作**: マウスクリックやキー入力の記録はできません
- **外部アプリ**: 他のアプリケーションの操作はできません
- **ネットワーク**: 直接的なネットワーク操作はできません
- **ハードウェア**: プリンタやスキャナーの制御はできません

#### ⚠️ **セキュリティ制限**
- **システムファイル**: 重要なシステムファイルの操作は制限
- **管理者権限**: 管理者権限が必要な操作はできません
- **ネットワークアクセス**: 不明な外部接続は制限

### 📋 **具体的な使い方**

#### 🇯🇵 **日本語版**

##### **基本的なマクロ作成**
```nadesiko
# 1. マクロ記録開始
マクログ「挨拶マクロ」の記録開始

# 2. 操作を実行
「こんにちは！なでしこパイソンです」を表示
現在の時刻を表示

# 3. 記録停止
記録停止

# 4. マクロ再生
マクログ「挨拶マクロ」を再生
```

##### **ファイル操作マクロ**
```nadesiko
# ファイル整理マクロ
マクログ「ファイル整理」の記録開始

「backup.txt」を作る
「重要なデータです」を「backup.txt」に書く
「backup.txt」を「documents」にコピー

記録停止
マクログ「ファイル整理」を再生
```

##### **計算マクロ**
```nadesiko
# 計算マクロ
マクログ「税込計算」の記録開始

価格は1000
消費税は0.1
税込価格は価格と価格と消費税を掛けたものを足す
「税込価格: {税込価格}円」を表示

記録停止
マクログ「税込計算」を再生
```

#### 🇺🇸 **英語版**

##### **Basic Macro Creation**
```english
# 1. Start macro recording
record macro "Greeting Macro"

# 2. Execute operations
show "Hello! This is Nadesiko3 Python"
show current time

# 3. Stop recording
stop recording

# 4. Play macro
play macro "Greeting Macro"
```

##### **File Operation Macro**
```english
# File organization macro
record macro "File Organization"

create "backup.txt"
write "Important data" to "backup.txt"
copy "backup.txt" to "documents"

stop recording
play macro "File Organization"
```

##### **Calculation Macro**
```english
# Calculation macro
record macro "Tax Calculation"

price is 1000
tax_rate is 0.1
tax_included_price is price plus price times tax_rate
show "Tax included price: {tax_included_price} yen"

stop recording
play macro "Tax Calculation"
```

### 🎯 **マクロの活用シナリオ**

#### 💼 **業務自動化**
- **定型文書作成**: 毎日の報告書作成を自動化
- **データ整理**: ファイルの整理・バックアップを自動化
- **計算処理**: 定期的な計算処理を自動化

#### 🏫 **教育用途**
- **練習問題**: 数学問題の自動生成
- **学習記録**: 学習進捗の記録
- **デモンストレーション**: プログラミングのデモ用

#### 🏠 **個人利用**
- **日次タスク**: 毎日の定型タスクを自動化
- **趣味の作業**: データ収集・整理を自動化
- **学習支援**: 学習内容の記録・再生

### 🔧 **マクロ管理**

#### 📂 **保存と読込**
```nadesiko
# マクロの保存
macro_system.save_macros("my_macros.json")

# マクロの読込
macro_system.load_macros("my_macros.json")
```

#### 🔍 **検索と一覧**
```nadesiko
# マクロ一覧の表示
マクロ一覧を表示

# マクロの検索
macro_system.search_macros("計算")
```

#### 📊 **マクロ情報**
```nadesiko
# マクロの詳細情報
macro = macro_system.get_macro("マクロ名")
print(f"名前: {macro.name}")
print(f"説明: {macro.description}")
print(f"ステップ数: {len(macro.steps)}")
```

### ⚡ **マクロの最適化**

#### 🚀 **高速化**
- **並列実行**: 複数のマクロを同時に実行
- **キャッシュ**: よく使うマクロをキャッシュ
- **最適化**: 不要なステップの削除

#### 🛡️ **エラー処理**
- **例外処理**: エラーが発生しても続行
- **ロールバック**: エラー時の状態復元
- **ログ記録**: 実行ログの記録

### 🎨 **マクロのカスタマイズ**

#### 🔧 **カスタムハンドラ**
```python
# 独自のアクションを追加
def custom_handler(params):
    # カスタム処理
    pass

macro_system.register_handler("custom_action", custom_handler)
```

#### 📝 **マクロテンプレート**
```nadesiko
# テンプレートマクロの作成
マクログ「テンプレート」を作成
# テンプレートのステップを定義
```

### 🌟 **マクロのベストプラクティス**

#### ✅ **推奨 practices**
- **分かりやすい名前**: 機能がわかる名前を付ける
- **適切な説明**: 何をするマクロか説明を追加
- **小さく分割**: 大きな処理は小さく分割
- **テスト**: 作成後に必ずテストする

#### ❌ **避けるべき practices**
- **過度な複雑化**: 一つのマクロに多くの機能を詰め込まない
- **依存関係**: 他のマクロに過度に依存しない
- **ハードコード**: 固定値を避けて変数を使用
- **エラー無視**: エラー処理を省略しない

### 📚 **マクロの例**

#### 🎯 **実用的なマクロ例**

##### **日報作成マクロ**
```nadesiko
マクログ「日報作成」の記録開始
今日の日付を表示
今日の作業内容を「report.txt」に書く
「日報を作成しました」を表示
記録停止
```

##### **データ集計マクロ**
```nadesiko
マクログ「データ集計」の記録開始
データは[10, 20, 30, 40, 50]
合計はデータの合計
平均はデータの平均
「合計: {合計}, 平均: {平均}」を表示
記録停止
```

##### **バックアップマクロ**
```nadesiko
マクログ「バックアップ」の記録開始
「data.txt」を「backup/data.txt」にコピー
「バックアップ完了」を表示
記録停止
```

---

## 🌍 バイリンガル仕様

### 📖 **言語対応概要**
なでしこパイソンは日本語と英語の2言語に完全対応しています。

### 🇯🇵 **日本語モード仕様**
- **文字コード**: UTF-8
- **変数名**: 日本語使用可能
- **演算子**: 日本語自然言語
- **制御構文**: 日本語自然表現

### 🇺🇸 **英語モード仕様**
- **文字コード**: UTF-8
- **変数名**: 英語推奨（日本語も可）
- **演算子**: 英語自然表現
- **制御構文**: 英語自然表現

### 🔄 **言語切替仕様**
- **GUIアプリ**: ツールバーからリアルタイム切替
- **モジュール**: API引数で指定
- **パーサー**: 個別のパーサークラスを使用

---

## 🚀 セットアップガイド / Setup Guide

### 📦 **システム要件 / System Requirements**
- **Python**: 3.7以上 / 3.7+
- **OS**: Windows, macOS, Linux
- **依存 / Dependencies**: tkinter, Pillow, pystray

### 🔧 **インストール手順 / Installation**

#### Option 1: PyPIからインストール / Install from PyPI
```bash
pip install nadesiko3-python
```

#### Option 2: GitHubからインストール / Install from GitHub
```bash
# 1. リポジトリをクローン / Clone repository
git clone https://github.com/nadesiko3-python/nadesiko3-python.git
cd nadesiko3-python

# 2. 依存関係をインストール / Install dependencies
pip install -r requirements.txt

# 3. パッケージをインストール / Install package
pip install -e .

# 4. 動作確認 / Test installation
python examples/nadesiko_examples.py
```

### 🚀 **クイックスタート / Quick Start**
```bash
# 初心者向け / For beginners
python start_gui.py

# GUIデザイナー / GUI designer
python start_gui_designer.py

# 開発者向け / For developers
python examples/module_usage_examples.py
```

---

## 📚 仕様変更履歴

### V6.0.0 (2026-05-03)
- ✅ 積み木GUIアプリケーション実装
- ✅ GUIデザイナー実装
- ✅ モジュールライブラリ実装
- ✅ コマンドラインパーサー実装
- ✅ バイリンガル対応完了
- ✅ タスクトレイ常駐機能
- ✅ ビジュアルGUIデザイナー実装
- ✅ 完全なモジュール化

---

## 📞 サポート情報

### 🐛 **バグ報告**
- **場所**: GitHub Issues
- **形式**: バグ再現手順と環境情報

### � **機能要望**
- **場所**: GitHub Discussions
- **形式**: 要望内容とユースケース

### 📧 **技術サポート**
- **ドキュメント**: 本README.md
- **サンプル**: examples/ディレクトリ
- **コード**: src/ディレクトリ

---

## 特徴

- 日本語の自然な文法でコードを記述可能
- 変数、条件分岐、繰り返し、関数などの基本構文をサポート
- なでしこコードをPythonコードに自動変換して実行
- 日本語変数名や日本語関数名の使用が可能

## インストール

```bash
pip install -e .
```

## 基本的な使い方

```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

# なでしこコードを実行
code = """
xは10
yは20
zはxとyを足す
zを表示する
"""

parser.execute(code)
```

## サポートされている構文

### 日本語版（なでしこ）

#### 変数宣言
```
変数名は値
```

#### 条件分岐
```
もし条件ならば
    処理
そうでなければ
    処理
```

#### 繰り返し
```
回数だけ繰り返す
    処理

条件の間
    処理
```

#### 関数定義
```
●関数名（引数）
    処理
    値を返す
```

#### 入出力
```
値を表示する
メッセージを読み込む
```

#### 演算子
- `と` - 加算 (+)
- `から` - 減算 (-)
- `を掛ける` - 乗算 (*)
- `で割る` - 除算 (/)
- `よりも大きい` - 大なり (>)
- `よりも小さい` - 小なり (<)
- `と等しい` - 等価 (==)
- `と異なる` - 非等価 (!=)
- `かつ` - 論理積 (and)
- `または` - 論理和 (or)
- `ではない` - 否定 (not)

---

### ここまで

#### 変数宣言
```
variable is value
Let variable be value
```

#### 条件分岐
```
If condition is true
    process
else
    process
```

#### 繰り返し
```
repeat N times
    process

while condition
    process
```

#### 関数定義
```
function name(parameter)
    process
    return value
```

#### 入出力
```
show value
print value
display value
```

#### 演算子
- `plus` - 加算 (+)
- `minus` - 減算 (-)
- `times` - 乗算 (*)
- `multiplied by` - 乗算 (*)
- `divided by` - 除算 (/)
- `greater than` - 大なり (>)
- `less than` - 小なり (<)
- `equal to` - 等価 (==)
- `not equal to` - 非等価 (!=)
- `and` - 論理積 (and)
- `or` - 論理和 (or)
- `not` - 否定 (not)

## 実行例

### 日本語版（なでしこ）

```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

# 基本的な例
code = """
年齢は25
もし年齢が18以上ならば
    「成人です」を表示
そうでなければ
    「未成年です」を表示
"""

parser.execute(code)
```

出力：
```
変換されたPythonコード:
年齢 = 25
if 年齢 >= 18:
    print("成人です")
else:
    print("未成年です")

実行結果:
成人です
```

### 英語版

```python
from src.english_parser import EnglishParser

parser = EnglishParser()

# 基本的な例
code = """
age is 25
if age is greater than 18
    print("Adult")
else
    print("Minor")
"""

parser.execute(code)
```

出力：
```
変換されたPythonコード:
age = 25
if age > 18:
    print("Adult")
else:
    print("Minor")

実行結果:
Adult
```

## 全コマンドリスト

### 日本語版（なでしこ）コマンド一覧

#### 🔰 基本コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `変数名は値` | 変数宣言 | `variable = value` |
| `変数名とは値` | 変数宣言 | `variable = value` |
| `変数名に値を代入` | 変数代入 | `variable = value` |
| `「内容」を表示` | 出力 | `print("content")` |
| `「内容」を表示する` | 出力 | `print("content")` |

#### 🧮 演算子コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `AとBを足す` | 加算 | `A + B` |
| `AからBを引く` | 減算 | `A - B` |
| `AにBを掛ける` | 乗算 | `A * B` |
| `AをBで割る` | 除算 | `A / B` |
| `AがB以上` | 大なり等価 | `A >= B` |
| `AがB以下` | 小なり等価 | `A <= B` |
| `AがBより大きい` | 大なり | `A > B` |
| `AがBより小さい` | 小なり | `A < B` |
| `AがBと等しい` | 等価 | `A == B` |
| `AがBと異なる` | 非等価 | `A != B` |

#### 🔄 制御構文コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `もし条件ならば` | if文 | `if condition:` |
| `そうでなければ` | else文 | `else:` |
| `違えば` | else文 | `else:` |
| `回数だけ繰り返す` | forループ | `for _ in range(count):` |
| `回数` | forループ | `for _ in range(count):` |
| `条件の間` | whileループ | `while condition:` |

#### 🎯 関数コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `●関数名（引数）` | 関数定義 | `def func_name(params):` |
| `値を返す` | return文 | `return value` |
| `値を戻る` | return文 | `return value` |
| `値して返す` | return文 | `return value` |

#### 📝 文字列操作コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `文字数(テキスト)` | 文字数取得 | `len(text)` |
| `左から(テキスト, 数)` | 文字列スライス | `text[:count]` |
| `大文字(テキスト)` | 大文字変換 | `text.upper()` |

#### 📁 ファイル操作コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `「ファイル名」に「内容」を書く` | ファイル書き込み | `with open(filename, "w") as f: f.write(content)` |
| `「ファイル名」を読む` | ファイル読み込み | `open(filename, "r").read()` |

#### 📅 日時操作コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `書式(日時, '形式')` | 日時フォーマット | `datetime.strftime(format)` |
| `年()` | 現在の年 | `datetime.now().year` |

#### 🎲 数学関数コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `パイ` | 円周率 | `math.pi` |
| `Xの平方根` | 平方根 | `math.sqrt(X)` |
| `真` | 真理値 | `True` |
| `偽` | 偽理値 | `False` |

#### 🔄 特殊変数
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `それ` | 直前の結果 | `_result` |

---

### 英語版コマンド一覧

#### 🔰 基本コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `variable is value` | 変数宣言 | `variable = value` |
| `Let variable be value` | 変数宣言 | `variable = value` |
| `show content` | 出力 | `print(content)` |
| `print content` | 出力 | `print(content)` |
| `display content` | 出力 | `print(content)` |

#### 🧮 演算子コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `A plus B` | 加算 | `A + B` |
| `A minus B` | 減算 | `A - B` |
| `A times B` | 乗算 | `A * B` |
| `A multiplied by B` | 乗算 | `A * B` |
| `A divided by B` | 除算 | `A / B` |
| `A is greater than B` | 大なり | `A > B` |
| `A is less than B` | 小なり | `A < B` |
| `A is equal to B` | 等価 | `A == B` |
| `A is not equal to B` | 非等価 | `A != B` |

#### 🔄 制御構文コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `If condition` | if文 | `if condition:` |
| `else` | else文 | `else:` |
| `otherwise` | else文 | `else:` |
| `repeat N times` | forループ | `for _ in range(N):` |
| `while condition` | whileループ | `while condition:` |

#### 🎯 関数コマンド
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `function name(parameter)` | 関数定義 | `def function_name(parameter):` |
| `return value` | return文 | `return value` |

#### 🧮 論理演算子
| コマンド | 説明 | Python相当 |
|---------|------|------------|
| `A and B` | 論理積 | `A and B` |
| `A or B` | 論理和 | `A or B` |
| `not A` | 否定 | `not A` |

---

## サンプルプログラムの実行

```bash
python examples/nadesiko_examples.py
```

## 🖥️ GUIアプリケーション V1

なでしこパイソンには、積み木デザインのGUIアプリケーションが付属しています。

### ✨ 主な機能

- 🧱 **積み木プログラミング**: ビジュアルブロックをクリックしてコードを構築
- 🌐 **バイリンガル対応**: 日本語と英語のプログラミング言語を切り替え
- 📝 **コードエディタ**: 直接コードを編集可能
- 📊 **実行結果表示**: リアルタイムで実行結果を確認
- 💾 **保存・読込**: プログラムをファイルに保存・読込
- 🔔 **タスクトレイ常駐**: バックグラウンドで常駐、いつでも呼び出せる

### 🚀 起動方法

```bash
# GUIアプリケーションを起動
python start_gui.py
```

### 📦 依存関係

GUIアプリケーションを使用するには、追加の依存関係をインストール：

```bash
pip install -r requirements.txt
```

### 🎮 使い方

1. **起動**: `python start_gui.py` を実行
2. **言語選択**: ツールバーから日本語/英語を選択
3. **積み木**: 左側のパレットからブロックをクリック
4. **編集**: 中央のエディタで直接編集も可能
5. **実行**: ▶ボタンでプログラムを実行
6. **保存**: 💾ボタンでプログラムを保存

### 🧱 積み木ブロック一覧

#### 日本語版
- **基本**: 変数宣言、表示、代入
- **数学**: 足し算、引き算、掛け算、割り算
- **制御**: もし、違えば、繰り返し
- **関数**: 関数定義、戻り値

#### 英語版
- **Basic**: Variable, Print, Assign
- **Math**: Add, Subtract, Multiply, Divide
- **Control**: If, Else, Repeat
- **Function**: Function, Return

### 🔔 タスクトレイ機能

- **常駐**: アプリケーションがバックグラウンドで実行
- **アイコン**: タスクトレイになでしこアイコンが表示
- **クイックアクセス**: アイコン右クリックでウィンドウを表示/非表示
- **終了**: メニューから安全に終了

---

## 📦 モジュールとしての使用

なでしこ GUIはPythonモジュールとしても使用できます。他のプログラムから簡単に呼び出せます。

### 🚀 基本的な使い方

```python
from src.nadesiko_gui_module import start_gui, execute_nadesiko_code

# GUIを起動
start_gui(language="japanese", show_window=True)

# なでしこコードを実行
result = execute_nadesiko_code("""
Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示
""")

print(result)
```

### 🎮 高度な使い方

#### バックグラウンド実行
```python
from src.nadesiko_gui_module import start_gui, show_gui_window

# バックグラウンドで起動
start_gui(language="japanese", show_window=False)

# 後でウィンドウを表示
show_gui_window()
```

#### コンテキストマネージャ
```python
from src.nadesiko_gui_module import gui_context

# with文でGUIを管理
with gui_context(language="english", show_window=True) as gui:
    result = gui.execute_code("""
    name is "Alice"
    show "Hello, {name}!"
    """)
    print(result)
```

#### デコレータ使用
```python
from src.nadesiko_gui_module import with_gui

@with_gui(language="japanese", show_window=True)
def my_program():
    # GUI付きで実行される
    result = execute_nadesiko_code("「こんにちは！」を表示")
    return result

# 実行
my_program()
```

### 📋 API一覧

| 関数 | 説明 | 戻り値 |
|------|------|--------|
| `start_gui(language, show_window)` | GUIを起動 | bool |
| `stop_gui()` | GUIを停止 | bool |
| `execute_nadesiko_code(code, language)` | コードを実行 | str |
| `show_gui_window()` | ウィンドウを表示 | bool |
| `hide_gui_window()` | ウィンドウを隠す | bool |
| `get_gui_status()` | ステータスを取得 | dict |

### 🧪 実行例

```bash
# モジュール使用例を実行
python examples/module_usage_examples.py
```

### 🔧 応用例

#### Webアプリケーション連携
```python
from flask import Flask, request, jsonify
from src.nadesiko_gui_module import execute_nadesiko_code

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    code = request.json.get('code')
    result = execute_nadesiko_code(code)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
```

#### データ分析ツール
```python
import pandas as pd
from src.nadesiko_gui_module import gui_context

# データ分析とGUI連携
def analyze_data():
    df = pd.read_csv('data.csv')
    
    with gui_context() as gui:
        # なでしこで結果を表示
        result = gui.execute_code(f"""
        データ件数は{len(df)}件です
        平均値は{df['value'].mean()}です
        「分析完了」を表示
        """)
        
    return df

analyze_data()
```

---

- 🎯 **ハンドル操作**: 8つのリサイズハンドルで精密な調整

### 🚀 起動方法

```bash
# GUIデザイナーを起動
python start_gui_designer.py
```

### 🎮 使い方

1. **部品選択**: 左側パレットから配置したい部品をクリック
2. **配置**: キャンバス上のクリックで部品を配置
3. **編集**: 
   - ドラッグで移動
   - 選択ハンドルでリサイズ
   - 右側パネルでプロパティ編集
4. **コード生成**: 右下の「💻 生成コード」でPythonコードを確認
5. **実行**: 「▶ 実行」ボタンで生成されたGUIを起動

### 🧩 対応部品一覧

| 部品名 | 説明 | 主なプロパティ |
|--------|------|----------------|
| ボタン | クリック可能なボタン | text, bg, fg, command |
| ラベル | テキスト表示 | text, bg, fg, font |
| 入力欄 | テキスト入力 | text, bg, fg, font |
| テキスト | 複数行テキスト | text, bg, fg, wrap |
| フレーム | コンテナ | bg, relief, bd |
| キャンバス | 描画領域 | bg, highlightthickness |
| リスト | 選択リスト | bg, fg, font |
| コンボ | ドロップダウン | values, state |
| チェック | チェックボックス | text, bg, fg |
| ラジオ | ラジオボタン | text, bg, fg, value |
| スケール | スライダー | from_, to, orient |
| スピン | 数値入力 | from_, to, text |

### 🎨 デザイン機能

#### マウス操作
- **左クリック**: 部品選択・配置
- **ドラッグ**: 部品移動
- **ハンドルドラッグ**: リサイズ
- **右クリック**: コンテキストメニュー

#### ツールバー機能
- 💾 **保存**: デザインをJSONファイルに保存
- 📁 **読込**: 保存したデザインを読込
- 🗑️ **クリア**: 全部品を削除
- 🗑️ **選択削除**: 選択部品のみ削除
- 📐 **グリッド**: グリッド線の表示/非表示
- 🎯 **スナップ**: グリッドへのスナップON/OFF

#### コンテキストメニュー（右クリック）
- **削除**: 部品を削除
- **前面に移動**: 部品を最前面に
- **背面に移動**: 部品を最背面に
- **プロパティコピー**: プロパティをコピー
- **プロパティ貼り付け**: プロパティを貼り付け

### 💻 コード生成

GUIデザイナーで作成したデザインは、実行可能なPythonコードに変換されます：

```python
# 生成されるコード例
import tkinter as tk
from tkinter import ttk

class GeneratedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('生成されたGUI')
        self.root.geometry('800x600')
        
        # 部品を作成
        self.button_123456789 = tk.Button(
            self.root,
            text='ボタン',
            bg='#4ECDC4',
            fg='white',
            command=self.on_button_click
        )
        self.button_123456789.place(
            x=50, y=50, width=100, height=30
        )
    
    def on_button_click(self):
        print('ボタンがクリックされました')
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = GeneratedGUI()
    app.run()
```

### 🔧 応用例

#### なでしこコードと連携
```python
# GUIデザイナーで作成したGUIをなでしこコードと連携
from src.nadesiko_gui_module import start_gui, execute_nadesiko_code
from src.gui_designer import GUIDesigner

# 1. GUIデザイナーでデザイン
designer = GUIDesigner()
# ... デザイン作業 ...

# 2. 生成コードをなでしこで制御
code = """
GUIボタンがクリックされた
    「こんにちは！」を表示
"""

start_gui()
execute_nadesiko_code(code)
```

#### カスタム部品の追加
```python
# 独自部品をGUIデザイナーに追加
class CustomComponent(GUIComponent):
    def get_default_properties(self):
        return {
            "text": "カスタム部品",
            "bg": "#FF6B6B",
            "custom_property": "value"
        }
```

### 📁 関連ファイル

- `src/gui_designer.py` - GUIデザイナーメイン
- `start_gui_designer.py` - 起動スクリプト
- `examples/` - デザイン例（作成予定）

## 拡張性

このモジュールは拡張可能です。新しいキーワードや構文を追加するには：

1. `src/nadesiko_keywords.py` の `KEYWORD_MAP` に新しいキーワードを追加
2. `src/nadesiko_parser.py` の `parse_line` メソッドに新しい構文パターンを追加
3. `gui_app.py` に新しい積み木ブロックを追加
4. テストコードを追加して動作を確認

## 📜 許可とライセンス

### ✅ **なでしこ作者の許可**
本プロジェクトは、なでしこの作者であるクジラ飛行机氏より、なでしこの構文・アイデアを使用する許可を得ています。

- **許可範囲**: なでしこの構文を使用したPython実装
- **目的**: 教育用途・プログラミング学習支援
- **形態**: オープンソースでの無償公開

### 🙏 **クレジット**
- **なでしこ**: クジラ飛行机氏
- **URL**: https://nadesi.com/
- **感謝**: なでしこの素晴らしいアイデアを共有いただきありがとうございます

### ⚠️ **免責事項**
- 本プロジェクトはなでしこの**非公式**実装です
- なでしこ本体とは別物です
- サポートは本プロジェクトの範囲内となります

## ライセンス

MIT License
