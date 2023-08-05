Base = __import__('base').Base

"""Module documentatin"""


class Rectangle(Base):
    """class documentation"""
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
         """documentation __init__"""
         id = super().__init__()
         self.__width = width
         self.__height = height
         self.__x = x
         self.__y = y