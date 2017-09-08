'''Player in the game GoFish'''
from src.book import Book

class Player():
    '''A player in the game GoFish'''
    def __init__(self, name):
        self.hand = list()
        self.books = list()
        self.name = name
    def accept_card(self, card):
        '''accept a card from the deck or opponent,
        this checks for any valid books'''
        self.hand.append(card)
        self.check_for_books()
    def accept_cards(self, cards):
        '''accept a list of cards'''
        for card in cards:
            self.accept_card(card)
    def check_for_books(self):
        '''check the current hand for any possible books'''
        #a dictionary of books
        possible_books = dict()
        #while the player still has cards
        while len(self.hand) > 0:
            #remove one from the top
            card = self.hand.pop()
            try:
                #check if the card's value already has a book
                #in the dict
                book = possible_books[card.value]
                #if that worked, we can add the card
                book.add(card)
            except KeyError:
                #if the dict didn't have a matching index
                #create a new book
                new_book = Book()
                #add the card to it
                new_book.add(card)
                #set the new book to the card's value in the dict
                possible_books[card.value] = new_book
        #create a list of the completed books
        complete_books = filter(lambda book: book.is_complete(),\
        list(possible_books.values()))
        #add any new books to the player's books
        self.books.extend(complete_books)
        #create a lit of the incomplete books
        incomplete_books = filter(lambda book: not book.is_complete(), \
        list(possible_books.values()))
        #add each of the book's cards back to the player's hand
        for book in incomplete_books:
            self.hand.extend(book.cards)
        #sort the player's hand smallest to largest
        self.hand.sort(key=lambda card: card.value)
    def give_cards(self, value):
        '''Return any cards with a matching value and remove them from the player's hand'''
        #capture a list of matching cards
        ret = list(filter(lambda card: card.value == value, self.hand))
        #reset the player's hand to only have non-matching cards
        self.hand = list(filter(lambda card: card.value != value, self.hand))
        #return the matching cards
        return ret