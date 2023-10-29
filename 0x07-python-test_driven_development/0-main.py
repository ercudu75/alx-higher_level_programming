#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1e300**2, 1e300000))
print(add_integer(-40))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
