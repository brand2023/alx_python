"""
fonction that check instance of a class

"""

def is_kind_of_class(obj, a_class):
    """
     a function that returns True if the object is an instance of a class that 
     inherited (directly or indirectly) from the specified class ; otherwise False.

    arg: if type of obj is a_class 
    """
    if issubclass(a_class, type(obj)):        return True
    else:
        return False
 