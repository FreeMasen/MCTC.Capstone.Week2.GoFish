'''An action in this game'''
class Request():
    '''A request for a cards'''
    def __init__(self, number):
        self.card = number
        self.response = None
    def respond(self, response):
        '''Add the response object to the request'''
        self.response = response
class Response():
    '''The player's response to a request'''
    def __init__(self, positive, cards):
        self.positive = positive
        self.cards = cards