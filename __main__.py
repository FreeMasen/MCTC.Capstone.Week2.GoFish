'''Main Go Fish module'''
from src.UI import UserInterface
from src.game import Game
def main():
    '''The main entry point for the game Go Fish'''
    ui = UserInterface()
    g = Game()
    ui.welcome()
    g.deal()
    while not g.game_over():
        value = ui.request_fish()
        computer_transfers = g.player_turn(value)
        ui.display(computer_transfers, True)
        player_transfers = g.auto_turn()
        ui.display(player_transfers, False)
        ui.print_player_hand(g.player1.hand)
        ui.print_books(g.player1.books, g.player2.books)
    ui.print_winner(g.tally_scores())
if __name__ == '__main__':
    main()
