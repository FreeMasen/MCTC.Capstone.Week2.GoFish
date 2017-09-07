'''Game of Go Fish'''
from src.deck import Deck
deck = Deck()
class Game():
    '''The main service that administers the rules of the game Go Fish'''
    def __init__(self):
        '''pass'''

    #gets a starting hand of 7 for player
    def get_player_hand(self):
        playerHand = list()
        for i in range(0, 7):
            playerHand.append(deck.get_card())
        return playerHand

    #asks for face value.
    #TODO: add importance to method. Does nothing except ask for now
    def ask_face_value(self):
        faceVal = int(input('Do you have a ' ))
        if faceVal < 1 or faceVal > 13:
            print("Please enter in a whole number from 1 to 13")
        else:
            pass

    #defines a main method? move to Main?
    def main(self):

        player1Hand = list(Game.get_player_hand(Game))
        player2Hand = list(Game.get_player_hand(Game))
        print(player1Hand)
        print(player2Hand)
        Game.ask_face_value(Game)


       #for c in range(0, deck.cards.__len__()):
                #print(deck.get_card())
#calls main method
if __name__ == '__main__':
    Game.main(Game)
