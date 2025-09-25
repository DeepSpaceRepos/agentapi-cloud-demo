#!/usr/bin/env python3
"""
Test file for the calculator.py module
"""

import calculator


def test_calculator():
    """Test basic calculator functionality."""
    print("Testing Calculator...")
    print("=" * 30)
    
    # Create calculator instance
    calc = calculator.Calculator()
    
    # Test addition
    print("Testing addition:")
    result = calc.add(5, 3)
    print(f"5 + 3 = {result}")
    assert result == 8, "Addition test failed"
    
    # Test subtraction
    print("\nTesting subtraction:")
    result = calc.subtract(10, 4)
    print(f"10 - 4 = {result}")
    assert result == 6, "Subtraction test failed"
    
    # Test multiplication
    print("\nTesting multiplication:")
    result = calc.multiply(7, 6)
    print(f"7 * 6 = {result}")
    assert result == 42, "Multiplication test failed"
    
    # Test division
    print("\nTesting division:")
    result = calc.divide(15, 3)
    print(f"15 / 3 = {result}")
    assert result == 5, "Division test failed"
    
    # Test power
    print("\nTesting power:")
    result = calc.power(2, 3)
    print(f"2 ^ 3 = {result}")
    assert result == 8, "Power test failed"
    
    # Test square root
    print("\nTesting square root:")
    result = calc.square_root(16)
    print(f"√16 = {result}")
    assert result == 4, "Square root test failed"
    
    # Test factorial
    print("\nTesting factorial:")
    result = calc.factorial(5)
    print(f"5! = {result}")
    assert result == 120, "Factorial test failed"
    
    # Test error handling
    print("\nTesting error handling:")
    try:
        calc.divide(10, 0)
        print("ERROR: Division by zero should have raised an exception!")
    except ValueError as e:
        print(f"✓ Correctly caught division by zero: {e}")
    
    try:
        calc.square_root(-4)
        print("ERROR: Negative square root should have raised an exception!")
    except ValueError as e:
        print(f"✓ Correctly caught negative square root: {e}")
    
    # Show history
    print("\nCalculation History:")
    calc.show_history()
    
    print("\n" + "=" * 30)
    print("All tests passed! ✓")


if __name__ == "__main__":
    test_calculator()