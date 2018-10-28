# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resimgosterici.ui'
#
# Created: Wed Oct 24 12:20:16 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgResimGosterici(object):
    def setupUi(self, dlgResimGosterici):
        dlgResimGosterici.setObjectName("dlgResimGosterici")
        dlgResimGosterici.resize(489, 359)
        self.verticalLayout = QtGui.QVBoxLayout(dlgResimGosterici)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDosyaAdi = QtGui.QLabel(dlgResimGosterici)
        self.lblDosyaAdi.setObjectName("lblDosyaAdi")
        self.horizontalLayout.addWidget(self.lblDosyaAdi)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnDosyaSec = QtGui.QPushButton(dlgResimGosterici)
        self.btnDosyaSec.setObjectName("btnDosyaSec")
        self.horizontalLayout.addWidget(self.btnDosyaSec)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lblResim = QtGui.QLabel(dlgResimGosterici)
        self.lblResim.setMinimumSize(QtCore.QSize(0, 300))
        self.lblResim.setObjectName("lblResim")
        self.verticalLayout.addWidget(self.lblResim)

        self.retranslateUi(dlgResimGosterici)
        QtCore.QObject.connect(self.btnDosyaSec, QtCore.SIGNAL("clicked()"), dlgResimGosterici.dosyaSec)
        QtCore.QMetaObject.connectSlotsByName(dlgResimGosterici)

    def retranslateUi(self, dlgResimGosterici):
        dlgResimGosterici.setWindowTitle(QtGui.QApplication.translate("dlgResimGosterici", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDosyaAdi.setText(QtGui.QApplication.translate("dlgResimGosterici", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDosyaSec.setText(QtGui.QApplication.translate("dlgResimGosterici", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResim.setText(QtGui.QApplication.translate("dlgResimGosterici", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

