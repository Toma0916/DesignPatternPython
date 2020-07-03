from abc import ABCMeta, abstractmethod
from typing import List
import argparse
import os

class AbstractBuilder(metaclass=ABCMeta):

    @abstractmethod
    def make_title(self, title: str):
        pass

    @abstractmethod
    def make_string(self, string: str):
        pass

    @abstractmethod
    def make_items(self, items: List[str]):
        pass

    @abstractmethod
    def close(self):
        pass



class Director():

    def __init__(self, builder: "AbstractBuilder"):
        self.__builder = builder
    
    def construct(self):
        self.__builder.make_title('Greeting')
        self.__builder.make_string('朝から昼にかけて')
        self.__builder.make_items(['おはようございます', 'こんにちは'])
        self.__builder.make_string('夜に')
        self.__builder.make_items(['こんばんは', 'おやすみなさい', 'さようなら'])
        self.__builder.close()


class TextBuilder(AbstractBuilder):

    def __init__(self):
        self.__string_buffer = ''

    def make_title(self, title: str):
        self.__string_buffer += '==============================\n'
        self.__string_buffer += ' 『%s』 \n' % title
        self.__string_buffer += '\n'
    
    def make_string(self, string: str):
        self.__string_buffer += '■ %s \n' % string
        self.__string_buffer += '\n'

    def make_items(self, items: str):
        for item in items:
            self.__string_buffer += '   ・%s \n' % item
        self.__string_buffer += '\n'
    
    def close(self):
        self.__string_buffer += '==============================\n'
    
    def get_result(self):
        return self.__string_buffer
    

class HTMLBuilder(AbstractBuilder):

    def __init__(self):
        self.__file_name = ''
        self.__string_buffer = ''

    def make_title(self, title: str):

        self.__file_name = os.path.dirname(__file__) + '/%s.html' % title

        self.__string_buffer += f'<html><head><title>' + title + f'</title></head><body>\n'
        self.__string_buffer += f'<h1>' + title + f'</h1>\n'
    
    def make_string(self, string: str):
        self.__string_buffer += f'<p>' + string + f'</p>\n'

    def make_items(self, items: str):
        self.__string_buffer += f'<ul>\n'
        for item in items:
            self.__string_buffer += f'<li>' + item + f'</li>\n'
        self.__string_buffer += f'</ul>\n'

    def close(self):
        self.__string_buffer += f'</body></html>'
        with open(self.__file_name, 'wb') as file:
            file.write(self.__string_buffer.encode('utf-8'))
            
    def get_result(self):
        return self.__file_name
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    args = parser.parse_args()

    if args.type == 'plane':
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)
    elif args.type == 'html':
        html_builder = HTMLBuilder()
        director = Director(html_builder)
        director.construct()
        file_name = html_builder.get_result()
        print(file_name)