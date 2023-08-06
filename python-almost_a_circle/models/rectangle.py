"""Module Base documentatin"""
from models.base import Base


class Rectangle(Base):
    """class base documentation"""
    @property
    def width(self):
        """
        documentation of def

        """
        return self.__width

    @property
    def height(self):
        """
        documentation of def

        """
        return self.__height

    @property
    def x(self):
        """
        documentation of def

        """
        return self.__x

    @property
    def y(self):
        """
        documentation of def

        """
        return self.__y

    @width.setter
    def width(self, value1):
        """documentation setter"""
        self.__width = value1

    @height.setter
    def height(self, value2):
        """documentation setter"""
        self.__height = value2

    @x.setter
    def x(self, value3):
        """documentation setter"""
        self.__x = value3

    @y.setter
    def y(self, value4):
        """documentation setter"""
        self.__y = value4

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance.
        Args:
        - width: width of the rectangle
        - heigth: height of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
