"""Geometry module"""



class BaseGeometry():
    """BaseGeometry class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    pass

class BrandMetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BrandClass(metaclass = BrandMetaClass):
    """documentation for class BrandClass"""

    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
