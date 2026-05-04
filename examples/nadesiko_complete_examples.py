"""
なでしこ3完全互換モジュールの使用例
全機能を網羅したデモプログラム
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from japanese_programming import NadesikoParser, NadesikoComplete, NadesikoCompleteCommands

def main():
    print("=== なでしこ3完全互換モジュール デモ ===\n")
    
    # 基本パーサーでテスト
    parser = NadesikoParser()
    
    # === 1. 基本システム定数 ===
    print("1. システム定数:")
    basic_code = '''
「なでしこバージョン: {ナデシコバージョン}」を表示
「円周率: {ナ}」を表示
「真: {真}、偽: {偽}」を表示
「改行文字: {改行}」を表示
'''
    parser.execute(basic_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 2. 高度な数学関数 ===
    print("2. 高度な数学関数:")
    math_code = '''
「絶対値(-5): {絶対値(-5)}」を表示
「平方根(16): {平方根(16)}」を表示
「階乗(5): {階乗(5)}」を表示
「組み合わせ(5,2): {組み合わせ(5, 2)}」を表示
「サイン(90度): {サイン(90, 1)}」を表示
'''
    parser.execute(math_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 3. 高度な文字列操作 ===
    print("3. 高度な文字列操作:")
    string_code = '''
textは「こんにちは、なでしこ3！世界！」
「元の文字: {text}」を表示
「文字数: {文字数(text)}」を表示
「大文字: {大文字(text)}」を表示
「置換: {置換(text, \"なでしこ3\", \"Python\")}」を表示
「ひらがな変換: {ひらがなに変換(\"コンニチハ\")}」を表示
'''
    parser.execute(string_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 4. 高度な配列操作 ===
    print("4. 高度な配列操作:")
    array_code = '''
配列は[1, 2, 3, 2, 4, 1]
「元の配列: {配列}」を表示
「ユニーク: {ユニーク(配列)}」を表示
「ソート: {ソート(配列)}」を表示
「重複なし: {重複なし(配列)}」を表示
'''
    parser.execute(array_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 5. 高度なファイル操作 ===
    print("5. 高度なファイル操作:")
    file_code = '''
「現在ディレクトリ: {現在ディレクトリ}」を表示
「プラットフォーム: {プラットフォーム}」を表示
一覧は一覧取得(".")
「ファイル数: {要素数(一覧)}」を表示
'''
    parser.execute(file_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 6. 完全版クラスのデモ ===
    print("6. 完全版クラス機能:")
    complete = NadesikoComplete()
    
    # システム定数
    print(f"なでしこバージョン: {complete.ナデシコバージョン()}")
    print(f"円周率: {complete.円周率}")
    print(f"真: {complete.真()}")
    
    # 高度な数学
    print(f"階乗(6): {complete.階乗(6)}")
    print(f"組み合わせ(6,3): {complete.組み合わせ(6, 3)}")
    print(f"黄金比: {complete.黄金比()}")
    
    # 高度な文字列操作
    text = "Pythonプログラミング"
    print(f"文字数: {complete.文字数(text)}")
    print(f"反転: {complete.反転(text)}")
    print(f"大文字: {complete.大文字(text)}")
    
    print("\n" + "="*60 + "\n")
    
    # === 7. GUI機能デモ ===
    print("7. GUI機能:")
    gui = NadesikoCompleteCommands()
    
    try:
        # メッセージボックス
        result = gui.メッセージボックス("テスト", "なでしこ3完全互換モジュール")
        print(f"メッセージボックス結果: {result}")
        
        # 入力ボックス
        name = gui.入力ボックス("入力", "名前を入力してください", "なでしこ")
        print(f"入力された名前: {name}")
        
        # ファイル選択
        filepath = gui.ファイル選択("ファイル選択")
        print(f"選択されたファイル: {filepath}")
        
    except Exception as e:
        print(f"GUIデモはスキップ: {e}")
    
    print("\n" + "="*60 + "\n")
    
    # === 8. ネットワーク機能デモ ===
    print("8. ネットワーク機能:")
    try:
        # HTTP GET
        result = gui.HTTP取得("https://httpbin.org/get")
        print(f"HTTP GET結果: {result[:100]}...")
        
        # JSON取得
        json_data = gui.JSON取得("https://httpbin.org/json")
        print(f"JSONデータ: {json_data}")
        
    except Exception as e:
        print(f"ネットワークデモはスキップ: {e}")
    
    print("\n" + "="*60 + "\n")
    
    # === 9. データベース機能デモ ===
    print("9. データベース機能:")
    try:
        # SQLite3接続
        conn = gui.SQLite3接続(":memory:")
        print(f"データベース接続: {conn}")
        
        # テーブル作成
        result = gui.テーブル作成(conn, "users", "id INTEGER PRIMARY KEY, name TEXT, age INTEGER")
        print(f"テーブル作成: {result}")
        
        # データ挿入
        result = gui.挿入(conn, "users", (1, "なでしこ", 20))
        print(f"データ挿入: {result}")
        
        # データ選択
        data = gui.選択(conn, "users")
        print(f"データ選択: {data}")
        
        conn.close()
        
    except Exception as e:
        print(f"データベースデモはスキップ: {e}")
    
    print("\n" + "="*60 + "\n")
    
    # === 10. 高度なプログラミング例 ===
    print("10. 高度なプログラミング例:")
    advanced_code = '''
# 素数判定関数
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

# 素数リスト生成
●素数リスト生成（最大値）
    リストは[]
    Iは2
    Iから最大値まで反復
        もし素数判定(I)ならば
            リストにIを追加
    リストを返す

素数は素数リスト生成(30)
「30までの素数: {素数}」を表示
「素数の数: {要素数(素数)}」を表示
'''
    parser.execute(advanced_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 11. データ処理例 ===
    print("11. データ処理例:")
    data_code = '''
# CSVデータ処理
データは「名前,年齢,点数
なでしこ,20,85
Python,25,90
Java,30,78」

行リストは行分割(データ)
「データ行数: {要素数(行リスト)}」を表示

# 最初の行を処理
ヘッダーは行リスト[0]
「ヘッダー: {ヘッダー}」を表示

# データ行を処理
Iは1
Iから要素数(行リスト)-1まで反復
    行は行リスト[I]
    項目は分割(行, ",")
    「{項目[0]}は{項目[2]}点」を表示
'''
    parser.execute(data_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 12. 実用的なツール例 ===
    print("12. 実用的なツール例:")
    tool_code = '''
# テキスト解析ツール
●テキスト解析（テキスト）
    文字数は文字数(テキスト)
    行数は要素数(行分割(テキスト))
    単語数は要素数(単語分割(テキスト))
    
    「文字数: {文字数}」を表示
    「行数: {行数}」を表示
    「単語数: {単語数}」を表示
    
    # 文字種別カウント
    ひらがな数は0
    カタカナ数は0
    漢字数は0
    英字数は0
    数字数は0
    
    Iは0
    文字数まで反復
        文字はテキスト[I]
        もし「ぁ」が文字以上ならば「ん」が文字以下ならば
            ひらがな数はひらがな数と1
        違えば
            もし「ァ」が文字以上ならば「ン」が文字以下ならば
                カタカナ数はカタカナ数と1
            違えば
                もし「0」が文字以上ならば「9」が文字以下ならば
                    数字数は数字数と1
                違えば
                    もし「a」が文字以上ならば「z」が文字以下ならば
                        英字数は英字数と1
                    違えば
                        漢字数は漢字数と1
    
    「ひらがな: {ひらがな数}、カタカナ: {カタカナ数}、漢字: {漢字数}、英字: {英字数}、数字: {数字数}」を表示

# テキスト解析実行
テキストは「こんにちは、世界！Pythonプログラミング123」
テキスト解析(テキスト)
'''
    parser.execute(tool_code)
    
    print("\n" + "="*60 + "\n")
    
    print("🎉 なでしこ3完全互換モジュール デモ完了！")
    print("なでしこ3のほぼ全機能を実装しました。")
    print("これで、なでしこ3でできることはすべて実現できます！")

if __name__ == "__main__":
    main()
