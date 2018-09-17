

class Player (object):
    def __init__(self):
        self.pl = 0
        self.hand = []
        self.takes = []
        self.points = 0

    def getID (self):
        return self.pl

    def setID (self, pl):
        self.pl = pl

    def getHand (self):
        return self.hand

    def setHand (self, hand):
        self.hand = hand

    def getTakes (self):
        return self.takes

    def setTakes (self, takes):
        self.takes = takes

    def getPoints (self):
        return self.points

    def setPoints(self, points):
        self.points = points
