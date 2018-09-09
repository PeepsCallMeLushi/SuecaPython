from Menu.Classes.card import Card as c
from Menu.Classes.player import Player as p
from random import shuffle


class Game(object):
    def __init__(self):
        self.deck = []
        self.players = []

    def getDeck (self):
        return self.deck
    def getPlayers (self):
        return self.players


Match = Game()


def deckManage ():
    houses = ['s','h','c','d']
    figures = ['2','3','4','5','6','q','j','k','7','a']
    for i in range(4):
        for h in range (10):
            card = c(houses[i],figures[h],h)
            Match.getDeck().append(card)
    for i in range (40):
        card = Match.deck[i]
        if card.getFigure() == 'q':
            card.setWorth(2)
        elif card.getFigure() == 'j':
            card.setWorth(3)
        elif card.getFigure() == 'k':
            card.setWorth(4)
        elif card.getFigure() == '7':
            card.setWorth(10)
        elif card.getFigure() == 'a':
            card.setWorth(11)
        else:
            card.setWorth(0)
    for i in range (4):
        shuffle(Match.getDeck())


def playerManage():
    for i in range(4):
        player = p()
        pl = i + 1
        player.setID(pl)
        for h in range (10):
            player.getHand().append(Match.deck[h])
        for h in range (10):
            Match.deck.remove(Match.deck[0])
        Match.getPlayers().append(player)


def viewDeck():
    for i in range(40):
        card = Match.deck[i]
        print ("figure: ", card.getFigure(), "house: ", card.getHouse(),"worth:", card.getWorth(), " power:", card.getPower())


def viewPlayers():
    for i in range (4):
        player = Match.players[i]
        print("ID: ", player.getID())
        print("Hand: ")
        for h in range (10):
            card = player.hand[h]
            print (card.getFigure()+card.getHouse())


def viewOnePlayer(a):
    player = Match.players[a]
    print("ID: ", player.getID())
    print("Hand: ")
    for h in range (10):
        card = player.hand[h]
        print (card.getFigure()+card.getHouse())


def cardSort(a,b):
    if b < 9:
        player = Match.players[a]
        for i in range(b,9):
            auxcard = player.hand[i]
            player.hand[i]=player.hand[i+1]
            player.hand[i+1]=auxcard
        Match.players[a] = player


deckManage()
playerManage()
viewOnePlayer(2)
cardSort(2, 0)
viewOnePlayer(2)
