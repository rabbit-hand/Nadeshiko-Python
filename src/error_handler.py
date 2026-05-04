"""
エラーハンドリングモジュール
詳細なエラーメッセージとデバッグ情報を提供
"""

import sys
import traceback
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class NadesikoErrorHandler:
    """なでしこ3パイソン用エラーハンドラー"""
    
    def __init__(self):
        self.error_log = []
        self.error_patterns = self._init_error_patterns()
        self.debug_mode = False
    
    def _init_error_patterns(self) -> Dict[str, str]:
        """エラーパターンの初期化"""
        return {
            # Pythonのエラーをなでしこ用に変換
            'NameError': '変名「{var}」が見つかりません。変数が定義されているか確認してください。',
            'TypeError': '型エラー: {msg}。データ型を確認してください。',
            'ValueError': '値エラー: {msg}。値が正しい形式か確認してください。',
            'IndexError': 'インデックスエラー: {msg}。配列の範囲を確認してください。',
            'KeyError': 'キーエラー: {msg}。辞書のキーを確認してください。',
            'AttributeError': '属性エラー: {msg}。オブジェクトの属性を確認してください。',
            'ImportError': 'インポートエラー: {msg}。モジュールが正しくインストールされているか確認してください。',
            'FileNotFoundError': 'ファイルエラー: {msg}。ファイルパスを確認してください。',
            'PermissionError': '権限エラー: {msg}。ファイルのアクセス権を確認してください。',
            'ZeroDivisionError': 'ゼロ除算エラー: 0で割ろうとしました。割る数が0でないか確認してください。',
            'SyntaxError': '構文エラー: {msg}。文法を確認してください。',
            'IndentationError': 'インデントエラー: {msg}。インデントを確認してください。',
            'UnicodeDecodeError': '文字コードエラー: {msg}。ファイルの文字コードを確認してください。',
            'MemoryError': 'メモリエラー: {msg}。メモリ使用量を確認してください。',
            'OverflowError': 'オーバーフローエラー: {msg}。数値が大きすぎます。'
        }
    
    def set_debug_mode(self, enabled: bool):
        """デバッグモードを設定"""
        self.debug_mode = enabled
    
    def handle_error(self, error: Exception, code: str = "", line_number: int = None) -> Dict:
        """エラーを処理して詳細情報を返す"""
        
        error_type = type(error).__name__
        error_msg = str(error)
        
        # エラー情報を収集
        error_info = {
            'timestamp': datetime.now().isoformat(),
            'error_type': error_type,
            'error_message': error_msg,
            'user_message': self._create_user_message(error_type, error_msg),
            'line_number': line_number,
            'code_snippet': self._get_code_snippet(code, line_number),
            'suggestions': self._get_suggestions(error_type, error_msg),
            'traceback': traceback.format_exc() if self.debug_mode else None,
            'debug_info': self._get_debug_info(error) if self.debug_mode else None
        }
        
        # エラーログに追加
        self.error_log.append(error_info)
        
        return error_info
    
    def _create_user_message(self, error_type: str, error_msg: str) -> str:
        """ユーザー向けのエラーメッセージを作成"""
        pattern = self.error_patterns.get(error_type)
        
        if pattern:
            # 変数名を抽出
            var_match = re.search(r"'([^']+)'", error_msg)
            if var_match:
                var = var_match.group(1)
                return pattern.format(var=var, msg=error_msg)
            else:
                return pattern.format(var="", msg=error_msg)
        
        # デフォルトメッセージ
        return f"エラーが発生しました: {error_type} - {error_msg}"
    
    def _get_code_snippet(self, code: str, line_number: int = None) -> Dict:
        """エラー箇所のコードスニペットを取得"""
        if not code or line_number is None:
            return {'before': '', 'current': '', 'after': ''}
        
        lines = code.split('\n')
        snippet = {
            'before': '',
            'current': '',
            'after': ''
        }
        
        # エラー行の前後を取得
        start = max(0, line_number - 2)
        end = min(len(lines), line_number + 2)
        
        for i in range(start, end):
            line = lines[i]
            line_num = i + 1
            
            if line_num == line_number:
                snippet['current'] = f"→ {line_num}: {line}"
            elif line_num < line_number:
                snippet['before'] += f"  {line_num}: {line}\n"
            else:
                snippet['after'] += f"  {line_num}: {line}\n"
        
        return snippet
    
    def _get_suggestions(self, error_type: str, error_msg: str) -> List[str]:
        """エラー解決のための提案を取得"""
        suggestions = []
        
        if error_type == 'NameError':
            suggestions = [
                '変数名のスペルを確認してください',
                '変数が正しく定義されているか確認してください',
                '変数名に日本語を使用している場合は正しく入力されているか確認してください'
            ]
        elif error_type == 'TypeError':
            suggestions = [
                'データ型を確認してください',
                '文字列と数値の演算をしていないか確認してください',
                '関数の引数の型を確認してください'
            ]
        elif error_type == 'ValueError':
            suggestions = [
                '入力値の形式を確認してください',
                '数値を期待している箇所に文字列を渡していないか確認してください',
                '範囲外の値を指定していないか確認してください'
            ]
        elif error_type == 'IndexError':
            suggestions = [
                '配列のインデックスが範囲内か確認してください',
                '0から始まるインデックスを確認してください',
                '配列の長さを確認してください'
            ]
        elif error_type == 'FileNotFoundError':
            suggestions = [
                'ファイルパスを確認してください',
                'ファイルが存在するか確認してください',
                '相対パスと絶対パスを確認してください'
            ]
        elif error_type == 'SyntaxError':
            suggestions = [
                '文法を確認してください',
                '括弧の対応を確認してください',
                '引用符の対応を確認してください',
                'インデントを確認してください'
            ]
        else:
            suggestions = [
                'エラーメッセージをよく読んでください',
                'コードの該当箇所を確認してください',
                'デバッグモードを有効にして詳細情報を確認してください'
            ]
        
        return suggestions
    
    def _get_debug_info(self, error: Exception) -> Dict:
        """デバッグ情報を取得"""
        return {
            'exception_type': type(error).__name__,
            'exception_args': error.args,
            'filename': traceback.extract_tb(error.__traceback__)[-1].filename if error.__traceback__ else None,
            'lineno': traceback.extract_tb(error.__traceback__)[-1].lineno if error.__traceback__ else None,
            'function': traceback.extract_tb(error.__traceback__)[-1].name if error.__traceback__ else None
        }
    
    def format_error_report(self, error_info: Dict) -> str:
        """エラー報告書をフォーマット"""
        report = []
        
        report.append(f"🔴 エラーが発生しました")
        report.append(f"📅 時刻: {error_info['timestamp']}")
        report.append(f"🔤 種類: {error_info['error_type']}")
        report.append(f"💬 メッセージ: {error_info['user_message']}")
        
        if error_info['line_number']:
            report.append(f"📍 行番号: {error_info['line_number']}")
        
        if error_info['code_snippet']['current']:
            report.append(f"📝 コード:")
            if error_info['code_snippet']['before']:
                report.append(error_info['code_snippet']['before'].rstrip())
            report.append(error_info['code_snippet']['current'])
            if error_info['code_snippet']['after']:
                report.append(error_info['code_snippet']['after'].rstrip())
        
        if error_info['suggestions']:
            report.append(f"💡 解決策:")
            for suggestion in error_info['suggestions']:
                report.append(f"  • {suggestion}")
        
        if self.debug_mode and error_info['debug_info']:
            report.append(f"🔍 デバッグ情報:")
            debug = error_info['debug_info']
            if debug['filename']:
                report.append(f"  ファイル: {debug['filename']}")
            if debug['lineno']:
                report.append(f"  行番号: {debug['lineno']}")
            if debug['function']:
                report.append(f"  関数: {debug['function']}")
        
        return '\n'.join(report)
    
    def get_error_summary(self) -> Dict:
        """エラーのサマリーを取得"""
        if not self.error_log:
            return {'total_errors': 0, 'error_types': {}, 'recent_errors': []}
        
        error_types = {}
        for error in self.error_log:
            error_type = error['error_type']
            error_types[error_type] = error_types.get(error_type, 0) + 1
        
        return {
            'total_errors': len(self.error_log),
            'error_types': error_types,
            'recent_errors': self.error_log[-5:]  # 最近の5件
        }
    
    def clear_error_log(self):
        """エラーログをクリア"""
        self.error_log.clear()

# グローバルインスタンス
error_handler = NadesikoErrorHandler()
