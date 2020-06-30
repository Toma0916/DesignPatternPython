from abc import ABCMeta, abstractmethod

class AbstractProduct(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class AbstractFactory(metaclass=ABCMeta):

    def create(self, owner: str):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner: str):
        pass

    @abstractmethod
    def register_product(self):
        pass


class IDCard(AbstractProduct):

    def __init__(self, owner: str):
        print('%sのカードを作ります。' % owner)
        self.__owner = owner

    def use(self):
        print('%sのカードを使います。' % self.__owner)
    
    @property
    def owner(self):
        return self.__owner


class IDCardFactory(AbstractFactory):

    def __init__(self):
        self.__owners = []
    
    def create_product(self, owner: str):
        return IDCard(owner)
    
    def register_product(self, product: IDCard):
        self.__owners.append(product.owner)
    
    @property
    def owners(self):
        return self.__owners


if __name__ == '__main__':

    factory = IDCardFactory()
    card1 = factory.create('鈴木')
    card2 = factory.create('井上')
    card3 = factory.create('四宮')

    card1.use()
    card2.use()
    card3.use()