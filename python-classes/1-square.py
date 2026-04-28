#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class that defines a square by a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
