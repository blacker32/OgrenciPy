class Ogrenci():
    __doc__='Öğrenci sınıfı'
    ogrenciler=[]
    def __init__(self, ogrenciAdiSoyadi):
     self.ogrenciAdiSoyadi = ogrenciAdiSoyadi
     self.dersleri = []
     self.sinavlar=[]
     self.ogrenciEkle(self.ogrenciAdiSoyadi)
    def ogrenciEkle(self, adSoyad):
     self.ogrenciler.append(adSoyad)
     print('{} adlı kişi öğrencilere eklendi.'.format(adSoyad))
    def ogrenciListesiYazdir(self):
     print('Öğrenci listesi')
     for ogrenci in self.ogrenciler:
       print(ogrenci)
    def dersEkle(self, dersAdi):
     self.dersleri.append(dersAdi)
    def ogrencininDersleri(self):
     print('{} adlı kişinin dersleri:'.format(self.ogrenciAdiSoyadi))
     for ders in self.dersleri:
       print(ders)
    def sinavPuaniEkle(self, sinavPuani):
     self.sinavlar.append(sinavPuani)
    def ogrencininSinavPuanlari(self):
     print('{} adlı kişinin sınav sonuçları:'.format(self.ogrenciAdiSoyadi))
     for sinav in self.sinavlar:
       print(sinav)