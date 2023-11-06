#!/usr/bin/python3
"""class Mylist"""


class MyList(list):
    def print_sorted(self):
        print(sorted(list(self)))
