"""
マクロシステムモジュール
簡単なマクロ作成と実行機能
"""

import json
import time
import threading
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import pickle

@dataclass
class MacroStep:
    """マクロのステップ"""
    action: str  # アクション種別
    parameters: Dict[str, Any]  # パラメータ
    description: str = ""  # 説明
    delay: float = 0.0  # 実行遅延（秒）

@dataclass
class Macro:
    """マクロクラス"""
    name: str
    description: str
    steps: List[MacroStep]
    created_at: datetime
    updated_at: datetime
    category: str = "一般"  # カテゴリ
    tags: List[str] = None  # タグ
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.fromisoformat(self.updated_at)

class MacroSystem:
    """マクロシステムクラス"""
    
    def __init__(self):
        self.macros: Dict[str, Macro] = {}
        self.recording = False
        self.current_recording: List[MacroStep] = []
        self.recording_name = ""
        self.playing = False
        self.macro_handlers = {}
        self._init_default_handlers()
    
    def _init_default_handlers(self):
        """デフォルトのハンドラを初期化"""
        self.macro_handlers = {
            'text_input': self._handle_text_input,
            'mouse_click': self._handle_mouse_click,
            'key_press': self._handle_key_press,
            'wait': self._handle_wait,
            'message': self._handle_message,
            'file_operation': self._handle_file_operation,
            'system_command': self._handle_system_command,
            'variable_set': self._handle_variable_set,
            'variable_get': self._handle_variable_get,
            'condition': self._handle_condition,
            'loop': self._handle_loop
        }
    
    def register_handler(self, action: str, handler: Callable):
        """カスタムハンドラを登録"""
        self.macro_handlers[action] = handler
    
    def start_recording(self, name: str, description: str = ""):
        """マクロ記録を開始"""
        if self.recording:
            raise ValueError("既に記録中です")
        
        self.recording = True
        self.current_recording = []
        self.recording_name = name
        print(f"🔴 マクロ記録開始: {name}")
    
    def stop_recording(self, description: str = "", category: str = "一般", tags: List[str] = None):
        """マクロ記録を停止"""
        if not self.recording:
            raise ValueError("記録中ではありません")
        
        self.recording = False
        
        if self.current_recording:
            macro = Macro(
                name=self.recording_name,
                description=description,
                steps=self.current_recording.copy(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                category=category,
                tags=tags or []
            )
            
            self.macros[self.recording_name] = macro
            print(f"⏹️ マクロ記録停止: {name} ({len(self.current_recording)}ステップ)")
        
        self.current_recording = []
        self.recording_name = ""
    
    def add_step(self, action: str, parameters: Dict[str, Any], description: str = "", delay: float = 0.0):
        """記録中にステップを追加"""
        if self.recording:
            step = MacroStep(
                action=action,
                parameters=parameters,
                description=description,
                delay=delay
            )
            self.current_recording.append(step)
            print(f"📝 ステップ追加: {action} - {description}")
    
    def play_macro(self, name: str, speed: float = 1.0) -> bool:
        """マクロを再生"""
        if self.playing:
            print("⚠️ 既に再生中です")
            return False
        
        if name not in self.macros:
            print(f"❌ マクロが見つかりません: {name}")
            return False
        
        self.playing = True
        macro = self.macros[name]
        
        def play():
            try:
                print(f"▶️ マクロ再生開始: {name}")
                
                for i, step in enumerate(macro.steps):
                    if not self.playing:  # 停止チェック
                        break
                    
                    print(f"🔄 ステップ {i+1}/{len(macro.steps)}: {step.description}")
                    
                    # ハンドラを実行
                    if step.action in self.macro_handlers:
                        try:
                            self.macro_handlers[step.action](step.parameters)
                        except Exception as e:
                            print(f"❌ ステップ実行エラー: {e}")
                    else:
                        print(f"⚠️ 未定義のアクション: {step.action}")
                    
                    # 遅延
                    if step.delay > 0:
                        time.sleep(step.delay / speed)
                
                print(f"✅ マクロ再生完了: {name}")
                
            except Exception as e:
                print(f"❌ マクロ再生エラー: {e}")
            finally:
                self.playing = False
        
        # 別スレッドで実行
        thread = threading.Thread(target=play)
        thread.daemon = True
        thread.start()
        
        return True
    
    def stop_playing(self):
        """マクロ再生を停止"""
        self.playing = False
        print("⏹️ マクロ再生を停止")
    
    def create_macro(self, name: str, description: str, steps: List[Dict], category: str = "一般", tags: List[str] = None):
        """マクロを手動で作成"""
        macro_steps = []
        for step_data in steps:
            step = MacroStep(
                action=step_data['action'],
                parameters=step_data['parameters'],
                description=step_data.get('description', ''),
                delay=step_data.get('delay', 0.0)
            )
            macro_steps.append(step)
        
        macro = Macro(
            name=name,
            description=description,
            steps=macro_steps,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            category=category,
            tags=tags or []
        )
        
        self.macros[name] = macro
        print(f"✅ マクロ作成完了: {name}")
    
    def delete_macro(self, name: str) -> bool:
        """マクロを削除"""
        if name in self.macros:
            del self.macros[name]
            print(f"🗑️ マクロ削除: {name}")
            return True
        return False
    
    def list_macros(self, category: str = None) -> List[Macro]:
        """マクロ一覧を取得"""
        macros = list(self.macros.values())
        
        if category:
            macros = [m for m in macros if m.category == category]
        
        return sorted(macros, key=lambda x: x.updated_at, reverse=True)
    
    def get_macro(self, name: str) -> Optional[Macro]:
        """マクロを取得"""
        return self.macros.get(name)
    
    def save_macros(self, filepath: str):
        """マクロをファイルに保存"""
        macro_data = {}
        for name, macro in self.macros.items():
            macro_data[name] = asdict(macro)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(macro_data, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"💾 マクロ保存完了: {len(self.macros)}件")
    
    def load_macros(self, filepath: str):
        """マクロをファイルから読み込み"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                macro_data = json.load(f)
            
            for name, data in macro_data.items():
                macro = Macro(**data)
                self.macros[name] = macro
            
            print(f"📂 マクロ読み込み完了: {len(self.macros)}件")
            
        except FileNotFoundError:
            print(f"⚠️ ファイルが見つかりません: {filepath}")
        except Exception as e:
            print(f"❌ 読み込みエラー: {e}")
    
    def get_categories(self) -> List[str]:
        """カテゴリ一覧を取得"""
        categories = set()
        for macro in self.macros.values():
            categories.add(macro.category)
        return sorted(list(categories))
    
    def search_macros(self, keyword: str) -> List[Macro]:
        """マクロを検索"""
        keyword_lower = keyword.lower()
        results = []
        
        for macro in self.macros.values():
            if (keyword_lower in macro.name.lower() or 
                keyword_lower in macro.description.lower() or
                any(keyword_lower in tag.lower() for tag in macro.tags)):
                results.append(macro)
        
        return results
    
    # デフォルトハンドラ
    def _handle_text_input(self, params: Dict[str, Any]):
        """テキスト入力ハンドラ"""
        text = params.get('text', '')
        target = params.get('target', '')
        print(f"⌨️ テキスト入力: {text} → {target}")
    
    def _handle_mouse_click(self, params: Dict[str, Any]):
        """マウスクリックハンドラ"""
        x = params.get('x', 0)
        y = params.get('y', 0)
        button = params.get('button', 'left')
        print(f"🖱️ マウスクリック: ({x}, {y}) - {button}")
    
    def _handle_key_press(self, params: Dict[str, Any]):
        """キー押下ハンドラ"""
        key = params.get('key', '')
        modifiers = params.get('modifiers', [])
        print(f"⌨️ キー押下: {key} + {modifiers}")
    
    def _handle_wait(self, params: Dict[str, Any]):
        """待機ハンドラ"""
        seconds = params.get('seconds', 1.0)
        print(f"⏱️ 待機: {seconds}秒")
        time.sleep(seconds)
    
    def _handle_message(self, params: Dict[str, Any]):
        """メッセージ表示ハンドラ"""
        message = params.get('message', '')
        level = params.get('level', 'info')
        print(f"💬 メッセージ: {message} ({level})")
    
    def _handle_file_operation(self, params: Dict[str, Any]):
        """ファイル操作ハンドラ"""
        operation = params.get('operation', '')
        filepath = params.get('filepath', '')
        content = params.get('content', '')
        print(f"📁 ファイル操作: {operation} - {filepath}")
    
    def _handle_system_command(self, params: Dict[str, Any]):
        """システムコマンドハンドラ"""
        command = params.get('command', '')
        print(f"🔧 システムコマンド: {command}")
    
    def _handle_variable_set(self, params: Dict[str, Any]):
        """変数設定ハンドラ"""
        name = params.get('name', '')
        value = params.get('value', '')
        print(f"📝 変数設定: {name} = {value}")
    
    def _handle_variable_get(self, params: Dict[str, Any]):
        """変数取得ハンドラ"""
        name = params.get('name', '')
        print(f"📖 変数取得: {name}")
    
    def _handle_condition(self, params: Dict[str, Any]):
        """条件分岐ハンドラ"""
        condition = params.get('condition', '')
        true_steps = params.get('true_steps', [])
        false_steps = params.get('false_steps', [])
        print(f"🔀 条件分岐: {condition}")
    
    def _handle_loop(self, params: Dict[str, Any]):
        """ループハンドラ"""
        loop_type = params.get('type', 'for')
        count = params.get('count', 0)
        steps = params.get('steps', [])
        print(f"🔄 ループ: {loop_type} × {count}")

# グローバルインスタンス
macro_system = MacroSystem()

# 便利な関数
def start_macro_recording(name: str, description: str = ""):
    """マクロ記録を開始"""
    macro_system.start_recording(name, description)

def stop_macro_recording(description: str = "", category: str = "一般", tags: List[str] = None):
    """マクロ記録を停止"""
    macro_system.stop_recording(description, category, tags)

def play_macro(name: str, speed: float = 1.0) -> bool:
    """マクロを再生"""
    return macro_system.play_macro(name, speed)

def create_simple_macro(name: str, description: str, steps: List[Dict]) -> None:
    """簡単なマクロを作成"""
    macro_system.create_macro(name, description, steps)

def list_macros() -> List[Macro]:
    """マクロ一覧を取得"""
    return macro_system.list_macros()

def save_macros(filepath: str = "macros.json"):
    """マクロを保存"""
    macro_system.save_macros(filepath)

def load_macros(filepath: str = "macros.json"):
    """マクロを読み込み"""
    macro_system.load_macros(filepath)
