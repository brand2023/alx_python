"""Module Base documentatin"""
from models.base import Base


class Rectangle(Base):
    """class base documentation"""
    @property
    def attributes(self):
        """
        documentation of def

        """
        return self.__width, self.__height, self.__x, self.__y

    @attributes.setter
    def attributes(self, value1, value2, value3, value4):
        """documentation setter"""
        self.__width = value1
        self.__height = value2
        self.__x = value3
        self.__y = value4

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance.
        Args:
        - width: width of the rectangle
        - heigth: height of the rectangle
        """
        id = super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
