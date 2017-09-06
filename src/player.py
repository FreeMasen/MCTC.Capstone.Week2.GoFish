from src.card import Card
from src.deck import Deck
import random

class Player():

    def __init__(self):
        self.playerHand = []

    def draw(self, deck):
        self.playerHand.append(deck.get_card(self))
        return self


class Bot():

    def __init__(self):
        self.botHand = []

    def draw(self, deck):
        self.botHand.append(deck.get_card(self))
        return self


#initial hand class
class Bot:

    botHand = []

    while len(botHand) != 7:
        botHand.append(random.randint(1,11)) #how do I implement Cards class here?
    if len(botHand) == 7:
        print("Bot has", botHand)