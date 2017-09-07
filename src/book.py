'''Book of cards'''
class Book():
    '''A collection of one card from each suit of the same value'''
    def __init__(self):
        self.cards = list()
    def add(self, card):
        '''Add a card to the book, raises a value error if the
        card is of the wrong suit or exceeds the maximum of 4 cards'''
        cards_length = len(self.cards)
        if cards_length > 0:
            if not self.cards[0].value == card.value:
                raise ValueError('A book can only contain cards of the same value %s is not %s' \
                % (self.cards[0].get_value(), card.get_value()))
        if cards_length > 4:
            raise ValueError('A book cannot contain more than 4 cards')
        self.cards.append(card)
    def is_complete(self):
        '''If the book is full'''
        return len(self.cards) > 3
