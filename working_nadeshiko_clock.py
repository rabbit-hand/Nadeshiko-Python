#!/usr/bin/env python3
"""
なでしこ時計プログラム - 実動作版
実際に動く時計をなでしこ風に表示
"""

import sys
import time
import datetime
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

def main():
    """メイン関数 - 実際に動く時計"""
    print("なでしこ時計を起動します...")
    print("終了するには Ctrl+C を押してください")
    print("=" * 40)
    
    try:
        while True:
            # 現在時刻を取得
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute
            second = now.second
            
            # 時刻文字列を作成
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
            date_str = f"{now.year}年{now.month}月{now.day}日"
            
            # 画面をクリア
            print("\033[H\033[J", end="")
            
            # なでしこ風の表示
            print("           なでしこ時計")
            print("=" * 40)
            print()
            print(f"           {time_str}")
            print(f"           {date_str}")
            print()
            print("           【なでしこコード】")
            print(f"           時={hour}")
            print(f"           分={minute}")
            print(f"           秒={second}")
            print(f"           時刻=\"{hour}:{minute}:{second}\"")
            print(f"           「現在時刻: {time_str}」を表示")
            print("=" * 40)
            print("           終了: Ctrl+C")
            
            # 1秒待機
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n時計を停止しました。")
        print("お疲れ様でした！")

def demo_nadeshiko_time_commands():
    """なでしこ時刻コマンドのデモ"""
    parser = NadesikoParser()
    variables = {}
    
    print("なでしこ時刻コマンドデモ")
    print("=" * 30)
    
    # 現在時刻を取得
    now = datetime.datetime.now()
    
    # なでしこ風の時刻設定コード
    nadeshiko_codes = [
        f"時={now.hour}",
        f"分={now.minute}", 
        f"秒={now.second}",
        f"年={now.year}",
        f"月={now.month}",
        f"日={now.day}",
        "時刻文字列=\"{時}:{分}:{秒}\"",
        "日付文字列=\"{年}年{月}月{日}日\"",
        "メッセージ=\"現在の時刻は{時刻文字列}です\""
    ]
    
    print("なでしこコードの実行:")
    print("-" * 25)
    
    for code in nadeshiko_codes:
        try:
            print(f"\nなでしこ: {code}")
            result = parser.parse_line(code)
            print(f"Python: {result}")
            
            if result and '=' in result and not result.startswith('print'):
                exec(result, {}, variables)
                print("実行: 変数を設定")
            
        except Exception as e:
            print(f"エラー: {e}")
    
    print(f"\n設定された変数:")
    for name, value in variables.items():
        if name != '_result':
            print(f"  {name} = {value}")

if __name__ == "__main__":
    print("Nadeshiko Python 時計プログラム")
    print("=" * 40)
    print("1. 時計を起動")
    print("2. なでしこコードデモ")
    
    try:
        choice = input("\n選択 (1-2): ")
        
        if choice == "1":
            main()
        elif choice == "2":
            demo_nadeshiko_time_commands()
        else:
            print("1または2を選択してください。")
            
    except KeyboardInterrupt:
        print("\nプログラムを終了します。")
    except Exception as e:
        print(f"エラー: {e}")
