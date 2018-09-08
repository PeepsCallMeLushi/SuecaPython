import sys

from PyQt5.uic.properties import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from Menu.Main import Ui_Dialog


class Gui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.dialog = dialog
        self.frame.setStyleSheet(
            "background-image:url('resources/backgrounds/bg.png'); background-color: transparent; background-repeat:no-repeat;")
        self.loadVisuals()


        '''
        self.bt_ok.clicked.connect(self.handlerbt)
        self.bt_ok.setStyleSheet(
            "QPushButton{background-image:url('456.png');background-position:center;margin:1px;border-style:outset;}QPushButton:hover{}")
            self.pl_label.setStyleSheet("* { background-color: rgba(0, 0, 0, 0); }")
        '''



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
        self.pl_bt_01.setStyleSheet("QPushButton{background-image:url('resources/cards/2s.png');}")
        self.pl_bt_02.setStyleSheet("QPushButton{background-image:url('resources/cards/3s.png');}")
        self.pl_bt_03.setStyleSheet("QPushButton{background-image:url('resources/cards/4s.png');}")
        self.pl_bt_04.setStyleSheet("QPushButton{background-image:url('resources/cards/5s.png');}")
        self.pl_bt_05.setStyleSheet("QPushButton{background-image:url('resources/cards/6s.png');}")
        self.pl_bt_06.setStyleSheet("QPushButton{background-image:url('resources/cards/7s.png');}")
        self.pl_bt_07.setStyleSheet("QPushButton{background-image:url('resources/cards/qs.png');}")
        self.pl_bt_08.setStyleSheet("QPushButton{background-image:url('resources/cards/js.png');}")
        self.pl_bt_09.setStyleSheet("QPushButton{background-image:url('resources/cards/ks.png');}")
        self.pl_bt_10.setStyleSheet("QPushButton{background-image:url('resources/cards/as.png');}")

'''
    def handlerbt(self):
        self.lb_nome.setText("Ola")
'''

app = QApplication(sys.argv)
dialog = QDialog()

prog = Gui(dialog)
dialog.show()
sys.exit(app.exec_())
