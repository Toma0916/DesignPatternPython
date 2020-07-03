from abc import ABCMeta, abstractmethod
import sys
import os
from .item import AbstractItem

class AbstractPage(metaclass=ABCMeta):

    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author
        self.__content = []

    @property
    def _title(self):
        return self.__title

    @property
    def _author(self):
        return self.__author

    @property
    def _content(self):
        return self.__content        
    
    def add(self, item: "AbstractItem"):
        self.__content.append(item)

    
    def output(self):
        filename = os.path.dirname(os.path.dirname(__file__)) + '/%s.html' % self.__title
        outputs = self.make_html()
        with open(filename, 'wb') as file:
            file.write(outputs.encode('utf-8'))
            
    @abstractmethod
    def make_html(self) -> str:
        pass


