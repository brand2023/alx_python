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
        elif value < 0:
            raise ValueError("{} must be greater than 0".format(name))
