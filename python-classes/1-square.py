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
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("ize must be >= 0")
