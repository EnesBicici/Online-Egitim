from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from kursolustur_ui import Ui_Form
from egitim import Kurs,Egitmen
from veritabani import Veritabani

class KursEkleSayfa(QWidget):
    ekle_sinyal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.olusturButon.clicked.connect(self.ekle)
        Veritabani.query('SELECT * FROM egitmenler')
        egitmenler = Veritabani.fetchall()
        for egitmen in egitmenler:
            egitmenn = Egitmen(*egitmen)
            self.form.egitmenBox.addItem(f"{egitmenn.ad} {egitmenn.soyad}",egitmenn.id)
        
    def ekle(self):
        yanit = QMessageBox.warning(self,"Kurs Oluştur", "Kurs oluşturmak istediğinize emin misiniz?",QMessageBox.Yes,QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        egitmen = self.form.egitmenBox.currentData()
        kursisim = self.form.kursadi.text()
        aciklama = self.form.aciklama.toPlainText()
        kazanimlar = self.form.kazanimlar.toPlainText()
        Kurs.kursolustur(kursisim,egitmen,aciklama,kazanimlar,"yazilim.png")
        self.ekle_sinyal.emit(0)
        QMessageBox.information(self,"Kurs Oluştur", "Kurs oluşturuldu.",QMessageBox.Ok)
