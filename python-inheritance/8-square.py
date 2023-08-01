"""Square class"""
Rectangle = __import__('7-rectangle.py').Rectangle

class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init class"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return self.__width * self.__height
