#!/usr/bin/env python3
"""
Basic Calculator - A command-line calculator with arithmetic operations
"""

import math
import sys


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Raise a to the power of b."""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """Calculate square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def factorial(self, a):
        """Calculate factorial of a."""
        if a < 0:
            raise ValueError("Cannot calculate factorial of negative number!")
        if not isinstance(a, int):
            raise ValueError("Factorial can only be calculated for integers!")
        result = math.factorial(a)
        self.history.append(f"{a}! = {result}")
        return result
    
    def show_history(self):
        """Display calculation history."""
        if not self.history:
            print("No calculations performed yet.")
            return
        
        print("\nCalculation History:")
        print("-" * 30)
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
        print("History cleared.")


def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_integer(prompt):
    """Get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def show_menu():
    """Display the calculator menu."""
    print("\n" + "="*40)
    print("           CALCULATOR MENU")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Show History")
    print("9. Clear History")
    print("0. Exit")
    print("="*40)


def main():
    """Main calculator function."""
    calc = Calculator()
    
    print("Welcome to the Python Calculator!")
    print("This calculator supports basic arithmetic operations.")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '0':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            elif choice == '1':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"Result: {result}")
            
            elif choice == '2':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            
            elif choice == '3':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            
            elif choice == '4':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.divide(a, b)
                print(f"Result: {result}")
            
            elif choice == '5':
                a = get_number("Enter base number: ")
                b = get_number("Enter exponent: ")
                result = calc.power(a, b)
                print(f"Result: {result}")
            
            elif choice == '6':
                a = get_number("Enter number: ")
                result = calc.square_root(a)
                print(f"Result: {result}")
            
            elif choice == '7':
                a = get_integer("Enter integer: ")
                result = calc.factorial(a)
                print(f"Result: {result}")
            
            elif choice == '8':
                calc.show_history()
            
            elif choice == '9':
                calc.clear_history()
            
            else:
                print("Invalid choice. Please enter a number between 0-9.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()