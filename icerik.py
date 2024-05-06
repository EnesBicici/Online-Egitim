from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from icerik_ui import Ui_Form
from veritabani import Veritabani
from egitim import Kurs
from icerikyukle import IcerikYukleSayfa

class IcerikSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ekleButon.clicked.connect(self.ekle)

    def goster(self):
        Veritabani.query("SELECT kurslar.* FROM kurslar LEFT JOIN icerik ON kurslar.id = icerik.kursid WHERE icerik.kursid IS NULL")
        kurslar = Veritabani.fetchall()
        self.kurslar = []
        self.form.kursBox.clear()
        for kurs in kurslar:
            kurss = Kurs(*kurs)
            self.form.kursBox.addItem(kurss.ad, kurss.id)
            self.kurslar.append(kurss)
        self.show()

    def ekle(self):
        index = self.form.kursBox.currentIndex()
        if index < 0:
            return
        kurs = self.kurslar[index]
        sayfa = self.form.sayfaBox.value()
        self.icerikyuklesayfa = IcerikYukleSayfa()
        self.icerikyuklesayfa.goster(kurs,sayfa)
        self.close()