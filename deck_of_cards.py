import random

class card:
    """a single standard playing card"""
    def __init__(self, suit, number):
        self.suit = suit
        self.num = number

    def __str__(self):
        suit_str = {0:'♥', 1:'♦', 2: '♣', 3:'♠'}
        if self.num == 1: num = 'A'
        elif self.num == 11: num = 'J'
        elif self.num == 12: num = 'Q'
        elif self.num == 13: num = 'K'
        else: num = self.num
        return str(num)+str(suit_str[self.suit])

class deck_of_cards:
    """representation of a deck of cards"""
    
    def __init__(self):
        self.deck = [card(s, n) for s in range(3) for n in range(1, 14) ]

    def __str__(self):
        for c in self.deck: print(c.__str__())
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.deck.append(self.deck.pop(0))
        return self.deck[len(self.deck)-1]
