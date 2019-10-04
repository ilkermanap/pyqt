from PySide2.QtWidgets import QApplication, QDialog, QFileDialog
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


from ui_resimgosterici import Ui_dlgResimGosterici
from ui_resimbilgi import Ui_dlgResimBilgi

import sys
        

class BilgiWindow(QDialog, Ui_dlgResimBilgi):
    def __init__(self, parent=None, gorsel=None):
        super(BilgiWindow, self).__init__()
        self.parent = parent
        self.resim = gorsel
        self.setupUi(self)
        self.editDosyaAdi.setText( self.parent.lblDosyaAdi.text())
        self.editYukseklik.setText(str(self.resim.height()))
        self.editGenislik.setText(str(self.resim.width()))

    def resimBoyutlandir(self):
        oran = self.sldBuyutme.value()
        eski_yukseklik = int(self.editYukseklik.text())
        eski_genislik = int(self.editGenislik.text())
        yeni_yukseklik = eski_yukseklik * ( oran / 100.0)
        yeni_genislik = eski_genislik * (oran / 100.0)
        
        
        self.parent.lblResim.setPixmap(self.resim.scaled(yeni_genislik, yeni_yukseklik, Qt.KeepAspectRatio))

        
class MainWindow(QDialog, Ui_dlgResimGosterici):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.resim = None
        self.bilgipenceresi = None
        self.setupUi(self)
        self.show()

    def dosyaSec(self):
        if self.bilgipenceresi is not None:
            self.bilgipenceresi.close()
            
        fname, ftype = QFileDialog.getOpenFileName(self, 'Open file',
                                                     '',"Image files (*.jpg *.gif)")
        self.resim = QPixmap(fname)
        self.lblResim.setPixmap(self.resim)
        self.lblDosyaAdi.setText( fname)
        self.bilgipenceresi = BilgiWindow(self, self.lblResim.pixmap())
        self.bilgipenceresi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
