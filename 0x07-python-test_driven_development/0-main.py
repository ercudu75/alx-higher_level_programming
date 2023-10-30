#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

# General Cases
try:
    print_square(4)  # Should print a 4x4 square of '#'
    print("---")  # Separator for better visual distinction
except Exception as e:
    print(e)

try:
    print_square(10)  # Should print a 10x10 square of '#'
    print("---")
except Exception as e:
    print(e)

# Edge Cases
try:
    print_square(0)  # Should not print anything
    print("---")
except Exception as e:
    print(e)

try:
    print_square(1)  # Should print a single '#'
    print("---")
except Exception as e:
    print(e)

# Type Errors
try:
    print_square(-1)  # size is negative, should raise ValueError
    print("---")
except Exception as e:
    print(e)

try:
    print_square("4")  # size is a string, should raise TypeError
    print("---")
except Exception as e:
    print(e)

try:
    print_square(None)  # size is None, should raise TypeError
    print("---")
except Exception as e:
    print(e)

try:
    print_square(4.0)  # size is a positive float, should raise TypeError
    print("---")
except Exception as e:
    print(e)

try:
    print_square(-4.0)  # size is a negative float, should raise TypeError
    print("---")
except Exception as e:
    print(e)

try:
    print_square(True)  # size is a boolean, should raise TypeError
    print("---")
except Exception as e:
    print(e)
