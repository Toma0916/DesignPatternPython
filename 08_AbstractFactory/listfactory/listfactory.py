from abc import ABCMeta, abstractmethod
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from factory.factory import Factory
from factory.link import AbstractLink
from factory.tray import AbstractTray
from factory.page import AbstractPage

class ListFactory(Factory):

    def create_link(self, caption: str, url: str):
        return ListLink(caption, url)

    def create_tray(self, caption: str):
        return ListTray(caption)
    
    def create_page(self, title: str, author: str):
        return ListPage(title, author)


class ListLink(AbstractLink):

    def __init(self, caption: str, url: str):
        super(AbstractLink, self).__init__(caption, url)
    
    def make_html(self):
        return f" <li><a href=\"{self._url}\">" + self._caption + f"</a></li>\n"

class ListTray(AbstractTray):

    def __init__(self, caption):
        super(ListTray, self).__init__(caption)
    
    def make_html(self):
        buffer = f''
        buffer += f'<li>\n'
        buffer += self._caption + f'\n'
        buffer += f'<ul>\n'
        for item in self._tray:
            buffer += item.make_html()
        buffer += f'</ul>'
        buffer += f'</li>'
        return buffer
    

class ListPage(AbstractPage):

    def __init__(self, title: str, author: str):
        super(ListPage, self).__init__(title, author)

    def make_html(self):
        buffer = f''
        buffer += f'<html><head><title>' + self._title + '</title><head>\n'
        buffer += f'<body>\n'
        buffer += f'<h1>' + self._title + f'</h1>'
        buffer += f'<ul>\n'
        for content in self._content:
            buffer += content.make_html()
        buffer += f'</ul>'
        buffer += f'<hr><address>' + self._author + f'</address>'
        buffer += f'</body></html>\n'
        return buffer
