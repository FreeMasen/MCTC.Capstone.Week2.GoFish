'''The terminal based user interface'''
from src.card import *
from pyfiglet import Figlet
class UserInterface():
    '''User interface instance'''
    def __init__(self):
        self.figlet = Figlet('cricket')
    def welcome(self):
        '''Welcome the user to the game'''
        #create the large text for the words Go Fish
        banner = self.figlet.renderText('Go Fish')
        #wrap that text in a box
        boxed_banner = self._wrap_in_box(banner)
        #print the result
        print(boxed_banner)
        #check if the user wants the tutorial
        tutorial = self.ask_boolean('Would you like to see the tutorial?')
        #if they do
        if tutorial == True:
            #show the tutorial and return early
            return self.tutorial()
        #if the special code was entered
        if tutorial == 'auto':
            #return true
            return True
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
        return False

    def request_fish(self):
        '''request a card to fish for from the user'''
        #infinite loop
        while True:
            #ask the user for a face value
            res = input('What card are you fishing for?\n')
            #try and parse the input
            try:
                #return the result early
                return self.parse_card(res)
            except ValueError:
                #if the parse failed, display the message and keep looping
                print('I don\'t know that card please enter 2-10, A, J, Q, or K')
    def display(self, play, player1):
        '''Display a digest of play'''
        #if player1 == True, set the variables to to = p1 from = p2 otherwise do the opposite
        to_player, from_player = ('Player 1', 'Player 2') if player1 else ('Player 2', 'Player 1')
        #print what the player asked for
        print('%s asked for any %ss' % (to_player, VALUES[play.requested_value]))
        #if the opponent provided cards
        if play.was_successful():
            #print what he/she provided
            print('%s had' % from_player)
            self.print_list_of_cards(play.cards_from_opponent)
        #if the opponent didn't provide cards
        else:
            #check if the deck is empty
            if play.empty_deck:
                #if it is, show this message
                print('The ocean is empty, no more fishing')
            else:
                #if it is not, say the player went fishing
                print('%s had none, %s went fishing' % (from_player, to_player))
                #if it is player1's turn
                if player1:
                    #print what was drawn
                    print('%s caught' % to_player)
                    print(play.drawn_card)
                if not play.bonus_card is None:
                    #if the player got a bonus card say that
                    print('%s gets a bonus card for catching their request' % to_player)
                    #if player 1
                    if player1:
                        #show the bonus card
                        print(play.bonus_card)
                    #if player 2
                    else:
                        #show the drawn card (the bonus should remain secret)
                        print(play.drawn_card)
    def print_player_hand(self, hand):
        '''Print the player's hand'''
        print('Your hand')
        self.print_list_of_cards(hand)
    def print_books(self, p1_books, p2_books):
        '''print the books that are on the table'''
        print('Closed books')
        print('Player 1')
        self.print_player_books(p1_books)
        print('Player 2')
        self.print_player_books(p2_books)
    def print_player_books(self, books):
        '''print the books, 3 books per line'''
        #this list will get printed
        cards = list()
        #for each book
        for book in books:
            #add the cards to the list
            cards.extend(book.cards)
            #if we have more than 8 cards
            if len(cards) > 8:
                #print the current list
                self.print_list_of_cards(cards)
                #empty the list
                cards = list()
        #after looping check for any remainders
        if len(cards) > 0:
            #print the remainders
            self.print_list_of_cards(cards)
    def print_winner(self, message):
        '''print the winner message'''
        print(self._wrap_in_box(self.figlet.renderText(message)))
    def ask_for_card(self, request):
        '''Ask the user for a card'''
        self.ask_boolean('Do you have any %ss' % VALUES[request.value])
        print('Need to flesh out the player class to continue here')
    def parse_card(self, res):
        '''parse the user's response to a card to fish for'''
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
        #infinite loop
        while True:
            #capture the response
            res = input(question + '\n')
            #if the response is empty
            if res == '':
                #ask again and continue early
                print('Please enter y or n')
                continue
            #if the first character entered was a y
            if res[0].lower() == 'y':
                return True
            #if the first character entered was an n
            if res[0].lower() == 'n':
                return False
            #if the response was our special code
            if res == 'auto':
                return 'auto'
            #if we got her it wasn't y or n
            print('Please enter y or n')
    def _wrap_in_box(self, text):
        '''Wrap text in a box'''
        #break all lines into a list on the new line
        all_lines = text.split('\n')
        #This is where our non blank lines will live
        lines = list()
        #loop over the lines
        for line in all_lines:
            #check if the line isn't blank
            if line.rstrip() != '':
                #if not blank add them to the lines list
                lines.append(line)
        #determine the total width of the text
        width = max(map(len, lines))
        #this is the top of the box
        top = '┌─' + ('─' * width) + '─┐\n'
        #loop over all of the lines and add a pipe and space on each side
        body = map(lambda line: '│ ' + line.ljust(width) + ' │', lines)
        #this is the bottom of the box
        bottom = '\n└─' + ('─' * width) + '─┘'
        #return top then all of the body lines joined
        #with a new line then the bottom
        return top + '\n'.join(body) + bottom
    def print_list_of_cards(self, cards):
        '''print cards in a horizontal line'''
        #if our list is empty
        if len(cards) < 1:
            #return early with an empty statement
            return print(self._wrap_in_box('empty'))
        #create a list of each card as text
        card_strings = list(map(lambda card: card.__str__(), cards))
        #calculate the maximum height of all the cards (this will always be 5...)
        max_height = max(map(lambda card_str: len(card_str.split('\n')), card_strings))
        #for returning
        ret = ''
        #loop our max_height number of times
        for i in range(max_height):
            #loop over each card
            for card_string in card_strings:
                #all the current line of each
                # card to the return value
                ret += card_string.split('\n')[i]
            #if we are at the end
            if i < max_height - 1:
                #add a new line
                ret += '\n'
        #print the total 
        print(ret)
