import sys

from PyQt5.uic.properties import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from Menu.Main import Ui_Dialog


class Gui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)


        self.dialog = dialog
        self.frame.setStyleSheet("background-image:url('123.png');background-repeat:no-repeat;")
        self.bt_ok.clicked.connect(self.handlerbt)
        self.bt_ok.setStyleSheet("QPushButton{background-image:url('456.png');background-position:center;margin:1px;border-style:outset;}QPushButton:hover{}")


    def handlerbt(self):
        self.lb_nome.setText("Ola")




app = QApplication(sys.argv)
dialog = QDialog()

prog = Gui(dialog)
dialog.show()
sys.exit(app.exec_())
