# Nadesiko3 Python Module

A Python module that enables programming in Japanese natural language, compatible with Nadesiko3 syntax.

## 🌟 Features

- **🇯🇵 Japanese Natural Language Programming**: Write code using natural Japanese expressions
- **🔄 Python Code Generation**: Automatically converts Nadesiko code to executable Python code
- **📚 Rich Function Library**: Supports 300+ mathematical functions, string operations, file handling
- **🎯 Beginner-Friendly**: Easy to learn for programming beginners and children
- **🔧 Modular Design**: Can be used as a standalone module or integrated into other applications
- **📖 Comprehensive Documentation**: Detailed examples and usage guides

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone [repository-url]
cd nadesiko-python

# Install dependencies
pip install -r requirements.txt

# Install the module
pip install -e .
```

### Basic Usage

```python
from nadesiko_parser import NadesikoParser

# Create parser instance
parser = NadesikoParser()

# Execute Nadesiko code
code = """
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
"""

parser.execute(code)
```

Output:
```
合計: 30
```

## 📖 Supported Syntax

### Variable Declaration
```nadesiko
変数名は値
変数名とは値
変数名に値を代入
```

### Mathematical Operations
```nadesiko
AとBを足す      # A + B
AからBを引く    # A - B
AにBを掛ける    # A * B
AをBで割る      # A / B
AのB乗         # A ** B
AをBで割った余り # A % B
```

### Comparison Operations
```nadesiko
AがBより大きい     # A > B
AがBより小さい     # A < B
AがB以上          # A >= B
AがB以下          # A <= B
AがBと等しい       # A == B
AがBと異なる       # A != B
```

### Logical Operations
```nadesiko
AかつB           # A and B
AまたはB          # A or B
Aではない          # not A
```

### Control Structures
```nadesiko
# If statement
もし条件ならば
    処理
そうでなければ
    処理
違えば
    処理

# For loop
回数だけ繰り返す
    処理

# While loop
条件の間
    処理
```

### Function Definition
```nadesiko
●関数名（引数1と引数2）
    処理
    値を返す
    値を戻る
    値して返す
```

### Input/Output
```nadesiko
「メッセージ」を表示
「メッセージ」を表示する
値を表示する
メッセージを読み込む
値を読み込む
```

## 🔧 Advanced Features

### Mathematical Functions
```python
from nadesiko_complete import NadesikoComplete

nadesiko = NadesikoComplete()

# Basic math
print(nadesiko.円周率())           # Pi
print(nadesiko.絶対値(-5))         # Absolute value
print(nadesiko.平方根(16))         # Square root

# Trigonometry
print(nadesiko.サイン(90, degrees=True))   # Sine
print(nadesiko.コサイン(60, degrees=True))  # Cosine
print(nadesiko.タンジェント(45, degrees=True)) # Tangent

# Statistics
print(nadesiko.平均([1, 2, 3, 4, 5]))      # Average
print(nadesiko.合計([1, 2, 3, 4, 5]))      # Sum
print(nadesiko.最大値([1, 2, 3, 4, 5]))    # Maximum
print(nadesiko.最小値([1, 2, 3, 4, 5]))    # Minimum
```

### String Operations
```python
# String manipulation
text = "こんにちは"
print(nadesiko.文字数(text))           # Character count
print(nadesiko.大文字(text))           # Uppercase
print(nadesiko.小文字(text))           # Lowercase
print(nadesiko.反転(text))             # Reverse
print(nadesiko.左から(text, 3))        # Left substring
print(nadesiko.右から(text, 3))        # Right substring
```

### File Operations
```python
# File handling
nadesiko.ファイル書き込み("test.txt", "内容")
content = nadesiko.ファイル読み込み("test.txt")
print(nadesiko.ファイル存在("test.txt"))  # Check if file exists
print(nadesiko.ファイルサイズ("test.txt")) # Get file size
```

### Date and Time
```python
# Date/time operations
print(nadesiko.今())                   # Current time
print(nadesiko.今日())                 # Today's date
print(nadesiko.年())                   # Current year
print(nadesiko.月())                   # Current month
print(nadesiko.日())                   # Current day
```

## 🎮 GUI Applications

### Message Boxes
```python
from nadesiko_complete_commands import NadesikoCompleteCommands

gui = NadesikoCompleteCommands()

# Basic message box
gui.メッセージボックス("タイトル", "メッセージ")

# Input dialog
name = gui.入力ボックス("入力", "名前を入力してください")
print(f"入力された名前: {name}")

# File selection dialog
filepath = gui.ファイル選択("ファイルを選択")
print(f"選択されたファイル: {filepath}")
```

### Window Operations
```python
# Create and manage windows
gui.ウィンドウ作成("My Window", 400, 300)
gui.ラベル作成("Hello, World!", 50, 50)
gui.ボタン作成("Click me", 50, 100, lambda: print("Clicked!"))
gui.ウィンドウ表示()
```

## 📚 Complete Function Reference

### Mathematical Functions (300+)

| Function | Description | Example |
|----------|-------------|---------|
| `円周率()` | Pi value | `円周率()` |
| `絶対値(値)` | Absolute value | `絶対値(-5)` |
| `平方根(値)` | Square root | `平方根(16)` |
| `階乗(値)` | Factorial | `階乗(5)` |
| `平均(配列)` | Average | `平均([1,2,3])` |
| `合計(配列)` | Sum | `合計([1,2,3])` |
| `最大値(配列)` | Maximum | `最大値([1,2,3])` |
| `最小値(配列)` | Minimum | `最小値([1,2,3])` |

### String Functions (100+)

| Function | Description | Example |
|----------|-------------|---------|
| `文字数(テキスト)` | Character count | `文字数("hello")` |
| `大文字(テキスト)` | Uppercase | `大文字("hello")` |
| `小文字(テキスト)` | Lowercase | `小文字("HELLO")` |
| `反転(テキスト)` | Reverse | `反転("hello")` |
| `左から(テキスト, 数)` | Left substring | `左から("hello", 3)` |
| `右から(テキスト, 数)` | Right substring | `右から("hello", 3)` |

### File Functions (50+)

| Function | Description | Example |
|----------|-------------|---------|
| `ファイル読み込み(パス)` | Read file | `ファイル読み込み("test.txt")` |
| `ファイル書き込み(パス, 内容)` | Write file | `ファイル書き込み("test.txt", "content")` |
| `ファイル存在(パス)` | File exists | `ファイル存在("test.txt")` |
| `ファイルサイズ(パス)` | File size | `ファイルサイズ("test.txt")` |
| `ディレクトリ作成(パス)` | Create directory | `ディレクトリ作成("folder")` |

## 🎯 Practical Examples

### Example 1: Simple Calculator
```nadesiko
Aは10
Bは20
合計はAとBを足す
差はAからBを引く
積はAにBを掛ける
商はAをBで割る
「合計: {合計}」を表示
「差: {差}」を表示
「積: {積}」を表示
「商: {商}」を表示
```

### Example 2: BMI Calculator
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

### Example 3: File Processing
```nadesiko
# Create a file with numbers
「1,2,3,4,5」を「numbers.txt」に書く

# Read and process
データは「numbers.txt」を読む
数字配列はデータを「,」で区切る

# Calculate statistics
合計は数字配列の合計
平均は数字配列の平均
最大は数字配列の最大値
最小は数字配列の最小値

「合計: {合計}」を表示
「平均: {平均}」を表示
「最大: {最大}」を表示
「最小: {最小}」を表示
```

### Example 4: Interactive Program
```nadesiko
「名前を入力してください」を読んで名前に代入
「年齢を入力してください」を読んで年齢に代入

もし年齢が18以上ならば
    「{名前}さん、ようこそ！」を表示
    「成人ですね」を表示
そうでなければ
    「{名前}さん、こんにちは！」を表示
    「未成年ですね」を表示
```

## 🔧 Error Handling

### Common Errors and Solutions

#### Syntax Errors
```nadesiko
# Incorrect
Aは10

# Correct - need proper verb ending
Aは10です
# or
Aに10を代入
```

#### Division by Zero
```nadesiko
# This will cause an error
Aは10
Bは0
CはAをBで割る

# Add error checking
もしBが0と異なるならば
    CはAをBで割る
そうでなければ
    「0で割ることはできません」を表示
```

#### File Not Found
```nadesiko
# Add file existence check
もし「data.txt」が存在するならば
    内容は「data.txt」を読む
    内容を表示
そうでなければ
    「ファイルが見つかりません」を表示
```

## 🚀 Performance Tips

### Optimizing Your Code

1. **Reuse Parser Instances**
```python
# Good - reuse parser
parser = NadesikoParser()
for code in codes:
    parser.execute(code)

# Avoid - creating new parser each time
for code in codes:
    parser = NadesikoParser()  # Inefficient
    parser.execute(code)
```

2. **Use Built-in Functions**
```nadesiko
# Good - use built-in functions
合計は配列の合計

# Less efficient - manual calculation
合計は0
配列の各要素について
    合計は合計と要素を足す
```

3. **Minimize String Operations**
```nadesiko
# Good - minimize string concatenation
結果は「値: {値}」

# Less efficient - multiple concatenations
結果は「値: 」と値を足す
```

## 📖 Learning Resources

### Step-by-Step Learning Path

1. **Start with Basics**
   - Variable declaration and assignment
   - Basic arithmetic operations
   - Simple output commands

2. **Learn Control Structures**
   - If statements and conditional logic
   - Loops and iterations
   - Function definitions

3. **Explore Advanced Features**
   - String manipulation
   - File operations
   - Mathematical functions

4. **Build Complete Applications**
   - Interactive programs
   - File processing tools
   - GUI applications

### Practice Exercises

#### Beginner Level
1. Create a program that calculates the area of a rectangle
2. Write a program that converts Celsius to Fahrenheit
3. Build a simple greeting program that responds to user input

#### Intermediate Level
1. Create a program that reads numbers from a file and calculates statistics
2. Build a text-based adventure game
3. Write a program that sorts and searches data

#### Advanced Level
1. Create a complete file management system
2. Build a GUI application with multiple windows
3. Develop a data analysis tool with charts

## 🤝 Contributing

### How to Contribute

1. **Report Bugs**: Use GitHub Issues to report bugs
2. **Request Features**: Suggest new features via GitHub Discussions
3. **Submit Code**: Fork the repository and submit pull requests
4. **Improve Documentation**: Help improve documentation and examples

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Ensure backward compatibility

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For support and questions:
- **Documentation**: This README and other docs files
- **Examples**: Check the `examples/` directory
- **Issues**: Report problems on GitHub Issues
- **Discussions**: Ask questions on GitHub Discussions

---

**🌍 Start programming in natural Japanese with Nadesiko3 Python!**
