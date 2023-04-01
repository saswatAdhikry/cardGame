import random

class Card(object):
    def __init__(self, color, val, cardId):
        self.color = color
        self.val = val
        self.cardId = cardId

    def show(self):
        print ("{} of {} has priority {}".format(self.val, self.color, self.cardId))


class Deck(object):
    def __init__(self, ):
        self.cards = []
        self.build()

    def build(self):
        cp = 52
        for color in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(2, 15):
                self.cards.append(Card(color,v,cp))
                cp-=1
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
    def dist(self):
        self.h1 = []
        self.h2 = []
        self.h3 = []
        self.h4 = []

        self.shuffle()
        for i in range(len(self.cards) - 1, 0, -4):
            self.h1.append(self.cards[i])
            self.h1.append(self.cards[i+1])
            self.h1.append(self.cards[i+2])
            self.h1.append(self.cards[i+3])
        return self

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.hand =[]

    def getHand(self):
        if (self.name =='p1'):





    def bid(self):
        self.calls[1:['c','d','h','s','nt'], 2:['c','d','h','s','nt'], 3:['c','d','h','s','nt'], 4:['c','d','h','s','nt'], 5:['c','d','h','s','nt']]


    def play(self, hand):
        pass


class Team(object):
    def __init__(self ):
        self.teamA = []
        self.teamB = []

    setTeam()

    def setTeam(self):
            for player in ["p1", "p2"]:
                self.teamA.append(Player(player, a))
            for player in ["p1", "p2"]:
                self.teamB.append(Player(player, b))



