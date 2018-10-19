from deck_of_cards import *

def point_total(cards):
    total = 0
    for x in cards:
        if x.num != 1:
            if x.num<11: total += x.num
            else: total += 10
    for x in cards:
        if x.num == 1 and total<11: total += 11
        elif x.num == 1: total += 1
    return total

class player:
    """each player has a name and a hand"""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        string = 'Your cards: '
        for c in self.hand: string += str(c)+' '
        return string

    def take_card(self, card):
        self.hand.append(card)

    def want_card(self):
        ask_card = input('Take another card?: ')
        if ask_card.lower() == 'y' or ask_card.lower() == 'yes': return True
        else: return False

class player_cpu(player):
    """similar to player, but automates decision-making"""

    def __init__(self, num = 1):
        self.name = 'cpu'+str(num)
        self.hand = []

    def __str__(self):
        string = self.name+'\'s cards: '
        for c in self.hand: string += str(c)+' '
        return string

    def want_card(self):
        if point_total(self.hand)<16: return True
        else: return False

class __main__:        
    deck = deck_of_cards()
    deck.shuffle()
    players = [player(input('Enter player name: '))]
    for n in range(4): players.append(player_cpu(n+1))
    for n in range(2):
        for p in players: p.take_card(deck.deal())
    can_take_card = True
    for n in range(4):
        if can_take_card:
            print(players[0].__str__())
            if players[0].want_card(): players[0].take_card(deck.deal())
            else: can_take_card = False
        for p in players[1:]:
            if p.want_card():
                p.take_card(deck.deal())
                print(p.name+' took another card')
    winner = players[0]
    for p in players:
        if point_total(p.hand)>point_total(winner.hand) and point_total(p.hand)<22 or point_total(winner.hand)>21: winner = p
    print('The winner is '+winner.name)
    for p in players: print(p.__str__()+'\t point total: '+str(point_total(p.hand)))
    
