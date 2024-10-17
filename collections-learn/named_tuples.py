import collections
from random import choices
from pprint import pprint

Card = collections.namedtuple('Card', ['rank', 'suit'])

beer_card = Card('7', 'Diamonds')

class FrenchDesk:
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

deck = FrenchDesk()
some_dict = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDesk.ranks.index(card.rank)
    print(rank_value * len(some_dict) + some_dict[card.suit])
    return rank_value * len(some_dict) + some_dict[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)





