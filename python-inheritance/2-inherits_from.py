"""
fonction that check instance of a class

"""

def is_kind_of_class(obj, a_class):
    """
    the fonction
    """

    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
 