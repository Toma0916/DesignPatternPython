from copy import deepcopy
import random
import time

class Memento():

    def __init__(self, money: int):
        self.__money = money
        self.__fruits = []
    
    def get_money(self):
        return self.__money

    def add_fruits(self, fruit: str):
        self.__fruits.append(fruit)
    
    def get_fluits(self):
        return deepcopy(self.__fruits)


class Gamer():

    __fruits_name = ['リンゴ', 'ぶどう', 'バナナ', 'みかん']

    def __init__(self, money: int):
        self.__money = money
        self.__fruits = []
    
    def get_money(self):
        return self.__money

    def bet(self):
        dice = random.randint(1, 6)
        if dice == 1:
            self.__money += 100
            print('所持金が増えました.')
        elif dice == 2:
            self.__money /= 2
            print('所持金が半分になりました.')
        elif dice == 6:
            f = self.__get_fruit()
            print('フルーツ（%s）が半分になりました.' % f)
            self.__fruits.append(f)
        else:
            print('何も起こりませんでした.')
    
    def __get_fruit(self):
        prefix = ''
        if random.randint(0, 1):
            prefix = 'おいしい'
        return prefix + Gamer.__fruits_name[random.randint(0, len(Gamer.__fruits_name)-1)]
    
    def to_string(self):
        return '[money= %d, fluits= %s]' % (self.__money, self.__fruits)
    
    def create_memento(self):
        m = Memento(self.__money)
        for f in self.__fruits:
            if 'おいしい' in f:
                m.add_fruits(f)
        return m
    
    def restore_memento(self, memento: 'Memento'):
        self.__money = memento.get_money()
        self.__fruits = memento.get_fluits()



if __name__ == '__main__':

    gamer = Gamer(100)
    memento = gamer.create_memento()
    for i in range(100):
        print('=== %d' % i)
        print('現状: %s' % gamer.to_string())
        gamer.bet()
        print('所持金は%d円になりました.' % gamer.get_money())

        if (gamer.get_money() > memento.get_money()):
            print('     （だいぶ増えたので、現在の状態を保存しておこう）')
            memento = gamer.create_memento()
        else:
            print('     （だいぶ減ったので、以前の状態に復帰しよう）')
            gamer.restore_memento(memento)
        
        time.sleep(0.1)
