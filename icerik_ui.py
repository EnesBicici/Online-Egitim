# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'icerik.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 232)
        self.kursBox = QtWidgets.QComboBox(Form)
        self.kursBox.setGeometry(QtCore.QRect(110, 24, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.kursBox.setFont(font)
        self.kursBox.setObjectName("kursBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 49))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sayfaBox = QtWidgets.QSpinBox(Form)
        self.sayfaBox.setGeometry(QtCore.QRect(217, 72, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.sayfaBox.setFont(font)
        self.sayfaBox.setMinimum(1)
        self.sayfaBox.setObjectName("sayfaBox")
        self.ekleButon = QtWidgets.QPushButton(Form)
        self.ekleButon.setGeometry(QtCore.QRect(110, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ekleButon.setFont(font)
        self.ekleButon.setObjectName("ekleButon")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "İçerik"))
        self.label.setText(_translate("Form", "Kurs"))
        self.label_2.setText(_translate("Form", "Sayfa Sayısı"))
        self.ekleButon.setText(_translate("Form", "Ekle"))