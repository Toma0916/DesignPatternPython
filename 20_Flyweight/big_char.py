import os


class BigChar():

    def __init__(self, charname: str):
        self.__charname = charname
        try:
            with open( '%s/big%s.txt' % (os.path.dirname(__file__), charname), 'r') as f:
                self.__fontdata =f.read()
        except:
            self.__fontdata = str(charname) + '?'
    
    def print_char(self):
        print(self.__fontdata)
    
if __name__ == '__main__':
    bc = BigChar(1)
    bc.print_char()