"""
日本語プログラミング言語の使用例
"""

from japanese_programming import JapaneseParser

def main():
    parser = JapaneseParser()
    
    print("=== 日本語プログラミング言語のデモ ===\n")
    
    # 基本的な変数操作
    print("1. 基本的な変数操作:")
    basic_code = """
xは10
yは20
zはxとy
zを表示する
"""
    parser.execute(basic_code)
    
    print("\n" + "="*50 + "\n")
    
    # 条件分岐
    print("2. 条件分岐:")
    if_code = """
年齢は18
もし年齢と等しい18ならば
    "成人です"を表示する
そうでなければ
    "未成年です"を表示する
"""
    parser.execute(if_code)
    
    print("\n" + "="*50 + "\n")
    
    # 繰り返し
    print("3. 繰り返し処理:")
    loop_code = """
5だけ繰り返す
    iを表示する
"""
    parser.execute(loop_code)
    
    print("\n" + "="*50 + "\n")
    
    # 関数定義
    print("4. 関数定義:")
    function_code = """
関数足し算は(aとb)を返す
    aとbを返す

結果は足し算(3と4)
結果を表示する
"""
    parser.execute(function_code)
    
    print("\n" + "="*50 + "\n")
    
    # 複合例
    print("5. 複合的な例:")
    complex_code = """
カウントは0
カウントよりも小さい5の間
    カウントを表示する
    カウントはカウントと1
"""
    parser.execute(complex_code)

if __name__ == "__main__":
    main()
