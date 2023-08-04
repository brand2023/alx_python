"""Geometry module"""



class BaseGeometry():
    """BaseGeometry class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    pass

class Myclass(metaclass = BaseGeometry):
    """my class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
