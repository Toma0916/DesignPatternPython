class Hand():

    names = ['グー', 'チョキ', 'パー']

    def __init__(self, hand_value):
        self.__hand_value = hand_value
    
    def is_stronger_than(self, h: 'Hand'):
        return self.__fight(h) == 1
    
    def is_weaker_than(self, h: 'Hand'):
        return self.__fight(h) == -1
    
    def __fight(self, h: 'Hand') -> int:
        if (self.__hand_value == h.__hand_value):
            return 0
        elif ((self.__hand_value + 1) % 3 == h.__hand_value):
            return 1
        else:
            return -1
    
    def to_string(self):
        return Hand.names[self.__hand_value]
    

if __name__ == '__main__':
    guu = Hand(0)
    assert guu.to_string() == 'グー'

    cho = Hand(1)
    assert cho.to_string() == 'チョキ'

    paa = Hand(2)
    assert paa.to_string() == 'パー'
