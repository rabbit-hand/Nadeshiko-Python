# Japanese-English Bilingual Programming Language

A programming language module that supports both Japanese natural language compatible with Nadesiko3 and natural English that American children can understand.

## Features

- **🇯🇵🇺🇸 Bilingual Support**: Programming possible in both Japanese and English
- **🎯 Child-Friendly**: Learn programming with natural language expressions
- **🔄 Automatic Language Detection**: Automatically determines language from code
- **📚 Nadesiko3 Compatible**: Fully compatible with Nadesiko3 grammar for Japanese
- **🚀 Beginner-Friendly**: Easy to start even for Python beginners

## Installation

```bash
cd nadesiko-python
pip install -e .
```

## Basic Usage

### Bilingual Automatic Detection

```python
from nadesiko_bilingual import BilingualParser

parser = BilingualParser()

# Japanese code
japanese_code = """
Aは10
Bは20
CはAとBを足す
「合計: {C}」を表示
"""

# English code
english_code = """
A is 10
B is 20
C is A plus B
show "Total: {C}"
"""

# Automatically detects language and executes
parser.execute(japanese_code)  # Executes as Japanese
parser.execute(english_code)  # Executes as English
```

### Language Mode Specification

```python
# Japanese mode
parser.set_language_mode('japanese')
parser.execute(japanese_code)

# English mode
parser.set_language_mode('english')
parser.execute(english_code)

# Auto detection mode (default)
parser.set_language_mode('auto')
```

## Supported Grammar

### Japanese Grammar (Nadesiko3 Compatible)

```nadesiko
# Variable assignment
Aは10
Bは20

# Calculations
CはAとBを足す      # C = A + B
DはAからBを引く    # D = A - B
EはAにBを掛ける    # E = A * B
FはAをBで割る      # F = A / B

# Display
「こんにちは」を表示
Aを表示する

# Conditional branching
もしAが10以上ならば
    「大きいです」を表示
違えば
    「小さいです」を表示

# Loops
5回繰り返す
    「こんにちは」を表示

# Function definition
●足し算（AとB）
    AとBを足して返す
```

### English Grammar (Child-Friendly)

```english
# Variable assignment
A is 10
B is 20
Let C be 30

# Calculations
C is A plus B          # C = A + B
D is A minus B         # D = A - B
E is A times B         # E = A * B
F is A divided by B    # F = A / B

# Display
show "Hello"
print "World"
display A

# Conditional branching
if A is greater than 10
    show "Big"
else
    show "Small"

# Loops
repeat 5 times
    show "Hello"

# Function definition
function add_numbers(x and y)
    return x plus y
```

## Language Comparison

| Japanese | English | Python |
|----------|---------|---------|
| Aは10 | A is 10 | A = 10 |
| AとBを足す | A plus B | A + B |
| 「こんにちは」を表示 | show "Hello" | print("Hello") |
| もしAが10以上ならば | if A is greater than 10 | if A >= 10 |
| 5回繰り返す | repeat 5 times | for _ in range(5) |
| ●関数名（引数） | function name(x and y) | def name(x, y) |

## Advanced Examples

### BMI Calculation (Japanese)

```nadesiko
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
```

### BMI Calculation (English)

```english
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
```

## Educational Features

### Simple Examples for Children

```english
# Fruit counting
apple is 5
banana is 3
total is apple plus banana
show "I have {total} fruits"

# Simple game
repeat 3 times
    show "Learning is fun!"

# Learning conditional branching
age is 12
if age is greater than or equal to 13
    show "You are a teenager"
else
    show "You are a kid"
```

### Mathematics Learning

```english
# Basic operations
a is 10
b is 3
show "Addition: {a} plus {b} is {a plus b}"
show "Multiplication: {a} times {b} is {a times b}"
show "Division: {a} divided by {b} is {a divided by b}"

# Simple shape areas
function rectangle_area(width and height)
    return width times height

area is rectangle_area(5 and 4)
show "Rectangle area: {area}"
```

## Game-Style Programming

```english
# Simple adventure game
player_name is "Hero"
player_health is 100
enemy_health is 50

show "Welcome {player_name}!"
show "Player Health: {player_health}"
show "Enemy Health: {enemy_health}"

while player_health is greater than 0 and enemy_health is greater than 0
    # Player attack
    damage is 10 plus random 5
    enemy_health is enemy_health minus damage
    show "Player deals {damage} damage!"
    
    if enemy_health is less than or equal to 0
        show "You win!"
        break
    
    # Enemy attack
    damage is 5 plus random 3
    player_health is player_health minus damage
    show "Enemy deals {damage} damage!"
    
    if player_health is less than or equal to 0
        show "Game Over!"
        break
    
    wait 1 second

if player_health is greater than 0
    show "Victory! {player_name} wins!"
else
    show "Defeat! Try again."
```

## Execution Examples

```bash
# Bilingual execution
python3 -c "
from nadesiko_bilingual import BilingualParser
parser = BilingualParser()
code = '''
A is 10
B is 20
C is A plus B
show \"Result: {C}\"
'''
parser.execute(code)
"
```

Output:
```
Detected language: English
Converted Python code:
A = 10
B = 20
C = A + B
print("Result: {C}")

Execution result:
Result: 30
```

## What You Can Do / Cannot Do

### ✅ What You Can Do

#### Basic Programming Features
- **Two-Language Support**: Programming possible in both Japanese and English
- **Automatic Language Detection**: Automatically determines used language from code
- **Variable Operations**: Variable declaration, assignment, reference in both languages
- **Calculation Processing**: Four arithmetic operations, exponentiation, remainder calculation
- **Control Structures**: if statements, for loops, while loops
- **Function Definitions**: Creation and calling of user-defined functions
- **Input/Output**: Console output, keyboard input

#### Advanced Features
- **Mathematical Functions**: Trigonometric functions, logarithms, random numbers, statistical calculations
- **String Operations**: Search, replace, split, join, encoding
- **File Operations**: Read/write, directory operations, path processing
- **GUI Programming**: Windows, buttons, text boxes, canvas
- **Date/Time Processing**: Current time acquisition, formatting, calculations

#### Bilingual-Specific Features
- **Mixed Code**: Can mix Japanese and English within one program
- **Inter-Language Translation**: Simple code conversion functionality
- **Educational Design**: Programming learning support in both languages
- **International Support**: Global programming education support

#### Educational Features
- **Beginner-Friendly**: Can start without Python knowledge
- **Visual Learning**: Intuitively understandable with natural language
- **Step-by-Step Learning**: From simple code to complex programs
- **Bilingual Education**: Learn English and programming simultaneously

### ❌ What You Cannot Do (Limitations)

#### Performance Related
- **High-Speed Processing**: Slower than native Python due to interpreter method
- **Large-Scale Data**: Not suitable for processing large amounts of data
- **Real-Time Processing**: Not suitable for high-frequency real-time processing

#### Advanced Features
- **Machine Learning**: Cannot directly use advanced libraries like scikit-learn
- **Web Development**: Not compatible with web frameworks like Flask/Django
- **Database**: Not compatible with direct SQL database operations
- **Network**: Not compatible with advanced network processing other than HTTP communication

#### Language Related
- **Complete Automatic Translation**: Limited advanced grammar conversion
- **Dialect Support**: Only supports standard Japanese and English
- **Complex Expressions**: Limited literary expressions and technical terms

#### System Level
- **OS Operations**: Limited direct execution of system calls
- **Hardware Control**: Cannot directly control hardware
- **Multithreading**: Not compatible with advanced parallel processing

#### Compatibility
- **Python 2**: Only supports Python 3
- **External Libraries**: Limited integration with specific external libraries
- **Existing Python Code**: Cannot directly execute existing Python code

## Extension Features

### Checking Supported Keywords

```python
from nadesiko_bilingual import BilingualParser

parser = BilingualParser()
keywords = parser.get_supported_keywords()

print("Japanese keywords:", keywords['japanese'])
print("English keywords:", keywords['english'])
```

### Code Translation

```python
# Convert Japanese code to English
japanese_code = "Aは10"
english_code = parser.translate_code(japanese_code, 'english')

# Convert English code to Japanese
english_code = "A is 10"
japanese_code = parser.translate_code(english_code, 'japanese')
```

## Educational Use

### Elementary School Programming Education

- **Logical Thinking**: Learn algorithms with natural language
- **Mathematical Thinking**: Understand calculation and shape concepts through programming
- **Problem-Solving Skills**: Develop creative thinking through game creation

### Middle and High School

- **English Learning**: Improve language skills while programming in English
- **Mathematical Applications**: Practical learning of functions, variables, algorithms
- **Career Education**: Develop foundational computational thinking

## License

MIT License

## Contributing

Bug reports, feature requests, and new language additions are welcome.

---

**🌍 With the Japanese-English Bilingual Programming Language, children around the world can enjoy learning programming!**
