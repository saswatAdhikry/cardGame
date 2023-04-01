import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print ("{} of {}".format(self.val, self.suit))


class Deck(object):
    def __init__(self, ):
        self.cards = []
        self.build()

    def build(self):
        for color in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for v in range(1, 14):
                self.cards.append(Card(color,v))
                #print('{} of {}'.format(v,color))

    def show(self):
        for c in self.cards:
            c.show()    # calls show() functiion of Card class as c has now become an instance of Card

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            #print(i)
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            # swaps card positions in self.cards[] array .. goes up to 52 swaps operations

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand =[]

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()



# card1 = Card('club', 5)
# card1.show()

deck = Deck()
deck.shuffle()
#deck.show()
# card = deck.draw()
# card.show()
p1 = Player('joy')
p1.draw(deck)
p1.draw(deck).draw(deck)
p1.showHand()

