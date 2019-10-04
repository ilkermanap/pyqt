# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resimbilgi.ui',
# licensing of 'resimbilgi.ui' applies.
#
# Created: Fri Oct  4 09:38:03 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlgResimBilgi(object):
    def setupUi(self, dlgResimBilgi):
        dlgResimBilgi.setObjectName("dlgResimBilgi")
        dlgResimBilgi.resize(399, 163)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlgResimBilgi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblDosyaAdi = QtWidgets.QLabel(dlgResimBilgi)
        self.lblDosyaAdi.setObjectName("lblDosyaAdi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblDosyaAdi)
        self.editDosyaAdi = QtWidgets.QLineEdit(dlgResimBilgi)
        self.editDosyaAdi.setEnabled(True)
        self.editDosyaAdi.setReadOnly(True)
        self.editDosyaAdi.setObjectName("editDosyaAdi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editDosyaAdi)
        self.lblgenislik = QtWidgets.QLabel(dlgResimBilgi)
        self.lblgenislik.setObjectName("lblgenislik")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblgenislik)
        self.editGenislik = QtWidgets.QLineEdit(dlgResimBilgi)
        self.editGenislik.setEnabled(True)
        self.editGenislik.setReadOnly(True)
        self.editGenislik.setObjectName("editGenislik")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editGenislik)
        self.lblYukseklik = QtWidgets.QLabel(dlgResimBilgi)
        self.lblYukseklik.setObjectName("lblYukseklik")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblYukseklik)
        self.editYukseklik = QtWidgets.QLineEdit(dlgResimBilgi)
        self.editYukseklik.setEnabled(True)
        self.editYukseklik.setReadOnly(True)
        self.editYukseklik.setObjectName("editYukseklik")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editYukseklik)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sldBuyutme = QtWidgets.QSlider(dlgResimBilgi)
        self.sldBuyutme.setMinimum(20)
        self.sldBuyutme.setMaximum(200)
        self.sldBuyutme.setProperty("value", 100)
        self.sldBuyutme.setOrientation(QtCore.Qt.Horizontal)
        self.sldBuyutme.setInvertedAppearance(False)
        self.sldBuyutme.setInvertedControls(False)
        self.sldBuyutme.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sldBuyutme.setTickInterval(20)
        self.sldBuyutme.setObjectName("sldBuyutme")
        self.verticalLayout.addWidget(self.sldBuyutme)

        self.retranslateUi(dlgResimBilgi)
        QtCore.QObject.connect(self.sldBuyutme, QtCore.SIGNAL("sliderReleased()"), dlgResimBilgi.resimBoyutlandir)
        QtCore.QMetaObject.connectSlotsByName(dlgResimBilgi)

    def retranslateUi(self, dlgResimBilgi):
        dlgResimBilgi.setWindowTitle(QtWidgets.QApplication.translate("dlgResimBilgi", "Dialog", None, -1))
        self.lblDosyaAdi.setText(QtWidgets.QApplication.translate("dlgResimBilgi", "Dosya Adi", None, -1))
        self.lblgenislik.setText(QtWidgets.QApplication.translate("dlgResimBilgi", "Genislik", None, -1))
        self.lblYukseklik.setText(QtWidgets.QApplication.translate("dlgResimBilgi", "Yukseklik", None, -1))

