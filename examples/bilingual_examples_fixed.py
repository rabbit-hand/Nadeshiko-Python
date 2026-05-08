#!/usr/bin/env python3
"""
Bilingual Programming Examples - Japanese and English
This file demonstrates that the Japanese Programming Language module
can be used with both Japanese and English documentation/examples.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from parser import JapaneseParser

def main():
    parser = JapaneseParser()
    
    print("=== 日本語・英語バイリンガルプログラミング言語デモ ===\n")
    print("このデモは、日本語と英語の両方でプログラミングできることを示します\n")
    
    # Example 1: Calculator with bilingual comments
    print("\n1. 計算機（バイリンガルコメント付き）:")
    calculator_code = '''# Japanese: 変数を代入
# English: Assign variables
数値1は5  # x = 5
数値2は3  # y = 3
合計は数値1と数値2  # z = x + y
"合計は{合計}です"を表示する  # print(f"Total is {z}")

# This works the same whether you read Japanese or English comments
'''
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(calculator_code)
    print(python_code)
    
    print("実行結果:")
    parser.execute(calculator_code)
    
    # Example 2: Conditional logic with bilingual explanation
    print("\n2. 条件分岐（バイリンガル説明付き）:")
    conditional_code = '''# Japanese: 条件分岐
# English: Conditional branching
年齢は20  # age = 20

# Japanese: もし年齢が18以上ならば
# English: If age is 18 or older
もし年齢よりも大きい18ならば  # if age >= 18:
    "成人です"を表示する  # print("Adult")
そうでなければ  # else:
    "未成年です"を表示する  # print("Minor")

# The same logic works regardless of documentation language
'''
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(conditional_code)
    print(python_code)
    
    print("実行結果:")
    parser.execute(conditional_code)
    
    # Example 3: Loop with bilingual description
    print("\n3. 繰り返し（バイリンガル説明付き）:")
    loop_code = '''# Japanese: 繰り返し処理
# English: Loop processing
カウンターは0  # counter = 0

# Japanese: 5回繰り返す
# English: Repeat 5 times
5だけ繰り返す  # for _ in range(5):
    "回数: {カウンター}"を表示する  # print(f"Count: {counter}")
    カウンターはカウンターと1  # counter = counter + 1

# Works the same way in any language
'''
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(loop_code)
    print(python_code)
    
    print("実行結果:")
    parser.execute(loop_code)
    
    # Example 4: Function with bilingual documentation
    print("\n4. 関数（バイリンガル文書付き）:")
    function_code = '''# Japanese: 関数定義
# English: Function definition
関数掛け算は(数値1と数値2)を返す  # def multiply(x, y):

# Japanese: 処理内容
# English: Function body
    数値1を掛ける数値2を返す  # return x * y

# Japanese: 関数呼び出し
# English: Function call
結果は掛け算(4と5)  # result = multiply(4, 5)
"4と5の掛け算は{結果}です"を表示する  # print(f"4 * 5 = {result}")

# Same functionality, multilingual documentation
'''
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(function_code)
    print(python_code)
    
    print("実行結果:")
    parser.execute(function_code)
    
    # Example 5: String processing with bilingual comments
    print("\n5. 文字列処理（バイリンガル説明付き）:")
    string_code = '''# Japanese: 文字列処理
# English: String processing
メッセージは"こんにちは世界"  # message = "Hello World"

# Japanese: f文字列
# English: f-string
"メッセージ: {メッセージ}"を表示する  # print(f"Message: {message}")

# Language-independent functionality
'''
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(string_code)
    print(python_code)
    
    print("実行結果:")
    parser.execute(string_code)
    
    print("\n=== 主な利点 ===")
    print("✓ 日本語で自然なプログラミングが可能")
    print("✓ 英語コメントで国際協業が容易")
    print("✓ 同じ機能を複数の言語で提供")
    print("✓ 完全なバイリンガル対応")
    
    print("\n=== 言語独立性 ===")
    print("この日本語プログラミング言語モジュールは:")
    print("- 日本語の自然な文法をPythonコードに変換")
    print("- どの言語のドキュメントでも理解可能")
    print("- 国際的な開発チームに最適")
    
    print("\nこのモジュールは、世界中の誰でも利用できる国際的なツールです！")

if __name__ == "__main__":
    main()
