class Card(object):
    def __init__(self,house,figure,power):
        self.id = 0
        self.house = house
        self.figure = figure
        self.power = power
        self.worth = 0
        self.owner = 0

    def getID (self):
        return self.id

    def setID (self, id):
        self.id = id

    def getHouse(self):
        return self.house

    def setHouse(self, house):
        self.house = house

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def getFigure(self):
        return self.figure

    def setFigure(self, figure):
        self.figure = figure

    def getWorth(self):
        return self.worth

    def setWorth(self, worth):
        self.worth = worth

    def getOwner(self):
        return self.owner

    def setOwner(self, owner):
        self.owner = owner
