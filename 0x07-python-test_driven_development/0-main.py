#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

# General Cases
try:
    say_my_name("John", "Smith")  # Should print: "My name is John Smith"
except Exception as e:
    print(e)

try:
    say_my_name("Bob")  # Should print: "My name is Bob "
except Exception as e:
    print(e)

# Edge Cases
try:
    say_my_name("", "")  # Should print: "My name is  "
except Exception as e:
    print(e)

# Type Errors
try:
    say_my_name(12, "White")  # first_name is not a string, should raise TypeError
except Exception as e:
    print(e)

try:
    say_my_name("John", 12)  # last_name is not a string, should raise TypeError
except Exception as e:
    print(e)

try:
    say_my_name(12, 12)  # Both first_name and last_name are not strings, should raise TypeError
except Exception as e:
    print(e)

try:
    say_my_name(None, "White")  # first_name is None, should raise TypeError
except Exception as e:
    print(e)

