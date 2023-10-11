#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        if num == search:
            new_list += list(filter(lambda x: x == replace, [replace]))
        else:
            new_list += list(filter(lambda x: x == num, [num]))
    return new_list
