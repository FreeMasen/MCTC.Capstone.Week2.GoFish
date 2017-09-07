'''An action in this game'''
class Play():
    '''One player's turn in game'''
    def __init__(self, number):
        self.requested_value = number
        self.cards_from_opponent = None
        self.drawn_card = None
        self.bonus_card = None
        self.empty_deck = False
        self.empty_hand = False
    def was_successful(self):
        return len(self.cards_from_opponent) > 0