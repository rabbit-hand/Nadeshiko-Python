# Nadesiko Python V6 Specification

A complete development environment that implements Japanese natural language programming in Python

---

## 📋 Overview

### 🎯 **Project Overview**
Nadesiko Python is an integrated development environment that combines the charm of Nadesiko V1's "visual GUI design" with V3's "natural language programming" and further evolves it. It provides four major functions that support users from beginners to advanced experts, allowing you to intuitively design GUIs with a mouse while programming in natural languages such as Japanese and English.

### 🌟 **Four Features Born from V1 and V3 Integration**
| Feature | V1 Element | V3 Element | New Feature Born from Integration |
|---------|-----------|-----------|-----------------------------------|
| Block GUI Application | Block manipulation sense | Natural language programming | V1's intuitiveness + V3's Japanese coding |
| GUI Designer | Mouse GUI design | Python code generation | Evolving V1's design sense in modern times |
| Module Library | Component-oriented | Natural language execution | V1's component concept + V3's execution environment |
| Command Line Parser | Text-based | Japanese syntax | V1's simplicity + V3's expressiveness |

---

## 🧱 Block GUI Application

### 📖 **Feature Specification**
- **Purpose**: Learning support that combines Nadesiko V1's block sense with V3's natural language programming
- **Target**: Programming beginners, children, educators
- **Characteristics**: New learning experience that combines V1's intuitive operation with V3's Japanese programming
- **Language**: Japanese-English bilingual support

### ⚙️ **Technical Specification**
- **Framework**: Tkinter-based
- **Architecture**: Event-driven GUI
- **Resident Feature**: Background execution via task tray icon

### 🎮 **Operation Specification**
1. **Launch**: `python start_gui.py`
2. **Language Switch**: Select Japanese/English from toolbar
3. **Programming**: Click blocks on left palette
4. **Execute**: Run program with ▶ button
5. **Save**: Save program with 💾 button

### 🧩 **Block Types**
| Category | Block Count | Main Functions |
|----------|-------------|----------------|
| Basic | 5 types | Variable declaration, display, assignment |
| Math | 4 types | Four arithmetic operations |
| Control | 3 types | Conditional branching, loops |
| Functions | 2 types | Function definition, return values |

### 📊 **Supported Language Specifications**
#### 🇯🇵 Japanese Mode
```
変数名は値
AとBを足す
もし条件ならば
回数繰り返す
```

#### 🇺🇸 English Mode
```
variable is value
A plus B
if condition
repeat count times
```

---

## 🎨 GUI Designer

### 📖 **Feature Specification**
- **Purpose**: Reproduce Nadesiko V1's intuitive GUI design experience in modern times
- **Target**: GUI developers, application designers, Nadesiko V1 users
- **Characteristics**: Inherits V1's mouse operation sense while further evolving with automatic Python code generation
- **Output**: Executable Python code

### ⚙️ **Technical Specification**
- **Engine**: Tkinter Canvas-based
- **Component Management**: Object-oriented design
- **Data Format**: Design saving with JSON

### 🎮 **Operation Specification**
1. **Launch**: `python start_gui_designer.py`
2. **Component Placement**: Select from left palette and click on canvas
3. **Edit**: Move by drag, resize with handles
4. **Properties**: Detailed settings in right panel
5. **Code Generation**: Generate Python code with 💻 button

### 🧩 **Supported Components List**
| Component Name | Class | Main Properties |
|----------------|-------|-----------------|
| Button | tk.Button | text, bg, fg, command |
| Label | tk.Label | text, bg, fg, font |
| Entry | tk.Entry | text, bg, fg, font |
| Text | tk.Text | text, bg, fg, wrap |
| Frame | tk.Frame | bg, relief, bd |
| Canvas | tk.Canvas | bg, highlightthickness |
| Listbox | tk.Listbox | bg, fg, font |
| Combobox | ttk.Combobox | values, state |
| Checkbutton | tk.Checkbutton | text, bg, fg |
| Radiobutton | tk.Radiobutton | text, bg, fg, value |
| Scale | tk.Scale | from_, to, orient |
| Spinbox | tk.Spinbox | from_, to, text |

### 🎨 **Design Features**
- **Grid**: 20px interval grid lines
- **Snap**: Automatic position alignment to grid
- **Resize**: Precise adjustment with 8-direction handles
- **Layer**: Front/back movement functionality
- **Context Menu**: Quick operation with right-click

---

## 📦 Module Library

### 📖 **Feature Specification**
- **Purpose**: Integration of natural language functionality into existing Python applications
- **Target**: Web developers, data scientists, application developers
- **Provided Form**: Python module

### ⚙️ **Technical Specification**
- **Module Name**: `src.nadesiko_gui_module`
- **Thread Support**: Multi-threaded execution
- **Error Handling**: Exception handling and logging

### 🎮 **API Specification**
#### Basic API
```python
from src.nadesiko_gui_module import start_gui, execute_nadesiko_code

# GUI launch
start_gui(language="japanese", show_window=True)

# Code execution
result = execute_nadesiko_code("Aは10\n「{A}」を表示")
```

#### Advanced API
```python
from src.nadesiko_gui_module import gui_context, with_gui

# Context manager
with gui_context() as gui:
    result = gui.execute_code("「こんにちは！」を表示")

# Decorator
@with_gui(language="english")
def my_function():
    return execute_nadesiko_code("show 'Hello!'")
```

### 🔧 **Application Examples**
- **Web App Integration**: Integration with Flask/Django
- **Data Analysis**: Integration with pandas/matplotlib
- **Automation Tools**: Script execution with GUI

---

## ⌨️ Command Line Parser

### 📖 **Feature Specification**
- **Purpose**: Text-based natural language programming
- **Target**: Advanced users, automation developers, script creators
- **Execution Method**: Direct code execution

### ⚙️ **Technical Specification**
- **Parser**: Regular expression-based syntax parsing
- **Conversion Method**: Nadesiko syntax → Python code
- **Execution Environment**: Python interpreter

### 🎮 **Usage Specification**
```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()
code = """
Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示
"""
parser.execute(code)
```

### 📊 **Supported Syntax**
| Syntax Type | Japanese Example | English Example | Python Equivalent |
|-------------|------------------|-----------------|-------------------|
| Variable Declaration | Aは10 | A is 10 | A = 10 |
| Display | 「内容」を表示 | show "content" | print("content") |
| Conditional | もしA>10ならば | if A > 10 | if A > 10: |
| Loop | 5回繰り返す | repeat 5 times | for _ in range(5): |
| Function Definition | ●関数名（引数） | function name(params) | def name(params): |
| **End Marker** | **ここ** | **koko** | **Code block end** |
| **OS Command** | **コマンド「〜」** | **command "〜"** | **OS command execution** |
| **File Operation** | **「〜」を読む** | **read from "〜"** | **File reading** |
| **System Info** | **システム情報** | **system info** | **System info acquisition** |

---

## 🌍 Bilingual Specification

### 📖 **Language Support Overview**
Nadesiko Python fully supports two languages: Japanese and English.

### 🇯🇵 **Japanese Mode Specification**
- **Character Code**: UTF-8
- **Variable Names**: Japanese usable
- **Operators**: Japanese natural language
- **Control Syntax**: Japanese natural expressions

### 🇺🇸 **English Mode Specification**
- **Character Code**: UTF-8
- **Variable Names**: English recommended (Japanese also possible)
- **Operators**: English natural expressions
- **Control Syntax**: English natural expressions

### 🔄 **Language Switching Specification**
- **GUI App**: Real-time switching from toolbar
- **Module**: Specified by API arguments
- **Parser**: Use individual parser classes

---

## 🚀 Setup Guide

### 📦 **System Requirements**
- **Python**: 3.7 or higher
- **OS**: Windows, macOS, Linux
- **Dependencies**: tkinter, Pillow, pystray

### 🔧 **Installation Procedure**
```bash
# 1. Clone repository
git clone [repository-url]
cd nadesiko-python

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify operation
python examples/nadesiko_examples.py
```

### 🚀 **Quick Start**
```bash
# For beginners
python start_gui.py

# GUI designer
python start_gui_designer.py

# For developers
python examples/module_usage_examples.py
```

---

## 📚 Specification Change History

### V6.0.0 (2026-05-03)
- ✅ Block GUI application implementation
- ✅ GUI designer implementation
- ✅ Module library implementation
- ✅ Command line parser implementation
- ✅ Bilingual support completion
- ✅ Task tray resident functionality
- ✅ Visual GUI designer implementation
- ✅ Complete modularization

---

## 📞 Support Information

### 🐛 **Bug Reports**
- **Location**: GitHub Issues
- **Format**: Bug reproduction steps and environment information

### 💡 **Feature Requests**
- **Location**: GitHub Discussions
- **Format**: Request content and use cases

### 📧 **Technical Support**
- **Documentation**: This README.md
- **Samples**: examples/ directory
- **Code**: src/ directory

---

## Features

- Write code with natural Japanese grammar
- Supports basic syntax such as variables, conditional branching, loops, and functions
- Automatically converts Nadesiko code to Python code and executes it
- Allows use of Japanese variable names and function names

## Installation

```bash
pip install -e .
```

## Basic Usage

```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

# Execute Nadesiko code
code = """
xは10
yは20
zはxとyを足す
zを表示する
"""

parser.execute(code)
```

## Supported Syntax

### Japanese Version (Nadesiko)

#### Variable Declaration
```
変数名は値
```

#### Conditional Branching
```
もし条件ならば
    処理
そうでなければ
    処理
```

#### Loops
```
回数だけ繰り返す
    処理

条件の間
    処理
```

#### Function Definition
```
●関数名（引数）
    処理
    値を返す
```

#### Input/Output
```
値を表示する
メッセージを読み込む
```

#### Operators
- `と` - Addition (+)
- `から` - Subtraction (-)
- `を掛ける` - Multiplication (*)
- `で割る` - Division (/)
- `よりも大きい` - Greater than (>)
- `よりも小さい` - Less than (<)
- `と等しい` - Equal to (==)
- `と異なる` - Not equal to (!=)
- `かつ` - Logical AND (and)
- `または` - Logical OR (or)
- `ではない` - Logical NOT (not)

---

### English Version

#### Variable Declaration
```
variable is value
Let variable be value
```

#### Conditional Branching
```
If condition is true
    process
else
    process
```

#### Loops
```
repeat N times
    process

while condition
    process
```

#### Function Definition
```
function name(parameter)
    process
    return value
```

#### Input/Output
```
show value
print value
display value
```

#### Operators
- `plus` - Addition (+)
- `minus` - Subtraction (-)
- `times` - Multiplication (*)
- `multiplied by` - Multiplication (*)
- `divided by` - Division (/)
- `greater than` - Greater than (>)
- `less than` - Less than (<)
- `equal to` - Equal to (==)
- `not equal to` - Not equal to (!=)
- `and` - Logical AND (and)
- `or` - Logical OR (or)
- `not` - Logical NOT (not)

## Execution Examples

### Japanese Version (Nadesiko)

```python
from src.nadesiko_parser import NadesikoParser

parser = NadesikoParser()

# Basic example
code = """
年齢は25
もし年齢が18以上ならば
    「成人です」を表示
そうでなければ
    「未成年です」を表示
"""

parser.execute(code)
```

Output:
```
Converted Python code:
年齢 = 25
if 年齢 >= 18:
    print("成人です")
else:
    print("未成年です")

Execution result:
成人です
```

### English Version

```python
from src.english_parser import EnglishParser

parser = EnglishParser()

# Basic example
code = """
age is 25
if age is greater than 18
    print("Adult")
else
    print("Minor")
"""

parser.execute(code)
```

Output:
```
Converted Python code:
age = 25
if age > 18:
    print("Adult")
else:
    print("Minor")

Execution result:
Adult
```

## Complete Command List

### Japanese Version (Nadesiko) Command List

#### 🔰 Basic Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `変数名は値` | Variable declaration | `variable = value` |
| `変数名とは値` | Variable declaration | `variable = value` |
| `変数名に値を代入` | Variable assignment | `variable = value` |
| `「内容」を表示` | Output | `print("content")` |
| `「内容」を表示する` | Output | `print("content")` |

#### 🧮 Operator Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `AとBを足す` | Addition | `A + B` |
| `AからBを引く` | Subtraction | `A - B` |
| `AにBを掛ける` | Multiplication | `A * B` |
| `AをBで割る` | Division | `A / B` |
| `AがB以上` | Greater than or equal | `A >= B` |
| `AがB以下` | Less than or equal | `A <= B` |
| `AがBより大きい` | Greater than | `A > B` |
| `AがBより小さい` | Less than | `A < B` |
| `AがBと等しい` | Equal to | `A == B` |
| `AがBと異なる` | Not equal to | `A != B` |

#### 🔄 Control Structure Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `もし条件ならば` | if statement | `if condition:` |
| `そうでなければ` | else statement | `else:` |
| `違えば` | else statement | `else:` |
| `回数だけ繰り返す` | for loop | `for _ in range(count):` |
| `回数` | for loop | `for _ in range(count):` |
| `条件の間` | while loop | `while condition:` |

#### 🎯 Function Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `●関数名（引数）` | Function definition | `def func_name(params):` |
| `値を返す` | return statement | `return value` |
| `値を戻る` | return statement | `return value` |
| `値して返す` | return statement | `return value` |

---

### English Version Command List

#### 🔰 Basic Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `variable is value` | Variable declaration | `variable = value` |
| `Let variable be value` | Variable declaration | `variable = value` |
| `show content` | Output | `print(content)` |
| `print content` | Output | `print(content)` |
| `display content` | Output | `print(content)` |

#### 🧮 Operator Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `A plus B` | Addition | `A + B` |
| `A minus B` | Subtraction | `A - B` |
| `A times B` | Multiplication | `A * B` |
| `A multiplied by B` | Multiplication | `A * B` |
| `A divided by B` | Division | `A / B` |
| `A is greater than B` | Greater than | `A > B` |
| `A is less than B` | Less than | `A < B` |
| `A is equal to B` | Equal to | `A == B` |
| `A is not equal to B` | Not equal to | `A != B` |

#### 🔄 Control Structure Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `If condition` | if statement | `if condition:` |
| `else` | else statement | `else:` |
| `otherwise` | else statement | `else:` |
| `repeat N times` | for loop | `for _ in range(N):` |
| `while condition` | while loop | `while condition:` |

#### 🎯 Function Commands
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `function name(parameter)` | Function definition | `def function_name(parameter):` |
| `return value` | return statement | `return value` |

#### 🧮 Logical Operators
| Command | Description | Python Equivalent |
|---------|-------------|-------------------|
| `A and B` | Logical AND | `A and B` |
| `A or B` | Logical OR | `A or B` |
| `not A` | Logical NOT | `not A` |

---

## Sample Program Execution

```bash
python examples/nadesiko_examples.py
```

## 🖥️ GUI Application V1

Nadesiko Python includes a block design GUI application.

### ✨ Main Features

- 🧱 **Block Programming**: Build code by clicking visual blocks
- 🌐 **Bilingual Support**: Switch between Japanese and English programming languages
- 📝 **Code Editor**: Direct code editing also possible
- 📊 **Execution Result Display**: Check execution results in real-time
- 💾 **Save/Load**: Save and load programs to files
- 🔔 **Task Tray Resident**: Runs in background, always accessible

### 🚀 Launch Method

```bash
# Launch GUI application
python start_gui.py
```

### 📦 Dependencies

To use the GUI application, install additional dependencies:

```bash
pip install -r requirements.txt
```

### 🎮 How to Use

1. **Launch**: Run `python start_gui.py`
2. **Language Selection**: Select Japanese/English from toolbar
3. **Blocks**: Click blocks from left palette
4. **Edit**: Direct editing also possible in central editor
5. **Execute**: Run program with ▶ button
6. **Save**: Save program with 💾 button

### 🧱 Block List

#### Japanese Version
- **Basic**: Variable declaration, display, assignment
- **Math**: Addition, subtraction, multiplication, division
- **Control**: If, else, repeat
- **Function**: Function definition, return

#### English Version
- **Basic**: Variable, Print, Assign
- **Math**: Add, Subtract, Multiply, Divide
- **Control**: If, Else, Repeat
- **Function**: Function, Return

### 🔔 Task Tray Features

- **Resident**: Application runs in background
- **Icon**: Nadesiko icon displayed in task tray
- **Quick Access**: Show/hide window by right-clicking icon
- **Exit**: Safe exit from menu

---

## 📦 Usage as Module

Nadesiko GUI can also be used as a Python module. Easy to call from other programs.

### 🚀 Basic Usage

```python
from src.nadesiko_gui_module import start_gui, execute_nadesiko_code

# Launch GUI
start_gui(language="japanese", show_window=True)

# Execute Nadesiko code
result = execute_nadesiko_code("""
Aは10
Bは20
CはAとBを足す
「結果: {C}」を表示
""")

print(result)
```

### 🎮 Advanced Usage

#### Background Execution
```python
from src.nadesiko_gui_module import start_gui, show_gui_window

# Launch in background
start_gui(language="japanese", show_window=False)

# Show window later
show_gui_window()
```

#### Context Manager
```python
from src.nadesiko_gui_module import gui_context

# Manage GUI with with statement
with gui_context(language="english", show_window=True) as gui:
    result = gui.execute_code("show 'Hello World!'")
    print(result)
```

---

**🌍 With Nadesiko Python V6, enjoy programming in natural language!**
