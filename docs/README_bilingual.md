# 日本語・英語バイリンガルプログラミング言語

Pythonでなでしこ3互換の日本語と、アメリカの子供たちが理解できる自然な英語の両方をサポートするプログラミング言語モジュールです。

## 特徴

- **🇯🇵🇺🇸 バイリンガル対応**: 日本語と英語の両方でプログラミング可能
- **🎯 子供向け**: 自然な言語表現でプログラミング学習
- **🔄 自動言語検出**: コードから言語を自動判定
- **📚 なでしこ3互換**: 日本語はなでしこ3文法に完全対応
- **🚀 初心者友好**: Python初心者でも簡単に始められる

## インストール

```bash
cd japanese_programming
pip install -e .
```

## 基本的な使い方

### バイリンガル自動判定

```python
from japanese_programming import BilingualParser

parser = BilingualParser()

# 日本語コード
japanese_code = """
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
"""

# 英語コード
english_code = """
A is 10
B is 20
C is A plus B
show "Total: {C}"
"""

# 自動で言語を判定して実行
parser.execute(japanese_code)  # 日本語として実行
parser.execute(english_code)  # 英語として実行
```

### 言語モードの指定

```python
# 日本語モード
parser.set_language_mode('japanese')
parser.execute(japanese_code)

# 英語モード
parser.set_language_mode('english')
parser.execute(english_code)

# 自動判定モード（デフォルト）
parser.set_language_mode('auto')
```

## サポートされている文法

### 日本語文法（なでしこ3互換）

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

# 条件分岐
もしAが10以上ならば
    「大きいです」を表示
違えば
    「小さいです」を表示

# 繰り返し
5回繰り返す
    「こんにちは」を表示

# 関数定義
●足し算（AとB）
    AとBを足して返す
```

### 英語文法（子供向け）

```english
# 変数代入
A is 10
B is 20
Let C be 30

# 計算
C is A plus B          # C = A + B
D is A minus B         # D = A - B
E is A times B         # E = A * B
F is A divided by B    # F = A / B

# 表示
show "Hello"
print "World"
display A

# 条件分岐
if A is greater than 10
    show "Big"
else
    show "Small"

# 繰り返し
repeat 5 times
    show "Hello"

# 関数定義
function add_numbers(x and y)
    return x plus y
```

## 各言語の比較

| 日本語 | 英語 | Python |
|--------|------|---------|
| Aは10 | A is 10 | A = 10 |
| AとBを足す | A plus B | A + B |
| 「こんにちは」を表示 | show "Hello" | print("Hello") |
| もしAが10以上ならば | if A is greater than 10 | if A >= 10 |
| 5回繰り返す | repeat 5 times | for _ in range(5) |
| ●関数名（引数） | function name(x and y) | def name(x, y) |

## 高度な例

### BMI計算（日本語）

```nadesiko
●BMI計算（身長と体重）
    身長の2乗で体重を割って返す

●BMI判定（BMI値）
    もしBMI値が18.5より小さいならば
        「低体重です」を返す
    もしBMI値が25以上ならば
        「肥満です」を返す
    違えば
        「普通体重です」を返す

身長は1.70
体重は65
BMIはBMI計算(身長と体重)
判定はBMI判定(BMI)
「BMI: {BMI:.1f} - {判定}」を表示
```

### BMI計算（英語）

```english
function calculate_bmi(height and weight)
    return weight divided by (height times height)

function check_bmi(bmi_value)
    if bmi_value is less than 18.5
        return "Underweight"
    if bmi_value is greater than 25
        return "Overweight"
    else
        return "Normal weight"

height is 1.70
weight is 65
bmi is calculate_bmi(height and weight)
status is check_bmi(bmi)
show "BMI: {bmi:.1f} - {status}"
```

## 教育向け機能

### 子供向け簡単な例

```english
# フルーツの数え算
apple is 5
banana is 3
total is apple plus banana
show "I have {total} fruits"

# 簡単なゲーム
repeat 3 times
    show "Learning is fun!"

# 条件分岐の学習
age is 12
if age is greater than or equal to 13
    show "You are a teenager"
else
    show "You are a kid"
```

### 数学の学習

```english
# 基本演算
a is 10
b is 3
show "Addition: {a} plus {b} is {a plus b}"
show "Multiplication: {a} times {b} is {a times b}"
show "Division: {a} divided by {b} is {a divided by b}"

# 簡単な図形の面積
function rectangle_area(width and height)
    return width times height

area is rectangle_area(5 and 4)
show "Rectangle area: {area}"
```

## ゲーム風プログラミング

```english
# 簡単な冒険ゲーム
player_name is "Hero"
player_health is 100
enemy_health is 50

show "Welcome {player_name}!"
show "Player Health: {player_health}"
show "Enemy Health: {enemy_health}"

while player_health is greater than 0 and enemy_health is greater than 0
    # プレイヤーの攻撃
    damage is 10 plus random 5
    enemy_health is enemy_health minus damage
    show "Player deals {damage} damage!"
    
    if enemy_health is less than or equal to 0
        show "You win!"
        break
    
    # 敵の攻撃
    damage is 5 plus random 3
    player_health is player_health minus damage
    show "Enemy deals {damage} damage!"
    
    if player_health is less than or equal to 0
        show "Game Over!"
        break
    
    wait 1 second

if player_health is greater than 0
    show "Victory! {player_name} wins!"
else
    show "Defeat! Try again."
```

## 実行例

```bash
# バイリンガル実行
python3 -c "
from japanese_programming import BilingualParser
parser = BilingualParser()
code = '''
A is 10
B is 20
C is A plus B
show \"Result: {C}\"
'''
parser.execute(code)
"
```

出力：
```
検出された言語: 英語
変換されたPythonコード:
A = 10
B = 20
C = A + B
print("Result: {C}")

実行結果:
Result: 30
```

## できること・できないこと

### ✅ できること

#### 基本プログラミング機能
- **二言語対応**: 日本語と英語の両方でプログラミング可能
- **自動言語検出**: コードから使用言語を自動判定
- **変数操作**: 両言語での変数宣言、代入、参照
- **計算処理**: 四則演算、べき乗、剰余計算
- **制御構文**: if文、forループ、whileループ
- **関数定義**: ユーザー定義関数の作成と呼び出し
- **入出力**: コンソールへの表示、キーボードからの入力

#### 高度な機能
- **数学関数**: 三角関数、対数、乱数、統計計算
- **文字列操作**: 検索、置換、分割、結合、エンコード
- **ファイル操作**: 読み書き、ディレクトリ操作、パス処理
- **GUIプログラミング**: ウィンドウ、ボタン、テキストボックス、キャンバス
- **日時処理**: 現在時刻取得、書式設定、計算

#### バイリンガル特有機能
- **混合コード**: 1つのプログラム内で日本語と英語を混在可能
- **言語間翻訳**: 簡易的なコード変換機能
- **教育向け設計**: 両言語でのプログラミング学習支援
- **国際対応**: グローバルなプログラミング教育支援

#### 教育向け機能
- **初心者友好**: Pythonの知識がなくても始められる
- **視覚的学習**: 自然言語で直感的に理解できる
- **段階的学習**: 簡単なコードから複雑なプログラムへ
- **バイリンガル教育**: 英語学習とプログラミングを同時に学習

### ❌ できないこと（制限事項）

#### パフォーマンス関連
- **高速処理**: インタプリタ方式のため、ネイティブPythonより遅い
- **大規模データ**: 大量のデータ処理には向いていない
- **リアルタイム処理**: 高頻度のリアルタイム処理には不向き

#### 高度な機能
- **機械学習**: scikit-learnなどの高度なライブラリ直接使用は不可
- **Web開発**: Flask/DjangoなどのWebフレームワークは未対応
- **データベース**: SQLデータベースの直接操作は未対応
- **ネットワーク**: HTTP通信以外の高度なネットワーク処理は未対応

#### 言語関連
- **完全自動翻訳**: 高度な文法変換は限定的
- **方言対応**: 標準的な日本語・英語のみ対応
- **複雑な表現**: 文学的な表現や専門用語は制限あり

#### システムレベル
- **OS操作**: システムコールの直接実行は制限あり
- **ハードウェア制御**: ハードウェアの直接制御は不可
- **マルチスレッド**: 高度な並列処理は未対応

#### 互換性
- **Python 2**: Python 3のみ対応
- **外部ライブラリ**: 特定の外部ライブラリとの連携は制限あり
- **既存Pythonコード**: 既存のPythonコードの直接実行は不可

## 拡張機能

### サポートされているキーワードの確認

```python
from japanese_programming import BilingualParser

parser = BilingualParser()
keywords = parser.get_supported_keywords()

print("日本語キーワード:", keywords['japanese'])
print("英語キーワード:", keywords['english'])
```

### コードの翻訳

```python
# 日本語コードを英語に変換
japanese_code = "Aは10"
english_code = parser.translate_code(japanese_code, 'english')

# 英語コードを日本語に変換
english_code = "A is 10"
japanese_code = parser.translate_code(english_code, 'japanese')
```

## 教育現場での活用

### 小学校プログラミング教育

- **論理的思考**: 自然な言語でアルゴリズムを学習
- **数学的思考**: 計算と図形の概念をプログラミングで理解
- **問題解決能力**: ゲーム作成を通じて創造的思考を養成

### 中学校・高等学校

- **英語学習**: 英語でプログラミングしながら語学力も向上
- **数学応用**: 関数、変数、アルゴリズムの実践的学習
- **キャリア教育**: プログラミング的思考の基礎を養成

## ライセンス

MIT License

## 貢献

バグ報告、機能要望、新しい言語の追加などを歓迎します。

---

**🌍 日本語・英語バイリンガルプログラミング言語で、世界の子供たちが楽しくプログラミングを学べます！**
