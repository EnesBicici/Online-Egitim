from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from kursliste_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani
from egitim import Kurs,Ogrenci

class ListeSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kursform = Ui_Form()
        self.kursform.setupUi(self)

        Veritabani.query('SELECT * FROM kurslar')
        kurslar = Veritabani.fetchall()
        self.kurslar = []
        for kurs in kurslar:
            kurss = Kurs(*kurs)
            self.kurslar.append(kurss)
            self.kursform.kursBox.addItem(f"{kurss.ad}",kurss.id)

        tablo = self.kursform.tablo
        tablo.setColumnWidth(0, 120)
        tablo.setColumnWidth(1, 120)
        tablo.setColumnWidth(2, 100)
        tablo.setColumnWidth(3, 80)

        self.kursform.kursBox.currentIndexChanged.connect(self.ogrenci_liste_guncelle)

    def goster(self):
        self.show()
        self.ogrenci_liste_guncelle()

    def ogrenci_liste_guncelle(self):
        kurs = self.kurslar[self.kursform.kursBox.currentIndex()]
        tablo = self.kursform.tablo
        Veritabani.query('select ogrenciid from kayitlar where kursid=?',(kurs.id,))
        kayitlar = Veritabani.fetchall()
            
        if kayitlar is None:
            tablo.setRowCount(0)
            return
        tablo.setRowCount(len(kayitlar))
        satir = 0


        for ogrenciid in kayitlar:
            Veritabani.query('SELECT * FROM kullanicilar WHERE id = ?', (ogrenciid[0],))
            ogrencisql = Veritabani.fetchone()
            ogrenci = Ogrenci(*ogrencisql)
            ad = QTableWidgetItem(ogrenci.ad)
            soyad = QTableWidgetItem(ogrenci.soyad)
            eposta = QTableWidgetItem(ogrenci.eposta)
            telefon = QTableWidgetItem(ogrenci.telefon)

            #Hepsinin yazısını ortala
            ad.setTextAlignment(QtCore.Qt.AlignCenter)
            soyad.setTextAlignment(QtCore.Qt.AlignCenter)
            eposta.setTextAlignment(QtCore.Qt.AlignCenter)
            telefon.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, ad)
            tablo.setItem(satir, 1, soyad)
            tablo.setItem(satir, 2, eposta)
            tablo.setItem(satir, 3, telefon)
            
            satir+=1


        #tablo.resizeColumnsToContents()