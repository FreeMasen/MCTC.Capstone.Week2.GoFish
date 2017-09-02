
class Book():
    def __init__(self):
        self.cards = list()
    
    def add(self, card):
        cards_length = len(self.cards)
        if cards_length > 0:
            if not self.cards[0].value == card.value:
                raise ValueError('A book can only contain cards of the same value %s is not %s' \
                % (self.cards[0].get_value(), card.get_value()))
        if cards_length > 3:
            raise ValueError('A book cannot contain more than 4 cards')
        self.cards.append(card)
    
    def is_complete(self):
        return len(self.cards) > 3