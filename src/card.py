suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

class Card():
    def __init__(self, suit, number):
        self.value = number
        self.suit = suit
    
    def get_value(self):
        if (self.value == 0):
            return 'A'
        if (self.value < 10):
            return str(self.value + 1)
        if (self.value == 10):
            return 'J'
        if (self.value == 11):
            return 'Q'
        if (self.value == 12):
            return 'K'

    def get_suit(self):
        return suits[self.suit]

    def __str__(self):
        return '%s %s' % (self.get_suit(), self.get_value())
    def __repr__(self):
        return self.__str__()