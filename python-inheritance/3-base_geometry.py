"""Geometry module"""



class BaseGeometry:
    """BaseGeometry class"""
    def __dir__(cls) -> None:
        Attributes=super().__dir__()
        liste_to_return=[]
        for attr in Attributes:
            if attr != "__init_subclass__":
                liste_to_return.append(attr)
        return liste_to_return
    pass
