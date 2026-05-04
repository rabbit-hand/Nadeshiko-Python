"""
なでしこ3互換数学ライブラリ
"""

import math
import random
import statistics
from decimal import Decimal, getcontext

class NadesikoMath:
    """なでしこ3の数学関数を拡張実装"""
    
    def __init__(self):
        self._result = None
        getcontext().prec = 28  # 高精度計算用
    
    # === 基本数学関数 ===
    def 絶対値(self, x):
        """絶対値"""
        self._result = abs(x)
        return self._result
    
    def 平方根(self, x):
        """平方根"""
        self._result = math.sqrt(x)
        return self._result
    
    def 立方根(self, x):
        """立方根"""
        self._result = x ** (1/3)
        return self._result
    
    def べき乗(self, x, y):
        """べき乗"""
        self._result = x ** y
        return self._result
    
    def 割り切れる(self, x, y):
        """剰余"""
        self._result = x % y
        return self._result
    
    def 商(self, x, y):
        """商"""
        self._result = x // y
        return self._result
    
    # === 三角関数 ===
    def サイン(self, x, degrees=False):
        """サイン"""
        if degrees:
            x = math.radians(x)
        self._result = math.sin(x)
        return self._result
    
    def コサイン(self, x, degrees=False):
        """コサイン"""
        if degrees:
            x = math.radians(x)
        self._result = math.cos(x)
        return self._result
    
    def タンジェント(self, x, degrees=False):
        """タンジェント"""
        if degrees:
            x = math.radians(x)
        self._result = math.tan(x)
        return self._result
    
    def アークサイン(self, x, degrees=False):
        """アークサイン"""
        result = math.asin(x)
        if degrees:
            result = math.degrees(result)
        self._result = result
        return self._result
    
    def アークコサイン(self, x, degrees=False):
        """アークコサイン"""
        result = math.acos(x)
        if degrees:
            result = math.degrees(result)
        self._result = result
        return self._result
    
    def アークタンジェント(self, x, degrees=False):
        """アークタンジェント"""
        result = math.atan(x)
        if degrees:
            result = math.degrees(result)
        self._result = result
        return self._result
    
    # === 双曲線関数 ===
    def ハイパーサイン(self, x):
        """ハイパーサイン"""
        self._result = math.sinh(x)
        return self._result
    
    def ハイパーコサイン(self, x):
        """ハイパーコサイン"""
        self._result = math.cosh(x)
        return self._result
    
    def ハイパータンジェント(self, x):
        """ハイパータンジェント"""
        self._result = math.tanh(x)
        return self._result
    
    # === 対数関数 ===
    def 対数(self, x, base=math.e):
        """対数"""
        if base == math.e:
            self._result = math.log(x)
        elif base == 10:
            self._result = math.log10(x)
        elif base == 2:
            self._result = math.log2(x)
        else:
            self._result = math.log(x, base)
        return self._result
    
    def 常用対数(self, x):
        """常用対数"""
        self._result = math.log10(x)
        return self._result
    
    def 自然対数(self, x):
        """自然対数"""
        self._result = math.log(x)
        return self._result
    
    def 二進対数(self, x):
        """二進対数"""
        self._result = math.log2(x)
        return self._result
    
    def 指数関数(self, x):
        """指数関数"""
        self._result = math.exp(x)
        return self._result
    
    # === 丸め関数 ===
    def 四捨五入(self, x, digits=0):
        """四捨五入"""
        self._result = round(x, digits)
        return self._result
    
    def 切り上げ(self, x):
        """切り上げ"""
        self._result = math.ceil(x)
        return self._result
    
    def 切り捨て(self, x):
        """切り捨て"""
        self._result = math.floor(x)
        return self._result
    
    def 整数部分(self, x):
        """整数部分"""
        self._result = int(x)
        return self._result
    
    def 小数部分(self, x):
        """小数部分"""
        self._result = x - int(x)
        return self._result
    
    def 符号(self, x):
        """符号"""
        if x > 0:
            self._result = 1
        elif x < 0:
            self._result = -1
        else:
            self._result = 0
        return self._result
    
    # === 特殊関数 ===
    def 階乗(self, n):
        """階乗"""
        self._result = math.factorial(n)
        return self._result
    
    def 順列(self, n, r):
        """順列"""
        if r > n:
            self._result = 0
        else:
            self._result = math.factorial(n) // math.factorial(n - r)
        return self._result
    
    def 組み合わせ(self, n, r):
        """組み合わせ"""
        if r > n:
            self._result = 0
        else:
            self._result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        return self._result
    
    def フィボナッチ(self, n):
        """フィボナッチ数"""
        if n <= 0:
            self._result = 0
        elif n == 1:
            self._result = 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            self._result = b
        return self._result
    
    # === 最大・最小 ===
    def 最大値(self, *args):
        """最大値"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            self._result = max(args[0])
        else:
            self._result = max(args)
        return self._result
    
    def 最小値(self, *args):
        """最小値"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            self._result = min(args[0])
        else:
            self._result = min(args)
        return self._result
    
    def 合計(self, *args):
        """合計"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            self._result = sum(args[0])
        else:
            self._result = sum(args)
        return self._result
    
    def 平均(self, *args):
        """平均"""
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            data = args[0]
        else:
            data = args
        self._result = sum(data) / len(data)
        return self._result
    
    # === 統計関数 ===
    def 中央値(self, data):
        """中央値"""
        self._result = statistics.median(data)
        return self._result
    
    def 最頻値(self, data):
        """最頻値"""
        try:
            self._result = statistics.mode(data)
        except statistics.StatisticsError:
            self._result = None
        return self._result
    
    def 分散(self, data):
        """分散"""
        self._result = statistics.variance(data)
        return self._result
    
    def 標準偏差(self, data):
        """標準偏差"""
        self._result = statistics.stdev(data)
        return self._result
    
    def 範囲(self, data):
        """範囲"""
        self._result = max(data) - min(data)
        return self._result
    
    # === 乱数 ===
    def 乱数(self, min_val=0, max_val=1):
        """乱数"""
        if min_val == 0 and max_val == 1:
            self._result = random.random()
        else:
            self._result = random.uniform(min_val, max_val)
        return self._result
    
    def 整数乱数(self, min_val, max_val):
        """整数乱数"""
        self._result = random.randint(min_val, max_val)
        return self._result
    
    def 選択(self, data):
        """ランダム選択"""
        self._result = random.choice(data)
        return self._result
    
    def シャッフル(self, data):
        """シャッフル"""
        random.shuffle(data)
        self._result = data
        return self._result
    
    def 重複なし乱数(self, min_val, max_val, count):
        """重複なし乱数"""
        if count > (max_val - min_val + 1):
            self._result = []
        else:
            self._result = random.sample(range(min_val, max_val + 1), count)
        return self._result
    
    # === 定数 ===
    def 円周率(self):
        """円周率"""
        self._result = math.pi
        return self._result
    
    def 自然対数の底(self):
        """自然対数の底"""
        self._result = math.e
        return self._result
    
    def 黄金比(self):
        """黄金比"""
        self._result = (1 + math.sqrt(5)) / 2
        return self._result
    
    def オイラー定数(self):
        """オイラー定数"""
        self._result = 0.5772156649015328606065120900824024310421
        return self._result
    
    # === 高精度計算 ===
    def 高精度絶対値(self, x):
        """高精度絶対値"""
        self._result = abs(Decimal(str(x)))
        return self._result
    
    def 高精度平方根(self, x):
        """高精度平方根"""
        self._result = Decimal(str(x)).sqrt()
        return self._result
    
    def 高精度べき乗(self, x, y):
        """高精度べき乗"""
        self._result = Decimal(str(x)) ** Decimal(str(y))
        return self._result
    
    # === 数値判定 ===
    def 偶数か(self, x):
        """偶数か"""
        self._result = x % 2 == 0
        return self._result
    
    def 奇数か(self, x):
        """奇数か"""
        self._result = x % 2 != 0
        return self._result
    
    def 素数か(self, n):
        """素数か"""
        if n < 2:
            self._result = False
        elif n == 2:
            self._result = True
        elif n % 2 == 0:
            self._result = False
        else:
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    self._result = False
                    break
            else:
                self._result = True
        return self._result
    
    def 完全数か(self, n):
        """完全数か"""
        if n < 2:
            self._result = False
        else:
            divisors = [1]
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
            self._result = sum(divisors) == n
        return self._result
    
    # === 進数変換 ===
    def 二進数に変換(self, x):
        """二進数に変換"""
        self._result = bin(x)
        return self._result
    
    def 八進数に変換(self, x):
        """八進数に変換"""
        self._result = oct(x)
        return self._result
    
    def 十六進数に変換(self, x):
        """十六進数に変換"""
        self._result = hex(x)
        return self._result
    
    def 二進数から変換(self, s):
        """二進数から変換"""
        self._result = int(s, 2)
        return self._result
    
    def 八進数から変換(self, s):
        """八進数から変換"""
        self._result = int(s, 8)
        return self._result
    
    def 十六進数から変換(self, s):
        """十六進数から変換"""
        self._result = int(s, 16)
        return self._result
    
    # === ユーティリティ ===
    def それ(self):
        """直前の計算結果"""
        return self._result
    
    def グラフ描画準備(self):
        """グラフ描画の準備（matplotlibが必要）"""
        try:
            import matplotlib.pyplot as plt
            self._result = plt
            return self._result
        except ImportError:
            self._result = None
            return self._result
    
    def ヒストグラム描画(self, data, bins=10):
        """ヒストグラムを描画"""
        plt = self.グラフ描画準備()
        if plt:
            plt.hist(data, bins=bins)
            plt.xlabel("値")
            plt.ylabel("頻度")
            plt.title("ヒストグラム")
            plt.show()
            self._result = True
        else:
            self._result = False
        return self._result
