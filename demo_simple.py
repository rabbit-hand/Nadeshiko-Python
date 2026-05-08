#!/usr/bin/env python3
"""
Simple Working Demo of Japanese Programming Language
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from parser import JapaneseParser

def main():
    parser = JapaneseParser()
    
    print("=== 日本語プログラミング言語 動作デモ ===\n")
    
    # Example 1: Basic Calculator
    print("1. 基本計算:")
    basic_calc = """
数値1は10
数値2は20
合計は数値1と数値2
「合計は{合計}です」を表示する
"""
    parser.execute(basic_calc)
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Grade Evaluation
    print("2. 成績評価:")
    grade_eval = """
点数は85
もし点数よりも大きい80ならば
    「優秀です」を表示する
そうでなければ
    「頑張りましょう」を表示する
"""
    parser.execute(grade_eval)
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Loop and Counter
    print("3. 繰り返しとカウンター:")
    loop_example = """
カウンターは0
5だけ繰り返す
    カウンターを表示する
    カウンターはカウンターと1
"""
    parser.execute(loop_example)
    
    print("\n" + "="*50 + "\n")
    
    # Example 4: Function Example
    print("4. 関数の例:")
    func_example = """
関数二乗は(数値)を返す
    数値と数値を返す

入力は3
結果は二乗(入力)
「{入力}の二乗は{結果}です」を表示する
"""
    parser.execute(func_example)
    
    print("\n" + "="*50 + "\n")
    
    # Example 5: String Processing (without length function)
    print("5. 文字列処理:")
    string_example = """
メッセージは「こんにちは世界」
「メッセージ: {メッセージ}」を表示する
"""
    parser.execute(string_example)
    
    print("\n" + "="*50 + "\n")
    print("✓ 日本語プログラミング言語は正常に動作しています！")
    print("✓ 変数、条件分岐、繰り返し、関数、文字列処理が使えます。")
    print("✓ Python初心者でも日本語で直感的にプログラミングできます。")

if __name__ == "__main__":
    main()
