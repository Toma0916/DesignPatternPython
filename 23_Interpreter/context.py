class Context():

    def __init__(self, text):
        self.__token = text.split(' ')
        self.__current_token = self.__token[0]        

    def next_token(self):
        self.__token.pop(0)
        if 0 < len(self.__token):
            self.__current_token = self.__token[0]
        else:
            self.__current_token = None
        return self.__current_token
    
    @property
    def current_token(self):
        return self.__current_token

    def skip_token(self, token: str):        
        if (self.__current_token != token):
            raise ValueError()
        self.next_token()
    
    def current_number(self):
        return int(self.__current_token)