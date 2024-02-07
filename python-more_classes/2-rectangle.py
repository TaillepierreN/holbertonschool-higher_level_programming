#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """Define the rectangle attribute"""

    def __init__(self, width=0, height=0):
        """
        initialisation of the rectangle
        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter of width

        Args:
            value (int): width of rectangle to set

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter of height

        Args:
            value (int): height of rectangle to set

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
