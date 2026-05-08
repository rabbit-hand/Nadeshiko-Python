"""
なでしこ3互換キーワード定義
助詞区切りの法則に基づいた日本語キーワード
"""

class NadesikoKeywords:
    """なでしこ3のキーワードと対応するPythonコードを管理"""
    
    # 助詞リスト - 単語の区切りに使用
    PARTICLES = ['と', 'を', 'が', 'の', 'に', 'へ', 'で', 'から', 'まで', 'より', 'など']
    
    # 基本命令のマッピング
    BASIC_COMMANDS = {
        # 表示・入力
        '表示': 'print',
        '表示する': 'print',
        '言う': 'print',
        '尋ねる': 'input',
        '入力': 'input',
        
        # 代入
        '代入': '=',
        'は': '=',
        'とは': '=',
        
        # 計算
        '足す': '+',
        '引く': '-',
        '掛ける': '*',
        '割る': '/',
        '割り切れる': '%',
        'べき乗': '**',
        
        # 比較
        '等しい': '==',
        '違う': '!=',
        '大きい': '>',
        '小さい': '<',
        '以上': '>=',
        '以下': '<=',
        
        # 論理
        'かつ': 'and',
        'または': 'or',
        'でない': 'not',
        
        # 制御構文
        'もし': 'if',
        'ならば': ':',
        '違えば': 'else',
        '条件分岐': 'elif',
        '繰り返す': 'for',
        '間': 'while',
        '回': 'range',
        '反復': 'for',
        '続ける': 'continue',
        '抜ける': 'break',
        
        # 関数定義
        '関数': 'def',
        '定義': 'def',
        '返す': 'return',
        '戻る': 'return',
        
        # データ型
        '配列': 'list',
        'リスト': 'list',
        '辞書': 'dict',
        'ハッシュ': 'dict',
        '文字列': 'str',
        '数値': 'int',
        '実数': 'float',
        '真偽値': 'bool',
        
        # システム
        '待つ': 'time.sleep',
        '終了': 'sys.exit',
        '終わる': 'return',
    }
    
    # なでしこ特有の命令 - 完全版
    NADESIKO_COMMANDS = {
        # === 数学関数 ===
        '絶対値': 'abs',
        '平方根': 'math.sqrt',
        '立方根': 'lambda x: x ** (1/3)',
        'サイン': 'math.sin',
        'コサイン': 'math.cos',
        'タンジェント': 'math.tan',
        'アークサイン': 'math.asin',
        'アークコサイン': 'math.acos',
        'アークタンジェント': 'math.atan',
        '双曲線サイン': 'math.sinh',
        '双曲線コサイン': 'math.cosh',
        '双曲線タンジェント': 'math.tanh',
        '対数': 'math.log',
        '常用対数': 'math.log10',
        '自然対数': 'math.log',
        '指数関数': 'math.exp',
        '整数部分': 'int',
        '小数部分': 'lambda x: x - int(x)',
        '四捨五入': 'round',
        '切り上げ': 'math.ceil',
        '切り捨て': 'math.floor',
        '符号': 'lambda x: 1 if x > 0 else -1 if x < 0 else 0',
        '階乗': 'math.factorial',
        '順列': 'lambda n, r: math.factorial(n) // math.factorial(n - r)',
        '組み合わせ': 'math.comb',
        'フィボナッチ': 'lambda n: [0, 1][:n+1] if n <= 1 else sum([0, 1][:n+1])',
        '乱数': 'random.random',
        '整数乱数': 'random.randint',
        '選択': 'random.choice',
        'シャッフル': 'random.shuffle',
        '円周率': 'math.pi',
        '自然対数の底': 'math.e',
        '黄金比': 'lambda: (1 + math.sqrt(5)) / 2',
        
        # === 文字列操作 ===
        '文字数': 'len',
        '長さ': 'len',
        '左から': 'str[:]',
        '右から': 'str[-:]',
        '中から': 'str[:]',
        '置換': 'str.replace',
        '全置換': 'str.replace',
        '正規表現置換': 're.sub',
        '検索': 'str.find',
        '逆検索': 'str.rfind',
        '正規表現検索': 're.search',
        '正規表現全検索': 're.findall',
        '含む': 'in',
        '前から含む': 'str.startswith',
        '後から含む': 'str.endswith',
        '分割': 'str.split',
        '行分割': 'str.splitlines',
        '単語分割': 'str.split',
        '結合': 'str.join',
        '行結合': 'str.join',
        '大文字': 'str.upper',
        '小文字': 'str.lower',
        '先頭大文字': 'str.capitalize',
        '単語先頭大文字': 'str.title',
        '入れ替え': 'str.swapcase',
        '反転': 'str[::-1]',
        'ソート': 'lambda s: \'\'.join(sorted(s))',
        '空白削除': 'str.strip',
        '左空白削除': 'str.lstrip',
        '右空白削除': 'str.rstrip',
        '空白統一': 'lambda s: \' \'.join(s.split())',
        'タブ削除': 'lambda s: s.replace(\'\\t\', \'\')',
        '改行削除': 'lambda s: s.replace(\'\\n\', \'\').replace(\'\\r\', \'\')',
        'ひらがなに変換': 'lambda s: \'\'.join(chr(ord(ch) - 0x60) if \'ァ\' <= ch <= \'ン\' else ch for ch in s)',
        'カタカナに変換': 'lambda s: \'\'.join(chr(ord(ch) + 0x60) if \'ぁ\' <= ch <= \'ん\' else ch for ch in s)',
        '半角に変換': 'lambda s: unicodedata.normalize(\'NFKC\', s)',
        '全角に変換': 'lambda s: unicodedata.normalize(\'NFKC\', s)',
        'URLエンコード': 'urllib.parse.quote',
        'URLデコード': 'urllib.parse.unquote',
        'Base64エンコード': 'lambda s: base64.b64encode(s.encode()).decode()',
        'Base64デコード': 'lambda s: base64.b64decode(s).decode()',
        'MD5ハッシュ': 'lambda s: hashlib.md5(s.encode()).hexdigest()',
        'SHA1ハッシュ': 'lambda s: hashlib.sha1(s.encode()).hexdigest()',
        'SHA256ハッシュ': 'lambda s: hashlib.sha256(s.encode()).hexdigest()',
        
        # === 配列操作 ===
        '要素数': 'len',
        '空': 'lambda a: len(a) == 0',
        '追加': 'append',
        '削除': 'remove',
        '挿入': 'insert',
        'ソート': 'sort',
        '配列反転': 'reverse',
        'コピー': 'copy',
        'スライス': 'lambda a, s, e: a[s:e]',
        '連結': 'lambda a, b: a + b',
        '重複なし': 'lambda a: list(dict.fromkeys(a))',
        'ユニーク': 'lambda a: list(set(a))',
        
        # === 辞書操作 ===
        'キー一覧': 'dict.keys',
        '値一覧': 'dict.values',
        '項目一覧': 'dict.items',
        'キー存在': 'dict.__contains__',
        '値取得': 'dict.get',
        '値設定': 'dict.__setitem__',
        '削除': 'dict.pop',
        '全削除': 'dict.clear',
        'マージ': 'lambda d1, d2: {**d1, **d2}',
        
        # === ファイル操作 ===
        '読む': 'open().read()',
        '書く': 'open().write()',
        '追記': 'open().write',
        '存在する': 'os.path.exists',
        'ファイル作成': 'open().close()',
        '削除': 'os.remove',
        'コピー': 'shutil.copy2',
        '移動': 'shutil.move',
        'ファイルサイズ': 'os.path.getsize',
        '更新日時': 'os.path.getmtime',
        '拡張子': 'os.path.splitext',
        'ファイル名': 'os.path.basename',
        'ディレクトリ名': 'os.path.dirname',
        '絶対パス': 'os.path.abspath',
        '相対パス': 'os.path.relpath',
        'パス結合': 'os.path.join',
        '正規化': 'os.path.normpath',
        '一覧取得': 'os.listdir',
        'ファイル一覧': 'lambda d: [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]',
        'ディレクトリ一覧': 'lambda d: [f for f in os.listdir(d) if os.path.isdir(os.path.join(d, f))]',
        'ディレクトリ作成': 'os.makedirs',
        'ディレクトリ削除': 'shutil.rmtree',
        'ディレクトリ存在': 'os.path.isdir',
        '現在ディレクトリ': 'os.getcwd',
        'ディレクトリ変更': 'os.chdir',
        '一時ファイル': 'tempfile.mkstemp',
        '一時ディレクトリ': 'tempfile.mkdtemp',
        
        # === 日時処理 ===
        '今': 'datetime.datetime.now',
        '今日': 'datetime.date.today',
        '年': 'datetime.datetime.now().year',
        '月': 'datetime.datetime.now().month',
        '日': 'datetime.datetime.now().day',
        '時': 'datetime.datetime.now().hour',
        '分': 'datetime.datetime.now().minute',
        '秒': 'datetime.datetime.now().second',
        '曜日': 'datetime.datetime.now().weekday',
        '書式': 'datetime.datetime.strftime',
        '日時解析': 'datetime.datetime.strptime',
        '日付加算': 'datetime.timedelta',
        'タイムスタンプ': 'datetime.datetime.timestamp',
        'UNIX時刻': 'time.time',
        'スリープ': 'time.sleep',
        
        # === GUI機能 ===
        'ウィンドウ作成': 'tkinter.Tk',
        'メッセージボックス': 'tkinter.messagebox.showinfo',
        '警告ボックス': 'tkinter.messagebox.showwarning',
        'エラーボックス': 'tkinter.messagebox.showerror',
        '確認ボックス': 'tkinter.messagebox.askyesno',
        '入力ボックス': 'tkinter.simpledialog.askstring',
        'ファイル選択': 'tkinter.filedialog.askopenfilename',
        'ファイル保存': 'tkinter.filedialog.asksaveasfilename',
        'ディレクトリ選択': 'tkinter.filedialog.askdirectory',
        'カラーセレクト': 'tkinter.colorchooser.askcolor',
        'ボタン': 'tkinter.Button',
        'ラベル': 'tkinter.Label',
        'エントリー': 'tkinter.Entry',
        'テキスト': 'tkinter.Text',
        'フレーム': 'tkinter.Frame',
        'キャンバス': 'tkinter.Canvas',
        'リストボックス': 'tkinter.Listbox',
        'コンボボックス': 'tkinter.Combobox',
        'チェックボタン': 'tkinter.Checkbutton',
        'ラジオボタン': 'tkinter.Radiobutton',
        'スケール': 'tkinter.Scale',
        'スクロールバー': 'tkinter.Scrollbar',
        'メニュー': 'tkinter.Menu',
        'メニューバー': 'tkinter.MenuBar',
        
        # === ネットワーク機能 ===
        'HTTP取得': 'requests.get',
        'HTTP投稿': 'requests.post',
        'HTTP_PUT': 'requests.put',
        'HTTP_DELETE': 'requests.delete',
        'JSON取得': 'lambda url: requests.get(url).json()',
        'JSON投稿': 'lambda url, data: requests.post(url, json=data).json()',
        'ファイルダウンロード': 'requests.get',
        'URL開く': 'webbrowser.open',
        'メール送信': 'smtplib.SMTP',
        'FTP接続': 'ftplib.FTP',
        'ソケット': 'socket.socket',
        'WebSocket': 'websocket.create_connection',
        
        # === データベース機能 ===
        'SQLite3接続': 'sqlite3.connect',
        'SQL実行': 'sqlite3.Cursor.execute',
        'SQL全実行': 'sqlite3.Cursor.executemany',
        'SQL取得': 'sqlite3.Cursor.fetchall',
        'SQL一行取得': 'sqlite3.Cursor.fetchone',
        'テーブル作成': 'sqlite3.Cursor.execute',
        'インデックス作成': 'sqlite3.Cursor.execute',
        'トランザクション開始': 'sqlite3.Connection.execute',
        'コミット': 'sqlite3.Connection.commit',
        'ロールバック': 'sqlite3.Connection.rollback',
        
        # === システム操作 ===
        '実行': 'os.system',
        'サブプロセス実行': 'subprocess.run',
        'プロセス開始': 'subprocess.Popen',
        '環境変数': 'os.environ',
        'コマンドライン': 'sys.argv',
        'プラットフォーム': 'sys.platform',
        'Pythonバージョン': 'sys.version',
        '終了': 'sys.exit',
        '再起動': 'os.execv',
        'クリップボード': 'pyperclip.copy',
        'マウス操作': 'pyautogui',
        'キーボード操作': 'pyautogui',
        'スクリーンショット': 'pyautogui.screenshot',
        
        # === マルチメディア ===
        '画像読込': 'PIL.Image.open',
        '画像保存': 'PIL.Image.save',
        '画像表示': 'PIL.Image.show',
        '画像リサイズ': 'PIL.Image.resize',
        '画像回転': 'PIL.Image.rotate',
        '音声再生': 'pygame.mixer.music.load',
        '音声停止': 'pygame.mixer.music.stop',
        'ビープ音': 'winsound.Beep',
        '動画再生': 'cv2.VideoCapture',
        
        # === データ処理 ===
        'CSV読込': 'csv.reader',
        'CSV書込': 'csv.writer',
        'JSON読込': 'json.load',
        'JSON書込': 'json.dump',
        'XML解析': 'xml.etree.ElementTree.parse',
        'YAML読込': 'yaml.safe_load',
        'エクセル読込': 'pandas.read_excel',
        'Pandas読込': 'pandas.read_csv',
        
        # === 機械学習 ===
        '線形回帰': 'sklearn.linear_model.LinearRegression',
        '決定木': 'sklearn.tree.DecisionTreeClassifier',
        'SVM': 'sklearn.svm.SVC',
        'KMeans': 'sklearn.cluster.KMeans',
        '主成分分析': 'sklearn.decomposition.PCA',
        'データ分割': 'sklearn.model_selection.train_test_split',
        
        # === その他高度な機能 ===
        'スレッド開始': 'threading.Thread',
        'プロセスプール': 'concurrent.futures.ThreadPoolExecutor',
        '非同期実行': 'asyncio.run',
        '正規表現': 're',
        '暗号化': 'cryptography',
        '圧縮': 'zipfile',
        '解凍': 'zipfile',
        'QRコード生成': 'qrcode',
        'バーコード生成': 'python-barcode',
    }
    
    # 特殊変数
    SPECIAL_VARIABLES = {
        'それ': '_result',  # 直前の計算結果
        'ナ': 'math.pi',    # 円周率
        'エー': 'math.e',    # 自然対数の底
        '空': 'None',       # 空っぽ
        '真': 'True',       # 真
        '偽': 'False',      # 偽
        'ナデシコバージョン': '"3.0.0"',  # なでしこバージョン
        'ナデシコエンジン': '"Python"',   # なでしこエンジン
        'ナデシコ種類': '"Python互換"',   # なでしこ種類
        'はい': 'True',      # はい
        'いいえ': 'False',   # いいえ
        '永遠': 'float("inf")',  # 永遠
        'オン': 'True',      # オン
        'オフ': 'False',     # オフ
        '改行': '"\\n"',     # 改行
        'タブ': '"\\t"',     # タブ
        'カッコ': '"("',     # カッコ
        'カッコ閉': '")"',   # カッコ閉
        '波カッコ': '"{"',   # 波カッコ
        '波カッコ閉': '"}"', # 波カッコ閉
        'OK': '"OK"',        # OK
        'NG': '"NG"',        # NG
        'キャンセル': '"CANCEL"',  # キャンセル
        'TRUE': 'True',      # TRUE
        'FALSE': 'False',    # FALSE
        'true': 'True',      # true
        'false': 'False',    # false
        'PI': 'math.pi',     # PI
        'NULL': 'None',      # NULL
        'undefined': 'None', # undefined
        '未定義': 'None',    # 未定義
        'エラーメッセージ': '""',  # エラーメッセージ
        '対象': 'None',      # 対象
        '対象キー': 'None',  # 対象キー
        '回数': 'None',      # 回数
        'CR': '"\\r"',       # CR
        'LF': '"\\n"',       # LF
        '非数': 'float("nan")',  # 非数
        '無限大': 'float("inf")',  # 無限大
        '戻値無': 'None',    # 戻値無
        '戻値有': 'True',    # 戻値有
        '空配列': '[]',      # 空配列
        '空辞書': '{}',      # 空辞書
        '空ハッシュ': '{}',  # 空ハッシュ
        '空オブジェクト': '{}',  # 空オブジェクト
    }
    
    @classmethod
    def is_particle(cls, word):
        """単語が助詞かどうかを判定"""
        return word in cls.PARTICLES
    
    @classmethod
    def translate_command(cls, command):
        """なでしこ命令をPython命令に変換"""
        return cls.BASIC_COMMANDS.get(command, command)
    
    @classmethod
    def translate_nadesiko_command(cls, command):
        """なでしこ特有命令をPythonに変換"""
        return cls.NADESIKO_COMMANDS.get(command, command)
    
    @classmethod
    def translate_variable(cls, var):
        """特殊変数をPython変数に変換"""
        return cls.SPECIAL_VARIABLES.get(var, var)
    
    @classmethod
    def split_by_particles(cls, text):
        """助詞でテキストを分割"""
        words = []
        current = ""
        
        for char in text:
            current += char
            # 助詞で分割
            if cls.is_particle(current.strip()):
                if words:
                    words[-1] += current
                else:
                    words.append(current)
                current = ""
            # 句読点でも分割
            elif char in ['、', '。', '，', '．']:
                if current.strip():
                    words.append(current.strip())
                current = ""
        
        if current.strip():
            words.append(current.strip())
        
        return words
