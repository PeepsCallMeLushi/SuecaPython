import sys

from PyQt5.QtWidgets import QApplication, QDialog
from Menu.Classes import HandlerGame as hg

from Menu.Main import Ui_Dialog


class Gui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.dialog = dialog
        self.frame.setStyleSheet(
            "background-image:url('resources/backgrounds/bg.png'); background-color: transparent; background-repeat:no-repeat;")

        '''
        self.bt_ok.clicked.connect(self.handlerbt)
        self.bt_ok.setStyleSheet(
            "QPushButton{background-image:url('456.png');background-position:center;margin:1px;border-style:outset;}QPushButton:hover{}")
            self.pl_label.setStyleSheet("* { background-color: rgba(0, 0, 0, 0); }")
        '''
        self.currentPlayer = 1
        self.pl = hg.Match.players[self.currentPlayer]
        self.clicked = 0
        hg.deckManage()
        hg.playerManage()
        self.loadVisuals()
        self.loafPlayerVisuals()

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

    def loadVisuals(self):

        self.pl_label.setStyleSheet("QLabel{background-image:url('resources/backgrounds/playerlabelbg.png');}")
        self.ai1_lablel.setStyleSheet("QLabel{background-image:url('resources/backgrounds/dariobg.png');}")
        self.ai2_label.setStyleSheet("QLabel{background-image:url('resources/backgrounds/nunobg.png');}")
        self.ai3_lablel.setStyleSheet("QLabel{background-image:url('resources/backgrounds/sanguibg.png');}")
        self.play_ai1.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/ai1bg.png');}")
        self.play_ai2.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/ai2bg.png');}")
        self.play_ai3.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/ai3bg.png');}")
        self.play_pl.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/playerchoicebg.png');}")
        self.ai1_crd_01.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_02.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_03.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_04.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_05.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_06.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_07.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_08.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_09.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai1_crd_10.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai2_bt_01.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_02.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_03.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_04.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_05.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_06.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_07.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_08.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_09.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai2_bt_10.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackv.png');}")
        self.ai3_crd_01.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_02.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_03.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_04.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_05.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_06.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_07.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_08.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_09.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")
        self.ai3_crd_10.setStyleSheet("QPushButton{background-image:url('resources/backgrounds/cardbackh1.png');}")

    def loafPlayerVisuals(self):
        self.pl_bt_01.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[0].getFigure() + self.pl.hand[
                0].getHouse() + ".png');}")
        self.pl_bt_02.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[1].getFigure() + self.pl.hand[
                1].getHouse() + ".png');}")
        self.pl_bt_03.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[2].getFigure() + self.pl.hand[
                2].getHouse() + ".png');}")
        self.pl_bt_04.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[3].getFigure() + self.pl.hand[
                3].getHouse() + ".png');}")
        self.pl_bt_05.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[4].getFigure() + self.pl.hand[
                4].getHouse() + ".png');}")
        self.pl_bt_06.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[5].getFigure() + self.pl.hand[
                5].getHouse() + ".png');}")
        self.pl_bt_07.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[6].getFigure() + self.pl.hand[
                6].getHouse() + ".png');}")
        self.pl_bt_08.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[7].getFigure() + self.pl.hand[
                7].getHouse() + ".png');}")
        self.pl_bt_09.setStyleSheet(
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[8].getFigure() + self.pl.hand[
                8].getHouse() + ".png');}")
        self.pl_bt_10.setStyleSheet( 
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[9].getFigure() + self.pl.hand[
                9].getHouse() + ".png');}")

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

    def playerChoice(self):

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
            "QPushButton{background-image:url('resources/cards/" + self.pl.hand[self.clicked].getFigure() + self.pl.hand[
                self.clicked].getHouse() + ".png');}")
        hg.cardSort(self.currentPlayer, self.clicked)
        self.loafPlayerVisuals()

'''
    def handlerbt(self):
        self.lb_nome.setText("Ola")
'''

app = QApplication(sys.argv)
dialog = QDialog()

prog = Gui(dialog)
dialog.show()
sys.exit(app.exec_())
