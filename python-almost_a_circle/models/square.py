"""Module rectangle documentatin"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """methode documentation"""
        super().__init__(self.__width, self.__height, self.__x, self.__y, self.id)
        self.size = self.__width = self.__height

    def __str__(self):
        """overriding the __str__ method ."""
        super().__init__(self.__width, self.__height, self.__x, self.__y, self.id)
        string = "[Square] ({})".format(self.id)
        string += " {}/{}".format(self.__x, self.__y)
        string += " - {}".format(self.size)
        return string