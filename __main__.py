'''Main Go Fish module'''
from src.UI import UserInterface
from src.game import Game
def main():
    '''The main entry point for the game Go Fish'''
    ui = UserInterface()
    g = Game()
    #welcom the user
    auto = ui.welcome()
    #deal the cards
    g.deal()
    ui.print_player_hand(g.player1.hand)
    while not g.game_over():
        if not auto:
            #ask the user for a value
            value = ui.request_fish()
            #attempt to get the cards from the opponent
            computer_transfers = g.player_turn(value)
            #display the transaction to the user
            ui.display(computer_transfers, g.player1_turn)
        #ask the computer for a value
        #and attempt to get the cards from the opponent
        player_transfers = g.auto_turn()
        #display the result
        ui.display(player_transfers, g.player1_turn)
        #print the player's hand
        ui.print_player_hand(g.player1.hand)
        #print the books on the table
        ui.print_books(g.player1.books, g.player2.books)
    #print the winner
    ui.print_winner(g.tally_scores())
if __name__ == '__main__':
    main()
