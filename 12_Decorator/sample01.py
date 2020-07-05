from abc import ABCMeta, abstractmethod
import unicodedata

class Display(metaclass=ABCMeta):

    @abstractmethod
    def get_columns(self) -> int:
        pass

    @abstractmethod
    def get_rows(self) -> int:
        pass

    @abstractmethod
    def get_row_text(self, row: int) -> str:
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):

    def __init__(self, string: str):
        self.__string = string
    
    def get_columns(self):
        return self.__get_width_count(self.__string)
    
    def get_rows(self):
        return 1

    def get_row_text(self, row: int):
        if row == 0:
            return self.__string
        else:
            return None
        
    def __get_width_count(self, string: str):
        count = 0
        for c in string:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


class Border(Display, metaclass=ABCMeta):

    def __init__(self, display: 'Display'):
        self.__display = display
    
    @property
    def _display(self):
        return self.__display


class SideBorder(Border):

    def __init__(self, display: 'Display', ch: str):
        super(SideBorder, self).__init__(display)
        self.__border_char = ch
    
    def get_columns(self):
        return 1 + self._display.get_columns() + 1
    
    def get_rows(self):
        return self._display.get_rows()
    
    def get_row_text(self, row: int):
        return self.__border_char + self._display.get_row_text(row) + self.__border_char


class FullBorder(Border):

    def __init__(self, display: 'Display'):
        super(FullBorder, self).__init__(display)
    
    def get_columns(self):
        return 1 + self._display.get_columns() + 1
    
    def get_rows(self):
        return 1 + self._display.get_rows() + 1
    
    def get_row_text(self, row: int):
        if row == 0:
            return '+' + self.__make_line('-', self._display.get_columns()) + '+'
        elif row == self._display.get_rows() + 1:
            return '+' + self.__make_line('-', self._display.get_columns()) + '+'
        else:
            return '|' + self._display.get_row_text(row - 1) + '|'
         
    def __make_line(self, ch: str, count: int):
        return ch * count

    
if __name__ == '__main__':

    b1 = StringDisplay('Hello, World.')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)

    b1.show()
    b2.show()
    b3.show()


    b4 = SideBorder(
            FullBorder(
                FullBorder(
                    SideBorder(
                        FullBorder(
                            StringDisplay('Ling')
                        )
                    , '*')
                )
            )
        , '0')
    
    b4.show()