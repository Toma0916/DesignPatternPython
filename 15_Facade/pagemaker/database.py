import sys
from .exception import CannotInitializeError

PYTHON_DICT_DB = {
    'sadistica@ut.ac.jp': 'toma',
    'shinamon@ut.ac.jp': 'dog'
}

class Database():

    def __init__(self):
        raise CannotInitializeError
    
    @staticmethod
    def get_properties(dbname: str):

        try:
            return PYTHON_DICT_DB[dbname]
        except KeyError:
            print('%s is invalid key' % dbname)
            sys.exit()
        


if __name__ == '__main__':
    Database.get_properties('sadistica@ut.ac.jp')



