from hand import Hand
from strategy import WinningStrategy, ProbStrategy
from player import Player

if __name__ == '__main__':

    player1 = Player('sadistica', WinningStrategy())
    player2 = Player('mint', ProbStrategy())

    for i in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()

        if (next_hand1.is_stronger_than(next_hand2)):
            print('Winner: %s' % player1.name)
            player1.win()
            player2.lose()
        elif (next_hand1.is_weaker_than(next_hand2)):
            print('Winner: %s' % player2.name)
            player1.lose()
            player2.win()
        else:
            print('Even')
            player1.even()
            player2.even()
    
    print('Total result')
    print(player1.to_string())
    print(player2.to_string())
            