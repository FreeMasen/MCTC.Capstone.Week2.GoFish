'''The terminal based user interface'''
from src.card import *
from pyfiglet import Figlet
class UserInterface():
    '''User interface instance'''
    def __init__(self):
        self.figlet = Figlet('cricket')
    def welcome(self):
        '''Welcome the user to the game'''
        banner = self.figlet.renderText('Go Fish')
        boxed_banner = self._wrap_in_box(banner)
        print(boxed_banner)
        if self.ask_boolean('Would you like to see the tutorial?'):
            self.tutorial()
    def tutorial(self):
        '''print out the instructions for the user'''
        print('INSTRUCTIONS'.center(43, '-'))
        print('Each Player is dealt 7 cards to start.')
        print('The rest of the cards are left in the deck')
        print('or what is referred to as the "ocean" or "pool".')
        print('Each turn a player asks for a card\'s face value.')
        print('i.e. "Do you have any 7s?"')
        print('If the other player has any of that card,')
        print('he/she must give all of them to their opponent')
        print('The asker then places these cards into "books"')
        print('A "Book" is a grouping of like cards. For example:')
        self.print_list_of_cards([Card(0,6), Card(1,6), Card(2,6), Card(3,6)])
        print('A "Book" is complete when all for like cards are added.')
        print('It is then placed face up and removed from Players hand.')
        print('If the other Player does not have any of the card asked for,')
        print('he/she then says, "Go-fish". The asker draws a card from the "Ocean".')
        print('If the card drawn matches what the player asked for,')
        print('he/she gets to draw a bonus card.')
        print('The Players turn is then over and the next Player then plays.')
        print('When all cards have been added to a "Book" and there are no more cards left, the game ends.')
        print('The player with the most face up "Books" then wins.')

    def request_fish(self):
        '''request a card to fish for from the user'''
        while True:
            res = input('What card are you fishing for?')
            try:
                return self.parse_card(res)
            except ValueError:
                print('I don\'t know that card please enter 2-10, A, J, Q, or K')
    def display(self, transfers, player1):
        to_player, from_player = ('Player 1', 'Player 2') if player1 else ('Player 2', 'Player 1')
        print('%s asked for any %ss\n' % (to_player, VALUES[transfers[0]]))
        if not transfers[1] is None or len(transfers[1]) > 1:
            print('%s had\n' % from_player)
            self.print_list_of_cards(transfers[1])
        elif not transfers[2] is None:
            print('%s had none, %s went fishing\n' % (from_player, to_player))
            print('%s caught\n' % to_player)
            print(transfers[2])
            if transfers[3] != None:
                print('%s gets a bonus card for catching their request\n' % to_player)
                print(transfers[3])
    def print_player_hand(self, hand):
        print('Your hand\n')
        self.print_list_of_cards(hand)
    def print_books(self, p1_books, p2_books):
        print('Closed books\n')
        print('Player 1\n')
        for book in p1_books:
            self.print_list_of_cards(book.cards)
        print('Player 2')
        for book in p2_books:
            self.print_books(book)
    def print_winner(self, message):
        '''print the winner message'''
        print(self._wrap_in_box(self.figlet.renderText(message)))
    def ask_for_card(self, request):
        '''Ask the user for a card'''
        self.ask_boolean('Do you have any %ss' % VALUES[request.value])
        print('Need to flesh out the player class to continue here')
    def parse_card(self, res):
        '''parse the user's response to a card to fish for'''
        #first make sure the response was only one character
        if len(res) != 1:
            #if not, raise an error
            raise ValueError
        try:
            #try to parse the resoonse as an int
            number = int(res)
            #if the value is in the number card range
            if number > 1 and number < 11:
                #return the card value (note: card values are index-like)
                return number - 1
            #If the number was not captured above check for face cards and Ace
            if number == 1:
                if self.ask_boolean('Did you mean A?'):
                    return 0
            if number == 11:
                if self.ask_boolean('Did you mean J?'):
                    return 10
            if number == 12:
                if self.ask_boolean('Did you mean Q?'):
                    return 11
            if number == 13:
                if self.ask_boolean('Did you mean K?'):
                    return 12
        except ValueError:
            #if we have gotten here the response was not a number
            #check for the face cards and Ace
            if res.lower() == 'a':
                return 0
            if res.lower() == 'j':
                return 10
            if res.lower() == 'q':
                return 11
            if res.lower() == 'k':
                return 12
        #if we made it here the user's response was either less than 1 or 
        # greater than 13 or not any of the face card chars
        raise ValueError
    def ask_boolean(self, question):
        '''ask the user a yes or no question getting a boolean as the response'''
        while True:
            res = input(question + '\n')
            if res == '':
                print('Please enter y or n')
                continue
            if res[0].lower() == 'y':
                return True
            if res[0].lower() == 'n':
                return False
            print('Please enter y or n')
    def _wrap_in_box(self, text):
        all_lines = text.split('\n')
        lines = list()
        for line in all_lines:
            if line.rstrip() != '': 
                lines.append(line)
        width = max(map(len, lines))
        top = '┌─' + ('─' * width) + '─┐\n'
        body = map(lambda line: '│ ' + line.ljust(width) + ' │', lines)
        bottom = '\n└─' + ('─' * width) + '─┘'
        return top + '\n'.join(body) + bottom
    def print_list_of_cards(self, cards):
        card_strings = list(map(lambda card: card.__str__(), cards))
        max_height = max(map(lambda card_str: len(card_str.split('\n')), card_strings))
        ret = ''
        for i in range(max_height):
            for card_string in card_strings:
                ret += card_string.split('\n')[i]
            if i < max_height - 1:
                ret += '\n'
        print(ret)
