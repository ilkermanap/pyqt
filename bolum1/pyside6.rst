PySide6
=======

Qt6 2020 yılının sonunda yayınlandı. Ardından PySide6'da duyuruldu.

Qt sürüm numarası ile uyumlu olması için sürüm numarası 2'den 6'ya atladı.

Kurulum
-------

Kullandığım debian 10 sistem üzerinde virtualenv kullanarak pyside6 kurulumu yapacağız. Diğer linux sürümlerinde de benzer şekilde kurulabilir.

.. code-block:: bash
		
   ilker@prodesk:~$ mkdir test_pyside6; cd test_pyside6
   ilker@prodesk:~/test_pyside6$ python3 -m virtualenv -p /usr/bin/python3 venv
   ilker@prodesk:~/test_pyside6$ source venv/bin/activate
   (venv) ilker@prodesk:~/test_pyside6$ 
    

Buraya kadar virtualenv ile test_pyside6/venv dizininde python3 kullanan bir sanal python ortamı kurduk. Yukarıdaki son satıra dikkat ederseniz, (venv) yazısını göreceksiniz. Burada çalıştıracağınız pip komutları, sizden yetkili kullanıcı istemeyecek ve istediğiniz paketleri venv dizini altına kuracaktır.

Şimdi pyside6 kuralım:

.. code-block:: bash
		
   (venv) ilker@prodesk:~/test_pyside6$ pip install pyside6
   Collecting pyside6
     Using cached PySide6-6.0.0-6.0.0-cp36.cp37.cp38.cp39-abi3-manylinux1_x86_64.whl (170.5 MB)
   Collecting shiboken6==6.0.0
     Using cached shiboken6-6.0.0-6.0.0-cp36.cp37.cp38.cp39-abi3-manylinux1_x86_64.whl (964 kB)
   Installing collected packages: shiboken6, pyside6
   Successfully installed pyside6-6.0.0 shiboken6-6.0.0

Artık PySide6 ile uygulama yazmaya başlayabiliriz. Aşağıdaki örnek `doc.qt.io <https://doc.qt.io/qtforpython/tutorials/basictutorial/dialog.html#complete-code>`_ sitesinden alınmıştır:

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog)

   class Form(QDialog):

       def __init__(self, parent=None):
           super(Form, self).__init__(parent)
           # Create widgets
           self.edit = QLineEdit("Write my name here")
           self.button = QPushButton("Show Greetings")
           # Create layout and add widgets
           layout = QVBoxLayout()
           layout.addWidget(self.edit)
           layout.addWidget(self.button)
           # Set dialog layout
           self.setLayout(layout)
           # Add button signal to greetings slot
           self.button.clicked.connect(self.greetings)
        # Greets the user
       def greetings(self):
           print ("Hello %s" % self.edit.text())

   if __name__ == '__main__':
       # Create the Qt Application
       app = QApplication(sys.argv)
       # Create and show the form
       form = Form()
       form.show()
       # Run the main Qt loop
       sys.exit(app.exec_())

Designer Kullanımı
------------------

Sisteminize Qt6 kurulumu yaparsanız, qt6 ile kullanılabilecek designer uygulamasını da kullanabilirsiniz.  pyside2-uic yerine pyside6-uic, pyside2-rcc yerine de pyside6-rcc kullanabilirsiniz.
