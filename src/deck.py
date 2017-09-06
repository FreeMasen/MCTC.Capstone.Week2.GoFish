'''Deck of cards'''
from random import randint
from src.card import Card
class Deck():
    '''Deck of cards, initialized with a standard 52 cards'''
    def __init__(self):
        self.cards = list()
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(i, j))
    def get_card(self):
        '''Get a card from a random position in the deck'''
        index = randint(0, len(self.cards) - 1)
        return self.cards.pop(index)

    def __str__(self):
        return '%s' % (self.get_card())
    def __repr__(self):
        return self.__str__()


