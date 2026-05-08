#!/usr/bin/env python3
"""
Children's English Programming Language Parser
Based on Nadesiko3 grammar structure but with simple English words
Designed for children to learn programming naturally
"""

import re
from keywords import JapaneseKeywords

class ChildrenEnglishParser:
    """Children's English Programming Language Parser"""
    
    def __init__(self):
        self.keywords = ChildrenEnglishKeywords()
    
    def parse_line(self, line):
        """Parse one line of children's English code"""
        line = line.strip()
        if not line or line.startswith('#'):
            return line
        
        # Function definition: "function name is (params) return"
        if line.startswith('function') and 'return' in line:
            match = re.match(r'function\s+(.+?)\s+is\s*\((.*?)\)\s+return', line)
            if match:
                func_name = match.group(1).strip()
                params = match.group(2).strip()
                # Convert "and" to commas in parameters
                params = params.replace(' and ', ', ')
                return f"def {func_name}({params}):"
        
        # Print statement: "show value"
        if line.startswith('show '):
            value = line.replace('show ', '').strip()
            return f"print({self._translate_expression(value)})"
        
        # Input statement: "ask value"
        if line.startswith('ask '):
            prompt = line.replace('ask ', '').strip()
            return f"input({prompt})"
        
        # Variable assignment: "name is value"
        if ' is ' in line and not any(keyword in line for keyword in ['if', 'while', 'for', 'return']):
            match = re.match(r'(.+?)\s+is\s+(.+)$', line)
            if match:
                var_name, value = match.groups()
                return f"{var_name} = {self._translate_expression(value)}"
        
        # If statement: "if condition then"
        if line.startswith('if ') and ' then' in line:
            condition = line.replace('if ', '').replace(' then', '').strip()
            python_condition = self._translate_expression(condition)
            return f"if {python_condition}:"
        
        # Else statement: "otherwise"
        if line.startswith('otherwise'):
            return "else:"
        
        # While loop: "while condition"
        if line.startswith('while '):
            condition = line.replace('while ', '').strip()
            python_condition = self._translate_expression(condition)
            return f"while {python_condition}:"
        
        # For loop: "repeat count times"
        if line.startswith('repeat ') and ' times' in line:
            match = re.match(r'repeat\s+(.+?)\s+times$', line)
            if match:
                count = match.group(1)
                return f"for _ in range({self._translate_expression(count)}):"
        
        # Return statement: "return value" or "value return"
        if line.startswith('return ') or line.endswith(' return'):
            if line.startswith('return '):
                value = line.replace('return ', '').strip()
            else:
                value = line.replace(' return', '').strip()
            return f"return {self._translate_expression(value)}"
        
        # Other expressions
        return self._translate_expression(line)
    
    def _translate_expression(self, expr):
        """Translate expression to Python code"""
        if not expr:
            return ""
        
        # Handle string literals with quotes
        if expr.startswith('"') and expr.endswith('"'):
            content = expr[1:-1]
            if '{' in content and '}' in content:
                return f'f"{content}"'
            else:
                return f'"{content}"'
        elif expr.startswith("'") and expr.endswith("'"):
            content = expr[1:-1]
            if '{' in content and '}' in content:
                return f"f'{content}'"
            else:
                return f"'{content}'"
        
        # Handle function calls - convert 'and' to commas in parameters
        import re
        func_match = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\((.*?)\)', expr)
        if func_match:
            func_name = func_match.group(1)
            params = func_match.group(2)
            # Convert "and" to commas in function parameters
            params = params.replace(' and ', ', ')
            expr = f"{func_name}({params})"
        
        # Handle comparison operators
        expr = expr.replace(' is greater than ', ' > ')
        expr = expr.replace(' is less than ', ' < ')
        expr = expr.replace(' is equal to ', ' == ')
        expr = expr.replace(' is not equal to ', ' != ')
        
        # Handle logical operators
        expr = expr.replace(' and ', ' and ')
        expr = expr.replace(' or ', ' or ')
        expr = expr.replace(' not ', ' not ')
        
        # Handle arithmetic operators
        expr = expr.replace(' plus ', ' + ')
        expr = expr.replace(' minus ', ' - ')
        expr = expr.replace(' times ', ' * ')
        expr = expr.replace(' divided by ', ' / ')
        
        # Handle keywords
        for english, python in self.keywords.KEYWORD_MAP.items():
            expr = expr.replace(english, python)
        
        return expr.strip()
    
    def parse_file(self, code):
        """Parse entire children's English code file"""
        lines = code.split('\n')
        python_lines = []
        indent_stack = []
        
        for line in lines:
            stripped_line = line.strip()
            
            # Skip empty lines and comments
            if not stripped_line or stripped_line.startswith('#'):
                python_lines.append(line)
                continue
            
            # Calculate indentation
            current_indent = len(line) - len(line.lstrip())
            
            # Handle indentation changes
            if indent_stack and current_indent <= indent_stack[-1]:
                while indent_stack and current_indent <= indent_stack[-1]:
                    indent_stack.pop()
            
            actual_indent = len(indent_stack) * 4
            python_line = self.parse_line(stripped_line)
            
            # Add indentation
            if python_line:
                python_lines.append(' ' * actual_indent + python_line)
                
                # Update indent stack for control structures
                if python_line.endswith(':'):
                    indent_stack.append(current_indent)
            else:
                python_lines.append(line)
        
        return '\n'.join(python_lines)
    
    def execute(self, code):
        """Execute children's English code"""
        python_code = self.parse_file(code)
        print(f"Generated Python code:\n{python_code}\n")
        print("Execution result:")
        exec(python_code, globals())

class ChildrenEnglishKeywords:
    """Keywords for Children's English Programming Language"""
    
    KEYWORD_MAP = {
        # Simple words for children
        'true': 'True',
        'false': 'False',
        'nothing': 'None',
        'length': 'len',
        'square root': 'math.sqrt',
        'absolute': 'abs',
    }
    
    PATTERNS = {
        # Simple patterns for children
        'variable': r'([a-zA-Z_][a-zA-Z0-9_]*)\s+is\s+(.+)',
        'function': r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+is\s*\((.*?)\)\s+return',
        'if': r'if\s+(.+?)\s+then',
        'while': r'while\s+(.+)',
        'for': r'repeat\s+(.+?)\s+times',
        'print': r'show\s+(.+)',
        'input': r'ask\s+(.+)',
        'return': r'return\s+(.+)',
    }
