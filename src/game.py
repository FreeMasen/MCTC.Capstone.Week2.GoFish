'''Game of Go Fish'''
from src.deck import Deck
from src.player import Player
from random import randint
from src.card import VALUES
class Game():
    '''The main service that administers the rules of the game Go Fish'''
    def __init__(self):
        self.player1 = Player('Player 1')
        self.player2 = Player('Player 2')
        self.deck = Deck()
        self.player1_turn = True
    def deal(self):
        '''populates player hand's'''
        #loop 7 times
        for _ in range(7):
            #give a card to each player
            self.player1.accept_card(self.deck.get_card())
            self.player2.accept_card(self.deck.get_card())
    def player_turn(self, value):
        '''standard player turn'''
        from_player, to_player = (self.player1, self.player2) if not self.player1_turn else (self.player2, self.player1)
        new_cards = self.check_for_card(value, from_player)
        drawn_card = None
        bonus_card = None
        if len(new_cards) < 1:
            drawn_card = self.deck.get_card()
            to_player.accept_card(drawn_card)
            if drawn_card.value == value:
                bonus_card = self.deck.get_card()
                to_player.accept_card(bonus_card)
        else:
            to_player.hand.extend(new_cards)
        self.player1_turn = not self.player1_turn
        return (value, new_cards, drawn_card, bonus_card)
    def check_for_card(self, value, from_player):
        '''check if oppoenent has any cards of that value and return a list of them if they exist'''
        return from_player.give_cards(value)

    def auto_turn(self):
        '''Automatically perform player2's turn'''
        max_len = len(self.player2.hand)
        if (max_len < 1):
            return 'Player 2 has no cards'
        index = randint(0, len(self.player2.hand) - 1)
        card = self.player2.hand[index]
        return self.player_turn(card.value)

    def tally_scores(self):
        '''Check to see who won, return a message with the result'''
        player1_score = len(self.player1.books)
        player2_score = len(self.player2.books)
        if player1_score == player2_score:
            return 'Tie game!'
        if player1_score > player2_score:
            return 'Player 1 wins!'
        return 'Player 2 wins!'
    def game_over(self):
        '''Check if the game is over yet'''
        return not len(self.player1.hand) > 0 \
        and len(self.player2.hand) > 0 \
        and len(self.deck) > 0