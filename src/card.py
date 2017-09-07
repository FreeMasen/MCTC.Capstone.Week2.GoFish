'''Card'''
SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
SYMBOLS = ['♣', '♠', '♥', '♦']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
class Card():
    '''1 standard playing card'''
    def __init__(self, suit, number):
        self.value = number
        self.suit = suit
    def get_value(self):
        '''Get the str representation of this card's value'''
        return VALUES[self.value]
    def get_suit(self):
        '''Get the string representation of this card's suit'''
        return SUITS[self.suit]
    def __str__(self):
        if self.value != 9:
            value = ' %s' % self.get_value()
        else:
            value = '%s' % self.get_value()
        return '┌────┐\n|  %s |\n| %s |\n└────┘' % (SYMBOLS[self.suit], value)
    def __repr__(self):
        return self.__str__()
