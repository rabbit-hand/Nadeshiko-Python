#!/usr/bin/env python3
"""
Nadeshiko Python サンプルプログラム
日本語プログラミング言語で簡単なアプリケーションを作成
"""

import sys
import os
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser
from nadesiko_functions import NadesikoFunctions

def main():
    """メインプログラム"""
    print("=" * 50)
    print("Nadeshiko Python サンプルプログラム")
    print("=" * 50)
    
    # パーサーの初期化
    parser = NadesikoParser()
    functions = NadesikoFunctions()
    
    # サンプル1: 基本的な計算と表示
    print("\n【サンプル1: 基本的な計算】")
    sample1_code = [
        "A=5",
        "B=3", 
        "C=A+B",
        "「合計は{C}です」を表示"
    ]
    
    for line in sample1_code:
        try:
            result = parser.parse_line(line)
            print(f"コード: {line}")
            if result:
                print(f"実行結果: {result}")
        except Exception as e:
            print(f"エラー: {e}")
    
    # サンプル2: 条件分岐
    print("\n【サンプル2: 条件分岐】")
    sample2_code = [
        "年齢=20",
        "もし年齢>=18ならば",
        "  「成人です」を表示",
        "違えば",
        "  「未成年です」を表示",
        "もし終わり"
    ]
    
    for line in sample2_code:
        try:
            result = parser.parse_line(line)
            print(f"コード: {line}")
            if result:
                print(f"実行結果: {result}")
        except Exception as e:
            print(f"エラー: {e}")
    
    # サンプル3: ループ処理
    print("\n【サンプル3: ループ処理】")
    sample3_code = [
        "回数=0",
        "回数<5の間",
        "  「{回数}回目のループです」を表示",
        "  回数=回数+1",
        "ループ終わり"
    ]
    
    for line in sample3_code:
        try:
            result = parser.parse_line(line)
            print(f"コード: {line}")
            if result:
                print(f"実行結果: {result}")
        except Exception as e:
            print(f"エラー: {e}")
    
    # サンプル4: 関数定義と呼び出し
    print("\n【サンプル4: 関数定義】")
    sample4_code = [
        "●挨拶する(名前とは)",
        "  「こんにちは、{名前とは}さん！」を表示",
        "ここまで",
        "",
        "挨拶する(\"田中\")"
    ]
    
    for line in sample4_code:
        try:
            result = parser.parse_line(line)
            print(f"コード: {line}")
            if result:
                print(f"実行結果: {result}")
        except Exception as e:
            print(f"エラー: {e}")
    
    # サンプル5: 数学関数の使用
    print("\n【サンプル5: 数学関数】")
    sample5_code = [
        "数値=16",
        "平方根=数値の平方根",
        "「{数値}の平方根は{平方根}です」を表示"
    ]
    
    for line in sample5_code:
        try:
            result = parser.parse_line(line)
            print(f"コード: {line}")
            if result:
                print(f"実行結果: {result}")
        except Exception as e:
            print(f"エラー: {e}")
    
    print("\n" + "=" * 50)
    print("サンプルプログラム終了")
    print("=" * 50)

def interactive_mode():
    """対話モード"""
    print("\n【対話モード】")
    print("日本語でプログラムを入力してください。'exit'で終了します。")
    
    parser = NadesikoParser()
    
    while True:
        try:
            code = input("\n>>> ")
            if code.lower() == 'exit':
                break
            
            result = parser.parse_line(code)
            if result:
                print(f"結果: {result}")
                
        except KeyboardInterrupt:
            print("\n終了します。")
            break
        except Exception as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
    
    # 対話モードを試す
    try:
        response = input("\n対話モードを試しますか？ (y/n): ")
        if response.lower() == 'y':
            interactive_mode()
    except KeyboardInterrupt:
        print("\n終了します。")
