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
        if not isinstance(value1, int):
            raise TypeError("width must be an integer")
        if value1 <= 0:
            raise ValueError("width must be > 0")
        self.__width = value1

    @height.setter
    def height(self, value2):
        """documentation setter"""
        if not isinstance(value2, int):
            raise TypeError("height must be an integer")
        if value2 <= 0:
            raise ValueError("height must be > 0")
        self.__height = value2

    @x.setter
    def x(self, value3):
        """documentation setter"""
        if not isinstance(value3, int):
            raise TypeError("x must be an integer")
        if value3 < 0:
            raise ValueError("x must be >= 0")
        self.__x = value3

    @y.setter
    def y(self, value4):
        """documentation setter"""
        if not isinstance(value4, int):
            raise TypeError("y must be an integer")
        if value4 < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")