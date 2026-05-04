#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこパイソン GUIアプリケーション V1
ナディスコ日本語プログラムV1の要素と積み木デザインを実装
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import queue
import json
from datetime import datetime
import pystray
from PIL import Image, ImageDraw
import webbrowser

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.nadesiko_parser import NadesikoParser
from src.english_parser import EnglishParser

class NadesikoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("なでしこパイソン V6 - 積み木プログラミング")
        self.root.geometry("1200x800")
        
        # パーサー初期化
        self.japanese_parser = NadesikoParser()
        self.english_parser = EnglishParser()
        
        # 言語モード
        self.language_mode = "japanese"
        
        # 積み木ブロック定義
        self.blocks = self.create_blocks()
        
        # 実行キュー
        self.execution_queue = queue.Queue()
        
        # GUI構築
        self.setup_ui()
        
        # タスクトレイアイコン
        self.setup_tray_icon()
        
        # プログラム実行スレッド
        self.execution_thread = None
        
    def create_blocks(self):
        """積み木ブロックを定義"""
        blocks = {
            "japanese": {
                "basic": [
                    {"name": "変数宣言", "template": "{変数名}は{値}", "color": "#FF6B6B"},
                    {"name": "表示", "template": "「{内容}」を表示", "color": "#4ECDC4"},
                    {"name": "代入", "template": "{変数名}に{値}を代入", "color": "#45B7D1"},
                ],
                "math": [
                    {"name": "足し算", "template": "{A}と{B}を足す", "color": "#96CEB4"},
                    {"name": "引き算", "template": "{A}から{B}を引く", "color": "#FFEAA7"},
                    {"name": "掛け算", "template": "{A}に{B}を掛ける", "color": "#DDA0DD"},
                    {"name": "割り算", "template": "{A}を{B}で割る", "color": "#98D8C8"},
                ],
                "control": [
                    {"name": "もし", "template": "もし{条件}ならば", "color": "#FFB6C1"},
                    {"name": "違えば", "template": "違えば", "color": "#87CEEB"},
                    {"name": "繰り返し", "template": "{回数}回繰り返す", "color": "#F0E68C"},
                ],
                "function": [
                    {"name": "関数定義", "template": "●{関数名}（{引数}）", "color": "#FFA07A"},
                    {"name": "戻り値", "template": "{値}を返す", "color": "#20B2AA"},
                ]
            },
            "english": {
                "basic": [
                    {"name": "Variable", "template": "{variable} is {value}", "color": "#FF6B6B"},
                    {"name": "Print", "template": "show {content}", "color": "#4ECDC4"},
                    {"name": "Assign", "template": "let {variable} be {value}", "color": "#45B7D1"},
                ],
                "math": [
                    {"name": "Add", "template": "{A} plus {B}", "color": "#96CEB4"},
                    {"name": "Subtract", "template": "{A} minus {B}", "color": "#FFEAA7"},
                    {"name": "Multiply", "template": "{A} times {B}", "color": "#DDA0DD"},
                    {"name": "Divide", "template": "{A} divided by {B}", "color": "#98D8C8"},
                ],
                "control": [
                    {"name": "If", "template": "if {condition}", "color": "#FFB6C1"},
                    {"name": "Else", "template": "else", "color": "#87CEEB"},
                    {"name": "Repeat", "template": "repeat {count} times", "color": "#F0E68C"},
                ],
                "function": [
                    {"name": "Function", "template": "function {name}({params})", "color": "#FFA07A"},
                    {"name": "Return", "template": "return {value}", "color": "#20B2AA"},
                ]
            }
        }
        return blocks
    
    def setup_ui(self):
        """UIを構築"""
        # メインフレーム
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 上部ツールバー
        self.setup_toolbar(main_frame)
        
        # 中央コンテンツ
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # 左側：積み木パレット
        self.setup_block_palette(content_frame)
        
        # 中央：コードエディタ
        self.setup_code_editor(content_frame)
        
        # 右側：実行結果
        self.setup_output_panel(content_frame)
        
        # 下部：ステータスバー
        self.setup_status_bar()
        
    def setup_toolbar(self, parent):
        """ツールバーを設定"""
        toolbar = ttk.Frame(parent)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # 言語切り替え
        ttk.Label(toolbar, text="言語:").pack(side=tk.LEFT, padx=(0, 5))
        self.language_var = tk.StringVar(value="japanese")
        language_combo = ttk.Combobox(toolbar, textvariable=self.language_var, 
                                     values=["japanese", "english"], width=10, state="readonly")
        language_combo.pack(side=tk.LEFT, padx=(0, 10))
        language_combo.bind("<<ComboboxSelected>>", self.change_language)
        
        # 実行ボタン
        ttk.Button(toolbar, text="▶ 実行", command=self.run_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🗑 クリア", command=self.clear_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="💾 保存", command=self.save_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="📁 読込", command=self.load_code).pack(side=tk.LEFT, padx=5)
        
        # ヘルプボタン
        ttk.Button(toolbar, text="❓ ヘルプ", command=self.show_help).pack(side=tk.RIGHT, padx=5)
        
    def setup_block_palette(self, parent):
        """積み木パレットを設定"""
        palette_frame = ttk.LabelFrame(parent, text="🧱 積み木ブロック", width=250)
        palette_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        palette_frame.pack_propagate(False)
        
        # スクロール可能なフレーム
        canvas = tk.Canvas(palette_frame)
        scrollbar = ttk.Scrollbar(palette_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # カテゴリ別にブロックを配置
        self.block_widgets = {}
        categories = ["basic", "math", "control", "function"]
        category_names = {"basic": "基本", "math": "数学", "control": "制御", "function": "関数"}
        
        for category in categories:
            # カテゴリフレーム
            cat_frame = ttk.LabelFrame(scrollable_frame, text=category_names[category])
            cat_frame.pack(fill=tk.X, padx=5, pady=5)
            
            # ブロックボタン
            self.block_widgets[category] = []
            blocks = self.blocks[self.language_mode][category]
            
            for block in blocks:
                btn = tk.Button(cat_frame, text=block["name"], 
                               bg=block["color"], fg="white",
                               font=("Arial", 10, "bold"),
                               relief=tk.RAISED, bd=2)
                btn.pack(fill=tk.X, padx=5, pady=2)
                btn.bind("<Button-1>", lambda e, b=block: self.add_block_to_code(b))
                self.block_widgets[category].append(btn)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def setup_code_editor(self, parent):
        """コードエディタを設定"""
        editor_frame = ttk.LabelFrame(parent, text="📝 コードエディタ")
        editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # テキストエディタ
        self.code_text = scrolledtext.ScrolledText(editor_frame, 
                                                  font=("Courier", 12),
                                                  wrap=tk.WORD,
                                                  height=20)
        self.code_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 行番号
        self.line_numbers = tk.Text(editor_frame, width=4, padx=3, takefocus=0,
                                   borderwidth=0, state="disabled", 
                                   background="lightgray", font=("Courier", 12))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # 行番号更新
        self.code_text.bind("<Key>", self.update_line_numbers)
        self.code_text.bind("<MouseWheel>", self.update_line_numbers)
        self.update_line_numbers()
        
    def setup_output_panel(self, parent):
        """出力パネルを設定"""
        output_frame = ttk.LabelFrame(parent, text="📊 実行結果", width=300)
        output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        output_frame.pack_propagate(False)
        
        # 出力テキスト
        self.output_text = scrolledtext.ScrolledText(output_frame, 
                                                    font=("Courier", 10),
                                                    wrap=tk.WORD,
                                                    height=20,
                                                    state="disabled")
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def setup_status_bar(self):
        """ステータスバーを設定"""
        self.status_bar = ttk.Label(self.root, text="準備完了", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_tray_icon(self):
        """タスクトレイアイコンを設定"""
        # なでしこの花のアイコンを作成
        image = Image.new('RGB', (64, 64), color='white')
        draw = ImageDraw.Draw(image)
        
        # なでしこの花を描画（簡易的な花のデザイン）
        # 花びら（ピンク）
        petal_color = '#FFB6C1'
        center_x, center_y = 32, 32
        
        # 5枚の花びら
        import math
        for i in range(5):
            angle = math.radians(i * 72 - 90)  # 72度間隔で5枚
            petal_x = center_x + math.cos(angle) * 15
            petal_y = center_y + math.sin(angle) * 15
            draw.ellipse([petal_x-8, petal_y-8, petal_x+8, petal_y+8], 
                         fill=petal_color, outline='#FF69B4', width=1)
        
        # 花の中心（黄色）
        draw.ellipse([center_x-6, center_y-6, center_x+6, center_y+6], 
                     fill='#FFD700', outline='#FFA500', width=1)
        
        # 茎（緑）
        draw.line([center_x, center_y+6, center_x, 58], fill='#228B22', width=3)
        
        # 葉（緑）
        leaf_x = center_x - 10
        leaf_y = center_y + 20
        draw.ellipse([leaf_x-4, leaf_y-2, leaf_x+4, leaf_y+2], 
                     fill='#32CD32', outline='#228B22', width=1)
        
        # メニュー
        menu = pystray.Menu(
            pystray.MenuItem("表示", self.show_window),
            pystray.MenuItem("終了", self.quit_app)
        )
        
        # タスクトレイアイコン作成
        self.tray_icon = pystray.Icon("nadesiko", image, "なでしこパイソン", menu)
        
        # 別スレッドで起動
        threading.Thread(target=self.tray_icon.run, daemon=True).start()
        
    def add_block_to_code(self, block):
        """積み木ブロックをコードに追加"""
        template = block["template"]
        self.code_text.insert(tk.END, template + "\n")
        self.update_line_numbers()
        
    def change_language(self, event=None):
        """言語を切り替え"""
        self.language_mode = self.language_var.get()
        self.update_block_palette()
        self.status_bar.config(text=f"言語を{self.language_mode}に切り替え")
        
    def update_block_palette(self):
        """積み木パレットを更新"""
        categories = ["basic", "math", "control", "function"]
        
        for category in categories:
            blocks = self.blocks[self.language_mode][category]
            widgets = self.block_widgets[category]
            
            for i, (block, widget) in enumerate(zip(blocks, widgets)):
                if i < len(widgets):
                    widget.config(text=block["name"], bg=block["color"])
                    
    def update_line_numbers(self, event=None):
        """行番号を更新"""
        self.line_numbers.config(state="normal")
        line_count = int(self.code_text.index('end-1c').split('.')[0])
        line_numbers_text = "\n".join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.delete(1.0, tk.END)
        self.line_numbers.insert(1.0, line_numbers_text)
        self.line_numbers.config(state="disabled")
        
    def run_code(self):
        """コードを実行"""
        code = self.code_text.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("警告", "コードが入力されていません")
            return
            
        self.status_bar.config(text="実行中...")
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        
        # 別スレッドで実行
        threading.Thread(target=self.execute_code, args=(code,), daemon=True).start()
        
    def execute_code(self, code):
        """コードを実行（別スレッド）"""
        try:
            if self.language_mode == "japanese":
                self.japanese_parser.execute(code)
            else:
                self.english_parser.execute(code)
                
            # 実行結果をUIに表示
            self.root.after(0, self.show_execution_result, "実行完了")
            
        except Exception as e:
            self.root.after(0, self.show_execution_result, f"エラー: {e}")
            
    def show_execution_result(self, result):
        """実行結果を表示"""
        self.output_text.insert(tk.END, result + "\n")
        self.output_text.config(state="disabled")
        self.status_bar.config(text="実行完了")
        
    def clear_code(self):
        """コードをクリア"""
        self.code_text.delete(1.0, tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state="disabled")
        self.update_line_numbers()
        self.status_bar.config(text="クリア完了")
        
    def save_code(self):
        """コードを保存"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".nako",
            filetypes=[("なでしこファイル", "*.nako"), ("すべてのファイル", "*.*")]
        )
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.code_text.get(1.0, tk.END))
            self.status_bar.config(text=f"保存: {filename}")
            
    def load_code(self):
        """コードを読み込み"""
        filename = filedialog.askopenfilename(
            filetypes=[("なでしこファイル", "*.nako"), ("すべてのファイル", "*.*")]
        )
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                self.code_text.delete(1.0, tk.END)
                self.code_text.insert(1.0, f.read())
            self.update_line_numbers()
            self.status_bar.config(text=f"読込: {filename}")
            
    def show_help(self):
        """ヘルプを表示"""
        help_text = """
なでしこパイソン V1 - 積み木プログラミング

🧱 積み木ブロック:
  左側のパレットからブロックをクリックしてコードに追加

📝 コード編集:
  直接コードを編集することも可能

▶ 実行:
  実行ボタンでコードを実行

💾 保存/読込:
  コードをファイルに保存・読込

🌐 言語切り替え:
  日本語と英語のプログラミング言語を切り替え

📚 詳細なドキュメント:
  README.mdを参照してください
        """
        messagebox.showinfo("ヘルプ", help_text)
        
    def show_window(self, icon=None, item=None):
        """ウィンドウを表示"""
        self.root.deiconify()
        self.root.lift()
        
    def quit_app(self, icon=None, item=None):
        """アプリケーションを終了"""
        self.tray_icon.stop()
        self.root.quit()
        
    def run(self):
        """アプリケーションを実行"""
        # ウィンドウが閉じられたときの処理
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        
        # アプリケーションを起動
        self.root.mainloop()
        
    def hide_window(self):
        """ウィンドウを隠す"""
        self.root.withdraw()

def main():
    """メイン関数"""
    app = NadesikoGUI()
    app.run()

if __name__ == "__main__":
    main()
