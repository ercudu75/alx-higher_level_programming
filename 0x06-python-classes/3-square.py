#!/usr/bin/python3
"""class square"""


class Square:
    """private instance and raise errors for exception"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the squarea area"""
        return self.__size ** 2
