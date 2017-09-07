'''Game of Go Fish'''
from src.deck import Deck
from src.player import Player
class Game():
    '''The main service that administers the rules of the game Go Fish'''
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.deck = Deck()
    def deal(self, player):
        '''populates player hand's'''
        for i in range(7):
            for j in range(2):
                if j % 2 == 0:
                    self.player1.accept_card(self.deck.get_card())
                else:
                    self.player2.accept_card(self.deck.get_card())
    def check_for_card(self, value, player1):
        '''check if oppoenent has any cards of that value and transfer if they exist'''
        from_player = self.player1 if player1 else self.player2
        cards_to_transfer = from_player.give_cards(value)
        to_player = self.player2 if player1 else self.player1
        for card in cards_to_transfer:
            to_player.accept_card(card)
