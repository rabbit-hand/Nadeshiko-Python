#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from parser import JapaneseParser
parser = JapaneseParser()

# Test function call parsing
result = parser.parse_line('結果は足し算(3と4)')
print('Parsed line:', repr(result))

# Test the full function code
function_code = """
関数足し算は(aとb)を返す
    aとbを返す

結果は足し算(3と4)
結果を表示する
"""
parsed = parser.parse_file(function_code)
print('Full parsed code:')
print(parsed)
