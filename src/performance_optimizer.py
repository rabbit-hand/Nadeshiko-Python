"""
パフォーマンス最適化モジュール
コード実行速度の最適化とメモリ使用量の削減
"""

import time
import gc
import functools
import threading
from typing import Dict, List, Optional, Callable, Any
from concurrent.futures import ThreadPoolExecutor
import sys

class PerformanceOptimizer:
    """パフォーマンス最適化クラス"""
    
    def __init__(self):
        self.execution_times = {}
        self.memory_usage = {}
        self.cache = {}
        self.thread_pool = ThreadPoolExecutor(max_workers=4)
        self.optimization_enabled = True
    
    def enable_optimization(self, enabled: bool):
        """最適化を有効/無効化"""
        self.optimization_enabled = enabled
    
    def measure_execution_time(self, func_name: str):
        """実行時間を測定するデコレータ"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not self.optimization_enabled:
                    return func(*args, **kwargs)
                
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.time()
                    execution_time = end_time - start_time
                    self.execution_times[func_name] = execution_time
                    
                    # 実行時間が長い場合は警告
                    if execution_time > 1.0:
                        print(f"⚠️ {func_name} の実行時間が長いです: {execution_time:.2f}秒")
                
                return result
            return wrapper
        return decorator
    
    def cache_result(self, max_size: int = 100):
        """結果をキャッシュするデコレータ"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not self.optimization_enabled:
                    return func(*args, **kwargs)
                
                # キャッシュキーの生成
                cache_key = (func.__name__, str(args), str(sorted(kwargs.items())))
                
                # キャッシュをチェック
                if cache_key in self.cache:
                    return self.cache[cache_key]
                
                # 実行して結果をキャッシュ
                result = func(*args, **kwargs)
                
                # キャッシュサイズの制限
                if len(self.cache) >= max_size:
                    # 最も古いキャッシュを削除
                    oldest_key = next(iter(self.cache))
                    del self.cache[oldest_key]
                
                self.cache[cache_key] = result
                return result
            return wrapper
        return decorator
    
    def optimize_memory_usage(self):
        """メモリ使用量を最適化"""
        if not self.optimization_enabled:
            return
        
        # ガベージコレクションを実行
        gc.collect()
        
        # メモリ使用量を取得
        if hasattr(sys, 'getsizeof'):
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            self.memory_usage['current'] = memory_info.rss
            
            # メモリ使用量が多い場合は警告
            if memory_info.rss > 100 * 1024 * 1024:  # 100MB
                print(f"⚠️ メモリ使用量が多いです: {memory_info.rss / 1024 / 1024:.2f}MB")
    
    def parallel_execute(self, func: Callable, tasks: List[Any]) -> List[Any]:
        """並列実行"""
        if not self.optimization_enabled or len(tasks) <= 1:
            return [func(task) for task in tasks]
        
        try:
            futures = [self.thread_pool.submit(func, task) for task in tasks]
            results = [future.result() for future in futures]
            return results
        except Exception as e:
            print(f"並列実行エラー: {e}")
            # フォールバック: シーケンシャル実行
            return [func(task) for task in tasks]
    
    def optimize_string_operations(self, text: str) -> str:
        """文字列操作の最適化"""
        if not self.optimization_enabled:
            return text
        
        # 文字列結合の最適化
        if isinstance(text, list):
            return ''.join(text)
        
        # 文字列置換の最適化
        if isinstance(text, str):
            # よく使われる置換をキャッシュ
            common_replacements = {
                'と': ' + ',
                'から': ' - ',
                'を掛ける': ' * ',
                'で割る': ' / ',
                'よりも大きい': ' > ',
                'よりも小さい': ' < ',
                'と等しい': ' == ',
                'と異なる': ' != ',
                'かつ': ' and ',
                'または': ' or ',
                'ではない': ' not '
            }
            
            result = text
            for old, new in common_replacements.items():
                if old in result:
                    result = result.replace(old, new)
            
            return result
        
        return text
    
    def get_performance_report(self) -> Dict:
        """パフォーマンスレポートを取得"""
        return {
            'execution_times': self.execution_times,
            'memory_usage': self.memory_usage,
            'cache_size': len(self.cache),
            'optimization_enabled': self.optimization_enabled
        }
    
    def clear_cache(self):
        """キャッシュをクリア"""
        self.cache.clear()
    
    def get_slow_functions(self, threshold: float = 0.5) -> List[str]:
        """遅い関数を取得"""
        return [func for func, time in self.execution_times.items() if time > threshold]
    
    def optimize_regex_patterns(self, patterns: Dict[str, str]) -> Dict[str, Any]:
        """正規表現パターンの最適化"""
        if not self.optimization_enabled:
            return patterns
        
        optimized_patterns = {}
        for name, pattern in patterns.items():
            # コンパイル済み正規表現をキャッシュ
            cache_key = f"regex_{name}"
            if cache_key in self.cache:
                optimized_patterns[name] = self.cache[cache_key]
            else:
                import re
                compiled_pattern = re.compile(pattern)
                optimized_patterns[name] = compiled_pattern
                self.cache[cache_key] = compiled_pattern
        
        return optimized_patterns
    
    def batch_process(self, items: List[Any], batch_size: int = 100) -> List[List[Any]]:
        """バッチ処理"""
        if not self.optimization_enabled:
            return [items]
        
        batches = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            batches.append(batch)
        
        return batches
    
    def __del__(self):
        """クリーンアップ"""
        if hasattr(self, 'thread_pool'):
            self.thread_pool.shutdown(wait=True)

# グローバルインスタンス
performance_optimizer = PerformanceOptimizer()

# デコレータのエイリアス
measure_time = performance_optimizer.measure_execution_time
cache_result = performance_optimizer.cache_result
