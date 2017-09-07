'''Game of Go Fish'''
from src.deck import Deck
from src.player import Player
from src.play import Play
from src.card import Card
from random import randint
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
        play = Play(value)
        from_player, to_player = (self.player1, self.player2) if not self.player1_turn else (self.player2, self.player1)
        self.player1_turn = not self.player1_turn
        play.cards_from_opponent = self.check_for_card(value, from_player)
        if play.was_successful():
            to_player.accept_cards(play.cards_from_opponent)
        elif not self.deck.is_empty():
            play.drawn_card = self.deck.get_card()
            to_player.accept_card(play.drawn_card)
            if play.drawn_card.value == value and not self.deck.is_empty():
                play.bonus_card = self.deck.get_card()
                to_player.accept_card(play.bonus_card)
        play.empty_deck = self.deck.is_empty()
        return play
    def check_for_card(self, value, from_player):
        '''check if oppoenent has any cards of that value and return a list of them if they exist'''
        return from_player.give_cards(value)
    def auto_turn(self):
        '''Automatically perform player2's turn'''
        card_bank = self.player2.hand if not self.player1_turn else self.player1.hand
        max_len = len(card_bank)
        if (max_len < 1):
            card_bank = self.get_non_books()
            max_len = len(card_bank)
        index = randint(0, max_len - 1)
        card = card_bank[index]
        return self.player_turn(card.value)
    def get_non_books(self):
        '''Get a list of values that are not currently in closed books'''
        #list of ints 0-12
        all = list(range(13))
        remove_player_one = self.remove_values(all, self.player1.books)
        remove_player_two = self.remove_values(remove_player_one, self.player2.books)
        return list(map(lambda val: Card(0, val), remove_player_two))
    def remove_values(self, all, books):
         #loop over the player1 books
        for book in self.player1.books:
            try:
                #if the value of the first card is still in all
                i = all.index(book[0].value)
                #remove it
                all.pop(i)
            except:
                #if the value wasn't in all, move on
                continue
        return all
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
        and not len(self.player2.hand) > 0 \
        and not len(self.deck.cards) > 0