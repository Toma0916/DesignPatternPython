from abc import ABCMeta, abstractmethod
import random
from hand import Hand
from strategy import WinningStrategy, ProbStrategy


class Player():

    def __init__(self, name: str, strategy: 'Strategy'):
        self.__name = name
        self.__strategy = strategy
        self.__win_count = 0
        self.__lose_count = 0
        self.__game_count = 0
    
    @property
    def name(self):
        return self.__name

    def next_hand(self):
        return self.__strategy.next_hand()
    
    def win(self):
        self.__strategy.study(True)
        self.__win_count += 1
        self.__game_count += 1
    
    def lose(self):
        self.__strategy.study(False)
        self.__lose_count += 1
        self.__game_count += 1
    
    def even(self):
        self.__game_count += 1
    
    def to_string(self):
        return ("[%s]: game count: %d, win count: %d, lose count: %d" % (self.__name, self.__game_count, self.__win_count, self.__lose_count))
    

if __name__ == '__main__':
    p1 = Player('sadistica', WinningStrategy())
    print(p1.to_string())