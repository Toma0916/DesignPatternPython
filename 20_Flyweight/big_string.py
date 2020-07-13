import argparse
from big_char import BigChar
from big_char_factory import BigCharFactory

class BigString():

    def __init__(self, string: str):
        self.__factory = BigCharFactory()
        self.__bigchars = [self.__factory.get_big_char(c) for c in string]
    
    def print_string(self):
        for bc in self.__bigchars:
            bc.print_char()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("str", type=str)
    args = parser.parse_args()
    string = args.str

    bs = BigString(string)
    bs.print_string()
