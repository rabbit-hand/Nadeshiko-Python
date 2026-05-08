#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import re

# Test the regex pattern directly
expr = '足し算(3と4)'
func_match = re.match(r'([^()]+?)\((.*?)\)', expr)
print('Function match:', func_match)

if func_match:
    func_name = func_match.group(1).strip()
    params = func_match.group(2).strip()
    print('Function name:', repr(func_name))
    print('Params before:', repr(params))
    
    # 数値間の「と」を「, 」に変換
    params = re.sub(r'(\d+)と(\d+)', r'\1, \2', params)
    print('Params after:', repr(params))
    
    expr = f"{func_name}({params})"
    print('Final expr:', repr(expr))
