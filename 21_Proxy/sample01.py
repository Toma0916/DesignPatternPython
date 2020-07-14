from abc import ABCMeta, abstractmethod
import time

@abstractmethod
class Printable():

    @abstractmethod
    def set_printer_name(self, name: str):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def print_string(self, string: str):
        pass


class Printer(Printable):

    def __init__(self, name: str):
        self.__heavy_job('Printerのインスタンスを生成中')
        self.__name = name

    
    def set_printer_name(self, name: str):
        self.__name = name
    
    def get_printer_name(self):
        return self.__name
    
    def print_string(self, string: str):
        print('=== %s ===' % self.__name)
        print(string)
    
    def __heavy_job(self, msg: str):
        print(msg)
        for i in range(5):
            print('.')
            time.sleep(1)
        print('完了')


class PrinterProxy(Printable):

    def __init__(self, name: str):
        self.__name = name
        self.__real = None
    
    def set_printer_name(self, name: str):
        if (self.__real):
            self.__real.set_printer_name(name)
        self.__name = name
    
    def get_printer_name(self):
        return self.__name
    
    def print_string(self, string: str):
        self.__realize()  # 本当に必要になって初めてPrinterのインスタンスを生成する
        self.__real.print_string(string)
    
    def __realize(self):
        if (self.__real is None): 
            self.__real = Printer(self.__name)


if __name__ == '__main__':

    p = PrinterProxy('Alice')
    print('名前は現在%sです.' % p.get_printer_name())
    p.set_printer_name('Bob')
    print('名前は現在%sです.' % p.get_printer_name())
    p.print_string('Hello World!')
