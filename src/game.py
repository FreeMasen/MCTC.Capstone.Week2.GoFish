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
        #create our play object with
        # the value that was asked for
        play = Play(value)
        #assign to and from player depending of who's turn it is
        from_player, to_player = (self.player1, self.player2) if not self.player1_turn else (self.player2, self.player1)
        #change the current turn early so we don't forget
        self.player1_turn = not self.player1_turn
        #check of the from player has any of the requested cards
        play.cards_from_opponent = self.check_for_card(value, from_player)
        #if that list had a value
        if play.was_successful():
            #give the cards to the asker
            to_player.accept_cards(play.cards_from_opponent)
        #if the list was empty
        #check if the deck is empty
        elif not self.deck.is_empty():
            #if not, draw a card
            play.drawn_card = self.deck.get_card()
            #give it to the asker
            to_player.accept_card(play.drawn_card)
            #if the drawn card matches the exact value, and the deck is not empty
            if play.drawn_card.value == value and not self.deck.is_empty():
                #draw a bonus card
                play.bonus_card = self.deck.get_card()
                #give that to the asker
                to_player.accept_card(play.bonus_card)
        #capture if the deck is empty
        play.empty_deck = self.deck.is_empty()
        #return the play object
        return play
    def check_for_card(self, value, from_player):
        '''check if oppoenent has any cards of that value and return a list of them if they exist'''
        return from_player.give_cards(value)
    def auto_turn(self):
        '''Automatically perform player2's turn'''
        #determine which hand we are using
        card_bank = self.player2.hand if not self.player1_turn else self.player1.hand
        #calculate the max value for randint
        max_len = len(card_bank)
        #if the player's hand is empty
        if (max_len < 1):
            #set the card bank to the non-booked cards
            card_bank = self.get_non_books()
            #set the new max length
            max_len = len(card_bank)
        #pick a random index from our card bank
        index = randint(0, max_len - 1)
        #choose a card from the bank
        card = card_bank[index]
        #return the result of a player's turn with
        #this random value
        return self.player_turn(card.value)
    def get_non_books(self):
        '''Get a list of values that are not currently in closed books'''
        #list of ints 0-12
        all_cards = list(range(13))
        #remove any values that player 1 has on the table
        remove_player_one = self.remove_values(all_cards, self.player1.books)
        #remove any values that player 2 has on the table
        remove_player_two = self.remove_values(remove_player_one, self.player2.books)
        #return a list of cards for the remaining numbers (we don't care about suits)
        return list(map(lambda val: Card(0, val), remove_player_two))
    def remove_values(self, all_cards, books):
        '''remove the elements of all_cards that are included in books'''
         #loop over the player1 books
        for book in books:
            try:
                #if the value of the first card is still in all
                i = all_cards.index(book[0].value)
                #remove it
                all_cards.pop(i)
            except:
                #if the value wasn't in all, move on
                continue
        return all_cards
    def tally_scores(self):
        '''Check to see who won, return a message with the result'''
        #count p1's books
        player1_score = len(self.player1.books)
        #cound p2's books
        player2_score = len(self.player2.books)
        #if the scores are the same, its a tie!
        if player1_score == player2_score:
            #return this early
            return 'Tie game!'
        #if p1 > p2
        if player1_score > player2_score:
            #return this early
            return 'Player 1 wins!'
        #if we made it here, player 2 won
        return 'Player 2 wins!'
    def game_over(self):
        '''Check if the game is over yet'''
        #both player's hands and the deck must be empty
        return not len(self.player1.hand) > 0 \
        and not len(self.player2.hand) > 0 \
        and not len(self.deck.cards) > 0