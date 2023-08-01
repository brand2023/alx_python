"""
fonction that check instance of a class

"""

def is_kind_of_class(obj, a_class):
    """
    the fonction kind of class
    Prototype: def inherits_from(obj, a_class):
    You are not allowed to import any module

    """
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
 