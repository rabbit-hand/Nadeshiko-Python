"""
UI改善モジュール
ユーザーインターフェースの操作性と視覚的な品質を向上
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass
from enum import Enum

class Theme(Enum):
    """テーマの種類"""
    LIGHT = "light"
    DARK = "dark"
    BLUE = "blue"
    GREEN = "green"

@dataclass
class UIConfig:
    """UI設定"""
    theme: Theme = Theme.LIGHT
    font_family: str = "Helvetica"
    font_size: int = 12
    window_width: int = 800
    window_height: int = 600
    animation_speed: float = 0.3
    show_line_numbers: bool = True
    auto_save: bool = True
    auto_save_interval: int = 300  # 5分

class UIEnhancer:
    """UI改善クラス"""
    
    def __init__(self):
        self.config = UIConfig()
        self.themes = self._init_themes()
        self.animations = {}
        self.notifications = []
        
    def _init_themes(self) -> Dict[Theme, Dict[str, str]]:
        """テーマの初期化"""
        return {
            Theme.LIGHT: {
                'bg': '#FFFFFF',
                'fg': '#000000',
                'select_bg': '#0078D4',
                'select_fg': '#FFFFFF',
                'button_bg': '#F0F0F0',
                'button_fg': '#000000',
                'entry_bg': '#FFFFFF',
                'entry_fg': '#000000',
                'frame_bg': '#F8F8F8',
                'text_bg': '#FFFFFF',
                'text_fg': '#000000'
            },
            Theme.DARK: {
                'bg': '#2D2D30',
                'fg': '#FFFFFF',
                'select_bg': '#0078D4',
                'select_fg': '#FFFFFF',
                'button_bg': '#3C3C3C',
                'button_fg': '#FFFFFF',
                'entry_bg': '#1E1E1E',
                'entry_fg': '#FFFFFF',
                'frame_bg': '#252526',
                'text_bg': '#1E1E1E',
                'text_fg': '#FFFFFF'
            },
            Theme.BLUE: {
                'bg': '#E3F2FD',
                'fg': '#1565C0',
                'select_bg': '#1976D2',
                'select_fg': '#FFFFFF',
                'button_bg': '#BBDEFB',
                'button_fg': '#1565C0',
                'entry_bg': '#FFFFFF',
                'entry_fg': '#1565C0',
                'frame_bg': '#E1F5FE',
                'text_bg': '#FFFFFF',
                'text_fg': '#1565C0'
            },
            Theme.GREEN: {
                'bg': '#E8F5E8',
                'fg': '#2E7D32',
                'select_bg': '#4CAF50',
                'select_fg': '#FFFFFF',
                'button_bg': '#C8E6C9',
                'button_fg': '#2E7D32',
                'entry_bg': '#FFFFFF',
                'entry_fg': '#2E7D32',
                'frame_bg': '#F1F8E9',
                'text_bg': '#FFFFFF',
                'text_fg': '#2E7D32'
            }
        }
    
    def apply_theme(self, widget: tk.Widget, theme: Theme = None):
        """テーマを適用"""
        if theme is None:
            theme = self.config.theme
        
        colors = self.themes[theme]
        
        # ウィジェットタイプに応じてテーマを適用
        if isinstance(widget, tk.Frame):
            widget.configure(bg=colors['frame_bg'])
        elif isinstance(widget, tk.Button):
            widget.configure(bg=colors['button_bg'], fg=colors['button_fg'])
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=colors['entry_bg'], fg=colors['entry_fg'])
        elif isinstance(widget, tk.Text):
            widget.configure(bg=colors['text_bg'], fg=colors['text_fg'])
        elif isinstance(widget, tk.Label):
            widget.configure(bg=colors['bg'], fg=colors['fg'])
        
        # 再帰的に子ウィジェットにも適用
        for child in widget.winfo_children():
            self.apply_theme(child, theme)
    
    def create_styled_button(self, parent: tk.Widget, text: str, command: Callable = None, **kwargs) -> tk.Button:
        """スタイル化されたボタンを作成"""
        colors = self.themes[self.config.theme]
        
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=colors['button_bg'],
            fg=colors['button_fg'],
            font=(self.config.font_family, self.config.font_size),
            relief=tk.RAISED,
            bd=1,
            padx=10,
            pady=5,
            **kwargs
        )
        
        # ホバーエフェクト
        def on_enter(e):
            button.configure(bg=colors['select_bg'], fg=colors['select_fg'])
        
        def on_leave(e):
            button.configure(bg=colors['button_bg'], fg=colors['button_fg'])
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    def create_styled_entry(self, parent: tk.Widget, **kwargs) -> tk.Entry:
        """スタイル化されたエントリーを作成"""
        colors = self.themes[self.config.theme]
        
        entry = tk.Entry(
            parent,
            bg=colors['entry_bg'],
            fg=colors['entry_fg'],
            font=(self.config.font_family, self.config.font_size),
            relief=tk.FLAT,
            bd=1,
            **kwargs
        )
        
        return entry
    
    def create_styled_text(self, parent: tk.Widget, **kwargs) -> tk.Text:
        """スタイル化されたテキストウィジェットを作成"""
        colors = self.themes[self.config.theme]
        
        text = tk.Text(
            parent,
            bg=colors['text_bg'],
            fg=colors['text_fg'],
            font=(self.config.font_family, self.config.font_size),
            relief=tk.FLAT,
            bd=1,
            **kwargs
        )
        
        # 行番号の表示（有効な場合）
        if self.config.show_line_numbers:
            self._add_line_numbers(text)
        
        return text
    
    def _add_line_numbers(self, text_widget: tk.Text):
        """行番号を追加"""
        line_numbers = tk.Text(text_widget.master, width=4, padx=3, takefocus=0)
        line_numbers.configure(bg=self.themes[self.config.theme]['frame_bg'])
        
        def update_line_numbers():
            line_numbers.delete(1.0, tk.END)
            line_numbers.insert(1.0, "\n".join(str(i) for i in range(1, int(text_widget.index('end-1c').split('.')[0]) + 1)))
        
        text_widget.bind("<Key>", lambda e: update_line_numbers())
        text_widget.bind("<Button-1>", lambda e: update_line_numbers())
        text_widget.bind("<MouseWheel>", lambda e: update_line_numbers())
        
        update_line_numbers()
        
        # スクロール同期
        def sync_scrolls(*args):
            text_widget.yview(*args)
            line_numbers.yview(*args)
        
        text_widget.configure(yscrollcommand=sync_scrolls)
    
    def create_progress_bar(self, parent: tk.Widget, **kwargs) -> ttk.Progressbar:
        """プログレスバーを作成"""
        progress = ttk.Progressbar(parent, **kwargs)
        return progress
    
    def create_status_bar(self, parent: tk.Widget) -> tk.Frame:
        """ステータスバーを作成"""
        colors = self.themes[self.config.theme]
        
        status_frame = tk.Frame(parent, bg=colors['frame_bg'], relief=tk.SUNKEN, bd=1)
        
        status_label = tk.Label(
            status_frame,
            text="準備完了",
            bg=colors['frame_bg'],
            fg=colors['fg'],
            font=(self.config.font_family, self.config.font_size - 1)
        )
        
        status_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        return status_frame
    
    def show_notification(self, parent: tk.Widget, message: str, notification_type: str = "info", duration: int = 3000):
        """通知を表示"""
        colors = self.themes[self.config.theme]
        
        # 通知の色を設定
        type_colors = {
            "info": {"bg": "#2196F3", "fg": "#FFFFFF"},
            "success": {"bg": "#4CAF50", "fg": "#FFFFFF"},
            "warning": {"bg": "#FF9800", "fg": "#FFFFFF"},
            "error": {"bg": "#F44336", "fg": "#FFFFFF"}
        }
        
        notif_colors = type_colors.get(notification_type, type_colors["info"])
        
        # 通知ウィンドウを作成
        notification = tk.Toplevel(parent)
        notification.overrideredirect(True)
        notification.configure(bg=notif_colors["bg"])
        
        # 位置を計算（右上）
        x = parent.winfo_x() + parent.winfo_width() - 300
        y = parent.winfo_y() + 50
        notification.geometry(f"300x50+{x}+{y}")
        
        # ラベルを作成
        label = tk.Label(
            notification,
            text=message,
            bg=notif_colors["bg"],
            fg=notif_colors["fg"],
            font=(self.config.font_family, self.config.font_size),
            pady=10
        )
        label.pack(fill=tk.BOTH, expand=True)
        
        # 自動的に閉じる
        notification.after(duration, notification.destroy)
        
        # アニメーション効果
        self._fade_in(notification)
    
    def _fade_in(self, widget: tk.Toplevel):
        """フェードインアニメーション"""
        widget.attributes('-alpha', 0.0)
        
        def fade():
            current = widget.attributes('-alpha')
            if current < 1.0:
                widget.attributes('-alpha', current + 0.1)
                widget.after(50, fade)
        
        fade()
    
    def create_menu_bar(self, parent: tk.Widget, menu_items: Dict[str, List[Dict[str, Any]]]) -> tk.Menu:
        """メニューバーを作成"""
        colors = self.themes[self.config.theme]
        
        menubar = tk.Menu(parent, bg=colors['frame_bg'], fg=colors['fg'])
        
        for menu_name, items in menu_items.items():
            menu = tk.Menu(menubar, tearoff=0, bg=colors['frame_bg'], fg=colors['fg'])
            menubar.add_cascade(label=menu_name, menu=menu)
            
            for item in items:
                if item.get('separator', False):
                    menu.add_separator()
                else:
                    menu.add_command(
                        label=item['label'],
                        command=item.get('command'),
                        accelerator=item.get('accelerator', '')
                    )
        
        return menubar
    
    def create_toolbar(self, parent: tk.Widget, tools: List[Dict[str, Any]]) -> tk.Frame:
        """ツールバーを作成"""
        colors = self.themes[self.config.theme]
        
        toolbar = tk.Frame(parent, bg=colors['frame_bg'], relief=tk.RAISED, bd=1)
        
        for tool in tools:
            if tool.get('separator', False):
                separator = tk.Frame(toolbar, bg=colors['fg'], width=1)
                separator.pack(side=tk.LEFT, fill=tk.Y, padx=2)
            else:
                button = self.create_styled_button(
                    toolbar,
                    text=tool['label'],
                    command=tool.get('command'),
                    width=3
                )
                button.pack(side=tk.LEFT, padx=2, pady=2)
                
                # ツールチップ
                if 'tooltip' in tool:
                    self._create_tooltip(button, tool['tooltip'])
        
        return toolbar
    
    def _create_tooltip(self, widget: tk.Widget, text: str):
        """ツールチップを作成"""
        tooltip = tk.Toplevel(widget)
        tooltip.overrideredirect(True)
        tooltip.withdraw()
        
        label = tk.Label(
            tooltip,
            text=text,
            bg="#FFFFCC",
            fg="#000000",
            relief=tk.SOLID,
            borderwidth=1,
            font=(self.config.font_family, self.config.font_size - 1)
        )
        label.pack()
        
        def on_enter(event):
            tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
            tooltip.deiconify()
        
        def on_leave(event):
            tooltip.withdraw()
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def set_theme(self, theme: Theme):
        """テーマを設定"""
        self.config.theme = theme
    
    def get_config(self) -> UIConfig:
        """設定を取得"""
        return self.config
    
    def update_config(self, **kwargs):
        """設定を更新"""
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)

# グローバルインスタンス
ui_enhancer = UIEnhancer()
