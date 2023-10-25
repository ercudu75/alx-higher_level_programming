#!/usr/bin/python3
"""square class"""


class Square:
    """private instance and raise errors for exception"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for position"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter for size"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(item, int) and item > 0 for item in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def my_print(self):
        """Prints a visual representation of the square to stdout"""
        if self.__size == 0:
            print()
        else:
            for new_line in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print("")

    def area(self):
        """print the square"""
        return self.__size ** 2

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
        for i in range(0, self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ("")
