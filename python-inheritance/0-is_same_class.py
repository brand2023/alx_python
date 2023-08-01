"""
fonction that check instance of a class

"""

def is_same_class(obj, a_class):
    """
    the fonction
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True