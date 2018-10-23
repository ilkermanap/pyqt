Nasıl Güncelleniyor?
====================

Bu belgelerin kaynak kodları github üzerinde bulunuyor. Bir webhook yardımıyla, 
belgelerde yaptığım değişiklikleri commit ettiğim zaman, otomatik olarak yeni html
sayfaları oluşturulup yayına alınmaktadır.

Yayına alan uygulamayı da burada bulacaksınız. Flask ile yazılmış küçük bir uygulamadır.


push/app/__init__.py
--------------------
.. literalinclude:: push/app/__init__.py
   :language: python

push/app/views.py
-----------------
.. literalinclude:: push/app/views.py
   :language: python

push/uwsgi.ini
--------------
.. literalinclude:: push/uwsgi.ini


Nginx Ayarları
--------------
.. literalinclude:: blog.manap.se.conf
