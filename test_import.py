#!/usr/bin/env python3
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from parser import JapaneseParser
    print("✓ JapaneseParser imported successfully")
    
    # Test basic functionality
    parser = JapaneseParser()
    print("✓ JapaneseParser instantiated successfully")
    
    # Test simple code
    code = "xは10\nxを表示する"
    result = parser.execute(code)
    print("✓ Basic execution completed")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
