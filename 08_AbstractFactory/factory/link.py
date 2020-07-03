from abc import ABCMeta, abstractmethod
import sys
import os
from .item import AbstractItem

class AbstractLink(AbstractItem, metaclass=ABCMeta):

    def __init__(self, caption: str, url: str):
        super(AbstractLink, self).__init__(caption)
        self.__url = url
    
    @property
    def _url(self):
        return self.__url
