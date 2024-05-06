from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui
from egitim import *
from veritabani import Veritabani
from kursolustur import KursEkleSayfa
from kurs import KursSayfa
from kursliste import ListeSayfa
from icerik import IcerikSayfa

class AnaSayfa(QMainWindow):
    def __init__(self, uye) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.uye = uye
        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki)
        Veritabani.query('SELECT * FROM egitmenler')
        egitmenler = Veritabani.fetchall()
        self.anasayfa.egitmenBox.currentIndexChanged.connect(lambda: self.kurs_liste_guncelle(1))
        for egitmen in egitmenler:
            egitmenn = Egitmen(*egitmen)
            self.anasayfa.egitmenBox.addItem(f"{egitmenn.ad} {egitmenn.soyad}",egitmenn.id)
        kursolustursayfa = KursEkleSayfa()
        self.anasayfa.kursolustur.triggered.connect(lambda: kursolustursayfa.show())
        kursolustursayfa.ekle_sinyal.connect(self.kurs_liste_guncelle)
        self.anasayfa.secButon.clicked.connect(self.kurssec)
        self.kurssayfa = KursSayfa()
        listesayfa = ListeSayfa()
        self.anasayfa.kurslistesi.triggered.connect(lambda: listesayfa.goster())
        iceriksayfa = IcerikSayfa()
        self.anasayfa.icerikyukle.triggered.connect(lambda: iceriksayfa.goster())

    def sonraki(self):
        self.index += 1
        if len(self.kurslar) == self.index:
            self.index = 0
        self.kursguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.kurslar)-1
        self.kursguncelle()

    def kursgoster(self, yeni_indeks):
        self.index = yeni_indeks
        self.kursguncelle()

    def kursguncelle(self):
        kurs = self.kurslar[self.index]
        Veritabani.query('SELECT * FROM kayitlar where ogrenciid=? and kursid=?',(self.uye.id, kurs.id))
        kayit = Veritabani.fetchone()
        if kayit is None:
            self.anasayfa.secButon.setText("Kayıt Ol")
        else:
            self.anasayfa.secButon.setText("Seç")
        egitmenid = self.anasayfa.egitmenBox.currentData()
        self.anasayfa.fotoLabel.setPixmap(QtGui.QPixmap("fotograf/" + kurs.fotograf))
        self.anasayfa.kursLabel.setText(kurs.ad)
        self.anasayfa.aciklamaLabel.setText(kurs.aciklama)
        self.anasayfa.kazanimlar.setText(kurs.kazanimlar)


    def kurs_liste_guncelle(self, index):
        if index == 1:
            self.index = 0
        egitmen = self.anasayfa.egitmenBox.currentData()
        Veritabani.query('SELECT * FROM kurslar where egitmenid=?',(egitmen,))
        kurslar = Veritabani.fetchall()
        self.kurslar = []
        for kurs in kurslar:
            self.kurslar.append(Kurs(*kurs))
        self.kursguncelle()

    def kurssec(self):
        buton = self.anasayfa.secButon 
        kurs = self.kurslar[self.index] 
        Veritabani.query('SELECT * FROM icerik where kursid=?',(kurs.id,))
        icerik = Veritabani.fetchone()
        if buton.text() == "Kayıt Ol":
            yanit = QMessageBox.warning(self,"Kurs", "Kurs'a kaydolmak istediğinize emin misiniz?",QMessageBox.Yes,QMessageBox.No)
            if yanit == QMessageBox.No:
                return
            kurs.kaydol(self.uye)
            self.kursguncelle()
            QMessageBox.information(self,"Kurs", "Kaydınız oluşturuldu.",QMessageBox.Ok)
        elif icerik is None:
            QMessageBox.information(self,"Kurs", "İçerik Bulunamadı",QMessageBox.Ok)
        else:
            self.kurssayfa.goster(kurs)
