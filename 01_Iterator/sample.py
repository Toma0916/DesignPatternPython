from abc import ABCMeta, abstractmethod


class AbstractAggregate(metaclass=ABCMeta):
    
    def __init__(self, iterator):
        self.__iterator = iterator
    
    def iterator(self):
        """
        Iteratorを生成するメソッド
        """
        return self.__iterator(self)
    

class AbstractIterator(metaclass=ABCMeta):

    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass
    

class Book():

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name



class BookShelf(AbstractAggregate):

    def __init__(self, max_size: int):
        super(BookShelf, self).__init__(BookShelfIterator)
        self.__max_size = max_size 
        self.__books = []

    def get_book_at(self, index: int):
        return self.__books[index]

    def append_book(self, book):
        if self.get_length() < self.__max_size:
            self.__books.append(book)
        else:
            raise self.BookShelfAppendError()
    
    def get_length(self):
        return len(self.__books)

    class BookShelfAppendError(Exception):
        pass


class BookShelfIterator(AbstractIterator):

    def __init__(self, book_shelf):
        """
        BookShelfIteratorはBookShelfがどのように実装されているかを知っている
        """
        self.__book_shelf = book_shelf
        self.__index = 0

    def hasNext(self) -> bool:
        if self.__index < self.__book_shelf.get_length():
            return True 
        else:
            return False
        
    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


if __name__ == '__main__':
    
    book_shelf = BookShelf(max_size=4)
    book_shelf.append_book("悲しみよこんにちは")
    book_shelf.append_book("アンドロイドは電気羊の夢を見るか")
    book_shelf.append_book("ライ麦畑でつかまえて")
    book_shelf.append_book("新世界より")
    # book_shelf.append_book("世界の終わりとハードボイルドワンダーランド")  # これはmax_sizeを超えるための入らない（例外が発生する

    it = book_shelf.iterator()
    while (it.hasNext()):
        book = it.next()
        print(book)
