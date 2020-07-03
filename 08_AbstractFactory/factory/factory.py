from abc import ABCMeta, abstractmethod
import sys
import os
from .item import AbstractItem
from .link import AbstractLink
from .tray import AbstractTray
from .page import AbstractPage

def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m


class Factory(metaclass=ABCMeta):

    @staticmethod
    def get_factory(class_name: str):
        factory = None
        
        try:
            factory = get_class(class_name)()
        except ValueError:
            print('%sが見つかりません' % class_name)
            sys.exit()
        
        return factory
    
    @abstractmethod
    def create_link(self, caption: str, url: str) -> "AbstractLink":
        pass

    @abstractmethod
    def create_tray(self, caption: str) -> "AbstractTray":
        pass

    @abstractmethod
    def create_page(self, title: str, author: str) -> "AbstractPage":
        pass

