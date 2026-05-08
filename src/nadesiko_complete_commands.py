"""
なでしこ3完全互換コマンド拡張
GUI、ネットワーク、データベースなどの高度な機能を実装
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import sqlite3
import requests
import json
import csv
import subprocess
import threading
import webbrowser
from pathlib import Path

class NadesikoCompleteCommands:
    """なでしこ3の高度なコマンドを実装"""
    
    def __init__(self):
        self.root = None
        self.widgets = {}
        self.canvas_items = {}
        self._result = None
        
    # === GUI機能 ===
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
        """メッセージボックス"""
        messagebox.showinfo(title, message)
        self._result = True
        return self._result
    
    def 警告ボックス(self, title="警告", message=""):
        """警告ボックス"""
        messagebox.showwarning(title, message)
        self._result = True
        return self._result
    
    def エラーボックス(self, title="エラー", message=""):
        """エラーボックス"""
        messagebox.showerror(title, message)
        self._result = True
        return self._result
    
    def 確認ボックス(self, title="確認", message=""):
        """確認ボックス"""
        self._result = messagebox.askyesno(title, message)
        return self._result
    
    def 入力ボックス(self, title="入力", message="", default=""):
        """入力ボックス"""
        self._result = simpledialog.askstring(title, message, initialvalue=default)
        return self._result
    
    def ファイル選択(self, title="ファイル選択", filetypes=[("すべてのファイル", "*.*")]):
        """ファイル選択"""
        self._result = filedialog.askopenfilename(title=title, filetypes=filetypes)
        return self._result
    
    def ファイル保存(self, title="ファイル保存", defaultextension=".txt", filetypes=[("テキストファイル", "*.txt")]):
        """ファイル保存"""
        self._result = filedialog.asksaveasfilename(title=title, defaultextension=defaultextension, filetypes=filetypes)
        return self._result
    
    def ボタン作成(self, parent=None, text="ボタン", x=10, y=10, width=100, height=30, command=None):
        """ボタン作成"""
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
        """ラベル作成"""
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
        """テキストボックス作成"""
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
        """テキストエリア作成"""
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
        """キャンバス作成"""
        if parent is None:
            parent = self.root
        
        if parent is None:
            return None
        
        canvas = tk.Canvas(parent, width=width, height=height, bg="white")
        canvas.place(x=x, y=y)
        
        widget_id = f"canvas_{len(self.widgets)}"
        self.widgets[widget_id] = canvas
        self._result = widget_id
        return widget_id
    
    def ウィジェット削除(self, widget_id):
        """ウィジェット削除"""
        if widget_id in self.widgets:
            self.widgets[widget_id].destroy()
            del self.widgets[widget_id]
    
    def ウィジェットテキスト設定(self, widget_id, text):
        """ウィジェットテキスト設定"""
        if widget_id in self.widgets:
            widget = self.widgets[widget_id]
            if hasattr(widget, 'config'):
                widget.config(text=text)
            elif hasattr(widget, 'delete') and hasattr(widget, 'insert'):
                widget.delete(1.0, tk.END)
                widget.insert(tk.END, text)
    
    def ウィジェットテキスト取得(self, widget_id):
        """ウィジェットテキスト取得"""
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
    
    # === キャンバス描画 ===
    def 線描画(self, canvas_id, x1, y1, x2, y2, color="black", width=1):
        """線描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
            self.canvas_items[f"line_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def 矩形描画(self, canvas_id, x1, y1, x2, y2, fill="white", outline="black"):
        """矩形描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
            self.canvas_items[f"rect_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def 円描画(self, canvas_id, x, y, radius, fill="white", outline="black"):
        """円描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill, outline=outline)
            self.canvas_items[f"circle_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def テキスト描画(self, canvas_id, x, y, text, color="black", font=("Arial", 12)):
        """テキスト描画"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            item_id = canvas.create_text(x, y, text=text, fill=color, font=font)
            self.canvas_items[f"text_{len(self.canvas_items)}"] = item_id
            self._result = item_id
            return item_id
    
    def キャンバスクリア(self, canvas_id):
        """キャンバスクリア"""
        if canvas_id in self.widgets:
            canvas = self.widgets[canvas_id]
            canvas.delete("all")
            self.canvas_items.clear()
    
    # === ネットワーク機能 ===
    def HTTP取得(self, url, headers=None, timeout=30):
        """HTTP GETリクエスト"""
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            self._result = response.text
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def HTTP投稿(self, url, data=None, headers=None, timeout=30):
        """HTTP POSTリクエスト"""
        try:
            response = requests.post(url, data=data, headers=headers, timeout=timeout)
            response.raise_for_status()
            self._result = response.text
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def JSON取得(self, url, headers=None, timeout=30):
        """JSONデータ取得"""
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            self._result = response.json()
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def JSON投稿(self, url, data=None, headers=None, timeout=30):
        """JSONデータ投稿"""
        try:
            response = requests.post(url, json=data, headers=headers, timeout=timeout)
            response.raise_for_status()
            self._result = response.json()
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ファイルダウンロード(self, url, save_path, timeout=30):
        """ファイルダウンロード"""
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            with open(save_path, 'wb') as f:
                f.write(response.content)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def URL開く(self, url):
        """URLをブラウザで開く"""
        try:
            webbrowser.open(url)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === データベース機能 ===
    def SQLite3接続(self, db_path):
        """SQLite3データベース接続"""
        try:
            conn = sqlite3.connect(db_path)
            self._result = conn
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def SQL実行(self, conn, sql, params=None):
        """SQL実行"""
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            
            if sql.strip().upper().startswith('SELECT'):
                self._result = cursor.fetchall()
            else:
                conn.commit()
                self._result = cursor.rowcount
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def テーブル作成(self, conn, table_name, columns):
        """テーブル作成"""
        try:
            cursor = conn.cursor()
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
            cursor.execute(sql)
            conn.commit()
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 挿入(self, conn, table_name, data):
        """データ挿入"""
        try:
            cursor = conn.cursor()
            placeholders = ', '.join(['?'] * len(data))
            sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(sql, data)
            conn.commit()
            self._result = cursor.lastrowid
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 選択(self, conn, table_name, where_clause="", params=None):
        """データ選択"""
        try:
            cursor = conn.cursor()
            sql = f"SELECT * FROM {table_name}"
            if where_clause:
                sql += f" WHERE {where_clause}"
            
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            
            self._result = cursor.fetchall()
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 更新(self, conn, table_name, set_clause, where_clause, params=None):
        """データ更新"""
        try:
            cursor = conn.cursor()
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            
            conn.commit()
            self._result = cursor.rowcount
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 削除(self, conn, table_name, where_clause, params=None):
        """データ削除"""
        try:
            cursor = conn.cursor()
            sql = f"DELETE FROM {table_name} WHERE {where_clause}"
            
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            
            conn.commit()
            self._result = cursor.rowcount
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === システム操作 ===
    def コマンド実行(self, command, shell=True):
        """コマンド実行"""
        try:
            result = subprocess.run(command, shell=shell, capture_output=True, text=True)
            self._result = {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ファイル実行(self, filepath):
        """ファイル実行"""
        try:
            result = subprocess.run([filepath], capture_output=True, text=True)
            self._result = {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def プロセス開始(self, command):
        """プロセス開始"""
        try:
            process = subprocess.Popen(command, shell=True)
            self._result = process.pid
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ディレクトリ作成(self, dirpath):
        """ディレクトリ作成"""
        try:
            os.makedirs(dirpath, exist_ok=True)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ディレクトリ削除(self, dirpath):
        """ディレクトリ削除"""
        try:
            import shutil
            shutil.rmtree(dirpath)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ファイルコピー(self, src, dst):
        """ファイルコピー"""
        try:
            import shutil
            shutil.copy2(src, dst)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ファイル移動(self, src, dst):
        """ファイル移動"""
        try:
            import shutil
            shutil.move(src, dst)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === マルチメディア ===
    def 音声再生(self, filepath):
        """音声ファイル再生"""
        try:
            import platform
            if platform.system() == 'Windows':
                import winsound
                winsound.PlaySound(filepath, winsound.SND_FILENAME)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.run(['afplay', filepath])
            else:  # Linux
                subprocess.run(['aplay', filepath])
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ビープ音(self, frequency=1000, duration=100):
        """ビープ音"""
        try:
            import platform
            if platform.system() == 'Windows':
                import winsound
                winsound.Beep(frequency, duration)
            else:
                # 他のOSでは簡易的なビープ
                print('\a')
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === その他高度な機能 ===
    def 非同期実行(self, func, *args, **kwargs):
        """非同期実行"""
        def async_func():
            try:
                result = func(*args, **kwargs)
                self._result = result
                return result
            except Exception as e:
                self._result = f"エラー: {e}"
                return f"エラー: {e}"
        
        thread = threading.Thread(target=async_func)
        thread.daemon = True
        thread.start()
        return thread
    
    def 定期実行(self, func, interval, *args, **kwargs):
        """定期実行"""
        def periodic_func():
            while True:
                try:
                    func(*args, **kwargs)
                    time.sleep(interval)
                except Exception as e:
                    print(f"定期実行エラー: {e}")
                    break
        
        thread = threading.Thread(target=periodic_func)
        thread.daemon = True
        thread.start()
        return thread
    
    def それ(self):
        """直前の結果"""
        return self._result
