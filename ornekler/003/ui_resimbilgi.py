# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resimbilgi.ui'
#
# Created: Wed Oct 24 22:04:59 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgResimBilgi(object):
    def setupUi(self, dlgResimBilgi):
        dlgResimBilgi.setObjectName("dlgResimBilgi")
        dlgResimBilgi.resize(399, 163)
        self.verticalLayout = QtGui.QVBoxLayout(dlgResimBilgi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblDosyaAdi = QtGui.QLabel(dlgResimBilgi)
        self.lblDosyaAdi.setObjectName("lblDosyaAdi")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblDosyaAdi)
        self.editDosyaAdi = QtGui.QLineEdit(dlgResimBilgi)
        self.editDosyaAdi.setEnabled(True)
        self.editDosyaAdi.setReadOnly(True)
        self.editDosyaAdi.setObjectName("editDosyaAdi")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editDosyaAdi)
        self.lblgenislik = QtGui.QLabel(dlgResimBilgi)
        self.lblgenislik.setObjectName("lblgenislik")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblgenislik)
        self.editGenislik = QtGui.QLineEdit(dlgResimBilgi)
        self.editGenislik.setEnabled(True)
        self.editGenislik.setReadOnly(True)
        self.editGenislik.setObjectName("editGenislik")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.editGenislik)
        self.lblYukseklik = QtGui.QLabel(dlgResimBilgi)
        self.lblYukseklik.setObjectName("lblYukseklik")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblYukseklik)
        self.editYukseklik = QtGui.QLineEdit(dlgResimBilgi)
        self.editYukseklik.setEnabled(True)
        self.editYukseklik.setReadOnly(True)
        self.editYukseklik.setObjectName("editYukseklik")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.editYukseklik)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sldBuyutme = QtGui.QSlider(dlgResimBilgi)
        self.sldBuyutme.setMinimum(20)
        self.sldBuyutme.setMaximum(200)
        self.sldBuyutme.setProperty("value", 100)
        self.sldBuyutme.setOrientation(QtCore.Qt.Horizontal)
        self.sldBuyutme.setInvertedAppearance(False)
        self.sldBuyutme.setInvertedControls(False)
        self.sldBuyutme.setTickPosition(QtGui.QSlider.TicksAbove)
        self.sldBuyutme.setTickInterval(20)
        self.sldBuyutme.setObjectName("sldBuyutme")
        self.verticalLayout.addWidget(self.sldBuyutme)

        self.retranslateUi(dlgResimBilgi)
        QtCore.QObject.connect(self.sldBuyutme, QtCore.SIGNAL("sliderReleased()"), dlgResimBilgi.resimBoyutlandir)
        QtCore.QMetaObject.connectSlotsByName(dlgResimBilgi)

    def retranslateUi(self, dlgResimBilgi):
        dlgResimBilgi.setWindowTitle(QtGui.QApplication.translate("dlgResimBilgi", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDosyaAdi.setText(QtGui.QApplication.translate("dlgResimBilgi", "Dosya Adi", None, QtGui.QApplication.UnicodeUTF8))
        self.lblgenislik.setText(QtGui.QApplication.translate("dlgResimBilgi", "Genislik", None, QtGui.QApplication.UnicodeUTF8))
        self.lblYukseklik.setText(QtGui.QApplication.translate("dlgResimBilgi", "Yukseklik", None, QtGui.QApplication.UnicodeUTF8))

