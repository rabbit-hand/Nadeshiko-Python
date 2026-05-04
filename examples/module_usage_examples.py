#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこ3 GUIモジュール使用例
様々な使い方を示すサンプルコード
"""

import sys
import os
import time

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# モジュールをインポート
from src.nadesiko_gui_module import (
    start_gui, stop_gui, execute_nadesiko_code,
    show_gui_window, hide_gui_window, get_gui_status,
    gui_context, with_gui, get_gui
)

def example_1_basic_usage():
    """例1: 基本的な使い方"""
    print("=== 例1: 基本的な使い方 ===")
    
    # GUIを起動
    if start_gui(language="japanese", show_window=True):
        print("✅ GUI起動成功")
        
        # なでしこコードを実行
        code = """
        名前は「なでしこ太郎」
        年齢は25
        「こんにちは、{名前}さん！」を表示
        「年齢は{年齢}歳です」を表示
        """
        
        result = execute_nadesiko_code(code)
        print("実行結果:")
        print(result)
        
        # ステータス確認
        status = get_gui_status()
        print(f"ステータス: {status}")
        
        # 少し待つ
        time.sleep(3)
        
    else:
        print("❌ GUI起動失敗")

def example_2_background_gui():
    """例2: バックグラウンドでGUI実行"""
    print("\n=== 例2: バックグラウンドでGUI実行 ===")
    
    # GUIをバックグラウンドで起動
    if start_gui(language="japanese", show_window=False):
        print("✅ GUIバックグラウンド起動成功")
        
        # コードを複数実行
        codes = [
            "Aは10\nBは20\nCはAとBを足す\n「合計: {C}」を表示",
            "5回繰り返す\n    「こんにちは！」を表示",
            "もし30が20より大きいならば\n    「30は20より大きい」を表示"
        ]
        
        for i, code in enumerate(codes, 1):
            print(f"\n--- コード{i} ---")
            result = execute_nadesiko_code(code)
            print(result)
            time.sleep(1)
        
        # ウィンドウを表示
        print("\nウィンドウを表示します...")
        show_gui_window()
        
        # 少し待つ
        time.sleep(3)
        
    else:
        print("❌ GUI起動失敗")

def example_3_context_manager():
    """例3: コンテキストマネージャ使用"""
    print("\n=== 例3: コンテキストマネージャ使用 ===")
    
    # コンテキストマネージャでGUIを管理
    with gui_context(language="english", show_window=True) as gui:
        print("✅ GUIコンテキスト開始")
        
        # 英語コードを実行
        code = """
        name is "Alice"
        age is 30
        show "Hello, {name}!"
        show "Age: {age}"
        """
        
        result = execute_nadesiko_code(code, language="english")
        print("実行結果:")
        print(result)
        
        # 少し待つ
        time.sleep(3)
    
    print("✅ GUIコンテキスト終了")

def example_4_decorator():
    """例4: デコレータ使用"""
    print("\n=== 例4: デコレータ使用 ===")
    
    @with_gui(language="japanese", show_window=True)
    def my_program():
        """GUI付きで実行するプログラム"""
        print("✅ プログラム開始")
        
        # 複雑な計算を実行
        code = """
        ●階乗計算（N）
            もしNが0以下ならば
                1を返す
            違えば
                Nに階乗計算(N-1)を掛けて返す
        
        結果は階乗計算(5)
        「5の階乗は{結果}です」を表示
        """
        
        result = execute_nadesiko_code(code)
        print("実行結果:")
        print(result)
        
        print("✅ プログラム終了")
        return "完了"
    
    # デコレータ付き関数を実行
    result = my_program()
    print(f"関数の戻り値: {result}")
    
    # 少し待つ
    time.sleep(3)

def example_5_language_switching():
    """例5: 言語切り替え"""
    print("\n=== 例5: 言語切り替え ===")
    
    # 日本語モードで起動
    if start_gui(language="japanese", show_window=False):
        print("✅ 日本語モードで起動")
        
        # 日本語コードを実行
        jp_code = """
        Aは100
        Bは50
        「日本語モード: A+B={AとBを足す}」を表示
        """
        
        result = execute_nadesiko_code(jp_code, language="japanese")
        print("日本語実行結果:")
        print(result)
        
        # 英語コードも実行（同じGUIで）
        en_code = """
        x is 200
        y is 75
        show "English Mode: x+y={x plus y}"
        """
        
        result = execute_nadesiko_code(en_code, language="english")
        print("英語実行結果:")
        print(result)
        
        # ウィンドウを表示
        show_gui_window()
        
        # 少し待つ
        time.sleep(3)
        
    else:
        print("❌ GUI起動失敗")

def example_6_advanced_control():
    """例6: 高度な制御"""
    print("\n=== 例6: 高度な制御 ===")
    
    gui = get_gui()
    
    # GUIを起動
    if gui.start_gui(language="japanese", show_window=False):
        print("✅ GUI起動成功")
        
        # 複数のコードを連続実行
        programs = [
            ("基本計算", "10と5を足す\n「足し算: {それ}」を表示"),
            ("条件分岐", "もし15が10より大きいならば\n    「15は10より大きい」を表示"),
            ("繰り返し", "3回繰り返す\n    「カウント: {それ}」を表示")
        ]
        
        for name, code in programs:
            print(f"\n--- {name} ---")
            result = gui.execute_code(code)
            print(result)
            time.sleep(1)
        
        # ウィンドウの表示/非表示テスト
        print("\nウィンドウ表示テスト...")
        gui.show_window()
        time.sleep(2)
        
        print("ウィンドウ非表示テスト...")
        gui.hide_window()
        time.sleep(2)
        
        print("再度ウィンドウ表示...")
        gui.show_window()
        time.sleep(3)
        
        # ステータス詳細確認
        status = gui.get_status()
        print(f"\n最終ステータス: {status}")
        
    else:
        print("❌ GUI起動失敗")

def main():
    """メイン関数 - 全例を実行"""
    print("なでしこ3 GUIモジュール使用例")
    print("=" * 50)
    
    examples = [
        example_1_basic_usage,
        example_2_background_gui,
        example_3_context_manager,
        example_4_decorator,
        example_5_language_switching,
        example_6_advanced_control
    ]
    
    try:
        for i, example_func in enumerate(examples, 1):
            print(f"\n🚀 例{i}を実行中...")
            example_func()
            
            if i < len(examples):
                print("\n" + "=" * 50)
                print("次の例に進むにはEnterキーを押してください...")
                input()
                
    except KeyboardInterrupt:
        print("\nユーザーによる中断")
    except Exception as e:
        print(f"\nエラー: {e}")
    finally:
        # 最後にGUIを停止
        print("\n🛑 GUIを停止します...")
        stop_gui()
        print("✅ 全例の実行完了")

if __name__ == "__main__":
    main()
