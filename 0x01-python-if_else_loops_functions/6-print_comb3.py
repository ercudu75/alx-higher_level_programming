#!/usr/bin/python3
for i in range(0, 100):
    last_digit = i % 10
    first_digit = i // 10
    if first_digit < last_digit:
        print("{}{}".format(first_digit, last_digit), end=", " if i < 89 else "\n")
