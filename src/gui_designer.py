#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
なでしこ GUIデザイナー V1
マウスでGUIの形を作れるビジュアルデザイナー
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import copy
from typing import Dict, List, Tuple, Optional

class GUIComponent:
    """GUI部品クラス"""
    
    def __init__(self, component_type: str, x: int, y: int, width: int = 100, height: int = 30):
        self.type = component_type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.properties = self.get_default_properties()
        self.id = f"{component_type}_{id(self)}"
        
    def get_default_properties(self) -> Dict:
        """部品のデフォルトプロパティ"""
        defaults = {
            "button": {
                "text": "ボタン",
                "bg": "#4ECDC4",
                "fg": "white",
                "font": ("Arial", 10),
                "command": "on_button_click"
            },
            "label": {
                "text": "ラベル",
                "bg": "#F0F0F0",
                "fg": "black",
                "font": ("Arial", 10)
            },
            "entry": {
                "text": "",
                "bg": "white",
                "fg": "black",
                "font": ("Arial", 10)
            },
            "text": {
                "text": "テキストエリア",
                "bg": "white",
                "fg": "black",
                "font": ("Arial", 10),
                "wrap": "word"
            },
            "frame": {
                "bg": "#E0E0E0",
                "relief": "raised",
                "bd": 2
            },
            "canvas": {
                "bg": "white",
                "highlightthickness": 1
            },
            "listbox": {
                "bg": "white",
                "fg": "black",
                "font": ("Arial", 10)
            },
            "combobox": {
                "values": ["選択1", "選択2", "選択3"],
                "state": "readonly"
            },
            "checkbutton": {
                "text": "チェックボックス",
                "bg": "#F0F0F0",
                "fg": "black"
            },
            "radiobutton": {
                "text": "ラジオボタン",
                "bg": "#F0F0F0",
                "fg": "black",
                "value": "option1"
            },
            "scale": {
                "from_": 0,
                "to": 100,
                "orient": "horizontal"
            },
            "spinbox": {
                "from_": 0,
                "to": 100,
                "text": "0"
            }
        }
        return defaults.get(self.type, {})
    
    def to_dict(self) -> Dict:
        """辞書に変換"""
        return {
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "properties": copy.deepcopy(self.properties),
            "id": self.id
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'GUIComponent':
        """辞書から復元"""
        component = cls(data["type"], data["x"], data["y"], data["width"], data["height"])
        component.properties = copy.deepcopy(data["properties"])
        component.id = data["id"]
        return component

class GUIDesigner:
    """GUIデザイナーメインクラス"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("なでしこ GUIデザイナー V6")
        self.root.geometry("1400x900")
        
        # デザインキャンバス
        self.canvas = None
        self.design_area = None
        
        # 部品リスト
        self.components: List[GUIComponent] = []
        self.selected_component: Optional[GUIComponent] = None
        
        # ドラッグ状態
        self.dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.component_start_x = 0
        self.component_start_y = 0
        
        # リサイズ状態
        self.resizing = False
        self.resize_handle = None
        
        # プロパティエディタ
        self.property_editor = None
        self.property_vars = {}
        
        # コード生成
        self.code_text = None
        
        # UI構築
        self.setup_ui()
        
    def setup_ui(self):
        """UIを構築"""
        # メインフレーム
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左側：部品パレット
        self.setup_component_palette(main_frame)
        
        # 中央：デザインキャンバス
        self.setup_design_canvas(main_frame)
        
        # 右側：プロパティとコード
        self.setup_right_panel(main_frame)
        
        # 下部：ツールバー
        self.setup_toolbar()
        
    def setup_component_palette(self, parent):
        """部品パレットを設定"""
        palette_frame = ttk.LabelFrame(parent, text="🧩 GUI部品", width=200)
        palette_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        palette_frame.pack_propagate(False)
        
        # 部品ボタン
        components = [
            ("ボタン", "button", "#4ECDC4"),
            ("ラベル", "label", "#F0F0F0"),
            ("入力欄", "entry", "white"),
            ("テキスト", "text", "white"),
            ("フレーム", "frame", "#E0E0E0"),
            ("キャンバス", "canvas", "white"),
            ("リスト", "listbox", "white"),
            ("コンボ", "combobox", "white"),
            ("チェック", "checkbutton", "#F0F0F0"),
            ("ラジオ", "radiobutton", "#F0F0F0"),
            ("スケール", "scale", "#F0F0F0"),
            ("スピン", "spinbox", "white")
        ]
        
        for name, comp_type, color in components:
            btn = tk.Button(
                palette_frame,
                text=name,
                bg=color,
                fg="black" if color in ["white", "#F0F0F0"] else "white",
                relief=tk.RAISED,
                bd=2,
                font=("Arial", 9)
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
            btn.bind("<Button-1>", lambda e, t=comp_type: self.add_component(t))
            
    def setup_design_canvas(self, parent):
        """デザインキャンバスを設定"""
        canvas_frame = ttk.LabelFrame(parent, text="🎨 デザインキャンバス")
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # スクロール可能なキャンバス
        self.canvas = tk.Canvas(canvas_frame, bg="white", scrollregion=(0, 0, 800, 600))
        
        # スクロールバー
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # 配置
        self.canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)
        
        # デザインエリア（グリッド）
        self.design_area = self.canvas.create_rectangle(
            0, 0, 800, 600,
            fill="#FAFAFA",
            outline="#CCCCCC",
            width=1
        )
        
        # イベントバインド
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)
        self.canvas.bind("<Button-3>", self.on_canvas_right_click)
        
        # グリッド線を描画
        self.draw_grid()
        
    def setup_right_panel(self, parent):
        """右側パネルを設定"""
        right_frame = ttk.Frame(parent)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # プロパティエディタ
        self.setup_property_editor(right_frame)
        
        # コード生成
        self.setup_code_generator(right_frame)
        
    def setup_property_editor(self, parent):
        """プロパティエディタを設定"""
        prop_frame = ttk.LabelFrame(parent, text="⚙️ プロパティ")
        prop_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # スクロール可能なフレーム
        canvas = tk.Canvas(prop_frame)
        scrollbar = ttk.Scrollbar(prop_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.property_editor = scrollable_frame
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def setup_code_generator(self, parent):
        """コード生成を設定"""
        code_frame = ttk.LabelFrame(parent, text="💻 生成コード")
        code_frame.pack(fill=tk.BOTH, expand=True)
        
        # ツールバー
        toolbar = ttk.Frame(code_frame)
        toolbar.pack(fill=tk.X, padx=5, pady=2)
        
        ttk.Button(toolbar, text="🔄 更新", command=self.update_code).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📋 コピー", command=self.copy_code).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="▶ 実行", command=self.run_code).pack(side=tk.LEFT, padx=2)
        
        # コードテキスト
        self.code_text = tk.Text(code_frame, font=("Courier", 9), wrap=tk.WORD)
        code_scrollbar = ttk.Scrollbar(code_frame, orient="vertical", command=self.code_text.yview)
        self.code_text.configure(yscrollcommand=code_scrollbar.set)
        
        self.code_text.pack(side="left", fill="both", expand=True, padx=(5, 0), pady=5)
        code_scrollbar.pack(side="right", fill="y", pady=5)
        
    def setup_toolbar(self):
        """ツールバーを設定"""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill=tk.X, side=tk.BOTTOM, pady=(5, 0))
        
        ttk.Button(toolbar, text="💾 保存", command=self.save_design).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📁 読込", command=self.load_design).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🗑️ クリア", command=self.clear_design).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🗑️ 選択削除", command=self.delete_selected).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        ttk.Button(toolbar, text="📐 グリッド", command=self.toggle_grid).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🎯 スナップ", command=self.toggle_snap).pack(side=tk.LEFT, padx=2)
        
        self.grid_enabled = True
        self.snap_enabled = True
        
    def draw_grid(self):
        """グリッドを描画"""
        if not self.grid_enabled:
            return
            
        grid_size = 20
        width = 800
        height = 600
        
        # 垂直線
        for x in range(0, width + 1, grid_size):
            self.canvas.create_line(x, 0, x, height, fill="#E0E0E0", width=1, tags="grid")
            
        # 水平線
        for y in range(0, height + 1, grid_size):
            self.canvas.create_line(0, y, width, y, fill="#E0E0E0", width=1, tags="grid")
            
    def toggle_grid(self):
        """グリッド表示切り替え"""
        self.grid_enabled = not self.grid_enabled
        self.canvas.delete("grid")
        if self.grid_enabled:
            self.draw_grid()
            
    def toggle_snap(self):
        """スナップ切り替え"""
        self.snap_enabled = not self.snap_enabled
        
    def snap_to_grid(self, x: int, y: int) -> Tuple[int, int]:
        """グリッドにスナップ"""
        if self.snap_enabled:
            grid_size = 20
            x = round(x / grid_size) * grid_size
            y = round(y / grid_size) * grid_size
        return x, y
        
    def add_component(self, component_type: str):
        """部品を追加"""
        x, y = 50, 50
        x, y = self.snap_to_grid(x, y)
        
        # デフォルトサイズ
        default_sizes = {
            "button": (100, 30),
            "label": (100, 20),
            "entry": (150, 25),
            "text": (200, 100),
            "frame": (200, 150),
            "canvas": (200, 150),
            "listbox": (150, 100),
            "combobox": (150, 25),
            "checkbutton": (100, 20),
            "radiobutton": (100, 20),
            "scale": (150, 25),
            "spinbox": (100, 25)
        }
        
        width, height = default_sizes.get(component_type, (100, 30))
        
        component = GUIComponent(component_type, x, y, width, height)
        self.components.append(component)
        
        # キャンバスに描画
        self.draw_component(component)
        
        # 選択
        self.select_component(component)
        
    def draw_component(self, component: GUIComponent):
        """部品をキャンバスに描画"""
        # 既存の描画を削除
        self.canvas.delete(component.id)
        
        # 背景と枠
        bg_color = component.properties.get("bg", "#F0F0F0")
        self.canvas.create_rectangle(
            component.x, component.y,
            component.x + component.width, component.y + component.height,
            fill=bg_color, outline="black", width=1,
            tags=(component.id, "component")
        )
        
        # テキスト
        text = component.properties.get("text", "")
        if text:
            self.canvas.create_text(
                component.x + component.width // 2,
                component.y + component.height // 2,
                text=text, font=("Arial", 9),
                tags=(component.id, "component")
            )
        
        # 選択ハンドル
        if component == self.selected_component:
            self.draw_selection_handles(component)
            
    def draw_selection_handles(self, component: GUIComponent):
        """選択ハンドルを描画"""
        handle_size = 8
        
        # 四隅と辺の中央
        handles = [
            (component.x, component.y, "nw"),  # 左上
            (component.x + component.width // 2, component.y, "n"),  # 上中央
            (component.x + component.width, component.y, "ne"),  # 右上
            (component.x + component.width, component.y + component.height // 2, "e"),  # 右中央
            (component.x + component.width, component.y + component.height, "se"),  # 右下
            (component.x + component.width // 2, component.y + component.height, "s"),  # 下中央
            (component.x, component.y + component.height, "sw"),  # 左下
            (component.x, component.y + component.height // 2, "w"),  # 左中央
        ]
        
        for x, y, position in handles:
            self.canvas.create_rectangle(
                x - handle_size // 2, y - handle_size // 2,
                x + handle_size // 2, y + handle_size // 2,
                fill="blue", outline="darkblue",
                tags=(f"handle_{position}", "handle")
            )
            
    def select_component(self, component: GUIComponent):
        """部品を選択"""
        self.selected_component = component
        self.update_property_editor()
        self.update_code()
        
        # 再描画
        self.redraw_canvas()
        
    def update_property_editor(self):
        """プロパティエディタを更新"""
        # 既存のウィジェットを削除
        for widget in self.property_editor.winfo_children():
            widget.destroy()
            
        self.property_vars.clear()
        
        if not self.selected_component:
            tk.Label(self.property_editor, text="部品が選択されていません").pack(pady=10)
            return
            
        component = self.selected_component
        
        # 基本情報
        tk.Label(self.property_editor, text=f"種類: {component.type}", font=("Arial", 10, "bold")).pack(pady=5)
        
        # 位置とサイズ
        tk.Label(self.property_editor, text="位置とサイズ", font=("Arial", 9, "bold")).pack(pady=(10, 5))
        
        props = [
            ("X", "x", component.x),
            ("Y", "y", component.y),
            ("幅", "width", component.width),
            ("高さ", "height", component.height)
        ]
        
        for label, key, value in props:
            frame = ttk.Frame(self.property_editor)
            frame.pack(fill=tk.X, padx=5, pady=2)
            
            tk.Label(frame, text=label, width=10).pack(side=tk.LEFT)
            var = tk.StringVar(value=str(value))
            self.property_vars[key] = var
            
            entry = ttk.Entry(frame, textvariable=var, width=10)
            entry.pack(side=tk.LEFT, padx=5)
            entry.bind("<Return>", lambda e, k=key: self.update_component_property(k))
            
        # 部品固有プロパティ
        tk.Label(self.property_editor, text="プロパティ", font=("Arial", 9, "bold")).pack(pady=(10, 5))
        
        for key, value in component.properties.items():
            frame = ttk.Frame(self.property_editor)
            frame.pack(fill=tk.X, padx=5, pady=2)
            
            tk.Label(frame, text=key, width=15).pack(side=tk.LEFT)
            
            if isinstance(value, bool):
                var = tk.BooleanVar(value=value)
                self.property_vars[key] = var
                ttk.Checkbutton(frame, variable=var, 
                              command=lambda k=key: self.update_component_property(k)).pack(side=tk.LEFT)
            elif isinstance(value, (int, float)):
                var = tk.StringVar(value=str(value))
                self.property_vars[key] = var
                ttk.Entry(frame, textvariable=var, width=10,
                         command=lambda k=key: self.update_component_property(k)).pack(side=tk.LEFT, padx=5)
            else:
                var = tk.StringVar(value=str(value))
                self.property_vars[key] = var
                ttk.Entry(frame, textvariable=var, width=15,
                         command=lambda k=key: self.update_component_property(k)).pack(side=tk.LEFT, padx=5)
                
    def update_component_property(self, property_name: str):
        """部品プロパティを更新"""
        if not self.selected_component:
            return
            
        var = self.property_vars.get(property_name)
        if not var:
            return
            
        value = var.get()
        
        # 型変換
        if property_name in ["x", "y", "width", "height"]:
            try:
                value = int(value)
            except ValueError:
                return
        elif property_name == "from_":
            try:
                value = float(value)
            except ValueError:
                return
        elif property_name == "to":
            try:
                value = int(value)
            except ValueError:
                return
                
        # プロパティを更新
        if property_name in ["x", "y", "width", "height"]:
            setattr(self.selected_component, property_name, value)
        else:
            self.selected_component.properties[property_name] = value
            
        # 再描画
        self.draw_component(self.selected_component)
        self.update_code()
        
    def on_canvas_click(self, event):
        """キャンバスクリック処理"""
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        
        # ハンドルチェック
        handle = self.get_handle_at(x, y)
        if handle:
            self.resizing = True
            self.resize_handle = handle
            self.drag_start_x = x
            self.drag_start_y = y
            return
            
        # 部品チェック
        component = self.get_component_at(x, y)
        if component:
            self.select_component(component)
            self.dragging = True
            self.drag_start_x = x
            self.drag_start_y = y
            self.component_start_x = component.x
            self.component_start_y = component.y
        else:
            self.selected_component = None
            self.update_property_editor()
            self.redraw_canvas()
            
    def on_canvas_drag(self, event):
        """キャンバスドラッグ処理"""
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        
        if self.resizing and self.selected_component:
            self.handle_resize(x, y)
        elif self.dragging and self.selected_component:
            dx = x - self.drag_start_x
            dy = y - self.drag_start_y
            
            new_x = self.component_start_x + dx
            new_y = self.component_start_y + dy
            
            new_x, new_y = self.snap_to_grid(new_x, new_y)
            
            self.selected_component.x = new_x
            self.selected_component.y = new_y
            
            self.draw_component(self.selected_component)
            
    def on_canvas_release(self, event):
        """キャンバスリリース処理"""
        self.dragging = False
        self.resizing = False
        self.resize_handle = None
        
        if self.selected_component:
            self.update_code()
            
    def on_canvas_right_click(self, event):
        """右クリック処理"""
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        component = self.get_component_at(x, y)
        
        if component:
            # コンテキストメニュー
            menu = tk.Menu(self.root, tearoff=0)
            menu.add_command(label="削除", command=lambda: self.delete_component(component))
            menu.add_command(label="前面に移動", command=lambda: self.bring_to_front(component))
            menu.add_command(label="背面に移動", command=lambda: self.send_to_back(component))
            menu.add_separator()
            menu.add_command(label="プロパティコピー", command=lambda: self.copy_properties(component))
            menu.add_command(label="プロパティ貼り付け", command=lambda: self.paste_properties(component))
            
            menu.post(event.x_root, event.y_root)
            
    def get_component_at(self, x: int, y: int) -> Optional[GUIComponent]:
        """指定位置の部品を取得"""
        for component in reversed(self.components):  # 手前からチェック
            if (component.x <= x <= component.x + component.width and
                component.y <= y <= component.y + component.height):
                return component
        return None
        
    def get_handle_at(self, x: int, y: int) -> Optional[str]:
        """指定位置のハンドルを取得"""
        if not self.selected_component:
            return None
            
        component = self.selected_component
        handle_size = 8
        
        handles = {
            "nw": (component.x, component.y),
            "n": (component.x + component.width // 2, component.y),
            "ne": (component.x + component.width, component.y),
            "e": (component.x + component.width, component.y + component.height // 2),
            "se": (component.x + component.width, component.y + component.height),
            "s": (component.x + component.width // 2, component.y + component.height),
            "sw": (component.x, component.y + component.height),
            "w": (component.x, component.y + component.height // 2),
        }
        
        for position, (hx, hy) in handles.items():
            if (hx - handle_size // 2 <= x <= hx + handle_size // 2 and
                hy - handle_size // 2 <= y <= hy + handle_size // 2):
                return position
                
        return None
        
    def handle_resize(self, x: int, y: int):
        """リサイズ処理"""
        if not self.selected_component or not self.resize_handle:
            return
            
        component = self.selected_component
        dx = x - self.drag_start_x
        dy = y - self.drag_start_y
        
        # ハンドルに応じてサイズ変更
        if self.resize_handle == "se":
            component.width = max(20, component.width + dx)
            component.height = max(20, component.height + dy)
        elif self.resize_handle == "e":
            component.width = max(20, component.width + dx)
        elif self.resize_handle == "s":
            component.height = max(20, component.height + dy)
        # 他のハンドルも同様に実装可能
        
        # スナップ
        if self.snap_enabled:
            component.width = round(component.width / 20) * 20
            component.height = round(component.height / 20) * 20
            
        self.draw_component(component)
        
    def delete_component(self, component: GUIComponent):
        """部品を削除"""
        if component in self.components:
            self.components.remove(component)
            self.canvas.delete(component.id)
            
            if component == self.selected_component:
                self.selected_component = None
                self.update_property_editor()
                
            self.update_code()
            
    def delete_selected(self):
        """選択部品を削除"""
        if self.selected_component:
            self.delete_component(self.selected_component)
            
    def bring_to_front(self, component: GUIComponent):
        """部品を前面に移動"""
        if component in self.components:
            self.components.remove(component)
            self.components.append(component)
            self.redraw_canvas()
            
    def send_to_back(self, component: GUIComponent):
        """部品を背面に移動"""
        if component in self.components:
            self.components.remove(component)
            self.components.insert(0, component)
            self.redraw_canvas()
            
    def copy_properties(self, component: GUIComponent):
        """プロパティをコピー"""
        self.copied_properties = copy.deepcopy(component.properties)
        
    def paste_properties(self, component: GUIComponent):
        """プロパティを貼り付け"""
        if hasattr(self, 'copied_properties'):
            component.properties = copy.deepcopy(self.copied_properties)
            self.update_property_editor()
            self.draw_component(component)
            self.update_code()
            
    def redraw_canvas(self):
        """キャンバスを再描画"""
        self.canvas.delete("component")
        self.canvas.delete("handle")
        
        for component in self.components:
            self.draw_component(component)
            
    def clear_design(self):
        """デザインをクリア"""
        if messagebox.askyesno("確認", "デザインをクリアしますか？"):
            self.components.clear()
            self.selected_component = None
            self.canvas.delete("component")
            self.canvas.delete("handle")
            self.update_property_editor()
            self.update_code()
            
    def save_design(self):
        """デザインを保存"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSONファイル", "*.json"), ("すべてのファイル", "*.*")]
        )
        
        if filename:
            design_data = {
                "components": [comp.to_dict() for comp in self.components],
                "canvas_size": {"width": 800, "height": 600}
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(design_data, f, ensure_ascii=False, indent=2)
                
            messagebox.showinfo("保存完了", f"デザインを保存しました: {filename}")
            
    def load_design(self):
        """デザインを読込"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSONファイル", "*.json"), ("すべてのファイル", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    design_data = json.load(f)
                    
                self.components.clear()
                self.selected_component = None
                
                for comp_data in design_data.get("components", []):
                    component = GUIComponent.from_dict(comp_data)
                    self.components.append(component)
                    
                self.redraw_canvas()
                self.update_code()
                
                messagebox.showinfo("読込完了", f"デザインを読み込みました: {filename}")
                
            except Exception as e:
                messagebox.showerror("エラー", f"読込エラー: {e}")
                
    def update_code(self):
        """コードを更新"""
        code = self.generate_code()
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(1.0, code)
        
    def generate_code(self) -> str:
        """Pythonコードを生成"""
        if not self.components:
            return "# 部品がありません"
            
        code_lines = [
            "# なでしこ GUIデザイナーで生成されたコード",
            "import tkinter as tk",
            "from tkinter import ttk",
            "",
            "class GeneratedGUI:",
            "    def __init__(self):",
            "        self.root = tk.Tk()",
            "        self.root.title('生成されたGUI')",
            "        self.root.geometry('800x600')",
            "",
            "        # 部品を作成",
            ""
        ]
        
        for component in self.components:
            # 部品作成コード
            if component.type == "button":
                code_lines.append(f"        self.{component.id} = tk.Button(")
                code_lines.append(f"            self.root,")
                code_lines.append(f"            text='{component.properties.get('text', 'ボタン')}',")
                code_lines.append(f"            bg='{component.properties.get('bg', '#4ECDC4')}',")
                code_lines.append(f"            fg='{component.properties.get('fg', 'white')}',")
                command = component.properties.get('command', 'on_button_click')
                code_lines.append(f"            command=self.{command}")
                code_lines.append(f"        )")
                
            elif component.type == "label":
                code_lines.append(f"        self.{component.id} = tk.Label(")
                code_lines.append(f"            self.root,")
                code_lines.append(f"            text='{component.properties.get('text', 'ラベル')}',")
                code_lines.append(f"            bg='{component.properties.get('bg', '#F0F0F0')}',")
                code_lines.append(f"            fg='{component.properties.get('fg', 'black')}'")
                code_lines.append(f"        )")
                
            elif component.type == "entry":
                code_lines.append(f"        self.{component.id} = tk.Entry(")
                code_lines.append(f"            self.root,")
                code_lines.append(f"            bg='{component.properties.get('bg', 'white')}',")
                code_lines.append(f"            fg='{component.properties.get('fg', 'black')}'")
                code_lines.append(f"        )")
                
            # 配置コード
            code_lines.append(f"        self.{component.id}.place(")
            code_lines.append(f"            x={component.x},")
            code_lines.append(f"            y={component.y},")
            code_lines.append(f"            width={component.width},")
            code_lines.append(f"            height={component.height}")
            code_lines.append(f"        )")
            code_lines.append("")
            
        # イベントハンドラ
        code_lines.extend([
            "    def on_button_click(self):",
            "        print('ボタンがクリックされました')",
            "",
            "    def run(self):",
            "        self.root.mainloop()",
            "",
            "if __name__ == '__main__':",
            "    app = GeneratedGUI()",
            "    app.run()"
        ])
        
        return "\n".join(code_lines)
        
    def copy_code(self):
        """コードをクリップボードにコピー"""
        code = self.code_text.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("コピー完了", "コードをクリップボードにコピーしました")
        
    def run_code(self):
        """生成されたコードを実行"""
        code = self.code_text.get(1.0, tk.END)
        
        try:
            # 一時ファイルに保存して実行
            import tempfile
            import subprocess
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name
                
            # 別プロセスで実行
            subprocess.Popen(['python', temp_file])
            
            messagebox.showinfo("実行", "GUIを起動しました")
            
        except Exception as e:
            messagebox.showerror("エラー", f"実行エラー: {e}")
            
    def run(self):
        """デザイナーを実行"""
        self.root.mainloop()

def main():
    """メイン関数"""
    designer = GUIDesigner()
    designer.run()

if __name__ == "__main__":
    main()
