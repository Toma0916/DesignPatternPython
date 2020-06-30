from abc import ABCMeta, abstractmethod


class Banner():

    def __init__(self, string: str):
        self.__string = string

    def show_with_paren(self):
        print('(%s)' % self.__string)
    
    def show_with_aster(self):
        print('*%s*' % self.__string)


class AbstractPrint(metaclass=ABCMeta):

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class PrintBanner(AbstractPrint):

    def __init__(self, string: str):
        self.__banner = Banner(string)
    
    def print_weak(self):
        self.__banner.show_with_paren()
    
    def print_strong(self):
        self.__banner.show_with_aster()


if __name__ == '__main__':
    p = PrintBanner('高度人工知能人材')
    # mainはPrintBannerの具体的実装を知らない
    # AbstractPrintInterfaceを使ってプログラミングをしている
    p.print_weak()
    p.print_strong()
