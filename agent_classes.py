import random

class Proposer:
    def __init__(self):
        None



class Bidder:
    def __init__(self, _index, _tip_type, _distribution = "U"):
        self.index = _index

        if _distribution == "U":
            # Pull the value of the bidder from a uniform distribution U[0,1]
            self.value = random.uniform(0, 1)

        self.tip = self.set_tip(_tip_type)

    def set_tip(self, _tip_type):
        if _tip_type == 0:
            return self.value / 3



class Seller:
    def __init__(self):
        self.auction_started = False

    def announce_auction(self):
        self.auction_started = True



class Auction:
    def __init__(self, _n, _tip_type, _distribution = "U"):
        self.bidders = [Bidder(_distribution) for i in range(_n + 1)]

    def select_winner(self):
        # Initialize the highest bidder to be the bidder at the 0 index
        highest_bidder = 0

        # Iterate through the bidders to find the one with the highest bid
        for bidder in self.bidders:
            # If the current bidder has a higher bid than the previous highest bidder 
            # updated the highest_bidder 
            if bidder.value > self.bidders[highest_bidder]:
                highest_bidder = bidder.index
