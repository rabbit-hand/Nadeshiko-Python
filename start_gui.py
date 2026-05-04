#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこパイソン GUIアプリケーション起動スクリプト
"""

import sys
import os

def check_dependencies():
    """依存関係をチェック"""
    required_packages = ['tkinter', 'PIL', 'pystray']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
            elif package == 'pystray':
                import pystray
            elif package == 'tkinter':
                import tkinter
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"以下のパッケージが見つかりません: {', '.join(missing_packages)}")
        print("インストールコマンド:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def main():
    """メイン関数"""
    print("なでしこパイソン V6 GUIアプリケーションを起動します...")
    
    # 依存関係チェック
    if not check_dependencies():
        sys.exit(1)
    
    # GUIアプリケーションを起動
    try:
        from gui_app import NadesikoGUI
        app = NadesikoGUI()
        app.run()
    except Exception as e:
        print(f"起動エラー: {e}")
        print("詳細なエラー情報:")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
