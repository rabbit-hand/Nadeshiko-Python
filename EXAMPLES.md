# サンプルプログラム集 / Sample Programs Collection

## 🎯 できることの詳細な説明と実例

### 📚 教育向けプログラミング例

#### 1. 小学生向け基本プログラミング

**日本語版:**
```nadesiko
# お買い物計算
りんごは100円
みかんは80円
ぶどうは150円

合計はりんごとみかんとぶどうを足す
「合計金額: {合計}円」を表示

# 割引計算
もし合計が300以上ならば
    割引は合計の0.1倍
    「10%割引: {割引}円」を表示
    支払いは合計から割引を引く
    「支払額: {支払い}円」を表示
違えば
    「割引なし」を表示
```

**英語版:**
```english
# Shopping calculation
apple is 100
orange is 80
grape is 150

total is apple plus orange plus grape
show "Total: {total} yen"

# Discount calculation
if total is greater than 300
    discount is total times 0.1
    show "10% discount: {discount} yen"
    payment is total minus discount
    show "Payment: {payment} yen"
else
    show "No discount"
```

#### 2. 中学生向け数学プログラミング

**日本語版:**
```nadesiko
# 二次方程式の解
●二次方程式を解く（AとBとC）
    判別式はBの二乗から4とAとCを掛けたものを引く
    「判別式: {判別式}」を表示
    
    もし判別式が0より大きいならば
        根1は(-Bと平方根(判別式)を足す)を(2とAを掛けたもの)で割る
        根2は(-Bと平方根(判別式)を引く)を(2とAを掛けたもの)で割る
        「実数解2つ: {根1}, {根2}」を表示
    違えば
        もし判別式が0と等しいならば
            根は-Bを(2とAを掛けたもの)で割る
            「重解: {根}」を表示
        違えば
            「実数解なし」を表示
    戻値無

# x²-5x+6=0を解く
二次方程式を解く(1と-5と6)
```

**英語版:**
```english
# Solve quadratic equation
function solve_quadratic(a and b and c)
    discriminant is b squared minus (4 times a times c)
    show "Discriminant: {discriminant}"
    
    if discriminant is greater than 0
        root1 is (-b plus square_root(discriminant)) divided by (2 times a)
        root2 is (-b minus square_root(discriminant)) divided by (2 times a)
        show "Two real roots: {root1}, {root2}"
    else
        if discriminant equals 0
            root is -b divided by (2 times a)
            show "Double root: {root}"
        else
            show "No real roots"
    return

# Solve x²-5x+6=0
solve_quadratic(1 and -5 and 6)
```

### 🎮 ゲームプログラミング例

#### 3. 簡単な数当てゲーム

**日本語版:**
```nadesiko
# 数当てゲーム
答えは整数乱数(1, 100)
回数は0
「1から100までの数を当ててください！」を表示

回数が10より小さい間
    回数は回数と1を足す
    予想は入力ボックス("数当て", "{回数}回目: 数字を入力してください")
    
    もし予想が空ならば
        「ゲームを終了します」を表示
        終了
    
    もし予想が答えと等しいならば
        「正解！{回数}回で当てました！」を表示
        終了
    違えば
        もし予想が答えより大きいならば
            「もっと小さいです」を表示
        違えば
            「もっと大きいです」を表示

「ゲームオーバー。答えは{答え}でした」を表示
```

**英語版:**
```english
# Number guessing game
answer is random_integer(1, 100)
tries is 0
show "Guess a number from 1 to 100!"

while tries is less than 10
    tries is tries plus 1
    guess is input_box("Number Game", "Try {tries}: Enter a number")
    
    if guess is empty
        show "Game ended"
        exit
    
    if guess equals answer
        show "Correct! You got it in {tries} tries!"
        exit
    else
        if guess is greater than answer
            show "Try smaller!"
        else
            show "Try larger!"

show "Game Over. The answer was {answer}"
```

### 📊 データ処理プログラミング例

#### 4. 成績管理プログラム

**日本語版:**
```nadesiko
# 成績管理システム
生徒リストは[
    ["田中", 85, 92, 78],
    ["鈴木", 90, 88, 95],
    ["佐藤", 75, 82, 80],
    ["高橋", 95, 90, 92]
]

●成績処理（生徒データ）
    名前は生徒データ[0]
    国語は生徒データ[1]
    数学は生徒データ[2]
    英語は生徒データ[3]
    
    合計点は国語と数学と英語を足す
    平均点は合計点を3で割る
    
    もし平均点が90以上ならば
        評価は"A"
    違えば
        もし平均点が80以上ならば
            評価は"B"
        違えば
            もし平均点が70以上ならば
                評価は"C"
            違えば
                評価は"D"
    
    「{名前}: 合計{合計点}点、平均{平均点}点、評価{評価}」を表示
    戻値無

「成績一覧」を表示
Iは0
生徒リストの要素数まで反復
    成績処理(生徒リスト[I])
    IはIと1を足す
```

**英語版:**
```english
# Grade management system
student_list is [
    ["Tanaka", 85, 92, 78],
    ["Suzuki", 90, 88, 95],
    ["Sato", 75, 82, 80],
    ["Takahashi", 95, 90, 92]
]

function process_grades(student_data)
    name is student_data[0]
    japanese is student_data[1]
    math is student_data[2]
    english is student_data[3]
    
    total is japanese plus math plus english
    average is total divided by 3
    
    if average is greater than 90
        grade is "A"
    else
        if average is greater than 80
            grade is "B"
        else
            if average is greater than 70
                grade is "C"
            else
                grade is "D"
    
    show "{name}: Total {total}, Average {average}, Grade {grade}"
    return

show "Grade Report"
for student_data in student_list
    process_grades(student_data)
```

### 🖥️ GUIプログラミング例

#### 5. 簡単な電卓アプリ

**日本語版:**
```nadesiko
# 電卓アプリ
ウィンドウ作成("電卓", 300, 200)

# 表示ラベル
表示ラベルはラベル作成("0", 10, 10, 280, 30)

# 数字ボタン
Iは0
9まで反復
    ボタンはボタン作成("{I}", 10 + (I%3)*90, 50 + (I//3)*40, 80, 30)
    IはIと1を足す

# 演算子ボタン
足すボタンはボタン作成("+", 10, 170, 60, 30)
引くボタンはボタン作成("-", 80, 170, 60, 30)
掛けるボタンはボタン作成("*", 150, 170, 60, 30)
割るボタンはボタン作成("/", 220, 170, 60, 30)

イコールボタンはボタン作成("=", 280, 170, 60, 30)

クリアボタンはボタン作成("C", 280, 50, 60, 30)

ウィンドウ表示()
```

**英語版:**
```english
# Calculator app
create_window("Calculator", 300, 200)

# Display label
display_label is create_label("0", 10, 10, 280, 30)

# Number buttons
for i from 0 to 9
    button is create_button("{i}", 10 + (i%3)*90, 50 + (i//3)*40, 80, 30)

# Operator buttons
plus_button is create_button("+", 10, 170, 60, 30)
minus_button is create_button("-", 80, 170, 60, 30)
times_button is create_button("*", 150, 170, 60, 30)
divide_button is create_button("/", 220, 170, 60, 30)

equals_button is create_button("=", 280, 170, 60, 30)

clear_button is create_button("C", 280, 50, 60, 30)

show_window()
```

### 🌐 ネットワークプログラミング例

#### 6. 天気情報取得プログラム

**日本語版:**
```nadesiko
# 天気情報取得
都市は"Tokyo"
API_URLは"https://api.openweathermap.org/data/2.5/weather?q={都市}&appid=YOUR_API_KEY"

# APIからデータ取得
JSONデータはJSON取得(API_URL)
もしJSONデータが"エラー"を含むならば
    「天気情報の取得に失敗しました」を表示
違えば
    天気はJSONデータ["weather"][0]["main"]
    気温はJSONデータ["main"]["temp"]
    湿度はJSONデータ["main"]["humidity"]
    
    「{都市}の天気」を表示
    「天気: {天気}」を表示
    「気温: {気温}°C」を表示
    「湿度: {湿度}%」を表示
```

**英語版:**
```english
# Weather information
city is "Tokyo"
api_url is "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

# Get data from API
json_data is get_json(api_url)
if json_data contains "error"
    show "Failed to get weather information"
else
    weather is json_data["weather"][0]["main"]
    temperature is json_data["main"]["temp"]
    humidity is json_data["main"]["humidity"]
    
    show "Weather in {city}"
    show "Weather: {weather}"
    show "Temperature: {temperature}°C"
    show "Humidity: {humidity}%"
```

### 🗄️ データベースプログラミング例

#### 7. 簡単な住所録プログラム

**日本語版:**
```nadesiko
# 住所録データベース
DB接続はSQLite3接続("address_book.db")

# テーブル作成
テーブル作成(DB接続, "addresses", 
    "id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT")

# データ挿入
挿入(DB接続, "addresses", (1, "田中太郎", "03-1234-5678", "tanaka@example.com", "東京都渋谷区"))
挿入(DB接続, "addresses", (2, "鈴木花子", "03-9876-5432", "suzuki@example.com", "東京都新宿区"))

# データ検索
全データは選択(DB接続, "addresses")

「住所録一覧」を表示
Iは0
全データの要素数まで反復
    データは全データ[I]
    「ID: {データ[0]}」を表示
    「名前: {データ[1]}」を表示
    「電話: {データ[2]}」を表示
    「メール: {データ[3]}」を表示
    「住所: {データ[4]}」を表示
    「---」を表示
    IはIと1を足す

DB接続を閉じる
```

**英語版:**
```english
# Address book database
db_conn is sqlite3_connect("address_book.db")

# Create table
create_table(db_conn, "addresses", 
    "id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT")

# Insert data
insert(db_conn, "addresses", (1, "Taro Tanaka", "03-1234-5678", "tanaka@example.com", "Shibuya, Tokyo"))
insert(db_conn, "addresses", (2, "Hanako Suzuki", "03-9876-5432", "suzuki@example.com", "Shinjuku, Tokyo"))

# Select data
all_data is select(db_conn, "addresses")

show "Address Book"
for data in all_data
    show "ID: {data[0]}"
    show "Name: {data[1]}"
    show "Phone: {data[2]}"
    show "Email: {data[3]}"
    show "Address: {data[4]}"
    show "---"

close_connection(db_conn)
```

### 🤖 機械学習プログラミング例

#### 8. 簡単な回帰分析

**日本語版:**
```nadesiko
# 簡単な回帰分析
# 勉強時間とテストの点数の関係
学習時間は[1, 2, 3, 4, 5, 6, 7, 8]
テスト点数は[60, 65, 70, 75, 80, 85, 90, 95]

# 線形回帰モデルを作成
モデルは線形回帰()

# データを整形
Xは学習時間を二次元配列に変換
Yはテスト点数

# モデルを訓練
モデルを訓練(XとY)

# 予測
予測時間は[9, 10]
予測点数はモデルを予測(予測時間)

「学習時間とテスト点数の関係分析」を表示
Iは0
学習時間の要素数まで反復
    「学習時間{学習時間[I]}時間 → テスト点数{テスト点数[I]}点」を表示
    IはIと1を足す

「予測結果」を表示
Iは0
予測時間の要素数まで反復
    「学習時間{予測時間[I]}時間 → 予測点数{予測点数[I]}点」を表示
    IはIと1を足す
```

**英語版:**
```english
# Simple regression analysis
# Study hours and test scores relationship
study_hours is [1, 2, 3, 4, 5, 6, 7, 8]
test_scores is [60, 65, 70, 75, 80, 85, 90, 95]

# Create linear regression model
model is linear_regression()

# Prepare data
X is convert_to_2d_array(study_hours)
Y is test_scores

# Train model
train_model(model, X, Y)

# Predict
predict_hours is [9, 10]
predicted_scores is predict(model, predict_hours)

show "Study Hours vs Test Scores Analysis"
for i from 0 to length(study_hours)-1
    show "{study_hours[i]} hours → {test_scores[i]} points"

show "Predictions"
for i from 0 to length(predict_hours)-1
    show "{predict_hours[i]} hours → {predicted_scores[i]} points"
```

### 🎨 マルチメディアプログラミング例

#### 9. 簡単な画像処理

**日本語版:**
```nadesiko
# 画像処理プログラム
入力画像は"input.jpg"

# 画像を読み込む
画像は画像読込(入力画像)

# 画像情報を表示
「画像サイズ: {画像.サイズ}」を表示
「画像モード: {画像.モード}」を表示

# 画像をリサイズ
リサイズ画像は画像リサイズ(画像, (300, 300))

# 画像を回転
回転画像は画像回転(リサイズ画像, 90)

# 画像を保存
画像保存(回転画像, "output_rotated.jpg")
画像保存(リサイズ画像, "output_resized.jpg")

「画像処理完了」を表示
「リサイズ画像: output_resized.jpg」を表示
「回転画像: output_rotated.jpg」を表示
```

**英語版:**
```english
# Image processing program
input_image is "input.jpg"

# Load image
image is load_image(input_image)

# Display image information
show "Image size: {image.size}"
show "Image mode: {image.mode}"

# Resize image
resized_image is resize_image(image, (300, 300))

# Rotate image
rotated_image is rotate_image(resized_image, 90)

# Save images
save_image(rotated_image, "output_rotated.jpg")
save_image(resized_image, "output_resized.jpg")

show "Image processing completed"
show "Resized image: output_resized.jpg"
show "Rotated image: output_rotated.jpg"
```

### 🔧 実用ツールプログラミング例

#### 10. ファイル整理ツール

**日本語版:**
```nadesiko
# ファイル整理ツール
対象ディレクトリは"./downloads"

# ファイル一覧を取得
ファイルリストはファイル一覧(対象ディレクトリ)

整理カウントは0
「ファイル整理開始」を表示

Iは0
ファイルリストの要素数まで反復
    ファイル名はファイルリスト[I]
    ファイルパスはパス結合(対象ディレクトリ, ファイル名)
    
    # 拡張子で分類
    拡張子は拡張子(ファイルパス)
    
    もし拡張子が".jpg"か".png"か".gif"ならば
        宛先はパス結合(対象ディレクトリ, "images")
    違えば
        もし拡張子が".pdf"か".doc"か".txt"ならば
            宛先はパス結合(対象ディレクトリ, "documents")
        違えば
            もし拡張子が".mp3"か".wav"か".flac"ならば
                宛先はパス結合(対象ディレクトリ, "music")
            違えば
                宛先はパス結合(対象ディレクトリ, "others")
    
    # 宛先ディレクトリを作成
    ディレクトリ作成(宛先)
    
    # ファイルを移動
    宛先ファイルはパス結合(宛先, ファイル名)
    ファイル移動(ファイルパス, 宛先ファイル)
    
    「{ファイル名} → {宛先}」を表示
    整理カウントは整理カウントと1を足す
    IはIと1を足す

「整理完了: {整理カウント}個のファイルを整理しました」を表示
```

**英語版:**
```english
# File organization tool
target_directory is "./downloads"

# Get file list
file_list is get_file_list(target_directory)

organized_count is 0
show "Starting file organization"

for file_name in file_list
    file_path is join_path(target_directory, file_name)
    
    # Classify by extension
    extension is get_extension(file_path)
    
    if extension is ".jpg" or ".png" or ".gif"
        destination is join_path(target_directory, "images")
    else
        if extension is ".pdf" or ".doc" or ".txt"
            destination is join_path(target_directory, "documents")
        else
            if extension is ".mp3" or ".wav" or ".flac"
                destination is join_path(target_directory, "music")
            else
                destination is join_path(target_directory, "others")
    
    # Create destination directory
    create_directory(destination)
    
    # Move file
    dest_file is join_path(destination, file_name)
    move_file(file_path, dest_file)
    
    show "{file_name} → {destination}"
    organized_count is organized_count plus 1

show "Organization complete: {organized_count} files organized"
```

## 🎯 これらの例からわかること

### 📚 教育分野での活用
- **算数・数学**: 計算、図形、統計、方程式
- **国語**: 文字列処理、文章解析
- **理科**: 実験データ処理、シミュレーション
- **社会**: データ分析、地図情報処理

### 🎮 エンターテイメント分野
- **ゲーム開発**: ロジック、アルゴリズム学習
- **アニメーション**:形描画、動きの制御
- **サウンド**: 音声処理、音楽生成

### 💼 実務分野
- **データ処理**: CSV、JSON、XML処理
- **自動化**: ファイル操作、システム管理
- **分析**: 統計、機械学習、予測

### 🔬 専門分野
- **科学技術**: 数値計算、シミュレーション
- **情報処理**: アルゴリズム、データ構造
- **AI・機械学習**: 基本的な機械学習アルゴリズム

これらのサンプルプログラムにより、なでしこ3互換モジュールでできることが具体的にわかります。教育から実務まで、幅広い用途で活用可能です！
