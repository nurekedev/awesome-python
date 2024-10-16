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
print(len(some_dict))

print(some_dict['spades'])

def spades_high(card):
    '''
    Firs interation: 
        Card(rank='2', suit='spades') от него беру (2)
        Возвращаю 2 * 4 + 3 -> 11

    Second iteration:
        Card(rank='3', suit='spades') от него беру (3)
        Возвращаю 3 * 4 + 3 -> 15
    '''
    rank_value = FrenchDesk.ranks.index(card.rank)
    return rank_value * len(some_dict) + some_dict[card.suit]


print("Difference")
for card in sorted(deck, key=spades_high):
    print(card)


