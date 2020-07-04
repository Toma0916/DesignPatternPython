from abc import ABCMeta, abstractmethod
import unicodedata 

"""
機能の階層と実装の階層を分ける
"""

class Display():

    def __init__(self, impl):
        self.__impl = impl
    
    def open(self):
        self.__impl.raw_open()
    
    def print(self):
        self.__impl.raw_print()

    def close(self):
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):

    def __init__(self, impl):
        super(CountDisplay, self).__init__(impl)
    
    def multiple_display(self, times: int):
        self.open()
        for i in range(times):
            self.print()
        self.close()


class DisplayImpl(metaclass=ABCMeta):

    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):

    def __init__(self, string: str):
        self.__string = string
        self.__width = self.__get_width_count(string)

    
    def __get_width_count(self, string: str):
        count = 0
        for c in string:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count

    def raw_open(self):
        self.__print_line()
    
    def raw_print(self):
        print('|%s|' % self.__string)

    def raw_close(self):
        self.__print_line()

    def __print_line(self):

        print('+', end='')
        for i in range(self.__width):
            print('-', end='')
        print('+')

if __name__ == '__main__':
    d1 = Display(StringDisplayImpl('Japan'))
    d2 = CountDisplay(StringDisplayImpl('Asia'))
    d3 = CountDisplay(StringDisplayImpl('Universe'))
    
    d1.display()
    d2.display()
    d3.multiple_display(3)