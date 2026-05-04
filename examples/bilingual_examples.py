"""
日本語・英語バイリンガルプログラミング言語の使用例
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from japanese_programming import BilingualParser, EnglishParser, NadesikoParser

def main():
    print("=== 日本語・英語バイリンガルプログラミング言語デモ ===\n")
    
    parser = BilingualParser()
    
    # === 日本語プログラミングの例 ===
    print("1. 日本語プログラミング:")
    japanese_code = """
Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示
"""
    parser.execute(japanese_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 英語プログラミングの例 ===
    print("2. 英語プログラミング:")
    english_code = """
A is 10
B is 20
C is A plus B
show "C value is {C}"
"""
    parser.execute(english_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 条件分岐の比較 ===
    print("3. 条件分岐の比較:")
    print("日本語版:")
    japanese_if = """
年齢は25
もし年齢が18以上ならば
    「成人です」を表示
違えば
    「未成年です」を表示
"""
    parser.execute(japanese_if)
    
    print("\n英語版:")
    english_if = """
age is 25
if age is greater than 18
    show "Adult"
else
    show "Minor"
"""
    parser.execute(english_if)
    
    print("\n" + "="*60 + "\n")
    
    # === 繰り返しの比較 ===
    print("4. 繰り返しの比較:")
    print("日本語版:")
    japanese_loop = """
5回繰り返す
    「こんにちは」を表示
"""
    parser.execute(japanese_loop)
    
    print("\n英語版:")
    english_loop = """
repeat 5 times
    show "Hello"
"""
    parser.execute(english_loop)
    
    print("\n" + "="*60 + "\n")
    
    # === 関数定義の比較 ===
    print("5. 関数定義の比較:")
    print("日本語版:")
    japanese_func = """
●足し算（AとB）
    AとBを足して返す

結果は足し算(10と20)
「結果: {結果}」を表示
"""
    parser.execute(japanese_func)
    
    print("\n英語版:")
    english_func = """
function add_numbers(x and y)
    return x plus y

result is add_numbers(10 and 20)
show "Result: {result}"
"""
    parser.execute(english_func)
    
    print("\n" + "="*60 + "\n")
    
    # === 複雑な例: BMI計算 ===
    print("6. 複雑な例: BMI計算")
    print("日本語版:")
    japanese_bmi = """
●BMI計算（身長と体重）
    身長の2乗で体重を割って返す

●BMI判定（BMI値）
    もしBMI値が18.5より小さいならば
        「低体重です」を返す
    もしBMI値が25以上ならば
        「肥満です」を返す
    違えば
        「普通体重です」を返す

身長は1.70
体重は65
BMIはBMI計算(身長と体重)
判定はBMI判定(BMI)
「BMI: {BMI:.1f} - {判定}」を表示
"""
    parser.execute(japanese_bmi)
    
    print("\n英語版:")
    english_bmi = """
function calculate_bmi(height and weight)
    return weight divided by (height times height)

function check_bmi(bmi_value)
    if bmi_value is less than 18.5
        return "Underweight"
    if bmi_value is greater than 25
        return "Overweight"
    else
        return "Normal weight"

height is 1.70
weight is 65
bmi is calculate_bmi(height and weight)
status is check_bmi(bmi)
show "BMI: {bmi:.1f} - {status}"
"""
    parser.execute(english_bmi)
    
    print("\n" + "="*60 + "\n")
    
    # === 言語自動検出のテスト ===
    print("7. 言語自動検出のテスト:")
    mixed_code = """
# 日本語コード
Xは100
「Xの値: {X}」を表示

# English code
Y is 200
show "Y value: {Y}"

# 日本語コード
ZはXとYを足す
「合計: {Z}」を表示
"""
    parser.execute(mixed_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 子供向け簡単な例 ===
    print("8. 子供向け簡単な例:")
    kids_code = """
# 英語で数字を学ぼう
apple is 5
banana is 3
total is apple plus banana
show "I have {total} fruits"

# 日本語であいさつ
「こんにちは！世界！」を表示
「ようこそプログラミングの世界へ！」を表示

# 英語でループ
repeat 3 times
    show "Learning is fun!"
"""
    parser.execute(kids_code)
    
    print("\n" + "="*60 + "\n")
    
    # === 高度な例: 素数判定 ===
    print("9. 高度な例: 素数判定:")
    print("英語版:")
    english_prime = """
function is_prime(n)
    if n is less than 2
        return false
    if n is equal to 2
        return true
    if n is even
        return false
    i is 3
    while i times i is less than or equal to n
        if n divided by i has remainder 0
            return false
        i is i plus 2
    return true

if is_prime(17)
    show "17 is prime"
else
    show "17 is not prime"

if is_prime(18)
    show "18 is prime"
else
    show "18 is not prime"
"""
    parser.execute(english_prime)
    
    print("\n" + "="*60 + "\n")
    
    # === ゲーム風の例 ===
    print("10. ゲーム風の例:")
    game_code = """
# Simple adventure game
player_name is "Hero"
player_health is 100
enemy_health is 50

show "Welcome {player_name}!"
show "Player Health: {player_health}"
show "Enemy Health: {enemy_health}"

while player_health is greater than 0 and enemy_health is greater than 0
    # Player attacks
    damage is 10 plus random 5
    enemy_health is enemy_health minus damage
    show "Player deals {damage} damage!"
    show "Enemy Health: {enemy_health}"
    
    if enemy_health is less than or equal to 0
        show "You win!"
        break
    
    # Enemy attacks
    damage is 5 plus random 3
    player_health is player_health minus damage
    show "Enemy deals {damage} damage!"
    show "Player Health: {player_health}"
    
    if player_health is less than or equal to 0
        show "Game Over!"
        break
    
    wait 1 second

if player_health is greater than 0
    show "Victory! {player_name} wins!"
else
    show "Defeat! Try again."
"""
    parser.execute(game_code)
    
    print("\n" + "="*60 + "\n")
    
    print("バイリンガルプログラミング言語デモ完了！")
    print("日本語と英語の両方で、自然な言語でプログラミングできます。")
    print("アメリカの子供たちも、日本の子供たちも、楽しく学べます！")

if __name__ == "__main__":
    main()
