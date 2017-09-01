suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

class Card():
    def __init__(self, suit, number):
        self._value = number
        self._suit = suit
    
    def get_value(self):
        if (self._value == 0):
            return 'A'
        if (self._value < 10):
            return str(self._value + 1)
        if (self._value == 10):
            return 'J'
        if (self._value == 11):
            return 'Q'
        if (self._value == 12):
            return 'K'

    def get_suit(self):
        return suits[self._suit]

    def __str__(self):
        return '%s %s' % (self.get_suit(), self.get_value())
    def __repr__(self):
        return self.__str__()