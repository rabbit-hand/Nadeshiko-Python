"""
なでしこ3互換ファイル操作ライブラリ
"""

import os
import json
import csv
import pickle
import shutil
from pathlib import Path

class NadesikoFile:
    """なでしこ3のファイル操作機能を実装"""
    
    def __init__(self):
        self._result = None
    
    # === 基本ファイル操作 ===
    def 読む(self, filepath, encoding="utf-8"):
        """ファイルを読み込む"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                self._result = f.read()
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 書く(self, filepath, content, encoding="utf-8"):
        """ファイルに書き込む"""
        try:
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(str(content))
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 追記(self, filepath, content, encoding="utf-8"):
        """ファイルに追記する"""
        try:
            with open(filepath, 'a', encoding=encoding) as f:
                f.write(str(content))
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 存在する(self, filepath):
        """ファイルが存在するか"""
        self._result = os.path.exists(filepath)
        return self._result
    
    def ファイル作成(self, filepath):
        """空のファイルを作成"""
        try:
            with open(filepath, 'w') as f:
                pass
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 削除(self, filepath):
        """ファイルを削除"""
        try:
            os.remove(filepath)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def コピー(self, src, dst):
        """ファイルをコピー"""
        try:
            shutil.copy2(src, dst)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 移動(self, src, dst):
        """ファイルを移動"""
        try:
            shutil.move(src, dst)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === ディレクトリ操作 ===
    def ディレクトリ作成(self, dirpath):
        """ディレクトリを作成"""
        try:
            os.makedirs(dirpath, exist_ok=True)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ディレクトリ削除(self, dirpath):
        """ディレクトリを削除"""
        try:
            shutil.rmtree(dirpath)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ディレクトリ存在する(self, dirpath):
        """ディレクトリが存在するか"""
        self._result = os.path.isdir(dirpath)
        return self._result
    
    def 一覧取得(self, dirpath=".", pattern="*"):
        """ディレクトリ内の一覧を取得"""
        try:
            from glob import glob
            files = glob(os.path.join(dirpath, pattern))
            self._result = [os.path.basename(f) for f in files]
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ファイル一覧(self, dirpath="."):
        """ファイル一覧を取得"""
        try:
            files = []
            for item in os.listdir(dirpath):
                full_path = os.path.join(dirpath, item)
                if os.path.isfile(full_path):
                    files.append(item)
            self._result = files
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ディレクトリ一覧(self, dirpath="."):
        """ディレクトリ一覧を取得"""
        try:
            dirs = []
            for item in os.listdir(dirpath):
                full_path = os.path.join(dirpath, item)
                if os.path.isdir(full_path):
                    dirs.append(item)
            self._result = dirs
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === ファイル情報 ===
    def ファイルサイズ(self, filepath):
        """ファイルサイズを取得"""
        try:
            self._result = os.path.getsize(filepath)
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 更新日時(self, filepath):
        """ファイルの更新日時を取得"""
        try:
            timestamp = os.path.getmtime(filepath)
            import datetime
            self._result = datetime.datetime.fromtimestamp(timestamp)
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def 拡張子取得(self, filepath):
        """ファイルの拡張子を取得"""
        self._result = os.path.splitext(filepath)[1]
        return self._result
    
    def ファイル名取得(self, filepath):
        """ファイル名を取得"""
        self._result = os.path.basename(filepath)
        return self._result
    
    def ディレクトリ名取得(self, filepath):
        """ディレクトリ名を取得"""
        self._result = os.path.dirname(filepath)
        return self._result
    
    # === 特殊ファイル形式 ===
    def JSON読む(self, filepath):
        """JSONファイルを読み込む"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self._result = json.load(f)
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def JSON書く(self, filepath, data):
        """JSONファイルに書き込む"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def CSV読む(self, filepath, delimiter=","):
        """CSVファイルを読み込む"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=delimiter)
                self._result = [row for row in reader]
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def CSV書く(self, filepath, data, delimiter=","):
        """CSVファイルに書き込む"""
        try:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, delimiter=delimiter)
                writer.writerows(data)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ピクル読む(self, filepath):
        """Pickleファイルを読み込む"""
        try:
            with open(filepath, 'rb') as f:
                self._result = pickle.load(f)
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    def ピクル書く(self, filepath, data):
        """Pickleファイルに書き込む"""
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(data, f)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === パス操作 ===
    def 絶対パス(self, filepath):
        """絶対パスを取得"""
        self._result = os.path.abspath(filepath)
        return self._result
    
    def 相対パス(self, filepath, base="."):
        """相対パスを取得"""
        self._result = os.path.relpath(filepath, base)
        return self._result
    
    def パス結合(self, *paths):
        """パスを結合"""
        self._result = os.path.join(*paths)
        return self._result
    
    def 正規化(self, filepath):
        """パスを正規化"""
        self._result = os.path.normpath(filepath)
        return self._result
    
    # === カレントディレクトリ ===
    def 現在ディレクトリ(self):
        """現在のディレクトリを取得"""
        self._result = os.getcwd()
        return self._result
    
    def ディレクトリ変更(self, dirpath):
        """ディレクトリを変更"""
        try:
            os.chdir(dirpath)
            self._result = True
            return self._result
        except Exception as e:
            self._result = f"エラー: {e}"
            return self._result
    
    # === その他 ===
    def 一時ファイル作成(self, suffix="", prefix="tmp"):
        """一時ファイルを作成"""
        import tempfile
        fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix)
        os.close(fd)
        self._result = path
        return self._result
    
    def 一時ディレクトリ作成(self, suffix="", prefix="tmp"):
        """一時ディレクトリを作成"""
        import tempfile
        self._result = tempfile.mkdtemp(suffix=suffix, prefix=prefix)
        return self._result
    
    def それ(self):
        """直前の操作結果を返す"""
        return self._result
