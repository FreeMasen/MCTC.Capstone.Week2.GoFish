from src.deck import Deck
def main():
    d = Deck()
    player_1 = list()
    player_2 = list()
    for i in range(7):
        player_1.append(d.get_card())
        player_2.append(d.get_card())
    print(player_1)
    print(player_2)
    print(d.cards)

if __name__ == '__main__':
    main()