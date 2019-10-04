# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ornek.ui',
# licensing of 'ornek.ui' applies.
#
# Created: Fri Oct  4 11:32:39 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DlgOrnek(object):
    def setupUi(self, DlgOrnek):
        DlgOrnek.setObjectName("DlgOrnek")
        DlgOrnek.resize(382, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgOrnek)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editMetin = QtWidgets.QLineEdit(DlgOrnek)
        self.editMetin.setObjectName("editMetin")
        self.verticalLayout.addWidget(self.editMetin)
        self.lblMetin = QtWidgets.QLabel(DlgOrnek)
        self.lblMetin.setObjectName("lblMetin")
        self.verticalLayout.addWidget(self.lblMetin)
        spacerItem = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGuncelle = QtWidgets.QPushButton(DlgOrnek)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.horizontalLayout.addWidget(self.btnGuncelle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnCikis = QtWidgets.QPushButton(DlgOrnek)
        self.btnCikis.setObjectName("btnCikis")
        self.horizontalLayout.addWidget(self.btnCikis)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DlgOrnek)
        QtCore.QObject.connect(self.btnCikis, QtCore.SIGNAL("clicked()"), DlgOrnek.close)
        QtCore.QObject.connect(self.btnGuncelle, QtCore.SIGNAL("clicked()"), DlgOrnek.etiket_guncelle)
        QtCore.QMetaObject.connectSlotsByName(DlgOrnek)

    def retranslateUi(self, DlgOrnek):
        DlgOrnek.setWindowTitle(QtWidgets.QApplication.translate("DlgOrnek", "Dialog", None, -1))
        self.lblMetin.setText(QtWidgets.QApplication.translate("DlgOrnek", "TextLabel", None, -1))
        self.btnGuncelle.setText(QtWidgets.QApplication.translate("DlgOrnek", "Etiketi Guncelle", None, -1))
        self.btnCikis.setText(QtWidgets.QApplication.translate("DlgOrnek", "Cikis", None, -1))

