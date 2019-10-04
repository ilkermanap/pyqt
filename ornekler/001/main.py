import sys
from PySide2.QtWidgets import QApplication, QDialog

from ui_ornek import Ui_DlgOrnek
class MainWindow(QDialog, Ui_DlgOrnek):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.show()
        
    def etiket_guncelle(self):
        self.lblMetin.setText(self.editMetin.text())
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
                
