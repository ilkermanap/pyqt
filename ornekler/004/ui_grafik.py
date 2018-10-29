# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafik.ui'
#
# Created: Mon Oct 29 17:46:18 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgGrafik(object):
    def setupUi(self, dlgGrafik):
        dlgGrafik.setObjectName("dlgGrafik")
        dlgGrafik.resize(472, 396)
        self.verticalLayout = QtGui.QVBoxLayout(dlgGrafik)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmbKaynak = QtGui.QComboBox(dlgGrafik)
        self.cmbKaynak.setObjectName("cmbKaynak")
        self.cmbKaynak.addItem("")
        self.cmbKaynak.addItem("")
        self.horizontalLayout.addWidget(self.cmbKaynak)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plotGrafik = PlotWidget(dlgGrafik)
        self.plotGrafik.setObjectName("plotGrafik")
        self.verticalLayout.addWidget(self.plotGrafik)

        self.retranslateUi(dlgGrafik)
        QtCore.QObject.connect(self.cmbKaynak, QtCore.SIGNAL("currentIndexChanged(int)"), dlgGrafik.degistir)
        QtCore.QMetaObject.connectSlotsByName(dlgGrafik)

    def retranslateUi(self, dlgGrafik):
        dlgGrafik.setWindowTitle(QtGui.QApplication.translate("dlgGrafik", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbKaynak.setItemText(0, QtGui.QApplication.translate("dlgGrafik", "İşlemci", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbKaynak.setItemText(1, QtGui.QApplication.translate("dlgGrafik", "Ağ", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
