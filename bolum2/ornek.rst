Örnek
=====

Tek Pencere
-----------
İçinde tek pencere olan basit uygulama yazacağız. İki buton, bir metin giriş alanı,
bir etiket bulunan pencer içinde, nesnelerin birbiriyle nasıl etkileştiğini göreceğiz.
Ayrıca oluşturduğumuz ekran tasarımını nasıl uygulamaya çevireceğimizi de ilerleyen
sayfalarda bulacaksınız.

.. figure:: ../images/qt-001.png
   :scale: 35 %

   Dialog tipinde boş sayfa ile başlıyoruz.

.. figure:: ../images/qt-002.png
   :scale: 35 %

   Boş ekranımız, üzerine iki buton, bir label, bir de edit box yerleştireceğiz.

.. figure:: ../images/qt-003.png
   :scale: 35 %
   
   Butonlar.

.. figure:: ../images/qt-004.png
   :scale: 35 %

   Label ve edit box. Sağ üstte bulunan Object Inspector ile nesne isimlerini düzenleyelim. Nesne isimlerini belirli bir kurala göre verin. Uygulama içinde bu isimler kullanılacak.

.. figure:: ../images/qt-005.png
   :scale: 35 %
   
   Sinyal/Slot baglantılarını, yani bu pencere için yazılacak metod/fonksiyon isimlerini tanımlamak için, tasarım ekranını signal/slot moduna almak için kırmızı okla gösterilen butona basın.

.. figure:: ../images/qt-006.png
   :scale: 35 %
	
   Uygulamayı kapatmak için kullanacağımız butona tıklayıp, pencere üzerinde boş alana sürüklüyoruz. Mouse tuşunu bıraktığımızda yukarıdaki ekran gelir. Configure Connection penceresinde close() metodunu görebilmek için, sol altta bulunan 'show signals and slots inherited from Qwidget' kutucuğunu işaretleriz. Çıkan listeden close seçip Ok tuşuna basarız.

.. figure:: ../images/qt-007.png
   :scale: 35 %
   
   Etiket güncelle butonu için, bir önceki butonda yaptığımız gibi, butonun üzerinden pencere üzerinde boş alana sürükleyip bırakırız. Çıkan ekranda, Configure Connection kısmında, clicked() sinyali için sağ tarafta hedef metodun ismini oluşturmamız gerekiyor. Bunun için 'Edit…' butonuna tıklayıp, ekrana gelen 'Signal/Slots of DlgOrnek' penceresinde üstte görünen yeşil + butonuna tıklarız. Slots listesine slot1() eklenir. Slot1() üzerine çift tıklayıp adını etiket_guncelle() yapacağız. Sonundaki parantezler önemlidir. Ok butonuna basıp, bir alttaki ekrana geçeriz.

.. figure:: ../images/qt-008.png
   :scale: 35 %
	
   Configure Connection ekranında, clicked() için sağ tarafta etiket_guncelle() seçilmelidir. Ok tuşuna basıp devam edilir. Bu aşamada designer uygulaması ile işimiz bitiyor. Dosyayı ornek.ui ismi ile kaydedip designer uygulamasını kapatırız.

.. figure:: ../images/qt-009.png
   :scale: 35 %
	
   Şimdi, bu ekran tasarımını python koduna çeviriyoruz. Pyside-uic yerine qt5 ile gelen uic uygulamasını kullanabilirsiniz. Yukarıdaki komut sonrasında elimizde ui_ornek.py dosyası olacaktır. Bu ui_ornek dosyasının içine hiçbir ek yapılmamalıdır.


.. code-block:: python   

   import sys
   from PySide.QtGui import *
   from PySide.QtCore import *
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

Değişikliklerin yapılabileceği main.py dosyasının içeriği yukarıdaki gibidir. Designer ile oluşturulan arayüz dosyasından üretilen sınıf, kendi penceremizi oluşturmak için kullanılmıştır. Ui_DlgOrnek, uic ile üretilen ui_ornek.py içindedir.


.. figure:: ../images/qt-010.png
   :scale: 35 %

   Uygulamamızı komut satırından, python main.py diyerek çalıştırınca, karşımıza yukarıdaki ekran çıkar.

Görüldüğü üzere, pencere içindeki yerleşim düzensizdir. Şimdi yapacağımız işlem, pencere boyutlandırıldığında içindekilerin de bu boyutlandırma işlemine uymasını sağlayacaktır. Pencere içinde Layout ayarlaması yapacağız. Bunun için yeniden ornek.ui dosyasını designer uygulamasi ile düzenleyeceğiz.

.. figure:: ../images/qt-011.png
   :scale: 35 %

   Layout oluşturma.
	   
Tasarıma küçük ekle yapıyoruz. Burada iki buton arasına yatay spacer ekliyoruz. Ardından, iki buton ve yatay spacer'i mouse ile seçerek, sağ mouse tuşuna tıkladığımızda, çıkan popup menünün en alt seçeneğinde Layout görürüz. Üzerine geldiğimizde, Horizontal Layout seçeriz. Böylece, bu iki buton ve spacer, bir yatay layout grubu oluştururlar. Ardından, pencerede boş bir alana sağ tuş ile tıklayıp, yine Layout kısmında 'Layout Vertically' seçersek, editbox, label, dikey spacer ve az önce oluşturduğumuz yatay layout grubu yeni bir Layout grubu oluşturur. Designer içinde yapılacaklar bitmiştir. Kaydedip çıkarız.


Bu aşamada, elimizde yeni bir ui dosyası ve yazılmış uygulama bulunmaktadır. Yeni ornek.ui dosyasını pysideuic (ya da pyqt5 icin pyuic) uygulamasından geçirip yeni ui_ornek.py dosyasını oluştururuz. Bu aşamada sadece görsel değişiklik yaptığımız için, main.py içinde değişiklik gerekmez. Uygulamayı yeniden çalıştırırsak, pencerenin boyutlanması ile içindeki nesnelerin de ona göre hareket ettiklerini göreceğiz.

.. figure:: ../images/qt-012.png
   :scale: 55 %

   Boyutlandırma

.. figure:: ../images/qt-013.png
   :scale: 55 %	   

   Boyutlandırma.

Çoklu Pencere
-------------
İçinde birden fazla pencere olan, bir butonla diğer pencereyi açabildiğimiz uygulamayı yazacağız.

Resim Kullanımı
---------------
Bir uygulamada nasıl resim kullanabileceğimizi göreceğiz.

Designer kullanarak bir buton, iki label bulunan bir ekran tasarlayacağız. Layout yerleşimi gibi konular yukarıda bahsedildiği için doğruca uygulamaya geçeceğiz.

.. figure:: ../images/qt-resimgosterici-001.png
   :scale: 55 %

   Uygulama için gerekli herşey. Butonlar, signal/slot bağlantıları, vs.

Şekilde görüldüğü gibi, içini doldurmamız gereken dosyaSec fonksiyonumuz bulunmaktadır. Bu fonksiyon, btnDosyaSec butonu tıklandığında çalışacaktır. Şekilde sağ altta görülen signal/slot editor kısmındadır.

Seçilen resim dosyasını QLabel tipindeki lblResim nesnesinin üzerine yerleştireceğiz. Seçilen dosya adını da yine QLabel tipindeki lblDosyaAdi nesnesi görüntüleyecektir.


.. code-block:: bash
		
    ~$ pyside-uic  resimgosterici.ui  > ui_resimgosterici.py

Yukarıdaki komut ile ekran tasarımını import edebileceğimiz python kaynak koduna çeviririz. Çok yapılan hatalardan birisi de, üretilen bu dosya içine kendi kodlarımızı yazmaya başlamaktır. Dosyanın giriş kısmında 'WARNING! All changes made in this file will be lost!' uyarısını dikkate almak gerekir. Arayüz ile kendi yazdığımız kısımları farklı dosyada tutmamız, arayüzde yapılacak değişikliklerden kendi yazdığımız kısmın etkilenmemesini, aynı zamanda da designer ile yaptığınız görsel değişikliklerin devreye alınmasını sağlar.

Aşağıda, üretilmiş olan arayüzü kullanan ve bu haliyle pencereyi görüntüleme dışında hiçbir şey yapmayan kod parçası bulunmaktadır. dosyaSec fonksiyonunu yazarak, uygulamanın istediğimiz işi yapmasını sağlayacağız.

.. code-block:: python
   :linenos:

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
        pass

   if __name__ == "__main__":
      app = QApplication(sys.argv)
      mainWin = MainWindow(app)
      ret = app.exec_()
      app.exit()
      sys.exit(ret)


QFileDialog nesnesi, bize dosya seçim penceresi sunar. getOpenFileName metodu ise dosya adı ve dosya tipi içeren ikili sonuc döndürür. Yukarıdaki uygulamada dosyaSec metodunu aşağıdaki kod bloğu ile değiştirdiğimizde, seçtiğimiz dosyanın lblResim nesnesi üzerinde görüntülendiğini görürüz.

.. code-block:: python
      
   def dosyaSec(self):
      fname, ftype = QFileDialog.getOpenFileName(self, 'Open file',
      '',"Image files (*.jpg *.gif)")
      self.lblResim.setPixmap(QPixmap(fname))

.. figure:: ../images/qt-resimgosterici-002.png
   :scale: 55 %

   Dosya seçme
	   
.. figure:: ../images/qt-resimgosterici-003.png
   :scale: 55 %

   Görüntüleme
