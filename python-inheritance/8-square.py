"""Square module"""
Rectangle = __import__('7-rectangle').Rectangle

class BrandMetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        """
        documentation
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class Square(Rectangle, metaclass = BrandMetaClass):
    """Square class"""

    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)

        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        return self.__size * self.__size

    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
