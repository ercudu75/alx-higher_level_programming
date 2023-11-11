#!/usr/bin/python3
"""Class Rectangle"""
from .base import Base


class Rectangle(Base):
    """"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            constructor for the class Rectangle
            and we call method form another class
            we use super and pass the id The goal of it is
            to manage id attribute in all our future classes
            avoid duplicating the same code
            """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    @get_width.setter
    def setter_width(self, width):
        self.__width = width

    @get_height.setter
    def setter_height(self, height):
        self.__height = height

    @get_x.setter
    def setter_x(self, x):
        self.__x = x

    @get_y.setter
    def setter_y(self, y):
        self.__y = y
