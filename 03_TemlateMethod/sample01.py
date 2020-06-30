from abc import ABCMeta, abstractmethod
import unicodedata

class AbstractDisplay(metaclass=ABCMeta):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print_one(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print_one()
        self.close()


class CharDisplay(AbstractDisplay):

    def __init__(self, char: str):
        self.__char = char
    
    def open(self):
        print('<', end='')

    def print_one(self):
        print(self.__char, end='')

    def close(self):
        print('>')

    

class StringDisplay(AbstractDisplay):

    def __init__(self, string: str):
        self.__string = string
        self.__width = self.__get_width_count(string)
    
    def open(self):
        self.__print_line()

    def print_one(self):
        print('|%s|' % self.__string)

    def close(self):
        self.__print_line()

    
    def __print_line(self):
        print('+', end='')
        for i in range(self.__width):
            print('-', end='')
        print('+')

    def __get_width_count(self, string: str):
        count = 0
        for c in string:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


if __name__ == '__main__':
    d1 = CharDisplay('コーヒー')
    d2 = StringDisplay('ウィスキー')
    d3 = StringDisplay('チョコレート')

    d1.display()
    d2.display()
    d3.display()
