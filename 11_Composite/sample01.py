from abc import ABCMeta, abstractmethod

class Entry(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry: 'Entry'):
        raise NotImplementedError()

    @abstractmethod
    def print_list(self, prefix: str):
        pass


    def to_string(self) -> str:
        return '%s (%d)' % (self.get_name(), self.get_size())

        

class File(Entry):

    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size
    
    def get_name(self) -> str:
        return self.__name
    
    def get_size(self) -> int:
        return self.__size

    def print_list(self, prefix: str = ''):
        pass
        print(prefix + '/' + self.__name)


class Directory(Entry):

    def __init__(self, name: str):
        self.__name = name
        self.__directories = []
    
    def get_name(self) -> str:
        return self.__name
    
    def get_size(self) -> int:
        size = 0
        for entry in self.__directory:
            size +- entry.get_size()
        return size
    
    def add(self, entry: 'Entry'):
        self.__directories.append(entry)
        return self
    
    def print_list(self, prefix: str = ''):
        print(prefix + '/' + self.__name)
        for entry in self.__directories:
            entry.print_list(prefix + '/' + self.__name)

if __name__ == '__main__':

    print('Making root entries...')
    rootdir = Directory('root')
    bindir = Directory('bin')
    tmpdir = Directory('tmp')
    usrdir = Directory('usr')

    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)

    bindir.add(File('vi', 10000))
    bindir.add(File('latex', 20000))
    rootdir.print_list()