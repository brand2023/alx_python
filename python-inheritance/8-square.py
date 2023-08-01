"""Rectangle class"""
Rectangle = __import__('7-rectangle.py').Rectangle

class Square(Rectangle):
    """REc class"""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return self.__width * self.__height
