"""
fonction that check instance of a class

"""

def is_kind_of_class(obj, a_class):
    """
    the fonction
    """
    if super(obj, a_class):
        return True
    else:
        return False
 