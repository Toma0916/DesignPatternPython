from abc import ABCMeta, abstractmethod

"""
ダブルディスパッチ
処理をデータ構造から分離する
"""

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit(self, entry: "Entry"):
        pass


class Element(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, v: "Visitor"):
        pass


class Entry(Element, metaclass=ABCMeta):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry: "Entry"):
        raise NotImplementedError

    def to_string(self):
        return '%s (%d)' % (self.get_name(), self.get_size())
    

class File(Entry):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size
    
    def get_name(self) -> str:
        return self.__name
    
    def get_size(self) -> int:
        return self.__size
    
    def accept(self, v: "Visitor"):
        v.visit(self)
    

class Directory(Entry):

    def __init__(self, name):
        self.__name = name 
        self.__directories = []
    
    @property
    def _directories(self):
        return self.__directories
    
    def get_name(self):
        return self.__name
    
    def get_size(self):
        size = 0
        for entry in self.__directories:
            size += entry.get_size()
        return size

    def add(self, entry: "Entry"):
        self.__directories.append(entry)
        return self
    
    def accept(self, v: "Visitor"):
        v.visit(self)
    

class ListVisitor(Visitor):

    def __init__(self):
        self.__current_dir = ''

    def visit(self, entry: "Entry"):
        if type(entry) is File:
            self.__visit_file(entry)
        elif type(entry) is Directory:
            self.__visit_directory(entry)
        else:
            pass
    
    def __visit_file(self, f: 'File'):
        print(self.__current_dir + '/' + f.get_name())

    def __visit_directory(self, v: "Directory"):
        print(self.__current_dir + '/' + v.get_name())
        save_fir = self.__current_dir
        self.__current_dir = self.__current_dir + '/' + v.get_name()
        for e in v._directories:
            e.accept(self)
        self.__current_dir = save_fir


class CountVisitor(Visitor):

    def __init__(self):
        self.__current_dir = ''
        self.__visit_count = 0
    
    def show_result(self):
        print('element num: %s' % self.__visit_count)

    def visit(self, entry: "Entry"):
        if type(entry) is File:
            self.__visit_file(entry)
        elif type(entry) is Directory:
            self.__visit_directory(entry)
        else:
            pass
    
    def __visit_file(self, f: 'File'):
        self.___visit_count += 1

    def __visit_directory(self, v: "Directory"):
        self.__visit_count += 1
        for e in v._directories:
            e.accept(self)


if __name__ == '__main__':

    print('Making root entries...')
    rootdir = Directory('root')
    bindir = Directory('bin')
    tmpdir = Directory('tmp')
    usrdir = Directory('usr')

    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)

    rootdir.accept(ListVisitor())

    count_visitor = CountVisitor()
    rootdir.accept(count_visitor)
    count_visitor.show_result()
    