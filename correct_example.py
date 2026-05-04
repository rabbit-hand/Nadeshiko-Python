#!/usr/bin/env python3
"""
Nadeshiko Python 正しい使用例
パーサーの仕様に合わせたサンプル
"""

import sys
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

def main():
    """メイン処理"""
    print("Nadeshiko Python 正しい使用例")
    print("=" * 40)
    
    parser = NadesikoParser()
    
    # グローバル変数を管理する辞書
    variables = {}
    
    def execute_code(code):
        """コードを実行して結果を変数辞書に保存"""
        try:
            result = parser.parse_line(code)
            print(f"  コード: {code}")
            print(f"  変換: {result}")
            
            if result and '=' in result and not result.startswith('print'):
                # 代入文を実行
                exec(result, {}, variables)
                print(f"  実行: 代入完了")
            elif result:
                print(f"  実行: {result}")
            else:
                print(f"  実行: なし")
                
        except Exception as e:
            print(f"  エラー: {e}")
    
    # 1. 基本的な代入
    print("\n1. 基本的な代入:")
    execute_code("A=10")
    execute_code("B=20")
    execute_code("C=A+B")
    
    print(f"  結果: A={variables.get('A', '未定義')}, B={variables.get('B', '未定義')}, C={variables.get('C', '未定義')}")
    
    # 2. 文字列操作
    print("\n2. 文字列操作:")
    execute_code('TEXT="Hello"')
    execute_code('RESULT=TEXT+" World"')
    
    print(f"  結果: TEXT={variables.get('TEXT', '未定義')}, RESULT={variables.get('RESULT', '未定義')}")
    
    # 3. 複雑な計算
    print("\n3. 複雑な計算:")
    execute_code("X=5")
    execute_code("Y=X*3+2")
    execute_code("Z=Y/2")
    
    print(f"  結果: X={variables.get('X', '未定義')}, Y={variables.get('Y', '未定義')}, Z={variables.get('Z', '未定義')}")
    
    # 4. パーサーの機能テスト
    print("\n4. パーサーの機能:")
    test_cases = [
        "NUM=100",
        "PERCENT=NUM*0.1",
        "FINAL=NUM-PERCENT"
    ]
    
    for code in test_cases:
        execute_code(code)
    
    print(f"\n最終的な変数の状態:")
    for name, value in variables.items():
        print(f"  {name} = {value} ({type(value).__name__})")

def interactive_demo():
    """対話デモ"""
    print("\n" + "=" * 40)
    print("対話デモ (終了するには 'exit' と入力)")
    
    parser = NadesikoParser()
    variables = {}
    
    while True:
        try:
            code = input("\n>>> ")
            if code.lower() == 'exit':
                break
            
            result = parser.parse_line(code)
            print(f"変換: {result}")
            
            if result and '=' in result and not result.startswith('print'):
                exec(result, {}, variables)
                print("変数が更新されました")
            elif result:
                try:
                    # Pythonコードとして実行
                    exec(result, {}, variables)
                except:
                    print(f"結果: {result}")
            
            # 現在の変数を表示
            if variables:
                print(f"現在の変数: {list(variables.keys())}")
                
        except KeyboardInterrupt:
            print("\n終了します。")
            break
        except Exception as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
    
    # 対話デモ
    try:
        response = input("\n対話デモを試しますか？ (y/n): ")
        if response.lower() == 'y':
            interactive_demo()
    except KeyboardInterrupt:
        print("\n終了します。")
