from Menu.Classes.card import Card as c
from Menu.Classes.player import Player as p
from random import shuffle


class Game(object):
    def __init__(self):
        self.deck = []
        self.players = []
        self.table = []

    def getDeck (self):
        return self.deck
    def getPlayers (self):
        return self.players


Match = Game()

'''Cria o baralho e as cartas'''
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

'''Cria os jogadores e atribui as cartas aos mesmos depois do baralho ser criado'''
def playerManage():
    powerhouse = Match.deck[39].getHouse()
    for i in range(4):
        player = p()
        pl = i + 1
        player.setID(pl)
        for h in range (10):
            if Match.deck[h].getHouse() == powerhouse:
                Match.deck[h].setPower(Match.deck[h].getPower()+10)
            Match.deck[h].setOwner(pl)
            player.getHand().append(Match.deck[h])
        for h in range (10):
            Match.deck.remove(Match.deck[0])
        Match.getPlayers().append(player)


'''Função para debug, serve para ver as cartas to baralho'''
def viewDeck():
    for i in range(40):
        card = Match.deck[i]
        print ("figure: ", card.getFigure(), "house: ", card.getHouse(),"worth:", card.getWorth(), " power:", card.getPower())


'''Função para debug, serve para ver as cartas de todos os jogadores e os seus IDs'''
def viewPlayers():
    for i in range (4):
        player = Match.players[i]
        print("ID: ", player.getID())
        print("Hand: ")
        for h in range (10):
            card = player.hand[h]
            print (card.getFigure(),card.getHouse(),card.getOwner())

'''Função para debug, serve para ver as cartas de um jogador e o seu ID'''
def viewOnePlayer(a):
    player = Match.players[a]
    print("ID: ", player.getID())
    print("Hand: ")
    for h in range (10):
        card = player.hand[h]
        print (card.getFigure()+card.getHouse())

'''Ordena as cartas do jogador. Empurra a carta (supostamente) jogada para o fim'''
def cardSort(a,b):
    if b < 9:
        player = Match.players[a]
        for i in range(b,9):
            auxcard = player.hand[i]
            player.hand[i]=player.hand[i+1]
            player.hand[i+1]=auxcard
        Match.players[a] = player

'''ordena as cartas por ordem de importancia Trunfo>naipe da carta puxada>resto. Cada uma destas categorias é ordenada depois por valor dentro de si'''
def tableSort(a,b,c):
    currentPowerHouse =c
    powerHouseCount = 0
    currentPlayHouse = b
    playHouseCount = 0
    lista = a
    players = Match.players

    if currentPowerHouse != currentPlayHouse:
        for i in range (4):
            if lista[i].getHouse() == currentPowerHouse:
                powerHouseCount = powerHouseCount + 1

            elif lista[i].getHouse() == currentPlayHouse:
                playHouseCount = playHouseCount + 1

        if powerHouseCount != 4:
            for i in range (powerHouseCount):
                for h in range (i, 4):
                    if lista[h].getHouse() == currentPowerHouse:
                        aux = lista[h]
                        lista[h] = lista[i]
                        lista[i] = aux
                        break

            for i in range(powerHouseCount):
                for h in range(powerHouseCount):
                    if lista[h].getPower() < lista[h + 1].getPower():
                        aux = lista[h]
                        lista[h] = lista[h + 1]
                        lista[h + 1] = aux

        elif powerHouseCount == 4:
            for i in range(3):
                for h in range(3):
                    if lista[h].getPower() < lista[h + 1].getPower():
                        aux = lista[h]
                        lista[h] = lista[h + 1]
                        lista[h + 1] = aux

        if playHouseCount != 4:
            for i in range(powerHouseCount,powerHouseCount+playHouseCount):
                for h in range (i, 4):
                    if lista[h].getHouse() == currentPlayHouse:
                        aux = lista[h]
                        lista[h] = lista[i]
                        lista[i] = aux
                        break
            for i in range(playHouseCount):
                for h in range(powerHouseCount,powerHouseCount+playHouseCount-1):
                    if lista[h].getPower() < lista[h + 1].getPower():
                        aux = lista[h]
                        lista[h] = lista[h + 1]
                        lista[h + 1] = aux
        elif playHouseCount == 4:
            for i in range(3):
                for h in range(3):
                    if lista[h].getPower() < lista[h + 1].getPower():
                        aux = lista[h]
                        lista[h] = lista[h + 1]
                        lista[h + 1] = aux

    elif currentPlayHouse == currentPlayHouse:
        for i in range (3):
            for h in range (3):
                if lista[h].getPower()< lista[h+1].getPower():
                    aux = lista[h]
                    lista[h] = lista[h+1]
                    lista[h+1] = aux
    else:
        for i in range (3):
            for h in range (3):
                if lista[h].getPower()< lista[h+1].getPower():
                    aux = lista[h]
                    lista[h] = lista[h+1]
                    lista[h+1] = aux

    for i in range(4):
        if players[i].getID() == lista[0].getOwner():
            score = players[i].getPoints()
            for h in range (4):
                score = score + lista[h].getWorth()

            players[i].setPoints(score)
    return lista

'''Função para debug, serve para ver as cartas postas em mesa'''
def tableView():
    for i in range(4):
        card = Match.table[i]
        print (card.getFigure(), card.getHouse(), card.getOwner(), card.getPower())

'''Ordena a lista de jogadores face a ordem de importancia das cartas que foram jogadas'''
def playerSort(a, b):
    cardList = b
    unsortedList = a
    sortedList = []
    counter = 5
    max = 5
    min = cardList[0].getOwner()

    for i in range (min, max):
        for h in range (4):
            play = unsortedList[h]
            if play.getID() == i:
                sortedList.append(play)
                counter = counter - 1

    if counter != 1:
        max = counter
        min = 1
        for i in range(min, max):
            for h in range(4):
                play = unsortedList[h]
                if play.getID() == i:
                    sortedList.append(play)

    for i in range(4):
        Match.table.remove(Match.table[0])

    return sortedList

'''Devolve a carta que define o trunfo, assume sempre a ultima carta do baralho'''
def powerHouseSelection():
    return Match.players[3].hand[9].getHouse()
