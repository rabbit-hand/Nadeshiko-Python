#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこパイソン V6 GUIモジュール
簡単なAPIでGUIアプリケーションを起動・制御
"""

import sys
import os
import threading
import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image, ImageDraw

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NadesikoGUIModule:
    """なでしこ GUIモジュール - 簡単API"""
    
    def __init__(self):
        self.app = None
        self.app_thread = None
        self.is_running = False
        
    def start_gui(self, language="japanese", show_window=True):
        """
        GUIアプリケーションを起動
        
        Args:
            language (str): "japanese" または "english"
            show_window (bool): 起動時にウィンドウを表示するか
        
        Returns:
            bool: 起動成功ならTrue
        """
        if self.is_running:
            print("GUIアプリケーションは既に実行中です")
            return False
            
        try:
            # 別スレッドでGUIを起動
            self.app_thread = threading.Thread(
                target=self._run_gui_app, 
                args=(language, show_window),
                daemon=True
            )
            self.app_thread.start()
            
            # 少し待って起動を確認
            import time
            time.sleep(0.5)
            
            if self.app_thread.is_alive():
                self.is_running = True
                print(f"なでしこ GUIを起動しました（言語: {language}）")
                return True
            else:
                print("GUIアプリケーションの起動に失敗しました")
                return False
                
        except Exception as e:
            print(f"起動エラー: {e}")
            return False
    
    def _run_gui_app(self, language, show_window):
        """GUIアプリケーションを実行（内部メソッド）"""
        try:
            from gui_app import NadesikoGUI
            self.app = NadesikoGUI()
            
            # 言語を設定
            self.app.language_mode = language
            
            if show_window:
                self.app.run()
            else:
                # ウィンドウを非表示で起動
                self.app.root.withdraw()
                self.app.run()
                
        except Exception as e:
            print(f"GUI実行エラー: {e}")
            
    def show_window(self):
        """ウィンドウを表示"""
        if self.app and self.is_running:
            try:
                self.app.root.after(0, self.app.show_window)
                return True
            except:
                return False
        return False
    
    def hide_window(self):
        """ウィンドウを隠す"""
        if self.app and self.is_running:
            try:
                self.app.root.after(0, self.app.hide_window)
                return True
            except:
                return False
        return False
    
    def execute_code(self, code, language="japanese"):
        """
        コードを実行
        
        Args:
            code (str): 実行するコード
            language (str): "japanese" または "english"
        
        Returns:
            str: 実行結果
        """
        try:
            if language == "japanese":
                from src.nadesiko_parser import NadesikoParser
                parser = NadesikoParser()
                # 結果をキャプチャ
                import io
                import sys
                old_stdout = sys.stdout
                sys.stdout = captured_output = io.StringIO()
                
                try:
                    parser.execute(code)
                    result = captured_output.getvalue()
                finally:
                    sys.stdout = old_stdout
                    
                return result
            else:
                from src.english_parser import EnglishParser
                parser = EnglishParser()
                import io
                import sys
                old_stdout = sys.stdout
                sys.stdout = captured_output = io.StringIO()
                
                try:
                    parser.execute(code)
                    result = captured_output.getvalue()
                finally:
                    sys.stdout = old_stdout
                    
                return result
                
        except Exception as e:
            return f"エラー: {e}"
    
    def stop_gui(self):
        """GUIアプリケーションを停止"""
        if self.is_running and self.app:
            try:
                self.app.root.after(0, self.app.quit_app)
                self.is_running = False
                print("GUIアプリケーションを停止しました")
                return True
            except:
                return False
        return False
    
    def get_status(self):
        """ステータスを取得"""
        return {
            "running": self.is_running,
            "language": getattr(self.app, 'language_mode', 'unknown') if self.app else 'unknown'
        }

# グローバルインスタンス
_gui_instance = None

def get_gui():
    """GUIインスタンスを取得（シングルトン）"""
    global _gui_instance
    if _gui_instance is None:
        _gui_instance = NadesikoGUIModule()
    return _gui_instance

# 簡単な関数API
def start_gui(language="japanese", show_window=True):
    """GUIを起動（簡単関数）"""
    return get_gui().start_gui(language, show_window)

def stop_gui():
    """GUIを停止（簡単関数）"""
    return get_gui().stop_gui()

def execute_nadesiko_code(code, language="japanese"):
    """なでしこコードを実行（簡単関数）"""
    return get_gui().execute_code(code, language)

def show_gui_window():
    """GUIウィンドウを表示（簡単関数）"""
    return get_gui().show_window()

def hide_gui_window():
    """GUIウィンドウを隠す（簡単関数）"""
    return get_gui().hide_window()

def get_gui_status():
    """GUIステータスを取得（簡単関数）"""
    return get_gui().get_status()

# デコレータ
def with_gui(language="japanese"):
    """GUI付きで関数を実行するデコレータ"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # GUIを起動
            if start_gui(language, show_window=False):
                try:
                    # 関数を実行
                    result = func(*args, **kwargs)
                    # ウィンドウを表示
                    show_gui_window()
                    return result
                except Exception as e:
                    print(f"実行エラー: {e}")
                    return None
                finally:
                    # GUIはバックグラウンドで実行継続
                    pass
            else:
                print("GUIの起動に失敗しました")
                return None
        return wrapper
    return decorator

# コンテキストマネージャ
class NadesikoGUIContext:
    """GUIコンテキストマネージャ"""
    
    def __init__(self, language="japanese", show_window=True):
        self.language = language
        self.show_window = show_window
        self.gui = get_gui()
        
    def __enter__(self):
        self.gui.start_gui(self.language, self.show_window)
        return self.gui
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # GUIはバックグラウンドで実行継続
        pass

# 使いやすいエイリアス
def gui_context(language="japanese", show_window=True):
    """GUIコンテキストを取得"""
    return NadesikoGUIContext(language, show_window)

if __name__ == "__main__":
    # テスト用
    print("なでしこ GUIモジュールテスト")
    
    # 簡単な起動テスト
    if start_gui():
        print("GUI起動成功")
        
        # コード実行テスト
        result = execute_nadesiko_code("""
        Aは10
        Bは20
        CはAとBを足す
        「結果: {C}」を表示
        """)
        print("実行結果:")
        print(result)
        
        # ステータス確認
        status = get_gui_status()
        print(f"ステータス: {status}")
        
    else:
        print("GUI起動失敗")
