"""
なでしこ3互換モジュールの使用例
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nadesiko_parser import NadesikoParser
from src.nadesiko_functions import NadesikoFunctions
from src.nadesiko_gui import NadesikoGUI
from src.nadesiko_file import NadesikoFile
from src.nadesiko_math import NadesikoMath
from src.nadesiko_string import NadesikoString

def main():
    print("=== なでしこ3互換日本語プログラミング言語のデモ ===\n")
    
    parser = NadesikoParser()
    
    # === 基本構文のデモ ===
    print("1. 基本構文:")
    basic_code = """
Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示
"""
    parser.execute(basic_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 制御構文のデモ ===
    print("2. 制御構文:")
    control_code = """
年齢は25
もし年齢が18以上ならば
    「成人です」を表示
違えば
    「未成年です」を表示
"""
    parser.execute(control_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 繰り返しのデモ ===
    print("3. 繰り返し:")
    loop_code = """
5回繰り返す
    「こんにちは」を表示
"""
    parser.execute(loop_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 関数定義のデモ ===
    print("4. 関数定義:")
    function_code = """
●足し算（AとB）
    AとBを足して返す

結果は足し算(10と20)
「10と20の合計は{結果}です」を表示
"""
    parser.execute(function_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 数学関数のデモ ===
    print("5. 数学関数:")
    math_code = """
「円周率は{ナ}です」を表示
「5の平方根は{平方根(5)}です」を表示
「3の階乗は{階乗(3)}です」を表示
"""
    parser.execute(math_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 文字列操作のデモ ===
    print("6. 文字列操作:")
    string_code = """
テキストは「こんにちは、世界！」
「文字数: {文字数(テキスト)}」を表示
「左から5文字: {左から(テキスト, 5)}」を表示
「大文字: {大文字(テキスト)}」を表示
"""
    parser.execute(string_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 配列操作のデモ ===
    print("7. 配列操作:")
    array_code = """
リストは[1, 2, 3, 4, 5]
「要素数: {要素数(リスト)}」を表示
「合計: {合計(リスト)}」を表示
「平均: {平均(リスト)}」を表示
"""
    parser.execute(array_code)
    
    print("\n" + "="*60 + "\n")
    
    # === ファイル操作のデモ ===
    print("8. ファイル操作:")
    file_code = """
「test.txt」に「なでしこ3テスト」を書く
内容は「test.txt」を読む
「ファイル内容: {内容}」を表示
"""
    parser.execute(file_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 日時操作のデモ ===
    print("9. 日時操作:")
    datetime_code = """
現在は今()
「現在時刻: {書式(現在, '%Y年%m月%d日 %H:%M:%S')}」を表示
「今年: {年()}年」を表示
"""
    parser.execute(datetime_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 複雑な例: 素数判定 ===
    print("10. 素数判定:")
    prime_code = """
●素数判定（N）
    もしNが2より小さいならば
        偽を返す
    もしNが2と等しいならば
        真を返す
    もしNが偶数ならば
        偽を返す
    Iは3
    Iの平方根がN以下の間
        もしNをIで割り切れるが0ならば
            偽を返す
        IはIと2を足す
    真を返す

17は素数判定(17)ならば
    「17は素数です」を表示
違えば
    「17は素数ではありません」を表示

18は素数判定(18)ならば
    「18は素数です」を表示
違えば
    「18は素数ではありません」を表示
"""
    parser.execute(prime_code)
    
    print("\n" + "="*60 + "\n")
    
    # === GUIデモ（コメントアウト - 自動実行を避けるため） ===
    print("11. GUI機能:")
    print("※GUI機能は手動実行が必要なため省略")
    gui_code = """
# ウィンドウ作成
# ウィンドウ作成「なでしこGUIテスト」
# 
# # ボタン作成
# ボタンIDはボタン作成(text=\"クリックしてね\")
# 
# # ラベル作成
# ラベルIDはラベル作成(text=\"こんにちは\", x=10, y=50)
# 
# # メッセージボックス
# 「ようこそなでしこへ！」をメッセージボックス
"""
    print("GUIコード例:")
    print(gui_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 総合デモ: 簡単な電卓 ===
    print("12. 簡単な電卓:")
    calculator_code = """
●電卓（操作とAとB）
    もし操作が「足す」ならば
        AとBを足して返す
    もし操作が「引く」ならば
        AからBを引いて返す
    もし操作が「掛ける」ならば
        AとBを掛けて返す
    もし操作が「割る」ならば
        AをBで割って返す
    0を返す

結果1は電卓(「足す」, 10, 5)
「10+5={結果1}」を表示

結果2は電卓(「掛ける」, 7, 8)
「7×8={結果2}」を表示

結果3は電卓(「引く」, 20, 3)
「20-3={結果3}」を表示
"""
    parser.execute(calculator_code)
    
    print("\n" + "="*60 + "\n")
    
    # === クラス機能のデモ ===
    print("13. オブジェクト指向的プログラミング:")
    oop_code = """
# 人間オブジェクトのようなデータ構造
人間は{
    「名前」: 「田中」,
    「年齢」: 30,
    「職業」: 「プログラマー」
}

「{人間[\"名前\"]}さんは{人間[\"年齢\"]}歳の{人間[\"職業\"]}です」を表示

# 自己紹介関数
●自己紹介（人物）
    「私は{人物[\"名前\"]}です。{人物[\"年齢\"]}歳です。」と表示

人間を自己紹介
"""
    parser.execute(oop_code)
    
    print("\n" + "="*60 + "\n")
    
    # === なでしこ特有の「それ」のデモ ===
    print("14. 「それ」の使用例:")
    sore_code = """
5と3を足す
「それ: {それ}」を表示

10を2で割る
「それ: {それ}」を表示

「こんにちは」の文字数
「それ: {それ}」を表示
"""
    parser.execute(sore_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 終了メッセージ ===
    print("デモ完了！なでしこ3互換モジュールで様々な機能が使えます。")
    print("Python初心者でも日本語で直感的にプログラミングできます。")

if __name__ == "__main__":
    main()
