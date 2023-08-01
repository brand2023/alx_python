"""Geometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area methode"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator methode"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
