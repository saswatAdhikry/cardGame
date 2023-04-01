import random

class Card(object):
    def __init__(self, color, val, cardId):
        self.color = color
        self.val = val
        self.cardId = cardId

    def show(self):
        print("{} of {} has priority {}".format(self.val, self.color, self.cardId))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        #self.readyHands = []

    def build(self):
        cp = 52
        for color in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(2, 15):
                self.cards.append(Card(color, v, cp))
                cp -= 1
                # print('{} of {}'.format(v,color))

    def show(self):
        for c in self.cards:
            c.show()  # calls show() functiion of Card class as c has now become an instance of Card

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            # print(i)
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            # swaps card positions in self.cards[] array .. goes up to 52 swaps operations

    def dist(self):
        self.h1 = []
        self.h2 = []
        self.h3 = []
        self.h4 = []

        self.shuffle()
        for i in range(len(self.cards) - 1, 0, -4):
            self.h1.append(self.cards.pop())
            self.h2.append(self.cards.pop())
            self.h3.append(self.cards.pop())
            self.h4.append(self.cards.pop())
        return (self.h1, self.h2, self.h3, self.h4)


    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.hand = []

    def bid(self):
        pass
        #self.calls = [1:['c', 'd', 'h', 's', 'nt'],2:['c', 'd', 'h', 's', 'nt'], 3:['c', 'd', 'h', 's', 'nt'], 4:['c', 'd', 'h', 's', 'nt'], 5:['c', 'd', 'h', 's', 'nt']]
    def play(self, hand):
        pass


class Team(object):
    def __init__(self):
        self.teamA = []
        self.teamB = []

    def setTeam(self):
        players_came=[]
        for i in range(1,3):
            players_came.append(input('Enter Your name: you are aloted team :a'))
        for player in players_came:
            self.teamA.append(Player(player, 'x'))
        for i in range(1, 3):
            players_came.append(input('Enter Your name: you are aloted team :b'))
        for player in players_came[2:4]:
            self.teamB.append(Player(player, 'y'))

    def showTeam(self):
        print("player {} of team: {} got {} cards".format(self.teamA[0].name, self.teamA[0].team, self.teamA[0].hand))
        for cds in self.teamA[0].hand:
            for bds in cds:
                bds.show()
        print("player {} of team: {} got {} cards".format(self.teamB[1].name, self.teamB[1].team, self.teamB[1].hand))
        # print("team a 1st member hand: ".format(self.teamA[0].hand))

class Gane(object):
    def __init__(self):
        self.score = 0


    def getHand(self):
        deck = Deck()
        #deck.readyHands.append(deck.dist())
        readyHands = deck.dist()
        team = Team()
        team.setTeam()
        team.teamB[0].hand.append(readyHands[0])
        team.teamA[0].hand.append(readyHands[1])
        team.teamB[1].hand.append(readyHands[2])
        team.teamA[1].hand.append(readyHands[3])
        team.showTeam()

# dec = Deck()
# team = Team()
# team.setTeam()
# team.showTeam()

g = Gane()
g.getHand()

# d1 = Deck()
# x = d1.dist()
# for clist in x:
#     for cd in clist:
#         cd.show()
