from big_char import BigChar


class Singleton():

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance



class BigCharFactory(Singleton):

    def __init__(self):
        self.__pool = {}
    
    def get_big_char(self, charname: str):

        bc = None
        if charname in self.__pool:
            bc = self.__pool[charname]
        else:
            bc = BigChar(charname)
            self.__pool[charname] = bc
        return bc