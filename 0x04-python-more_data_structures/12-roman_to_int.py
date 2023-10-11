#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                roman_letters[roman_string[i]] <
                roman_letters[roman_string[i + 1]]):
            result -= roman_letters[roman_string[i]]
        else:
            result += roman_letters[roman_string[i]]

    return result
