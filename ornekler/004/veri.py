import psutil

class Veri:
    def __init__(self, aralik=1, maxnokta = 50, artan=False):
        self.noktalar = []
        self.aralik = aralik
        self.maxnokta = maxnokta
        self.artan = artan
        self.sonsayi = 0
        
    def sayi_ekle(self, sayi):
        if len(self.noktalar) >= self.maxnokta:
            self.noktalar = self.noktalar[1:]
        if self.artan is False:
            self.noktalar.append(sayi)
        else:
            if len(self.noktalar) == 0:
                self.sonsayi = sayi
                self.noktalar = [0]
            else:

                self.noktalar.append(sayi  - self.sonsayi)
                self.sonsayi = sayi
                
class Islemci(Veri):
    def __init__(self):
        Veri.__init__(self)

    def ekle(self):
        self.sayi_ekle(psutil.cpu_percent())

class Ag(Veri):
    def __init__(self):
        Veri.__init__(self, artan=True)

    def ekle(self):
        # net_io_counters()[1], bytes received veriyor
        self.sayi_ekle(psutil.net_io_counters()[1])
        
if __name__ == "__main__":
    ag = Ag()
    import time
    for i in range(500):
        ag.ekle()
        print( ag.noktalar)
        time.sleep(2)
