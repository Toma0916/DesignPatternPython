from abc import ABCMeta, abstractmethod

class Trouble:

    def __init__(self, number: int):
        self.__number = number
    
    def get_number(self):
        return self.__number
    
    def to_string(self):
        return '[Trouble %s]' % self.__number
    

class Support(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name
        self.__next = None
    
    def set_next(self, next: 'Support') -> 'Support':
        self.__next = next
        return self.__next 
    
    def support(self, trouble: 'Trouble'):
        if (self.resolve(trouble)):
            self.__done(trouble)
        elif self.__next is not None:
            self.__next.support(trouble)
        else:
            self.__fail(trouble)
        
    def to_string(self):
        return '[ %s ]' % self.__name

    @abstractmethod
    def resolve(self, trouble: 'Trouble'):
        pass

    def __done(self, trouble: 'Trouble'):
        print('%d is resolved by %s' % (trouble.get_number(), self.__name))
    
    def __fail(self, trouble: 'Trouble'):
        print('%d cannot be resolved' % (trouble.get_number()))


class NoSupport(Support):

    def __init__(self, name: str):
        super(NoSupport, self).__init__(name)
    
    def resolve(self, trouble: 'Trouble'):
        return False
    

class LimitSupport(Support):

    def __init__(self, name: str, limit: int):
        super(LimitSupport, self).__init__(name)
        self.__limit = limit
    
    def resolve(self, trouble: 'Trouble'):
        if (trouble.get_number() < self.__limit):
            return True
        else:
            return False


class OddSupport(Support):

    def __init__(self, name: str):
        super(OddSupport, self).__init__(name)
    
    def resolve(self, trouble: 'Trouble'):
        if (trouble.get_number() % 2 == 1):
            return True
        else:
            return False


class SpecialSupport(Support):

    def __init__(self, name: str, number: int):
        super(SpecialSupport, self).__init__(name)
        self.__number = number
    
    def resolve(self, trouble: 'Trouble'):
        if (trouble.get_number() == self.__number):
            return True
        else:
            return False
        

if __name__ == '__main__':
    alice = NoSupport('Alice')
    bob = LimitSupport('Bob', 100)
    charlie = SpecialSupport('Charlie', 429)
    diana = LimitSupport('Diana', 200)
    elmo = OddSupport('Elmo')
    fred = LimitSupport('Fred', 300)

    alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)
    for i in range(500):
        alice.support(Trouble(i))
    
