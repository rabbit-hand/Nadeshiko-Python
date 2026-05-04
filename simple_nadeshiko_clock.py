#!/usr/bin/env python3
"""
なでしこ時計プログラム - シンプル版
日本語で現在時刻を表示する
"""

import sys
import time
import datetime
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

def show_nadeshiko_clock():
    """なでしこ時計を表示"""
    parser = NadesikoParser()
    variables = {}
    
    print("なでしこ時計")
    print("=" * 30)
    
    try:
        while True:
            # 現在時刻を取得
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute
            second = now.second
            
            # なでしこコードで時刻を設定
            time_codes = [
                f"時={hour}",
                f"分={minute}",
                f"秒={second}",
                "時刻=\"{時}:{分}:{秒}\""
            ]
            
            # 画面をクリアして時刻を表示
            print("\033[H\033[J", end="")
            print("なでしこ時計")
            print("=" * 30)
            
            # なでしこコードを実行
            for code in time_codes:
                try:
                    result = parser.parse_line(code)
                    if result and '=' in result and not result.startswith('print'):
                        exec(result, {}, variables)
                except:
                    pass
            
            # 時刻を表示
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
            print(f"\n           {time_str}")
            print("\n終了: Ctrl+C")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n時計を停止しました。")

def test_nadeshiko_time():
    """なでしこ時刻コードのテスト"""
    parser = NadesikoParser()
    variables = {}
    
    print("なでしこ時刻コードテスト")
    print("-" * 25)
    
    # テストコード
    test_codes = [
        "時=10",
        "分=30",
        "秒=45",
        "時刻=\"{時}:{分}:{秒}\"",
        "「現在時刻: {時刻}」を表示"
    ]
    
    for code in test_codes:
        try:
            print(f"\nなでしこコード: {code}")
            result = parser.parse_line(code)
            print(f"Pythonコード: {result}")
            
            if result and '=' in result and not result.startswith('print'):
                exec(result, {}, variables)
                print("実行: 変数を設定しました")
            elif result:
                print(f"実行: {result}")
                
        except Exception as e:
            print(f"エラー: {e}")
    
    print(f"\n設定された変数:")
    for name, value in variables.items():
        print(f"  {name} = {value}")

def main():
    """メイン関数"""
    print("Nadeshiko Python 時計プログラム")
    print("=" * 40)
    print("1. 時計を表示")
    print("2. なでしこコードテスト")
    
    try:
        choice = input("\n選択 (1-2): ")
        
        if choice == "1":
            show_nadeshiko_clock()
        elif choice == "2":
            test_nadeshiko_time()
        else:
            print("1または2を選択してください。")
            
    except KeyboardInterrupt:
        print("\nプログラムを終了します。")
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    main()
