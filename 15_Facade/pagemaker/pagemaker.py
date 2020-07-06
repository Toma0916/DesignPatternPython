import sys
from .exception import CannotInitializeError
from .database import Database
from .htmlwriter import HtmlWriter

class PageMaker():

    def __init__(self):
        raise CannotInitializeError

    @staticmethod
    def make_welcome_page(mailaddr: str, filename: str):

        user_name = Database.get_properties(mailaddr)                
        with open(filename, 'wb') as file:
            writer = HtmlWriter()
            writer.title('Welcome to %s`s page!' % user_name)
            writer.paragraph('%sのページへようこそ。' % user_name)
            writer.paragraph('お気軽に連絡をどうぞ。')
            writer.mailto(mailaddr, user_name)
            writer.close()
            file.write(writer.string_buffer.encode('utf-8'))

    
if __name__ == '__main__':
    PageMaker.make_welcome_page('sadistica@ut.ac.jp', 'test.html')

