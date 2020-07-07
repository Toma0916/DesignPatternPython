from abc import ABCMeta, abstractmethod
import random
import time

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, generator):
        pass
    

class DigitObserver(Observer):

    def update(self, generator):
        print('DigitObserver: %d' % generator.get_number())
        time.sleep(0.1)


class GraphObserver(Observer):

    def update(self, generator):
        print('GraphObserver: %s' % ('*' * generator.get_number()))
        time.sleep(0.1)


class NumberGenerator(metaclass=ABCMeta):

    def __init__(self):
        self.__observers = []
    
    def add_observer(self, observer):
        self.__observers.append(observer)
    
    def remove_observer(self, observer):
        self.__observers.remove(observer)
    
    def notify_observers(self):
        for obs in self.__observers:
            obs.update(self)
    
    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):

    def __init__(self):
        super(RandomNumberGenerator, self).__init__()
        self.__number = -1
    
    def get_number(self):
        return self.__number
    
    def execute(self):
        for i in range(20):
            self.__number = random.randint(0, 50)
            self.notify_observers()


if __name__ == '__main__':

    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()