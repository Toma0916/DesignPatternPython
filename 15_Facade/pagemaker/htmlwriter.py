class HtmlWriter():

    def __init__(self):
        self.__string_buffer = ''
    
    def title(self, title: str):
        self.__string_buffer += '<html>\n'
        self.__string_buffer += '<head>\n'
        self.__string_buffer += '<title> %s </title>\n' % title
        self.__string_buffer += '</head>\n'
        self.__string_buffer += '<body>\n'
        self.__string_buffer += '<h1> %s </h1>\n' % title
    
    def paragraph(self, msg: str):
        self.__string_buffer += '<p> %s </p>\n' % msg
    
    def link(self, href: str, caption: str):
        self.paragraph('<a href=\" %s \"> %s </a>' % (href, caption))
    
    def mailto(self, mailaddr: str, username: str):
        self.link('mailto: %s' % mailaddr, username)
    
    def close(self):
        self.__string_buffer += '</body>\n'
        self.__string_buffer += '</html>\n'
    
    @property
    def string_buffer(self):
        return self.__string_buffer
    

