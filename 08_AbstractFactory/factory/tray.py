from abc import ABCMeta, abstractmethod
import sys
import os
from .item import AbstractItem

class AbstractTray(AbstractItem, metaclass=ABCMeta):

    def __init__(self, caption: str):
        super(AbstractTray, self).__init__(caption)
        self.__tray = []

    @property
    def _tray(self):
        return self.__tray
    
    def add(self, item: "AbstractItem"):
        self.__tray.append(item)

