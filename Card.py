class Card(object):
    ranks = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K"}
    suits = {"D":"\u2662", "C":"\u2663", "S":"\u2664", "H":"\u2665"}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.ranks[self.value]+self.suits[self.suit]