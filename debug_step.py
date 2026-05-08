#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import re

# Test the regex pattern directly
expr = '足し算(3と4)'
func_match = re.match(r'([a-zA-Z_\u3040-\u309F\u30A0-\u30FF][a-zA-Z0-9_\u3040-\u309F\u30A0-\u30FF]*)\((.*?)\)', expr)
print('Function match:', func_match)

if func_match:
    func_name = func_match.group(1)
    params = func_match.group(2)
    print('Function name:', repr(func_name))
    print('Params before:', repr(params))
    
    # 数値間の「と」を「, 」に変換
    params = re.sub(r'(\d+)と(\d+)', r'\1, \2', params)
    print('Params after:', repr(params))
    
    expr = f"{func_name}({params})"
    print('Final expr:', repr(expr))
