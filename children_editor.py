#!/usr/bin/env python3
"""
Children's Programming Editor
Simple and friendly interface for children to learn programming
Based on Nadesiko3 grammar with simple English words
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.children_english_parser import ChildrenEnglishParser

class ChildrenEditor:
    """Simple editor for children's programming"""
    
    def __init__(self):
        self.parser = ChildrenEnglishParser()
        self.examples = self._get_examples()
    
    def _get_examples(self):
        """Get child-friendly examples"""
        return {
            "Hello World": 'show "Hello World!"',
            "Counting": '''number is 1
show "Counting:"
repeat 5 times
    show number
    number is number plus 1''',
            "Simple Math": '''apple is 5
orange is 3
total is apple plus orange
show "Total fruits:"
show total''',
            "If Statement": '''age is 10
if age is greater than 5 then
    show "You are a big kid!"
otherwise
    show "You are a little kid!"''',
            "Function": '''function add is (a and b) return
    return a plus b

result is add(10 and 20)
show "Result:"
show result''',
            "Input": '''name is ask "What is your name? "
show "Hello " plus name plus "!"''',
            "Loop with Counter": '''counter is 0
while counter is less than 3
    show "Counter is " plus counter
    counter is counter plus 1''',
            "String Fun": '''message is "Programming is fun!"
show "Message length is " plus length(message)''',
        }
    
    def show_welcome(self):
        """Show welcome message"""
        print("=" * 60)
        print("🌟 CHILDREN'S PROGRAMMING EDITOR 🌟")
        print("=" * 60)
        print("Welcome to the fun world of programming!")
        print("You can write code in simple English words.")
        print("Type 'help' to see examples or 'quit' to exit.")
        print("=" * 60)
    
    def show_help(self):
        """Show help and examples"""
        print("\n📚 EXAMPLES:")
        print("-" * 40)
        for i, (title, code) in enumerate(self.examples.items(), 1):
            print(f"{i}. {title}")
        
        print("\n📝 SIMPLE WORDS YOU CAN USE:")
        print("-" * 40)
        print("• Variables: name is value")
        print("• Math: plus, minus, times, divided by")
        print("• Compare: is greater than, is less than, is equal to")
        print("• Logic: and, or, not")
        print("• If: if condition then")
        print("• Else: otherwise")
        print("• Loop: repeat number times")
        print("• While: while condition")
        print("• Function: function name is (params) return")
        print("• Show: show value")
        print("• Ask: ask question")
        print("• Return: return value")
        
        print("\n🎯 TRY IT:")
        print("-" * 40)
        print("Type an example number (1-8) to load it")
        print("Or type your own code line by line")
        print("Type 'run' to execute your code")
        print("Type 'clear' to start over")
        print("Type 'quit' to exit")
    
    def run_example(self, example_num):
        """Run a specific example"""
        if 1 <= example_num <= len(self.examples):
            title = list(self.examples.keys())[example_num - 1]
            code = self.examples[title]
            print(f"\n🎮 Running: {title}")
            print("-" * 40)
            print("Code:")
            print(code)
            print("-" * 40)
            print("Output:")
            try:
                self.parser.execute(code)
            except Exception as e:
                print(f"Oops! Something went wrong: {e}")
                print("Don't worry, programming is all about learning!")
            print("-" * 40)
        else:
            print("Please choose a number between 1 and 8")
    
    def interactive_mode(self):
        """Interactive programming mode"""
        print("\n✏️  INTERACTIVE MODE")
        print("Type your code line by line. Type 'run' to execute.")
        print("-" * 40)
        
        code_lines = []
        line_number = 1
        
        while True:
            try:
                line = input(f"Line {line_number}> ").strip()
                
                if line.lower() == 'run':
                    if code_lines:
                        code = '\n'.join(code_lines)
                        print("\n🚀 Running your code:")
                        print("-" * 40)
                        try:
                            self.parser.execute(code)
                        except Exception as e:
                            print(f"Oops! Something went wrong: {e}")
                            print("Don't worry, programming is all about learning!")
                        print("-" * 40)
                        code_lines = []
                        line_number = 1
                    else:
                        print("No code to run! Write some code first.")
                elif line.lower() == 'clear':
                    code_lines = []
                    line_number = 1
                    print("Code cleared! Start fresh.")
                elif line.lower() == 'back':
                    if code_lines:
                        code_lines.pop()
                        line_number -= 1
                        print("Last line removed.")
                elif line.lower() == 'quit':
                    break
                elif line:
                    code_lines.append(line)
                    line_number += 1
                    print(f"✅ Line added. {len(code_lines)} lines total.")
                
            except KeyboardInterrupt:
                print("\nGoodbye! Happy coding! 🌈")
                break
            except EOFError:
                print("\nGoodbye! Happy coding! 🌈")
                break
    
    def run(self):
        """Run the children's editor"""
        self.show_welcome()
        
        while True:
            try:
                command = input("\nWhat would you like to do? ").strip().lower()
                
                if command == 'quit' or command == 'exit':
                    print("Goodbye! Happy coding! 🌈")
                    break
                elif command == 'help':
                    self.show_help()
                elif command.isdigit():
                    self.run_example(int(command))
                elif command == 'interactive':
                    self.interactive_mode()
                elif command == 'examples':
                    for i, (title, code) in enumerate(self.examples.items(), 1):
                        print(f"\n{i}. {title}:")
                        print(code)
                        print("-" * 40)
                else:
                    print("I don't understand that. Try 'help' to see what you can do!")
                    
            except KeyboardInterrupt:
                print("\nGoodbye! Happy coding! 🌈")
                break
            except EOFError:
                print("\nGoodbye! Happy coding! 🌈")
                break

def main():
    """Main function"""
    editor = ChildrenEditor()
    editor.run()

if __name__ == "__main__":
    main()
