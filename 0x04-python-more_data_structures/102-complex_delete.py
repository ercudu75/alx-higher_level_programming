#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    to_delete = []
    to_delete = [key for key, val in a_dictionary.items() if val == value]
    for i in to_delete:
        del a_dictionary[i]
    return (a_dictionary)
