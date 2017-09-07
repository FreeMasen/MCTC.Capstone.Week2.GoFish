'''Player in the game GoFish'''
from src.book import Book

class Player():
    '''A player in the game GoFish'''
    def __init__(self):
        self.hand = list()
        self.books = list()
    def accept_card(self, card):
        '''accept a card from the deck or opponent, this checks for any valid books'''
        try:
            last_matching = list(map(lambda card: card.value, self.hand)).index(card.value)
            self.hand.insert(last_matching + 1, card)
        except ValueError:
            self.hand.append(card)
        self.check_for_books()
    def check_for_books(self):
        '''check the current hand for any possible books'''
        possible_books = dict()
        while len(self.hand) > 0:
            card = self.hand.pop()
            try:
                book = possible_books[card.value]
                book.add(card)
            except KeyError:
                new_book = Book()
                new_book.add(card)
        complete_books = filter(lambda book: book.is_complete(),\
        list(possible_books.values()))
        self.books.extend(complete_books)
        incomplete_books = filter(lambda book: not book.is_complete(), \
        list(possible_books.values()))
        self.hand = list(map(lambda book: book.cards, incomplete_books))
    def give_cards(self, value):
        '''Return any cards with a matching value and remove them from the player's hand'''
        ret = list(filter(lambda card: card.value == value, self.hand))
        self.hand = list(filter(lambda card: card.value != value, self.hand))
        return ret
