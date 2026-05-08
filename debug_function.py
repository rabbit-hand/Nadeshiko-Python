#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from parser import JapaneseParser
parser = JapaneseParser()
result = parser.parse_line('関数足し算は(aとb)を返す')
print('Parsed function:', repr(result))
