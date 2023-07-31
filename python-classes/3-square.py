"""
this is class

"""


class Square:
    """
    class Square that defines a square

    """

    def __init__(self, size=0):
        """
        Instantiation with size (no type/value verification)

        """
        self.__size = size

    def size(self):
        """
        Instantiation with size (no type/value verification)

        """
        return self.__size

    def size(self, value):
        """
        Instantiation with size (no type/value verification)

        """
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Instantiation with size (no type/value verification)

        """
        self.area = self.__size ** 2
        return self.area
