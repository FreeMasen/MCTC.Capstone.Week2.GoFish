'''Card'''
SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
class Card():
    '''1 standard playing card'''
    def __init__(self, suit, number):
        self.value = number
        self.suit = suit
    def get_value(self):
        '''Get the str representation of this card's value'''
        if self.value == 0:
            return 'A'
        if self.value < 10:
            return str(self.value + 1)
        if self.value == 10:
            return 'J'
        if self.value == 11:
            return 'Q'
        if self.value == 12:
            return 'K'
    def get_suit(self):
        '''Get the string representation of this card's suit'''
        return SUITS[self.suit]
    def __str__(self):
        return '%s %s' % (self.get_suit(), self.get_value())
    def __repr__(self):
        return self.__str__()
