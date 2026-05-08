#!/usr/bin/env python3
"""
Test PIP installation functionality
"""

import sys
import os

def test_pip_import():
    """Test importing after pip install"""
    print("=== Test: PIP Installation Import ===")
    try:
        import japanese_programming
        print("✓ Package imported after pip install")
        
        from japanese_programming import JapaneseParser
        print("✓ JapaneseParser imported from package")
        
        parser = JapaneseParser()
        print("✓ JapaneseParser instantiated")
        
        # Test basic functionality
        result = parser.parse_line("xは10")
        print(f"✓ Basic parsing: {result}")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def test_pip_execution():
    """Test execution after pip install"""
    print("\n=== Test: PIP Installation Execution ===")
    try:
        from japanese_programming import JapaneseParser
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

def test_package_info():
    """Test package information"""
    print("\n=== Test: Package Information ===")
    try:
        import japanese_programming
        
        print(f"✓ Package version: {getattr(japanese_programming, '__version__', 'Unknown')}")
        print(f"✓ Package author: {getattr(japanese_programming, '__author__', 'Unknown')}")
        print(f"✓ Package __all__: {getattr(japanese_programming, '__all__', 'Unknown')}")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def test_different_python_interpreter():
    """Test with different Python interpreter"""
    print("\n=== Test: Different Python Interpreter ===")
    try:
        import subprocess
        import tempfile
        
        # Create a test script
        test_script = '''
import sys
sys.path.insert(0, ".")
from japanese_programming import JapaneseParser

parser = JapaneseParser()
result = parser.parse_line("xは10")
print(f"SUCCESS: {result}")
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(test_script)
            temp_file = f.name
        
        try:
            # Run with python3
            result = subprocess.run(['python3', temp_file], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0 and "SUCCESS" in result.stdout:
                print("✓ Different interpreter test passed")
                return True
            else:
                print(f"✗ Different interpreter test failed: {result.stderr}")
                return False
        finally:
            os.unlink(temp_file)
            
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False

def main():
    """Run all PIP tests"""
    print("Testing PIP Installation of Japanese Programming Language\n")
    
    tests = [
        test_pip_import,
        test_pip_execution,
        test_package_info,
        test_different_python_interpreter
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n=== PIP Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All PIP tests passed!")
        return True
    else:
        print("✗ Some PIP tests failed!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
