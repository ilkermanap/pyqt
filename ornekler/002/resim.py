from PySide.QtGui import *
from PySide.QtCore import *
from ui_resimgosterici import Ui_dlgResimGosterici

import sys
        

class MainWindow(QDialog, Ui_dlgResimGosterici):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.show()

    def dosyaSec(self):
        fname, ftype = QFileDialog.getOpenFileName(self, 'Open file',
                                                     '',"Image files (*.jpg *.gif)")
        self.lblResim.setPixmap(QPixmap(fname))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
