"""
データ構造モジュール
リスト、辞書、セットなどのデータ構造をサポート
"""

from typing import Any, List, Dict, Set, Tuple, Optional, Union
import json
import pickle
from datetime import datetime

class NadesikoList:
    """なでしこ用リストクラス"""
    
    def __init__(self, items: List[Any] = None):
        self.items = items if items is not None else []
    
    def __str__(self):
        return f"[{', '.join(str(item) for item in self.items)}]"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def append(self, item: Any):
        """要素を追加"""
        self.items.append(item)
    
    def insert(self, index: int, item: Any):
        """指定位置に要素を挿入"""
        self.items.insert(index, item)
    
    def remove(self, item: Any):
        """要素を削除"""
        if item in self.items:
            self.items.remove(item)
    
    def pop(self, index: int = -1):
        """要素を取り出して削除"""
        if self.items:
            return self.items.pop(index)
        return None
    
    def clear(self):
        """すべての要素を削除"""
        self.items.clear()
    
    def sort(self, reverse: bool = False):
        """ソート"""
        self.items.sort(reverse=reverse)
    
    def reverse(self):
        """逆順にする"""
        self.items.reverse()
    
    def count(self, item: Any) -> int:
        """要素の数を数える"""
        return self.items.count(item)
    
    def index(self, item: Any) -> int:
        """要素の位置を取得"""
        return self.items.index(item)
    
    def extend(self, other_list):
        """リストを連結"""
        if isinstance(other_list, NadesikoList):
            self.items.extend(other_list.items)
        else:
            self.items.extend(other_list)
    
    def slice(self, start: int, end: int = None):
        """スライスを取得"""
        if end is None:
            return NadesikoList(self.items[start:])
        return NadesikoList(self.items[start:end])
    
    def copy(self):
        """コピーを作成"""
        return NadesikoList(self.items.copy())
    
    def to_json(self) -> str:
        """JSONに変換"""
        return json.dumps(self.items, ensure_ascii=False)
    
    def from_json(self, json_str: str):
        """JSONから読み込み"""
        self.items = json.loads(json_str)

class NadesikoDict:
    """なでしこ用辞書クラス"""
    
    def __init__(self, data: Dict[str, Any] = None):
        self.data = data if data is not None else {}
    
    def __str__(self):
        return f"{{{', '.join(f'{k}: {v}' for k, v in self.data.items())}}}"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key: str):
        return self.data[key]
    
    def __setitem__(self, key: str, value: Any):
        self.data[key] = value
    
    def __contains__(self, key: str):
        return key in self.data
    
    def get(self, key: str, default: Any = None):
        """値を取得"""
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any):
        """値を設定"""
        self.data[key] = value
    
    def delete(self, key: str):
        """キーを削除"""
        if key in self.data:
            del self.data[key]
    
    def keys(self):
        """キーの一覧を取得"""
        return list(self.data.keys())
    
    def values(self):
        """値の一覧を取得"""
        return list(self.data.values())
    
    def items(self):
        """キーと値のペアを取得"""
        return list(self.data.items())
    
    def clear(self):
        """すべての要素を削除"""
        self.data.clear()
    
    def copy(self):
        """コピーを作成"""
        return NadesikoDict(self.data.copy())
    
    def update(self, other_dict):
        """辞書を更新"""
        if isinstance(other_dict, NadesikoDict):
            self.data.update(other_dict.data)
        else:
            self.data.update(other_dict)
    
    def has_key(self, key: str) -> bool:
        """キーが存在するか確認"""
        return key in self.data
    
    def to_json(self) -> str:
        """JSONに変換"""
        return json.dumps(self.data, ensure_ascii=False)
    
    def from_json(self, json_str: str):
        """JSONから読み込み"""
        self.data = json.loads(json_str)

class NadesikoSet:
    """なでしこ用セットクラス"""
    
    def __init__(self, items: Set[Any] = None):
        self.items = set(items) if items is not None else set()
    
    def __str__(self):
        return f"{{{', '.join(str(item) for item in self.items)}}}"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item):
        return item in self.items
    
    def add(self, item: Any):
        """要素を追加"""
        self.items.add(item)
    
    def remove(self, item: Any):
        """要素を削除"""
        if item in self.items:
            self.items.remove(item)
    
    def discard(self, item: Any):
        """要素を削除（存在しなくてもエラーにならない）"""
        self.items.discard(item)
    
    def clear(self):
        """すべての要素を削除"""
        self.items.clear()
    
    def copy(self):
        """コピーを作成"""
        return NadesikoSet(self.items.copy())
    
    def union(self, other_set):
        """和集合"""
        if isinstance(other_set, NadesikoSet):
            return NadesikoSet(self.items.union(other_set.items))
        return NadesikoSet(self.items.union(other_set))
    
    def intersection(self, other_set):
        """積集合"""
        if isinstance(other_set, NadesikoSet):
            return NadesikoSet(self.items.intersection(other_set.items))
        return NadesikoSet(self.items.intersection(other_set))
    
    def difference(self, other_set):
        """差集合"""
        if isinstance(other_set, NadesikoSet):
            return NadesikoSet(self.items.difference(other_set.items))
        return NadesikoSet(self.items.difference(other_set))
    
    def is_subset(self, other_set) -> bool:
        """部分集合か確認"""
        if isinstance(other_set, NadesikoSet):
            return self.items.issubset(other_set.items)
        return self.items.issubset(other_set)
    
    def is_superset(self, other_set) -> bool:
        """上位集合か確認"""
        if isinstance(other_set, NadesikoSet):
            return self.items.issuperset(other_set.items)
        return self.items.issuperset(other_set)
    
    def to_list(self) -> NadesikoList:
        """リストに変換"""
        return NadesikoList(list(self.items))
    
    def to_json(self) -> str:
        """JSONに変換"""
        return json.dumps(list(self.items), ensure_ascii=False)
    
    def from_json(self, json_str: str):
        """JSONから読み込み"""
        self.items = set(json.loads(json_str))

class NadesikoQueue:
    """なでしこ用キュークラス"""
    
    def __init__(self, items: List[Any] = None):
        from collections import deque
        self.queue = deque(items if items is not None else [])
    
    def __str__(self):
        return f"Queue([{', '.join(str(item) for item in self.queue)}])"
    
    def __len__(self):
        return len(self.queue)
    
    def enqueue(self, item: Any):
        """要素を追加"""
        self.queue.append(item)
    
    def dequeue(self) -> Any:
        """要素を取り出して削除"""
        if self.queue:
            return self.queue.popleft()
        return None
    
    def peek(self) -> Any:
        """先頭の要素を確認"""
        if self.queue:
            return self.queue[0]
        return None
    
    def is_empty(self) -> bool:
        """空か確認"""
        return len(self.queue) == 0
    
    def clear(self):
        """すべての要素を削除"""
        self.queue.clear()
    
    def to_list(self) -> NadesikoList:
        """リストに変換"""
        return NadesikoList(list(self.queue))

class NadesikoStack:
    """なでしこ用スタッククラス"""
    
    def __init__(self, items: List[Any] = None):
        self.stack = items if items is not None else []
    
    def __str__(self):
        return f"Stack([{', '.join(str(item) for item in self.stack)}])"
    
    def __len__(self):
        return len(self.stack)
    
    def push(self, item: Any):
        """要素を追加"""
        self.stack.append(item)
    
    def pop(self) -> Any:
        """要素を取り出して削除"""
        if self.stack:
            return self.stack.pop()
        return None
    
    def peek(self) -> Any:
        """先頭の要素を確認"""
        if self.stack:
            return self.stack[-1]
        return None
    
    def is_empty(self) -> bool:
        """空か確認"""
        return len(self.stack) == 0
    
    def clear(self):
        """すべての要素を削除"""
        self.stack.clear()
    
    def to_list(self) -> NadesikoList:
        """リストに変換"""
        return NadesikoList(list(self.stack))

class DataStructureFactory:
    """データ構造ファクトリー"""
    
    @staticmethod
    def create_list(items: List[Any] = None) -> NadesikoList:
        """リストを作成"""
        return NadesikoList(items)
    
    @staticmethod
    def create_dict(data: Dict[str, Any] = None) -> NadesikoDict:
        """辞書を作成"""
        return NadesikoDict(data)
    
    @staticmethod
    def create_set(items: Set[Any] = None) -> NadesikoSet:
        """セットを作成"""
        return NadesikoSet(items)
    
    @staticmethod
    def create_queue(items: List[Any] = None) -> NadesikoQueue:
        """キューを作成"""
        return NadesikoQueue(items)
    
    @staticmethod
    def create_stack(items: List[Any] = None) -> NadesikoStack:
        """スタックを作成"""
        return NadesikoStack(items)
    
    @staticmethod
    def from_json(json_str: str, data_type: str):
        """JSONからデータ構造を作成"""
        if data_type == "list":
            lst = NadesikoList()
            lst.from_json(json_str)
            return lst
        elif data_type == "dict":
            dct = NadesikoDict()
            dct.from_json(json_str)
            return dct
        elif data_type == "set":
            st = NadesikoSet()
            st.from_json(json_str)
            return st
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

# グローバル関数
def create_list(items: List[Any] = None) -> NadesikoList:
    """リストを作成"""
    return DataStructureFactory.create_list(items)

def create_dict(data: Dict[str, Any] = None) -> NadesikoDict:
    """辞書を作成"""
    return DataStructureFactory.create_dict(data)

def create_set(items: Set[Any] = None) -> NadesikoSet:
    """セットを作成"""
    return DataStructureFactory.create_set(items)

def create_queue(items: List[Any] = None) -> NadesikoQueue:
    """キューを作成"""
    return DataStructureFactory.create_queue(items)

def create_stack(items: List[Any] = None) -> NadesikoStack:
    """スタックを作成"""
    return DataStructureFactory.create_stack(items)
