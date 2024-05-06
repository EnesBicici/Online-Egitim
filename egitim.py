from veritabani import Veritabani

class Ogrenci:
    def __init__(self, id, eposta, sifre, ad, soyad, telefon):
        self.id = id
        self.eposta = eposta
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(eposta, sifre, ad, soyad, telefon):
        Veritabani.query('INSERT INTO kullanicilar (eposta, sifre, ad, soyad, telefon) VALUES(?, ?, ?, ?, ?)', (eposta, sifre, ad, soyad, telefon))
    
class Kurs:
    def __init__(self, id, ad, egitmen, aciklama, kazanimlar, fotograf) -> None:
        self.id = id
        self.ad = ad
        self.egitmen = egitmen
        self.aciklama = aciklama
        self.kazanimlar = kazanimlar
        self.fotograf = fotograf

    @staticmethod
    def kursolustur(ad, egitmen, aciklama, kazanimlar, fotograf):
        Veritabani.query('INSERT INTO kurslar (ad, egitmenid, aciklama, kazanimlar, fotograf) VALUES(?, ?, ?, ?, ?)', (ad, egitmen, aciklama, kazanimlar, fotograf))

    def kaydol(self, ogrenci):
        Veritabani.query('INSERT INTO kayitlar (ogrenciid, kursid) VALUES(?, ?)', (ogrenci.id, self.id))


class Egitmen:
    def __init__(self, id,ad, soyad, uzmanlik):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.uzmanlikalani = uzmanlik

class Icerik:
    def __init__(self, id , kursid, sayfa, baslik, aciklama):
        self.id = id
        self.kursid = kursid
        self.sayfa = sayfa
        self.baslik = baslik
        self.aciklama = aciklama

