from abc import ABCMeta, abstractmethod
import hashlib
import unicodedata
from copy import deepcopy

"""
Prototypeパターン
インスタンスから別のインスタンスを作る
"""

class AbstractProduct(metaclass=ABCMeta):

    @abstractmethod
    def use(self, s: str):
        pass


    @abstractmethod
    def create_clone(self) -> 'AbstractProduct':
        pass


class Manager():

    def __init__(self):
        self.__hashmap = {}

    def register(self, name: str, proto: AbstractProduct):
        self.__hashmap[self.__hash_str(name)] = proto

    def create(self, protoname: str):
        p = self.__hashmap.get(self.__hash_str(protoname))
        return p.create_clone()


    def __hash_str(self, string: str):
        return hashlib.md5(string.encode()).hexdigest()


class MessageBox(AbstractProduct):

    def __init__(self, decochar: str):
        self.__decochar = decochar

    def use(self, s: str):
        length = self.__get_width_count(s)
        for i in range(length+4):
            print(self.__decochar, end='')
        print('')
        print('%s %s %s' % (self.__decochar, s, self.__decochar))
        for i in range(length+4):
            print(self.__decochar, end='')
        print('')

    def create_clone(self):
        return deepcopy(self)
    
    def __get_width_count(self, string: str):
        count = 0
        for c in string:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count


class UnderlinePen(AbstractProduct):

    def __init__(self, ulchar: str):
        self.__ulchar = ulchar
    
    def use(self, s: str):
        length = self.__get_width_count(s)
        print("\" %s \"" % s)
        for i in range(length+4):
            print(self.__ulchar, end='')
        print('')

    def create_clone(self):
        return deepcopy(self)

    def __get_width_count(self, string: str):
        count = 0
        for c in string:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count

if __name__ == '__main__':

    manager = Manager()
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    upen = UnderlinePen('~')

    manager.register('warning box', mbox)
    manager.register('slash box', sbox)
    manager.register('strong message', upen)

    p1 = manager.create('warning box')
    p1.use('フォートナイト')
    print('')
    p2 = manager.create('slash box')
    p2.use('フォートナイト')  
    print('')
    p3 = manager.create('strong message')  
    p3.use('フォートナイト')
    print('')
    