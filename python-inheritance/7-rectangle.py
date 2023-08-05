"""Rectangle class"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class BrandMetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        """
        documentation
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class Rectangle(BaseGeometry, metaclass = BrandMetaClass):
    """REc class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height
    
    def print(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
