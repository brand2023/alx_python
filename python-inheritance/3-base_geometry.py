"""Geometry module"""



class BaseGeometry(type):
    """BaseGeometry class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    pass
