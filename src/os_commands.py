"""
OSコマンド実行モジュール
Windows、Mac、Linuxすべてで動作するOSコマンド実行機能
"""

import os
import platform
import subprocess
import shutil
import glob
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class OSCommands:
    """OSコマンド実行クラス"""
    
    def __init__(self):
        self.os_type = self._detect_os()
        self.security_mode = True  # セキュリティモード（デフォルト有効）
        self.allowed_commands = self._get_allowed_commands()
    
    def _detect_os(self) -> str:
        """OSタイプを検出"""
        system = platform.system().lower()
        if system == 'windows':
            return 'windows'
        elif system == 'darwin':
            return 'mac'
        elif system == 'linux':
            return 'linux'
        else:
            return 'unknown'
    
    def _get_allowed_commands(self) -> Dict[str, List[str]]:
        """許可されるコマンドリスト"""
        return {
            'windows': [
                'dir', 'ls', 'cd', 'pwd', 'echo', 'type', 'copy', 'del', 'move',
                'mkdir', 'rmdir', 'tree', 'find', 'grep', 'sort', 'uniq',
                'head', 'tail', 'wc', 'cat', 'less', 'more', 'ping', 'ipconfig',
                'tasklist', 'systeminfo', 'ver', 'whoami', 'date', 'time'
            ],
            'mac': [
                'ls', 'cd', 'pwd', 'echo', 'cat', 'cp', 'mv', 'rm', 'mkdir',
                'rmdir', 'tree', 'find', 'grep', 'sort', 'uniq', 'head', 'tail',
                'wc', 'less', 'more', 'ping', 'ifconfig', 'ps', 'top', 'df',
                'du', 'uname', 'whoami', 'date', 'uptime', 'say'
            ],
            'linux': [
                'ls', 'cd', 'pwd', 'echo', 'cat', 'cp', 'mv', 'rm', 'mkdir',
                'rmdir', 'tree', 'find', 'grep', 'sort', 'uniq', 'head', 'tail',
                'wc', 'less', 'more', 'ping', 'ifconfig', 'ip', 'ps', 'top', 'df',
                'du', 'uname', 'whoami', 'date', 'uptime', 'free', 'lsblk'
            ]
        }
    
    def _is_command_allowed(self, command: str) -> bool:
        """コマンドが許可されているかチェック"""
        if not self.security_mode:
            return True
        
        # コマンドの最初の部分を取得
        cmd_parts = command.strip().split()
        if not cmd_parts:
            return False
        
        base_cmd = cmd_parts[0].lower()
        allowed = self.allowed_commands.get(self.os_type, [])
        
        return base_cmd in allowed
    
    def _normalize_command(self, command: str) -> str:
        """OSごとにコマンドを正規化"""
        if self.os_type == 'windows':
            # Windows用のコマンド変換
            command = command.replace('ls', 'dir')
            command = command.replace('pwd', 'cd')
            command = command.replace('cat', 'type')
        return command
    
    def execute_command(self, command: str, shell: bool = True) -> Tuple[int, str, str]:
        """
        OSコマンドを実行
        
        Args:
            command: 実行するコマンド
            shell: シェル実行フラグ
            
        Returns:
            (終了コード, 標準出力, 標準エラー出力)
        """
        if not self._is_command_allowed(command):
            return 1, "", f"Security: Command '{command}' is not allowed"
        
        try:
            # コマンドを正規化
            normalized_cmd = self._normalize_command(command)
            
            # コマンド実行
            result = subprocess.run(
                normalized_cmd,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=30  # 30秒タイムアウト
            )
            
            return result.returncode, result.stdout, result.stderr
            
        except subprocess.TimeoutExpired:
            return 1, "", "Command execution timeout"
        except Exception as e:
            return 1, "", f"Command execution error: {str(e)}"
    
    def get_current_directory(self) -> str:
        """現在のディレクトリを取得"""
        return os.getcwd()
    
    def list_directory(self, path: str = ".") -> List[str]:
        """ディレクトリ内容を一覧表示"""
        try:
            return os.listdir(path)
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def create_directory(self, path: str) -> bool:
        """ディレクトリを作成"""
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    def remove_directory(self, path: str) -> bool:
        """ディレクトリを削除"""
        try:
            shutil.rmtree(path)
            return True
        except Exception as e:
            print(f"Error removing directory: {e}")
            return False
    
    def copy_file(self, src: str, dst: str) -> bool:
        """ファイルをコピー"""
        try:
            shutil.copy2(src, dst)
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False
    
    def move_file(self, src: str, dst: str) -> bool:
        """ファイルを移動"""
        try:
            shutil.move(src, dst)
            return True
        except Exception as e:
            print(f"Error moving file: {e}")
            return False
    
    def delete_file(self, path: str) -> bool:
        """ファイルを削除"""
        try:
            os.remove(path)
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
    
    def file_exists(self, path: str) -> bool:
        """ファイルが存在するかチェック"""
        return os.path.exists(path)
    
    def get_file_info(self, path: str) -> Dict:
        """ファイル情報を取得"""
        try:
            stat = os.stat(path)
            return {
                'size': stat.st_size,
                'modified': stat.st_mtime,
                'created': stat.st_ctime,
                'is_dir': os.path.isdir(path),
                'is_file': os.path.isfile(path)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def find_files(self, pattern: str, path: str = ".") -> List[str]:
        """ファイルを検索"""
        try:
            search_path = Path(path)
            return [str(p) for p in search_path.rglob(pattern)]
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def get_system_info(self) -> Dict:
        """システム情報を取得"""
        return {
            'os': self.os_type,
            'platform': platform.platform(),
            'architecture': platform.architecture(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'current_directory': self.get_current_directory()
        }
    
    def set_security_mode(self, enabled: bool):
        """セキュリティモードを設定"""
        self.security_mode = enabled
    
    def add_allowed_command(self, command: str):
        """許可コマンドを追加"""
        if self.os_type in self.allowed_commands:
            if command not in self.allowed_commands[self.os_type]:
                self.allowed_commands[self.os_type].append(command)

# グローバルインスタンス
os_commands = OSCommands()
