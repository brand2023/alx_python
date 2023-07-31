class Square:
    print(__import__("my_module").MyClass.__doc__)
    def Square(self,size):
        print(__import__("my_module").my_function.__doc__)
        print(__import__("my_module").MyClass.my_function.__doc__)
        self.__size=size
        return self.__size