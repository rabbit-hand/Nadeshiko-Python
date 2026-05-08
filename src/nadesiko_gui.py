"""
なでしこ3互換GUIライブラリ
tkinterを使用してGUI機能を実装
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, Canvas
import threading

class NadesikoGUI:
    """なでしこ3のGUI機能を実装"""
    
    def __init__(self):
        self.root = None
        self.widgets = {}
        self.canvas_items = {}
        self._result = None
        
    def ウィンドウ作成(self, title="なでしこプログラム", width=400, height=300):
        """メインウィンドウを作成"""
        if self.root is None:
            self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self._result = self.root
        return self._result
    
    def ウィンドウ表示(self):
        """ウィンドウを表示"""
        if self.root:
            self.root.mainloop()
    
    def ウィンドウ閉じる(self):
        """ウィンドウを閉じる"""
        if self.root:
            self.root.destroy()
            self.root = None
    
    def メッセージボックス(self, title="メッセージ", message=""):
        """メッセージボックスを表示"""
        messagebox.showinfo(title, message)
    
    def 警告ボックス(self, title="警告", message=""):
        """警告ボックスを表示"""
        messagebox.showwarning(title, message)
    
    def エラーボックス(self, title="エラー", message=""):
        """エラーボックスを表示"""
        messagebox.showerror(title, message)
    
    def 確認ボックス(self, title="確認", message=""):
        """確認ボックスを表示"""
        self._result = messagebox.askyesno(title, message)
        return self._result
    
    def 入力ボックス(self, title="入力", message="", default=""):
        """入力ボックスを表示"""
        self._result = simpledialog.askstring(title, message, initialvalue=default)
        return self._result
    
    def ファイル選択(self, title="ファイル選択", filetypes=[("すべてのファイル", "*.*")]):
        """ファイル選択ダイアログ"""
        self._result = filedialog.askopenfilename(title=title, filetypes=filetypes)
        return self._result
    
    def ファイル保存(self, title="ファイル保存", defaultextension=".txt", filetypes=[("テキストファイル", "*.txt")]):
        """ファイル保存ダイアログ"""
        self._result = filedialog.asksaveasfilename(title=title, defaultextension=defaultextension, filetypes=filetypes)
        return self._result
    
    def ボタン作成(self, parent=None, text="ボタン", x=10, y=10, width=100, height=30, command=None):
        """ボタンを作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        btn = tk.Button(parent, text=text, command=command, width=width//10, height=height//20)
        btn.place(x=x, y=y)
        
        widget_id = f"button_{len(self.widgets)}"
        self.widgets[widget_id] = btn
        self._result = widget_id
        return widget_id
    
    def ラベル作成(self, parent=None, text="ラベル", x=10, y=10):
        """ラベルを作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        label = tk.Label(parent, text=text)
        label.place(x=x, y=y)
        
        widget_id = f"label_{len(self.widgets)}"
        self.widgets[widget_id] = label
        self._result = widget_id
        return widget_id
    
    def テキストボックス作成(self, parent=None, x=10, y=10, width=200, height=30):
        """テキストボックスを作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        entry = tk.Entry(parent, width=width//10)
        entry.place(x=x, y=y)
        
        widget_id = f"entry_{len(self.widgets)}"
        self.widgets[widget_id] = entry
        self._result = widget_id
        return widget_id
    
    def テキストエリア作成(self, parent=None, x=10, y=10, width=300, height=200):
        """テキストエリアを作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        text_area = tk.Text(parent, width=width//10, height=height//20)
        text_area.place(x=x, y=y)
        
        widget_id = f"text_{len(self.widgets)}"
        self.widgets[widget_id] = text_area
        self._result = widget_id
        return widget_id
    
    def キャンバス作成(self, parent=None, x=10, y=10, width=400, height=300):
        """キャンバスを作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        canvas = Canvas(parent, width=width, height=height, bg="white")
        canvas.place(x=x, y=y)
        
        widget_id = f"canvas_{len(self.widgets)}"
        self.widgets[widget_id] = canvas
        self._result = widget_id
        return widget_id
    
    def ウィジェット削除(self, widget_id):
        """ウィジェットを削除"""
        if widget_id in self.widgets:
            self.widgets[widget_id].destroy()
            del self.widgets[widget_id]
    
    def ウィジェットテキスト設定(self, widget_id, text):
        """ウィジェットのテキストを設定"""
        if widget_id in self.widgets:
            widget = self.widgets[widget_id]
            if hasattr(widget, 'config'):
                widget.config(text=text)
            elif hasattr(widget, 'delete') and hasattr(widget, 'insert'):
                widget.delete(1.0, tk.END)
                widget.insert(tk.END, text)
    
    def ウィジェットテキスト取得(self, widget_id):
        """ウィジェットのテキストを取得"""
        if widget_id in self.widgets:
            widget = self.widgets[widget_id]
            if hasattr(widget, 'cget'):
                self._result = widget.cget("text")
            elif hasattr(widget, 'get'):
                if hasattr(widget, 'index'):  # Text widget
                    self._result = widget.get(1.0, tk.END).strip()
                else:  # Entry widget
                    self._result = widget.get()
            else:
                self._result = ""
            return self._result
        return ""
    
    # === キャンバス描画機能 ===
    def 線描画(self, canvas_id, x1, y1, x2, y2, color="black", width=1):
        """キャンバスに線を描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
            self.canvas_items[f"line_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def 矩形描画(self, canvas_id, x1, y1, x2, y2, fill="white", outline="black"):
        """キャンバスに矩形を描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
            self.canvas_items[f"rect_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def 円描画(self, canvas_id, x, y, radius, fill="white", outline="black"):
        """キャンバスに円を描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill, outline=outline)
            self.canvas_items[f"circle_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def テキスト描画(self, canvas_id, x, y, text, color="black", font=("Arial", 12)):
        """キャンバスにテキストを描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_text(x, y, text=text, fill=color, font=font)
            self.canvas_items[f"text_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def キャンバスクリア(self, canvas_id):
        """キャンバスをクリア"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            canvas.delete("all")
            self.canvas_items.clear()
    
    # === イベント処理 ===
    def イベント待つ(self):
        """イベントを待つ（非ブロッキング）"""
        if self.root:
            self.root.update()
    
    def イベントループ開始(self):
        """イベントループを開始（別スレッドで実行）"""
        if self.root:
            def run_loop():
                self.root.mainloop()
            thread = threading.Thread(target=run_loop, daemon=True)
            thread.start()
    
    def ウィンドウサイズ変更(self, width, height):
        """ウィンドウサイズを変更"""
        if self.root:
            self.root.geometry(f"{width}x{height}")
    
    def ウィンドウタイトル設定(self, title):
        """ウィンドウタイトルを設定"""
        if self.root:
            self.root.title(title)
    
    def ウィンドウ背景色設定(self, color):
        """ウィンドウ背景色を設定"""
        if self.root:
            self.root.config(bg=color)
    
    def それ(self):
        """直前の操作結果を返す"""
        return self._result
    
    def get_widget(self, widget_id):
        """ウィジェットオブジェクトを取得"""
        return self.widgets.get(widget_id)
    
    def get_canvas_item(self, item_id):
        """キャンバスアイテムを取得"""
        return self.canvas_items.get(item_id)
