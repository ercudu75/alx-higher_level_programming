#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# General Cases)

# Edge Cases
try:
    print(matrix_divided([[1]], 1))  # Single element, should return [[1.0]]
except Exception as e:
    print(e)

try:
    print(matrix_divided([], 1))  # Empty matrix, should return []
except Exception as e:
    print(e)

# Type Errors
try:
    print(matrix_divided("Not a matrix", 2))  # Not a list of lists, should raise TypeError
except Exception as e:
    print(e)

try:
    print(matrix_divided([[1, 2], [3, '4']], 2))  # Element is not a number, should raise TypeError
except Exception as e:
    print(e)

try:
    print(matrix_divided([[1, 2], [3, 4]], '2'))  # Divisor is not a number, should raise TypeError
except Exception as e:
    print(e)

# Zero Division Errors
try:
    print(matrix_divided([[1, 2], [3, 4]], 0))  # Divisor is zero, should raise ZeroDivisionError
except Exception as e:
    print(e)

# Rows of Different Sizes
try:
    print(matrix_divided([[1, 2], [3, 4, 5]], 2))  # Rows have different sizes, should raise TypeError
except Exception as e:
    print(e)
