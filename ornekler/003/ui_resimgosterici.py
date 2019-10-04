# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resimgosterici.ui',
# licensing of 'resimgosterici.ui' applies.
#
# Created: Fri Oct  4 09:38:14 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlgResimGosterici(object):
    def setupUi(self, dlgResimGosterici):
        dlgResimGosterici.setObjectName("dlgResimGosterici")
        dlgResimGosterici.resize(489, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlgResimGosterici)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDosyaAdi = QtWidgets.QLabel(dlgResimGosterici)
        self.lblDosyaAdi.setObjectName("lblDosyaAdi")
        self.horizontalLayout.addWidget(self.lblDosyaAdi)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnDosyaSec = QtWidgets.QPushButton(dlgResimGosterici)
        self.btnDosyaSec.setObjectName("btnDosyaSec")
        self.horizontalLayout.addWidget(self.btnDosyaSec)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lblResim = QtWidgets.QLabel(dlgResimGosterici)
        self.lblResim.setMinimumSize(QtCore.QSize(0, 300))
        self.lblResim.setObjectName("lblResim")
        self.verticalLayout.addWidget(self.lblResim)

        self.retranslateUi(dlgResimGosterici)
        QtCore.QObject.connect(self.btnDosyaSec, QtCore.SIGNAL("clicked()"), dlgResimGosterici.dosyaSec)
        QtCore.QMetaObject.connectSlotsByName(dlgResimGosterici)

    def retranslateUi(self, dlgResimGosterici):
        dlgResimGosterici.setWindowTitle(QtWidgets.QApplication.translate("dlgResimGosterici", "Dialog", None, -1))
        self.lblDosyaAdi.setText(QtWidgets.QApplication.translate("dlgResimGosterici", "TextLabel", None, -1))
        self.btnDosyaSec.setText(QtWidgets.QApplication.translate("dlgResimGosterici", "PushButton", None, -1))
        self.lblResim.setText(QtWidgets.QApplication.translate("dlgResimGosterici", "TextLabel", None, -1))

