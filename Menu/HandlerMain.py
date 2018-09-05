import sys

from PyQt5.uic.properties import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from Menu.Main import Ui_Dialog


class Gui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.dialog = dialog
        self.frame.setStyleSheet("background-image:url('bg.png');background-repeat:no-repeat;")
        '''
        self.bt_ok.clicked.connect(self.handlerbt)
        self.bt_ok.setStyleSheet(
            "QPushButton{background-image:url('456.png');background-position:center;margin:1px;border-style:outset;}QPushButton:hover{}")
            self.pl_label.setStyleSheet("* { background-color: rgba(0, 0, 0, 0); }")
        '''
        self.ai1_crd_01.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_02.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_03.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_04.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_05.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_06.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_07.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_08.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_09.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai1_crd_10.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai2_bt_01.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_02.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_03.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_04.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_05.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_06.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_07.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_08.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_09.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai2_bt_10.setStyleSheet("QPushButton{background-image:url('cardbackv.png');}")
        self.ai3_crd_01.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_02.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_03.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_04.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_05.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_06.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_07.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_08.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_09.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")
        self.ai3_crd_10.setStyleSheet("QPushButton{background-image:url('cardbackh1.png');}")


    def handlerbt(self):
        self.lb_nome.setText("Ola")


app = QApplication(sys.argv)
dialog = QDialog()

prog = Gui(dialog)
dialog.show()
sys.exit(app.exec_())
