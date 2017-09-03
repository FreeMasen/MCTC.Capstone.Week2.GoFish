'''The terminal based user interface'''
from src.play import *
from src.card import VALUES
from pyfiglet import Figlet
class UserInterface():
    '''User interface instance'''
    def __init__(self):
        pass
    def welcome(self):
        '''Welcome the user to the game'''
        figlet = Figlet('cricket')
        banner = figlet.renderText('Go Fish')
        boxed_banner = self._wrap_in_box(banner)
        print(boxed_banner)
        if self.ask_boolean('Would you like to see the tutorial?'):
            self.tutorial()
    def tutorial(self):
        '''print out the instructions for the user'''
        print('The instructions will go here eventually')
    def request_fish(self):
        '''request a card to fish for from the user'''
        while True:
            res = input('What card are you fishing for?')
            try:
                return self.parse_card(res)
            except ValueError:
                print('I don\'t know that card please enter 2-10, A, J, Q, or K')
    def ask_for_card(self, request, opponent):
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
                return Request(number - 1)
            #If the number was not captured above check for face cards and Ace
            if number == 1:
                if self.ask_boolean('Did you mean A?'):
                    return Request(0)
            if number == 11:
                if self.ask_boolean('Did you mean J?'):
                    return Request(10)
            if number == 12:
                if self.ask_boolean('Did you mean Q?'):
                    return Request(11)
            if number == 13:
                if self.ask_boolean('Did you mean K?'):
                    return Request(12)
        except ValueError:
            #if we have gotten here the response was not a number
            #check for the face cards and Ace
            if res.lower() == 'a':
                return Request(0)
            if res.lower() == 'j':
                return Request(10)
            if res.lower() == 'q':
                return Request(11)
            if res.lower() == 'k':
                return Request(12)
        #if we made it here the user's response was either less than 1 or 
        # greater than 13 or not any of the face card chars
        raise ValueError
    def ask_boolean(self, question):
        '''ask the user a yes or no question getting a boolean as the response'''
        while True:
            res = input(question + '\n')
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
