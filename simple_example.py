#!/usr/bin/env python3
"""
Nadeshiko Python 簡単なサンプル
基本的な機能を試す
"""

import sys
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

def test_basic_functionality():
    """基本的な機能テスト"""
    print("Nadeshiko Python 基本機能テスト")
    print("=" * 40)
    
    parser = NadesikoParser()
    
    # テスト用のコード
    test_codes = [
        "「こんにちは、世界！」を表示",
        "A=10",
        "B=20",
        "C=A+B",
        "「計算結果: {C}」を表示",
        "X=5",
        "Y=X*2",
        "「{X}の2倍は{Y}です」を表示"
    ]
    
    for i, code in enumerate(test_codes, 1):
        try:
            print(f"\n{i}. コード: {code}")
            result = parser.parse_line(code)
            if result:
                print(f"   変換結果: {result}")
                # 実際にPythonコードを実行
                try:
                    exec(result)
                except Exception as e:
                    print(f"   実行エラー: {e}")
            else:
                print("   変換結果: なし")
        except Exception as e:
            print(f"   パースエラー: {e}")

if __name__ == "__main__":
    test_basic_functionality()
