"""Module documentatin"""



class Base:
    """class documentation"""
    __nb_objects = 0
    def __init__(self, id=None):
        """methode documentation"""
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
