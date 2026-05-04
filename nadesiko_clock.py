#!/usr/bin/env python3
"""
Nadeshiko Python 時計プログラム
日本語で現在時刻を表示する
"""

import sys
import time
import datetime
sys.path.insert(0, 'src')

from nadesiko_parser import NadesikoParser

class NadeshikoClock:
    """なでしこ時計クラス"""
    
    def __init__(self):
        self.parser = NadesikoParser()
        self.variables = {}
        self.running = True
    
    def get_current_time(self):
        """現在時刻を取得"""
        now = datetime.datetime.now()
        return {
            'hour': now.hour,
            'minute': now.minute,
            'second': now.second,
            'year': now.year,
            'month': now.month,
            'day': now.day,
            'weekday': now.strftime('%A')
        }
    
    def format_time(self, time_data):
        """時刻をフォーマット"""
        return f"{time_data['hour']:02d}:{time_data['minute']:02d}:{time_data['second']:02d}"
    
    def format_date(self, time_data):
        """日付をフォーマット"""
        return f"{time_data['year']}年{time_data['month']}月{time_data['day']}日"
    
    def display_clock(self):
        """時計を表示"""
        while self.running:
            try:
                # 現在時刻を取得
                current_time = self.get_current_time()
                
                # 画面をクリア
                print("\033[H\033[J", end="")
                
                # 時計の表示
                print("=" * 50)
                print("           なでしこ時計")
                print("=" * 50)
                print()
                
                # 大きな時刻表示
                time_str = self.format_time(current_time)
                print(f"           {time_str}")
                print()
                
                # 日付表示
                date_str = self.format_date(current_time)
                print(f"           {date_str}")
                print(f"           {current_time['weekday']}")
                print()
                
                # なでしこコードで時刻を表示
                self.display_with_nadeshiko(current_time)
                
                print("=" * 50)
                print("終了するには Ctrl+C を押してください")
                
                # 1秒待機
                time.sleep(1)
                
            except KeyboardInterrupt:
                self.running = False
                print("\n時計を停止します。")
                break
            except Exception as e:
                print(f"エラー: {e}")
                break
    
    def display_with_nadeshiko(self, time_data):
        """なでしこコードで時刻を表示"""
        print("【なでしこコードでの表示】")
        
        # 時刻を変数に代入
        nadeshiko_codes = [
            f"時={time_data['hour']}",
            f"分={time_data['minute']}",
            f"秒={time_data['second']}",
            f"年={time_data['year']}",
            f"月={time_data['month']}",
            f"日={time_data['day']}",
            "時刻文字列=\"{時}:{分}:{秒}\"",
            "日付文字列=\"{年}年{月}月{日}日\"",
            "「現在時刻: {時刻文字列}」を表示",
            "「今日の日付: {日付文字列}」を表示"
        ]
        
        # グローバル変数に datetime を追加
        globals_dict = {'datetime': datetime, 'print': print}
        
        for code in nadeshiko_codes:
            try:
                result = self.parser.parse_line(code)
                if result:
                    if '=' in result and not result.startswith('print'):
                        exec(result, globals_dict, self.variables)
                    elif result.startswith('print'):
                        # print 実行時は、self.variables をローカルスコープに追加
                        local_scope = {**globals_dict, **self.variables}
                        exec(result, local_scope, self.variables)
            except Exception as e:
                pass
    
    def show_simple_clock(self):
        """シンプルな時計表示"""
        print("シンプルなでしこ時計")
        print("-" * 30)
        
        while self.running:
            try:
                current_time = self.get_current_time()
                time_str = self.format_time(current_time)
                
                # なでしこ風の表示
                nadeshiko_time = f"「{time_str}」を表示"
                result = self.parser.parse_line(nadeshiko_time)
                
                print(f"\r{time_str}", end="", flush=True)
                time.sleep(1)
                
            except KeyboardInterrupt:
                self.running = False
                print("\n終了します。")
                break

def main():
    """メイン関数"""
    print("Nadeshiko Python 時計プログラム")
    print("=" * 40)
    
    clock = NadeshikoClock()
    
    print("時計のモードを選択してください:")
    print("1. 詳細表示モード")
    print("2. シンプル表示モード")
    print("3. なでしこコードテスト")
    
    try:
        choice = input("\n選択 (1-3): ")
        
        if choice == "1":
            clock.display_clock()
        elif choice == "2":
            clock.show_simple_clock()
        elif choice == "3":
            test_nadeshiko_time_codes(clock)
        else:
            print("無効な選択です。")
            
    except KeyboardInterrupt:
        print("\nプログラムを終了します。")
    except Exception as e:
        print(f"エラー: {e}")

def test_nadeshiko_time_codes(clock):
    """なでしこ時刻コードのテスト"""
    print("\nなでしこ時刻コードテスト")
    print("-" * 30)
    
    test_codes = [
        "現在時刻=今",
        "「こんにちは！」を表示",
        "HOUR=10",
        "MINUTE=30",
        "TIME_STR=\"{HOUR}:{MINUTE}\"",
        "「時刻: {TIME_STR}」を表示"
    ]
    
    # グローバル変数に datetime を追加
    globals_dict = {'datetime': datetime, 'print': print}
    variables = {}
    
    for code in test_codes:
        try:
            print(f"\nコード: {code}")
            result = clock.parser.parse_line(code)
            print(f"変換: {result}")
            
            if result and '=' in result and not result.startswith('print'):
                # 変数代入時は、variables にも追加
                exec(result, globals_dict, variables)
                print("実行: 代入完了")
            elif result and result.startswith('print'):
                # print 実行時は、variables をローカルスコープに追加
                local_scope = {**globals_dict, **variables}
                exec(result, local_scope, variables)
                print("実行: 表示完了")
                
        except Exception as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
