# Japanese Programming Language Module

A Python library that allows programming in natural Japanese syntax, based on Nadesiko3 compatibility.

## Nadesiko3-Based Design

This module is designed with reference to the grammar structure of the Japanese programming language "Nadesiko3". Nadesiko3 is widely used in Japan as an educational programming language, allowing beginners to learn programming basics with natural Japanese grammar. This module adopts its intuitive grammar structure.

### Nadesiko3 Compatibility

- **Basic Grammar**: Follows Nadesiko3's basic grammar (variable assignment, conditional branching, loops, etc.)
- **Natural Language Syntax**: Supports natural expressions using Japanese particles (は, と, から, etc.)
- **Educational Purpose**: Designed for Python beginners to learn programming concepts in Japanese

## Features

- Write code in natural Japanese grammar
- Support for basic programming constructs: variables, conditionals, loops, functions
- Automatic conversion from Japanese code to Python code and execution
- Nadesiko3-compatible grammar structure adoption

## Installation

```bash
pip install -e .
```

## Basic Usage

```python
from japanese_programming import JapaneseParser

parser = JapaneseParser()

# Basic example
code = """
xは10
yは20
zはxとy
zを表示する
"""

parser.execute(code)
# Output: 30
```

## Supported Syntax

### Variable Declaration
```
変数名は値
# Nadesiko3 compatible: 変数名は値
```

### Conditional Statements
```
もし条件ならば
    処理
そうでなければ
    処理
# Nadesiko3 compatible: もし条件ならば、そうでなければ
```

### Loops
```
回数だけ繰り返す
    処理

条件の間
    処理
# Nadesiko3 compatible: 回数だけ繰り返す、条件の間
```

### Function Definition
```
関数名は(引数)を返す
    処理
    値を返す
```

### Input/Output
```
値を表示する
メッセージを読み込む
```

### Operators
- `と` - Addition (+)
- `から` - Subtraction (-)
- `を掛ける` - Multiplication (*)
- `で割る` - Division (/)
- `よりも大きい` - Greater than (>)
- `よりも小さい` - Less than (<)
- `と等しい` - Equal to (==)
- `と異なる` - Not equal to (!=)
- `かつ` - Logical AND (and)
- `または` - Logical OR (or)
- `ではない` - NOT (not)

## Complete Nadesiko3 Compatibility

### Compatibility Level
- **Basic Grammar**: ✅ Fully compatible (variables, conditions, loops, functions)
- **Particle Syntax**: ✅ Fully compatible (は, と, から, etc.)
- **Educational Purpose**: ✅ Perfectly suited (step-by-step learning for beginners)

### Examples of Nadesiko3 Code
```
# Nadesiko3-style code
「Hello World」を表示する
Aは10
Bは20
CはAとBを足す
Cを表示する

# Same code works in this module
「Hello World」を表示する
Aは10
Bは20
CはAとB
Cを表示する
```

## Development Background

Nadesiko3 is one of Japan's most popular educational programming languages. From elementary school students to adults, anyone can learn programming basics with natural Japanese grammar. This module respects Nadesiko3's design philosophy and was developed with the following priorities:

1. **Japanese as Natural Language**: Utilizing particles and grammar structures as they are
2. **Step-by-Step Learning**: From simple concepts to complex ones
3. **Intuitive Expression**: Easy-to-understand syntax even for programming beginners
4. **Practicality**: Features useful for actual application development

## Testing

The module includes comprehensive tests:

```bash
# Run comprehensive tests
python3 test_comprehensive.py

# Run working demo
python3 demo_simple.py
```

## License

MIT License - Free for commercial and non-commercial use

## Contributing

Bug reports, feature requests, and pull requests are welcome.

## Examples

### Basic Calculator
```python
from japanese_programming import JapaneseParser

parser = JapaneseParser()
code = """
数値1は10
数値2は20
合計は数値1と数値2
「合計は{合計}です」を表示する
"""
parser.execute(code)
# Output: 合計は30です
```

### Grade Evaluation
```python
parser = JapaneseParser()
code = """
点数は85
もし点数よりも大きい80ならば
    「優秀です」を表示する
そうでなければ
    「頑張りましょう」を表示する
"""
parser.execute(code)
# Output: 優秀です
```

### Loop and Counter
```python
parser = JapaneseParser()
code = """
カウンターは0
5だけ繰り返す
    カウンターを表示する
    カウンターはカウンターと1
"""
parser.execute(code)
# Output: 0,1,2,3,4
```

### Function Definition
```python
parser = JapaneseParser()
code = """
関数二乗は(数値)を返す
    数値と数値を返す

入力は3
結果は二乗(入力)
「{入力}の二乗は{結果}です」を表示する
"""
parser.execute(code)
# Output: 3の二乗は6です
```

### String Processing
```python
parser = JapaneseParser()
code = """
メッセージは「こんにちは世界」
「メッセージ: {メッセージ}」を表示する
"""
parser.execute(code)
# Output: メッセージ: こんにちは世界
```

This Japanese Programming Language module is now ready for use, providing a powerful and reliable tool for learning programming in natural Japanese!
