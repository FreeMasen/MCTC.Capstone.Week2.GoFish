from random import randint
from src.card import Card


class Deck():
    def __init__(self):
        self.cards = set()
        for i in range(4):
            for j in range(13):
                self.cards.add(Card(i, j))
    
    def get_card(self):
        index = randint(0, len(self.cards) - 1)
        return self.cards.pop(index)
