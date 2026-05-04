#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこ GUIデザイナー起動スクリプト
"""

import sys
import os

def check_dependencies():
    """依存関係をチェック"""
    try:
        import tkinter
        return True
    except ImportError:
        print("tkinterが見つかりません")
        print("GUIデザイナーにはtkinterが必要です")
        return False

def main():
    """メイン関数"""
    print("なでしこパイソン V6 GUIデザイナーを起動します...")
    
    # 依存関係チェック
    if not check_dependencies():
        sys.exit(1)
    
    # GUIデザイナーを起動
    try:
        from src.gui_designer import GUIDesigner
        designer = GUIDesigner()
        designer.run()
    except Exception as e:
        print(f"起動エラー: {e}")
        print("詳細なエラー情報:")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
