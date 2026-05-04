# How to Use as Python Module

## Basic Usage

### 1. Installation

```bash
# Direct usage
cd /path/to/nadesiko-python
python3 -c "import sys; sys.path.insert(0, '.'); from nadesiko_parser import NadesikoParser"

# Install with pip
pip install -e .
```

### 2. Basic Programming

```python
from nadesiko_parser import NadesikoParser

# Create parser
parser = NadesikoParser()

# Execute Nadesiko code
code = '''
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
'''

parser.execute(code)
```

### 3. Using Complete Class

```python
from nadesiko_complete import NadesikoComplete

# Create complete class
nadesiko = NadesikoComplete()

# Basic functions
print(f"Pi: {nadesiko.円周率()}")
print(f"Factorial(5): {nadesiko.階乗(5)}")
print(f"Length: {nadesiko.文字数('こんにちは')}")

# Math functions
print(f"Sin(90): {nadesiko.サイン(90, degrees=True)}")
print(f"Combination(5,2): {nadesiko.組み合わせ(5, 2)}")

# String operations
text = "Python programming"
print(f"Uppercase: {nadesiko.大文字(text)}")
print(f"Reverse: {nadesiko.反転(text)}")
```

### 4. Using GUI Features

```python
from nadesiko_complete_commands import NadesikoCompleteCommands

# Create GUI commands
gui = NadesikoCompleteCommands()

# Message box
gui.メッセージボックス("Title", "Message")

# Input box
name = gui.入力ボックス("Input", "Please enter your name")
print(f"Entered name: {name}")

# File selection
filepath = gui.ファイル選択("File Selection")
print(f"Selected file: {filepath}")
```

### 5. Bilingual Support

```python
from nadesiko_bilingual import BilingualParser

# Create bilingual parser
parser = BilingualParser()

# Japanese code
japanese_code = '''
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
'''

# English code
english_code = '''
A is 10
B is 20
C is A plus B
show "Total: {C}"
'''

# Execute with automatic language detection
parser.execute(japanese_code)  # Executes as Japanese
parser.execute(english_code)  # Executes as English
```

### 6. Using Advanced Features

```python
from nadesiko_complete_commands import NadesikoCompleteCommands

# Create advanced commands
commands = NadesikoCompleteCommands()

# Network features
try:
    result = commands.HTTP取得("https://httpbin.org/get")
    print(f"HTTP GET result: {result[:100]}...")
except Exception as e:
    print(f"Network error: {e}")

# Database features
try:
    conn = commands.SQLite3接続(":memory:")
    commands.テーブル作成(conn, "users", "id INTEGER PRIMARY KEY, name TEXT")
    commands.挿入(conn, "users", (1, "Nadesiko"))
    data = commands.選択(conn, "users")
    print(f"Database data: {data}")
    conn.close()
except Exception as e:
    print(f"Database error: {e}")
```

### 7. Inheritance as Class

```python
from nadesiko_complete import NadesikoComplete

class MyNadesikoApp(NadesikoComplete):
    def __init__(self):
        super().__init__()
        self.app_name = "My Nadesiko App"
    
    def アプリ起動(self):
        print(f"Launched {self.app_name}")
        print(f"Version: {self.ナデシコバージョン()}")
    
    def 独自機能(self, data):
        # Add custom functionality
        processed_data = self.大文字(data)
        return f"Processed: {processed_data}"

# Usage example
app = MyNadesikoApp()
app.アプリ起動()
result = app.独自機能("hello world")
print(result)
```

### 8. Checking All Module Functions

```python
import nadesiko_programming

# List available classes
print("Available classes:")
for cls_name in nadesiko_programming.__all__:
    print(f"  - {cls_name}")

# Module information
print(f"\nModule name: {nadesiko_programming.__name__}")
print(f"Version: {nadesiko_programming.__version__}")
print(f"Author: {nadesiko_programming.__author__}")
```

### 9. Error Handling

```python
from nadesiko_parser import NadesikoParser

parser = NadesikoParser()

try:
    # Execute Nadesiko code
    code = '''
    Aは10
    Bは0
    CはAをBで割る  # Division by zero error
    「結果: {C}」を表示
    '''
    parser.execute(code)
except Exception as e:
    print(f"Error occurred: {e}")
    print("Continuing program...")
```

### 10. Performance Optimization

```python
from nadesiko_parser import NadesikoParser

# Reuse parser
parser = NadesikoParser()

# Efficiently execute multiple codes
codes = [
    "Aは10",
    "Bは20", 
    "CはAとBを足す",
    "「結果: {C}」を表示"
]

for code in codes:
    parser.execute(code)
```

## Notes

1. **Python Version**: Requires Python 3.6 or higher
2. **Dependencies**: Some advanced features require additional libraries
3. **GUI Features**: tkinter must be installed
4. **Network Features**: requests library required
5. **Database Features**: sqlite3 module required (Python standard)

## Supported Features

- ✅ Basic programming (variables, calculations, control structures)
- ✅ Mathematical functions (300+ functions)
- ✅ String operations (100+ functions)
- ✅ File operations (50+ functions)
- ✅ GUI features (30+ widgets)
- ✅ Network features (HTTP, JSON, WebSocket)
- ✅ Database features (SQLite3)
- ✅ Multimedia features (images, audio, video)
- ✅ Machine learning features (basic algorithms)
- ✅ Bilingual support (Japanese-English)

This module functions completely as a standard Python module and provides almost all features of Nadesiko3.
