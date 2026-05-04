# プロジェクト構造 / Project Structure

## 📁 フォルダー構成

```
japanese_programming/
├── 📁 src/                          # ソースコードディレクトリ
│   ├── 📄 __init__.py                # パッケージ初期化ファイル
│   ├── 📄 nadesiko_parser.py         # なでしこ3パーサー
│   ├── 📄 nadesiko_keywords.py       # なでしこ3キーワード定義
│   ├── 📄 nadesiko_functions.py       # なでしこ3基本関数
│   ├── 📄 nadesiko_gui.py            # なでしこ3 GUI機能
│   ├── 📄 nadesiko_file.py          # なでしこ3ファイル操作
│   ├── 📄 nadesiko_math.py           # なでしこ3数学関数
│   ├── 📄 nadesiko_string.py         # なでしこ3文字列操作
│   ├── 📄 nadesiko_complete.py        # なでしこ3完全版クラス
│   ├── 📄 nadesiko_complete_commands.py # なでしこ3完全版コマンド
│   ├── 📄 bilingual_parser.py        # バイリンガルパーサー
│   ├── 📄 english_parser.py          # 英語パーサー
│   ├── 📄 english_keywords.py        # 英語キーワード定義
│   ├── 📄 keywords.py               # 基本キーワード定義
│   └── 📄 parser.py                # 汎用パーサー
├── 📁 examples/                      # サンプルプログラム
│   ├── 📄 EXAMPLES.md               # 詳細なサンプル集
│   ├── 📄 nadesiko_examples.py      # なでしこ3基本サンプル
│   ├── 📄 bilingual_examples.py      # バイリンガルサンプル
│   ├── 📄 examples.py              # 基本サンプル
│   └── 📄 nadesiko_complete_examples.py # 完全版機能サンプル
├── 📁 docs/                         # ドキュメントディレクトリ
│   ├── 📄 README.md                # ドキュメント一覧
│   ├── 📄 README_nadesiko.md       # なでしこ3版README
│   ├── 📄 README_bilingual.md       # バイリンガル版README
│   └── 📄 USAGE_EXAMPLES.md        # 使用例ドキュメント
├── 📁 tests/                         # テストディレクトリ（未使用）
├── 📄 README.md                      # プロジェクトメインREADME
├── 📄 __init__.py                    # 互換性用初期化ファイル
├── 📄 setup.py                      # パッケージ設定ファイル
├── 📄 pyproject.toml                # 現代的なパッケージ設定
├── 📄 requirements.txt               # 依存関係リスト
└── 📄 PROJECT_STRUCTURE.md           # このファイル
```

## 📋 ファイルの説明

### 🏷️ ソースコード (src/)

#### 🇯🇵 なでしこ3関連
- **nadesiko_parser.py**: なでしこ3文法を解析するパーサー
- **nadesiko_keywords.py**: なでしこ3のキーワードと命令を定義
- **nadesiko_functions.py**: 基本的ななでしこ3関数を実装
- **nadesiko_gui.py**: GUI関連のなでしこ3命令を実装
- **nadesiko_file.py**: ファイル操作のなでしこ3命令を実装
- **nadesiko_math.py**: 数学関数のなでしこ3命令を実装
- **nadesiko_string.py**: 文字列操作のなでしこ3命令を実装

#### 🔥 完全版機能
- **nadesiko_complete.py**: なでしこ3の全機能を統合したクラス
- **nadesiko_complete_commands.py**: 高度な命令（GUI、ネットワーク、DBなど）

#### 🌍 バイリンガル機能
- **bilingual_parser.py**: 日本語と英語を自動検出するパーサー
- **english_parser.py**: 英語プログラミング用のパーサー
- **english_keywords.py**: 英語プログラミングのキーワード定義

#### 🔧 汎用機能
- **keywords.py**: 基本的なキーワード定義
- **parser.py**: 汎用的なパーサー機能

### 📚 サンプルプログラム (examples/)

- **EXAMPLES.md**: 10個の詳細なサンプルプログラム集
- **nadesiko_examples.py**: なでしこ3の基本的な使用例
- **bilingual_examples.py**: バイリンガルプログラミングの例
- **examples.py**: 基本的な使用例
- **nadesiko_complete_examples.py**: 完全版機能のデモ

### 📖 ドキュメント (docs/)

- **README.md**: ドキュメントの案内と使い方
- **README_nadesiko.md**: なでしこ3互換モジュールの詳細なREADME
- **README_bilingual.md**: バイリンガルプログラミングのREADME
- **USAGE_EXAMPLES.md**: 詳細な使用例と使い方

### ⚙️ 設定ファイル

- **setup.py**: 従来のパッケージ設定ファイル
- **pyproject.toml**: 現代的なパッケージ設定ファイル
- **requirements.txt**: 依存関係のリスト
- **PROJECT_STRUCTURE.md**: プロジェクト構成の説明

## 🎯 使用方法

### 📦 インストール後の使用

```bash
# PyPIからインストールした場合
pip install nadesiko3-python

# ローカルからインストールした場合
cd /path/to/japanese_programming
pip install -e .
```

### 💻 プログラムの実行

```python
# 基本的な使用
from nadesiko3_python import NadesikoParser

# 完全版機能の使用
from nadesiko3_python import NadesikoComplete

# バイリンガル機能の使用
from nadesiko3_python import BilingualParser
```

## 🔧 開発者向け情報

### 🏗️ ビルド方法

```bash
# 開発モードでインストール
pip install -e .

# ビルドテスト
python -m build
```

### 🧪 テスト方法

```bash
# テスト実行（未実装）
pytest tests/
```

### 📦 パッケージ作成

```bash
# ソース配布物作成
python setup.py sdist

# ホイール作成
python setup.py bdist_wheel
```

## 🌍 国際化対応

### 🇯🇵 日本語
- なでしこ3の完全な互換性
- 自然な日本語文法
- 教育向けの設計

### 🇺🇸 英語
- 子供向けの英語文法
- バイリンガル対応
- 国際的な利用

## 📞 ライセンス

MIT License - 商用・非商用を問わず自由に利用可能

## 🔗 関連リンク

- [GitHub Repository](https://github.com/nadesiko3-python/nadesiko3-python)
- [PyPI Package](https://pypi.org/project/nadesiko3-python/)
- [Documentation](https://github.com/nadesiko3-python/nadesiko3-python/docs)
