# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(955, 579)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 951, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_ok_4 = QtWidgets.QPushButton(self.frame)
        self.bt_ok_4.setGeometry(QtCore.QRect(380, 10, 121, 121))
        self.bt_ok_4.setFlat(True)
        self.bt_ok_4.setObjectName("bt_ok_4")
        self.bt_ok_2 = QtWidgets.QPushButton(self.frame)
        self.bt_ok_2.setGeometry(QtCore.QRect(360, 240, 121, 121))
        self.bt_ok_2.setFlat(True)
        self.bt_ok_2.setObjectName("bt_ok_2")
        self.bt_ok_3 = QtWidgets.QPushButton(self.frame)
        self.bt_ok_3.setGeometry(QtCore.QRect(530, 100, 121, 121))
        self.bt_ok_3.setFlat(True)
        self.bt_ok_3.setObjectName("bt_ok_3")
        self.bt_ok = QtWidgets.QPushButton(self.frame)
        self.bt_ok.setGeometry(QtCore.QRect(240, 110, 521, 261))
        self.bt_ok.setFlat(True)
        self.bt_ok.setObjectName("bt_ok")
        self.lb_nome = QtWidgets.QLabel(self.frame)
        self.lb_nome.setGeometry(QtCore.QRect(330, 10, 221, 81))
        self.lb_nome.setObjectName("lb_nome")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bt_ok_4.setText(_translate("Dialog", "ok"))
        self.bt_ok_2.setText(_translate("Dialog", "ok"))
        self.bt_ok_3.setText(_translate("Dialog", "ok"))
        self.bt_ok.setText(_translate("Dialog", "ok"))
        self.lb_nome.setText(_translate("Dialog", "TextLabel"))

