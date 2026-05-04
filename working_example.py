#!/usr/bin/env python3
"""
Nadeshiko Python 動作サンプル
実際に動作する簡単な例
"""

import sys
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

def main():
    """メイン処理"""
    print("Nadeshiko Python 動作サンプル")
    print("=" * 40)
    
    parser = NadesikoParser()
    
    # 変数代入のテスト
    print("\n1. 変数代入:")
    test_codes = [
        "A=10",
        "B=20", 
        "C=A+B",
        "D=C*2"
    ]
    
    for code in test_codes:
        try:
            result = parser.parse_line(code)
            print(f"  {code} -> {result}")
            if result and '=' in result:
                exec(result)
        except Exception as e:
            print(f"  エラー: {e}")
    
    # 簡単な計算結果の表示
    print("\n2. 計算結果:")
    try:
        print(f"  A = {A}")
        print(f"  B = {B}")
        print(f"  C = {C}")
        print(f"  D = {D}")
    except:
        print("  変数が定義されていません")
    
    # 文字列操作
    print("\n3. 文字列操作:")
    string_tests = [
        "TEXT=\"Hello\"",
        "RESULT=TEXT+\" World\"",
        "RESULT"
    ]
    
    for code in string_tests:
        try:
            result = parser.parse_line(code)
            print(f"  {code} -> {result}")
            if result and not result.startswith('print'):
                exec(result)
        except Exception as e:
            print(f"  エラー: {e}")
    
    print(f"  結果: {RESULT}")

if __name__ == "__main__":
    main()
