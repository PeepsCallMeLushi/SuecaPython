import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from classes import HandlerGame as hg
import time
from visuals.Main import *

directions = os.path.dirname(os.path.realpath(__file__))
directions = directions[:-7]
'''Thread feita para um ciclo ifinito poder correr'''
class myFirstThread(QtCore.QThread):
    def __init__(self, funcao, *args):
        QtCore.QThread.__init__(self)
        self.funcao = funcao
        self.args = args

    def __del__(self):
        self.wait()

    def run(self):
        self.funcao(*self.args)
        return

'''Main'''
class Gui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.dialog = dialog
        self.frame.setStyleSheet(
            "background-image:url('"+directions+"resources/backgrounds/bg.png'); background-color: transparent; background-repeat:no-repeat;")
        hg.deckManage()
        hg.playerManage()
        '''Define o nipe em mesa'''
        self.playHouse = 'E'
        '''Define o trunfo'''
        self.powerHouse = hg.powerHouseSelection()
        '''Contador global de cartas dos jogadores'''
        self.availCards = 10
        '''contador de vez'''
        self.counter = 0
        '''variavel para dizer à função que carta do jogador que foi clicada'''
        self.clicked = 0
        '''Invoca a função que carrega o jogo com os visuais basicos'''
        self.loadVisuals()
        '''Invoca a função que carrega o jogo com os Do jogador'''
        self.loadPlayerVisuals()
        '''instancia os botões do jogador'''
        self.pl_bt_01.clicked.connect(self.btn1)
        self.pl_bt_02.clicked.connect(self.btn2)
        self.pl_bt_03.clicked.connect(self.btn3)
        self.pl_bt_04.clicked.connect(self.btn4)
        self.pl_bt_05.clicked.connect(self.btn5)
        self.pl_bt_06.clicked.connect(self.btn6)
        self.pl_bt_07.clicked.connect(self.btn7)
        self.pl_bt_08.clicked.connect(self.btn8)
        self.pl_bt_09.clicked.connect(self.btn9)
        self.pl_bt_10.clicked.connect(self.btn10)
        self.pl_bt_01.clicked.connect(self.playerChoice)
        self.pl_bt_02.clicked.connect(self.playerChoice)
        self.pl_bt_03.clicked.connect(self.playerChoice)
        self.pl_bt_04.clicked.connect(self.playerChoice)
        self.pl_bt_05.clicked.connect(self.playerChoice)
        self.pl_bt_06.clicked.connect(self.playerChoice)
        self.pl_bt_07.clicked.connect(self.playerChoice)
        self.pl_bt_08.clicked.connect(self.playerChoice)
        self.pl_bt_09.clicked.connect(self.playerChoice)
        self.pl_bt_10.clicked.connect(self.playerChoice)

        '''invoca a thread com a função e inicia a mesma'''
        self.genericThread = myFirstThread(self.gameMechs,self.availCards)
        self.genericThread.start()

    '''Função que faz o jogo correr a partir das outras funções'''
    def gameMechs(self, a):
        while a != 0:
            playerID = hg.Match.players[self.counter].getID()
            if playerID == 1:
                self.enablePlayerButtons()
            elif playerID != 1:
                self.botDecisionMaking()
            if self.counter == 4:
                self.roundEnd()

    '''Ciclo de decisão dos bots'''
    def botDecisionMaking(self):
        time.sleep(1)
        bot = hg.Match.players[self.counter]
        bestCard = 0
        power = 0

        for i in range(4):
            if hg.Match.players[i].getID()== bot.getID():
                botBot = hg.Match.players[i]
        if self.counter == 0:
            for i in range(self.availCards):
                if bot.hand[i].getPower() > power:
                    power = bot.hand[i].getPower()
                    bestCard = i
            self.playHouse = botBot.hand[bestCard].getHouse()

        elif self.counter != 0:
            for i in range(self.availCards):
                if bot.hand[i].getPower() > power and bot.hand[i].getHouse() == self.playHouse:
                    power = bot.hand[i].getPower()
                    bestCard = i

        if bot.getID() == 2:
            self.ai3Management(botBot,bestCard)
            hg.Match.table.append(bot.hand[bestCard])
        elif bot.getID() == 3:
            self.ai2Management(botBot,bestCard)
            hg.Match.table.append(bot.hand[bestCard])
        elif bot.getID() == 4:
            self.ai1Management(botBot, bestCard)
            hg.Match.table.append(bot.hand[bestCard])

        hg.cardSort(self.counter, bestCard)
        self.counter = self.counter + 1

    '''Gestão dos visais do bot 3'''
    def ai3Management(self, a, b):
        self.play_ai3.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"resources/cards/" + a.hand[b].getFigure() + a.hand[
                b].getHouse() + ".png');}")
        if self.ai3_crd_10.isVisible():
            self.ai3_crd_10.hide()
        elif self.ai3_crd_09.isVisible():
            self.ai3_crd_09.hide()
        elif self.ai3_crd_08.isVisible():
            self.ai3_crd_08.hide()
        elif self.ai3_crd_07.isVisible():
            self.ai3_crd_07.hide()
        elif self.ai3_crd_06.isVisible():
            self.ai3_crd_06.hide()
        elif self.ai3_crd_05.isVisible():
            self.ai3_crd_05.hide()
        elif self.ai3_crd_04.isVisible():
            self.ai3_crd_04.hide()
        elif self.ai3_crd_03.isVisible():
            self.ai3_crd_03.hide()
        elif self.ai3_crd_02.isVisible():
            self.ai3_crd_02.hide()
        elif self.ai3_crd_01.isVisible():
            self.ai3_crd_01.hide()

    '''Gestão dos visais do bot 2'''
    def ai2Management(self,a,b):
        self.play_ai2.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"resources/cards/" + a.hand[b].getFigure() + a.hand[
                b].getHouse() + ".png');}")
        if self.ai2_bt_10.isVisible():
            self.ai2_bt_10.hide()
        elif self.ai2_bt_09.isVisible():
            self.ai2_bt_09.hide()
        elif self.ai2_bt_08.isVisible():
            self.ai2_bt_08.hide()
        elif self.ai2_bt_07.isVisible():
            self.ai2_bt_07.hide()
        elif self.ai2_bt_06.isVisible():
            self.ai2_bt_06.hide()
        elif self.ai2_bt_05.isVisible():
            self.ai2_bt_05.hide()
        elif self.ai2_bt_04.isVisible():
            self.ai2_bt_04.hide()
        elif self.ai2_bt_03.isVisible():
            self.ai2_bt_03.hide()
        elif self.ai2_bt_02.isVisible():
            self.ai2_bt_02.hide()
        elif self.ai2_bt_01.isVisible():
            self.ai2_bt_01.hide()

    '''Gestão dos visais do bot 1'''
    def ai1Management(self,a,b):
        self.play_ai1.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"resources/cards/" + a.hand[b].getFigure() + a.hand[
                b].getHouse() + ".png');}")
        if self.ai1_crd_10.isVisible():
            self.ai1_crd_10.hide()
        elif self.ai1_crd_09.isVisible():
            self.ai1_crd_09.hide()
        elif self.ai1_crd_08.isVisible():
            self.ai1_crd_08.hide()
        elif self.ai1_crd_07.isVisible():
            self.ai1_crd_07.hide()
        elif self.ai1_crd_06.isVisible():
            self.ai1_crd_06.hide()
        elif self.ai1_crd_05.isVisible():
            self.ai1_crd_05.hide()
        elif self.ai1_crd_04.isVisible():
            self.ai1_crd_04.hide()
        elif self.ai1_crd_03.isVisible():
            self.ai1_crd_03.hide()
        elif self.ai1_crd_02.isVisible():
            self.ai1_crd_02.hide()
        elif self.ai1_crd_01.isVisible():
            self.ai1_crd_01.hide()

    '''Carregamento dos visais do jogo'''
    def loadVisuals(self):
        self.wwcd.setHidden(True)
        self.lldl.setHidden(True)
        self.wwcd.setStyleSheet(
            "background-image:url('"+directions+"resources/backgrounds/wwcdbg.png'); background-color: transparent; background-repeat:no-repeat;")
        self.lldl.setStyleSheet(
            "background-image:url('"+directions+"resources/backgrounds/lldlbg.png'); background-color: transparent; background-repeat:no-repeat;")
        self.powerHouseLabel.setStyleSheet("QLabel{background-image:url('');}")
        self.allyTeam_label.setStyleSheet("QLabel{background-image:url('');}")
        self.enemyTeam_label.setStyleSheet("QLabel{background-image:url('');}")
        self.atPoints.setStyleSheet("QLabel{background-image:url('');}")
        self.etPoints.setStyleSheet("QLabel{background-image:url('');}")
        self.pl_label.setStyleSheet("QLabel{background-image:url('');}")
        self.ai1_lablel.setStyleSheet("QLabel{background-image:url('');}")
        self.ai2_label.setStyleSheet("QLabel{background-image:url('');}")
        self.ai3_lablel.setStyleSheet("QLabel{background-image:url('');}")
        self.play_ai1.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_ai2.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_ai3.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_pl.setStyleSheet("QPushButton{background-image:url('');}")
        self.powerHouseIcon.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"resources/cards/" + self.powerHouse + ".png');}")
        self.ai1_crd_01.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_02.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_03.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_04.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_05.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_06.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_07.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_08.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_09.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_10.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackh1.png');}")
        self.ai2_bt_01.setStyleSheet("QPushButton{background-image:url('"+directions+"resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_02.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_03.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_04.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_05.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_06.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_07.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_08.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_09.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai2_bt_10.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackv.png');}")
        self.ai3_crd_01.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_02.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_03.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_04.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_05.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_06.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_07.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_08.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_09.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")
        self.ai3_crd_10.setStyleSheet("QPushButton{background-image:url('"+directions+"backgrounds/cardbackh1.png');}")

    '''Carregamento dos visais do jogador'''
    def loadPlayerVisuals(self):
        for i in range(4):
            if hg.Match.players[i].getID()==1:
                human = hg.Match.players[i]

        self.pl_bt_01.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[0].getFigure() + human.hand[
                0].getHouse() + ".png');}")
        self.pl_bt_02.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[1].getFigure() + human.hand[
                1].getHouse() + ".png');}")
        self.pl_bt_03.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[2].getFigure() + human.hand[
                2].getHouse() + ".png');}")
        self.pl_bt_04.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[3].getFigure() + human.hand[
                3].getHouse() + ".png');}")
        self.pl_bt_05.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[4].getFigure() + human.hand[
                4].getHouse() + ".png');}")
        self.pl_bt_06.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[5].getFigure() + human.hand[
                5].getHouse() + ".png');}")
        self.pl_bt_07.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[6].getFigure() + human.hand[
                6].getHouse() + ".png');}")
        self.pl_bt_08.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[7].getFigure() + human.hand[
                7].getHouse() + ".png');}")
        self.pl_bt_09.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[8].getFigure() + human.hand[
                8].getHouse() + ".png');}")
        self.pl_bt_10.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[9].getFigure() + human.hand[
                9].getHouse() + ".png');}")

    '''Série de funões para dizer ao jogo que butão foi carregado'''
    def btn1 (self):
        self.clicked=0

    def btn2 (self):
        self.clicked=1

    def btn3 (self):
        self.clicked=2

    def btn4 (self):
        self.clicked=3

    def btn5 (self):
        self.clicked=4

    def btn6 (self):
        self.clicked=5

    def btn7 (self):
        self.clicked=6

    def btn8 (self):
        self.clicked=7

    def btn9 (self):
        self.clicked=8

    def btn10 (self):
        self.clicked=9

    '''Reabilita os botões do jogador face o que este pode ou não jogar para evitar renuncia'''
    def enablePlayerButtons(self):
        playHouseInHand = 0

        for i in range(4):
            if hg.Match.players[i].getID() == 1:
                human = hg.Match.players[i]

        for i in range (self.availCards):
            if human.hand[i].getHouse() == self.playHouse:
                playHouseInHand = playHouseInHand + 1

        if self.counter == 0:
            self.pl_bt_01.setDisabled(False)
            self.pl_bt_02.setDisabled(False)
            self.pl_bt_03.setDisabled(False)
            self.pl_bt_04.setDisabled(False)
            self.pl_bt_05.setDisabled(False)
            self.pl_bt_06.setDisabled(False)
            self.pl_bt_07.setDisabled(False)
            self.pl_bt_08.setDisabled(False)
            self.pl_bt_09.setDisabled(False)
            self.pl_bt_10.setDisabled(False)

        elif self.counter !=0 and playHouseInHand == 0:
            self.pl_bt_01.setDisabled(False)
            self.pl_bt_02.setDisabled(False)
            self.pl_bt_03.setDisabled(False)
            self.pl_bt_04.setDisabled(False)
            self.pl_bt_05.setDisabled(False)
            self.pl_bt_06.setDisabled(False)
            self.pl_bt_07.setDisabled(False)
            self.pl_bt_08.setDisabled(False)
            self.pl_bt_09.setDisabled(False)
            self.pl_bt_10.setDisabled(False)

        elif self.counter != 0:
            for i in range (self.availCards):
                if human.hand[i].getHouse() == self.playHouse:
                    if i == 0:
                        self.pl_bt_01.setDisabled(False)
                    elif i == 1:
                        self.pl_bt_02.setDisabled(False)
                    elif i == 2:
                        self.pl_bt_03.setDisabled(False)
                    elif i == 3:
                        self.pl_bt_04.setDisabled(False)
                    elif i == 4:
                        self.pl_bt_05.setDisabled(False)
                    elif i == 5:
                        self.pl_bt_06.setDisabled(False)
                    elif i == 6:
                        self.pl_bt_07.setDisabled(False)
                    elif i == 7:
                        self.pl_bt_08.setDisabled(False)
                    elif i == 8:
                        self.pl_bt_09.setDisabled(False)
                    elif i == 9:
                        self.pl_bt_10.setDisabled(False)

    '''Eventos depois de o jogador escolher a carta'''
    def playerChoice(self):

        self.pl_bt_01.setDisabled(True)
        self.pl_bt_02.setDisabled(True)
        self.pl_bt_03.setDisabled(True)
        self.pl_bt_04.setDisabled(True)
        self.pl_bt_05.setDisabled(True)
        self.pl_bt_06.setDisabled(True)
        self.pl_bt_07.setDisabled(True)
        self.pl_bt_08.setDisabled(True)
        self.pl_bt_09.setDisabled(True)
        self.pl_bt_10.setDisabled(True)


        player = 0
        for i in range(4):
            if hg.Match.players[i].getID()==1:
                human = hg.Match.players[i]
                player = i

        if self.pl_bt_10.isVisible():
            self.pl_bt_10.hide()
        elif self.pl_bt_09.isVisible():
            self.pl_bt_09.hide()
        elif self.pl_bt_08.isVisible():
            self.pl_bt_08.hide()
        elif self.pl_bt_07.isVisible():
            self.pl_bt_07.hide()
        elif self.pl_bt_06.isVisible():
            self.pl_bt_06.hide()
        elif self.pl_bt_05.isVisible():
            self.pl_bt_05.hide()
        elif self.pl_bt_04.isVisible():
            self.pl_bt_04.hide()
        elif self.pl_bt_03.isVisible():
            self.pl_bt_03.hide()
        elif self.pl_bt_02.isVisible():
            self.pl_bt_02.hide()
        elif self.pl_bt_01.isVisible():
            self.pl_bt_01.hide()

        self.play_pl.setStyleSheet(
            "QPushButton{background-image:url('"+directions+"cards/" + human.hand[self.clicked].getFigure() + human.hand[
                self.clicked].getHouse() + ".png');}")

        if self.counter == 0:
            self.playHouse = human.hand[self.clicked].getHouse()

        hg.Match.table.append(human.hand[self.clicked])
        hg.cardSort(player, self.clicked)
        self.loadPlayerVisuals()
        self.counter = self.counter + 1

    ''' Ciclo de acontecimentos depois de os quatro jogadores terem jogado'''
    def roundEnd(self):
        allyTeam = 0
        enemyTeam = 0
        self.availCards = self.availCards - 1
        hg.Match.table = hg.tableSort(hg.Match.table,self.playHouse, self.powerHouse)
        hg.Match.players = hg.playerSort(hg.Match.players, hg.Match.table)
        for i in range(4):
            if hg.Match.players[i].getID() == 1 or hg.Match.players[i].getID() == 3:
                allyTeam = allyTeam + hg.Match.players[i].getPoints()
            elif hg.Match.players[i].getID() == 2 or hg.Match.players[i].getID() == 4:
                enemyTeam = enemyTeam + hg.Match.players[i].getPoints()
        self.counter = 0
        time.sleep(3)
        self.atPoints.setText(str(allyTeam))
        self.etPoints.setText(str(enemyTeam))
        self.play_ai1.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_ai2.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_ai3.setStyleSheet("QPushButton{background-image:url('');}")
        self.play_pl.setStyleSheet("QPushButton{background-image:url('');}")
        if self.availCards == 0:
            if allyTeam > enemyTeam:
                self.wwcd.setHidden(False)
                time.sleep(10)
                sys.exit(app.exec_())
            elif allyTeam < enemyTeam:
                time.sleep(5)
                self.lldl.setHidden(False)
                time.sleep(10)
                sys.exit(app.exec_())

app = QApplication(sys.argv)
dialog = QDialog()
prog = Gui(dialog)
window = QMainWindow()
dialog.setWindowTitle("Sueca Python")
dialog.show()
sys.exit(app.exec_())