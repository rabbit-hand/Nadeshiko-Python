#!/usr/bin/env python3
"""
Test module import from different locations
"""

import sys
import os

def test_import_from_project_root():
    """Test importing from project root"""
    print("=== Test 1: Import from project root ===")
    try:
        from src.parser import JapaneseParser
        print("✓ JapaneseParser imported from src.parser")
        
        parser = JapaneseParser()
        print("✓ JapaneseParser instantiated")
        
        # Test basic functionality
        result = parser.parse_line("xは10")
        print(f"✓ Basic parsing: {result}")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def test_import_from_package():
    """Test importing as package"""
    print("\n=== Test 2: Import as package ===")
    try:
        # Add project root to path
        project_root = os.path.dirname(os.path.abspath(__file__))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
        
        import japanese_programming
        print("✓ Package imported")
        
        from japanese_programming import JapaneseParser
        print("✓ JapaneseParser imported from package")
        
        parser = JapaneseParser()
        print("✓ JapaneseParser instantiated")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality"""
    print("\n=== Test 3: Basic functionality ===")
    try:
        from src.parser import JapaneseParser
        parser = JapaneseParser()
        
        # Test various features
        test_cases = [
            ("xは10", "x = 10"),
            ("aとb", "a + b"),
            ("「こんにちは」", "\"こんにちは\""),
            ("もし条件ならば", "if condition:"),
            ("5だけ繰り返す", "for _ in range(5):"),
            ("関数testは(x)を返す", "def test(x):")
        ]
        
        for japanese, expected_start in test_cases:
            result = parser.parse_line(japanese)
            if result.startswith(expected_start):
                print(f"✓ {japanese} → {result}")
            else:
                print(f"✗ {japanese} → {result} (expected to start with {expected_start})")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def test_execution():
    """Test code execution"""
    print("\n=== Test 4: Code execution ===")
    try:
        from src.parser import JapaneseParser
        parser = JapaneseParser()
        
        # Test simple execution
        code = """
xは10
yは20
zはxとy
zを表示する
"""
        
        # Capture output
        import io
        from contextlib import redirect_stdout
        
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            parser.execute(code)
        
        output = captured_output.getvalue().strip()
        if output == "30":
            print(f"✓ Execution successful: {output}")
            return True
        else:
            print(f"✗ Unexpected output: {output}")
            return False
            
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Japanese Programming Language Module\n")
    
    tests = [
        test_import_from_project_root,
        test_import_from_package,
        test_basic_functionality,
        test_execution
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n=== Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return True
    else:
        print("✗ Some tests failed!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
