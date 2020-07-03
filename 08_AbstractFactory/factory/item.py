from abc import ABCMeta, abstractmethod

class AbstractItem(metaclass=ABCMeta):

    def __init__(self, caption: str):
        self.__caption = caption
    
    @property
    def _caption(self):
        return self.__caption

    
    @abstractmethod
    def make_html(self) -> str:
        pass
