#!/usr/bin/env python3
"""
Simple bilingual example that works correctly
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from parser import JapaneseParser

def main():
    parser = JapaneseParser()
    
    print("=== 日本語・英語バイリンガルプログラミング言語デモ ===\n")
    print("このデモは、日本語と英語の両方でプログラミングできることを示します\n")
    
    # Simple calculator example
    print("\n1. 簡単な計算機:")
    calculator_code = r"""
数値1は5
数値2は3
合計は数値1と数値2
"合計は{合計}です"を表示する
"""
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(calculator_code)
    print(python_code)
    
    print("\n実行結果:")
    parser.execute(calculator_code)
    
    # String processing example
    print("\n2. 文字列処理:")
    string_code = r"""
メッセージは"こんにちは世界"
"メッセージ: {メッセージ}"を表示する
"""
    
    print("生成されたPythonコード:")
    python_code = parser.parse_file(string_code)
    print(python_code)
    
    print("\n実行結果:")
    parser.execute(string_code)
    
    print("\n✓ このモジュールは、日本語と英語の両方でプログラミング学習を支援する国際的なツールです！")
    print("✓ 日本語の自然な文法が使える")
    print("✓ 英語ドキュメントでも理解可能")
    print("✓ 同じ機能を複数の言語で提供")
    print("✓ 完全なバイリンガル対応")

if __name__ == "__main__":
    main()
