#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from parser import JapaneseParser
parser = JapaneseParser()
result = parser.parse_line('「こんにちは」を表示する')
print('Parsed line:', repr(result))
