#!/usr/bin/env python3
"""
Comprehensive test suite for Japanese Programming Language Parser
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from parser import JapaneseParser

class TestSuite:
    def __init__(self):
        self.parser = JapaneseParser()
        self.passed = 0
        self.failed = 0
        self.results = []
    
    def run_test(self, name, japanese_code, expected_output=None, should_run=True):
        """Run a single test case"""
        print(f"Testing: {name}")
        try:
            python_code = self.parser.parse_file(japanese_code)
            print(f"Generated Python code:\n{python_code}")
            
            if should_run:
                # Capture output
                import io
                from contextlib import redirect_stdout
                
                old_stdout = sys.stdout
                sys.stdout = captured_output = io.StringIO()
                
                try:
                    exec(python_code, {})
                    actual_output = captured_output.getvalue()
                    print(f"Output: {actual_output}")
                    
                    if expected_output is not None:
                        if actual_output.strip() == expected_output.strip():
                            print("✓ PASSED")
                            self.passed += 1
                            self.results.append((name, "PASSED", None))
                        else:
                            print(f"✗ FAILED - Expected: {expected_output}, Got: {actual_output}")
                            self.failed += 1
                            self.results.append((name, "FAILED", f"Expected: {expected_output}, Got: {actual_output}"))
                    else:
                        print("✓ PASSED (execution successful)")
                        self.passed += 1
                        self.results.append((name, "PASSED", None))
                        
                except Exception as e:
                    print(f"✗ FAILED - Execution error: {e}")
                    self.failed += 1
                    self.results.append((name, "FAILED", f"Execution error: {e}"))
                    
                finally:
                    sys.stdout = old_stdout
            else:
                print("✓ PASSED (parsing only)")
                self.passed += 1
                self.results.append((name, "PASSED", None))
                
        except Exception as e:
            print(f"✗ FAILED - Parsing error: {e}")
            self.failed += 1
            self.results.append((name, "FAILED", f"Parsing error: {e}"))
        
        print("-" * 50)
    
    def run_all_tests(self):
        """Run all test cases"""
        print("=== Japanese Programming Language Test Suite ===\n")
        
        # Test 1: Basic variable assignment
        self.run_test(
            "Basic Variable Assignment",
            "xは10\nxを表示する",
            "10"
        )
        
        # Test 2: Arithmetic operations
        self.run_test(
            "Arithmetic Operations",
            "aは5\nbは3\ncはaとb\ncを表示する",
            "8"
        )
        
        # Test 3: String handling
        self.run_test(
            "String Handling",
            "「こんにちは」を表示する",
            "こんにちは"
        )
        
        # Test 4: Conditional statements
        self.run_test(
            "Conditional Statements",
            "ageは20\nもしageよりも大きい18ならば\n   「成人」を表示する\nそうでなければ\n    「未成年」を表示する",
            "成人"
        )
        
        # Test 5: For loops
        self.run_test(
            "For Loops",
            "3だけ繰り返す\n    「こんにちは」を表示する",
            "こんにちは\nこんにちは\nこんにちは"
        )
        
        # Test 6: While loops
        self.run_test(
            "While Loops",
            "countは0\ncountよりも小さい3の間\n    countを表示する\n    countはcountと1",
            "0\n1\n2"
        )
        
        # Test 7: Function definition and call
        self.run_test(
            "Function Definition and Call",
            "関数addは(xとy)を返す\n    xとyを返す\nresultはadd(5と3)\nresultを表示する",
            "8"
        )
        
        # Test 8: Complex expressions
        self.run_test(
            "Complex Expressions",
            "aは10\nbは20\ncは30\nresultはaとbとc\ncを表示する",
            "30"
        )
        
        # Test 9: Comparison operators
        self.run_test(
            "Comparison Operators",
            "xは10\nyは20\nもしxよりも小さいyならば\n    「xはyより小さい」を表示する",
            "xはyより小さい"
        )
        
        # Test 10: F-strings
        self.run_test(
            "F-strings",
            "nameは「田中」\nageは25\n「{name}さんは{age}歳です」を表示する",
            "田中さんは25歳です"
        )
        
        # Print summary
        print(f"\n=== Test Summary ===")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Total: {self.passed + self.failed}")
        
        if self.failed > 0:
            print("\nFailed Tests:")
            for name, status, error in self.results:
                if status == "FAILED":
                    print(f"- {name}: {error}")
        
        return self.failed == 0

if __name__ == "__main__":
    test_suite = TestSuite()
    success = test_suite.run_all_tests()
    sys.exit(0 if success else 1)
