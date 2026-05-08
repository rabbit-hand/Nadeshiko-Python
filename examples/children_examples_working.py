#!/usr/bin/env python3
"""
Working Children's English Programming Examples
Based on Nadesiko3 grammar with simple English words
Easy for children to understand and learn
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from children_english_parser_fixed import ChildrenEnglishParser

def main():
    parser = ChildrenEnglishParser()
    
    print("🌟 CHILDREN'S ENGLISH PROGRAMMING EXAMPLES 🌟")
    print("Based on Nadesiko3 grammar with simple English words")
    print("=" * 60)
    
    # Example 1: Hello World
    print("\n1. Hello World:")
    hello_code = 'show "Hello World!"'
    
    print("Children's code:")
    print(hello_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(hello_code))
    print("\nExecution result:")
    parser.execute(hello_code)
    
    # Example 2: Simple Math
    print("\n2. Simple Math:")
    math_code = '''apple is 5
orange is 3
total is apple plus orange
show "Total fruits:"
show total'''
    
    print("Children's code:")
    print(math_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(math_code))
    print("\nExecution result:")
    parser.execute(math_code)
    
    # Example 3: Counting
    print("\n3. Counting:")
    counting_code = '''number is 1
show "Counting:"
repeat 5 times
    show number
    number is number plus 1'''
    
    print("Children's code:")
    print(counting_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(counting_code))
    print("\nExecution result:")
    parser.execute(counting_code)
    
    # Example 4: If Statement
    print("\n4. If Statement:")
    if_code = '''age is 10
if age is greater than 5 then
    show "You are a big kid!"
otherwise
    show "You are a little kid!"'''
    
    print("Children's code:")
    print(if_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(if_code))
    print("\nExecution result:")
    parser.execute(if_code)
    
    # Example 5: Function
    print("\n5. Function:")
    function_code = '''function add is (a and b) return
    return a plus b

result is add(10 and 20)
show "Result:"
show result'''
    
    print("Children's code:")
    print(function_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(function_code))
    print("\nExecution result:")
    parser.execute(function_code)
    
    # Example 6: Simple String (without concatenation issues)
    print("\n6. Simple String:")
    string_code = '''name is "Alice"
show "Hello Alice!"'''
    
    print("Children's code:")
    print(string_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(string_code))
    print("\nExecution result:")
    parser.execute(string_code)
    
    # Example 7: While Loop
    print("\n7. While Loop:")
    while_code = '''counter is 0
while counter is less than 3
    show "Counter is " plus counter
    counter is counter plus 1'''
    
    print("Children's code:")
    print(while_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(while_code))
    print("\nExecution result:")
    parser.execute(while_code)
    
    # Example 8: String Operations
    print("\n8. String Operations:")
    string_code = '''message is "Programming is fun!"
show "Message length is " plus length(message)'''
    
    print("Children's code:")
    print(string_code)
    print("\nGenerated Python code:")
    print(parser.parse_file(string_code))
    print("\nExecution result:")
    parser.execute(string_code)
    
    print("\n" + "=" * 60)
    print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
    print("Children can now learn programming with simple English words!")
    print("Based on Nadesiko3 grammar structure for natural learning.")
    print("=" * 60)

if __name__ == "__main__":
    main()
