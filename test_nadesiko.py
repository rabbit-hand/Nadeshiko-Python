#!/usr/bin/env python3
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from nadesiko_parser import NadesikoParser
    print("✓ NadesikoParser imported successfully")
    
    # Test basic functionality
    parser = NadesikoParser()
    print("✓ NadesikoParser instantiated successfully")
    
    # Test simple code
    code = """Aは10
Bは20
CはAとBを足す
「Cの値は{C}です」を表示"""
    result = parser.execute(code)
    print("✓ Basic nadesiko execution completed")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
