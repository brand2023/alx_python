"""Geometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area methode"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        """integer validator methode"""
        if not isinstance(value, int):
            raise TypeError(name," must be an integer")
        elif value < 0:
            raise ValueError(name," must be greater than 0")
