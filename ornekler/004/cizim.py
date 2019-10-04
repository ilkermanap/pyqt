from PySide.QtGui import *
from PySide.QtCore import *

from ui_grafik import Ui_dlgGrafik

from veri import Ag, Islemci
import time
import sys
        

class VeriKaynagi(QThread):
    updateProgress = Signal()
    
    def __init__(self):
        QThread.__init__(self)
        self.kaynaklar = {0: Islemci(), 1: Ag()}

    def veri(self, id):
        return self.kaynaklar[id].noktalar
        
    def run(self):
        while 1:
            for kaynak in self.kaynaklar.values():
                kaynak.ekle()
            self.updateProgress.emit()
            time.sleep(1)

class MainWindow(QDialog, Ui_dlgGrafik):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.kaynak = VeriKaynagi()
        self.kaynak.start()
        self.kaynak.updateProgress.connect(self.ciz)
        self.secili = 0
        self.show()

        
    def degistir(self):
        if self.cmbKaynak.currentIndex() != self.secili:
            self.plotGrafik.clear()
            self.secili = self.cmbKaynak.currentIndex()
            self.plotGrafik.plot(self.kaynak[self.secili].noktalar)
        
    def ciz(self):
        sayilar = self.kaynak.veri(self.secili)
        if len(sayilar) == self.kaynak.kaynaklar[self.secili].maxnokta:
            self.plotGrafik.clear()
        self.plotGrafik.plot(sayilar)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
