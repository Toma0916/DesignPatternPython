from abc import ABCMeta, abstractmethod
import random
from hand import Hand

class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def next_hand(self) -> 'Hand':
        pass

    @abstractmethod
    def study(self, win: bool):
        pass


class WinningStrategy(Strategy):

    def __init__(self):
        self.__won = False
        self.__prev_hand_value = None
    
    def next_hand(self) -> 'Hand':
        if (not self.__won):
            self.__prev_hand_value = random.randint(0, 2)
        return Hand(self.__prev_hand_value)
    
    def study(self, win: bool):
        self.__won = win
    

class ProbStrategy(Strategy):

    def __init__(self):
        self.__prev_hand_value = 0
        self.__current_hand_value = 0

        self.__history = [[1 for _ in range(3)] for _ in range(3)]

    def next_hand(self) -> 'Hand':
        bet = random.randint(1, sum(self.__history[self.__current_hand_value]))
        if (bet <= self.__history[self.__current_hand_value][0]):
            hand_value = 0
        elif bet <= (self.__history[self.__current_hand_value][0] + self.__history[self.__current_hand_value][1]):
            hand_value = 1
        else:
            hand_value = 2
        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = hand_value
        return Hand(self.__current_hand_value)
    
    def study(self, win: bool):
        if (win):
            self.__history[self.__prev_hand_value][self.__current_hand_value] += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] += 1
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] += 1
    

if __name__ == '__main__':
    ws = WinningStrategy()
    ws.next_hand()

    ps = ProbStrategy()
    ps.next_hand()