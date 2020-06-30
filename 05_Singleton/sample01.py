from abc import ABCMeta, abstractmethod


class Singleton():

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Counter(Singleton):
    
    def __init__(self):
        self.__counter = 0

    def count_up(self):
        self.__counter += 1

    @property
    def counter(self):
        return self.__counter


if __name__ == '__main__':
    one = Counter()
    print('one.counter = %d' % one.counter)
    one.count_up()
    print('one.counter = %d' % one.counter)
    two = Counter()
    print('one.counter = %d, two.counter = %d' % (one.counter, two.counter))
    two.count_up()
    print('one.counter = %d, two.counter = %d' % (one.counter, two.counter))

    if id(one) == id(two):
        print('oneとtwoは同一のインスタンスです。')
    else:
        print('oneとtwoは異なるインスタンスです。')
