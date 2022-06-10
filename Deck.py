from Card import Card
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["S", "C", "D", "H"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self, passes = 1):
        for i in range(passes):
            for j in range(len(self.cards)-1, -1, -1):
                r = random.randint(0, len(self.cards)-1)
                self.cards[j], self.cards[r] = self.cards[r], self.cards[j]

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += str(card)+"\n"
        return deck

deck = Deck()
deck.shuffle(3)
print(deck)