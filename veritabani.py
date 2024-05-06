import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kurslar'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kurslar (ID INTEGER PRIMARY KEY AUTOINCREMENT, Ad TEXT, egitmenid INTEGER, aciklama TEXT, kazanimlar TEXT, Fotograf TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, eposta TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS egitmenler (ID INTEGER PRIMARY KEY AUTOINCREMENT, ad TEXT, soyad TEXT, uzmanlik TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kayitlar (ID INTEGER PRIMARY KEY AUTOINCREMENT, ogrenciid INTEGER, kursid INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS icerik (ID INTEGER PRIMARY KEY AUTOINCREMENT, kursid INTEGER, sayfa INTEGER, baslik TEXT, aciklama TEXT)')
            

            ders_icerikleri = [
                (
                    1,
                    1,
                    "Bilgisayar Biliminin Temelleri",
                    "Bu dersin amacı, katılımcılara bilgisayar biliminin temel prensiplerini ve tarihçesini öğretmektir. Bilgisayarın temel yapı taşları, bilgisayar biliminin dalları ve gelişim süreci ele alınacaktır. Bilgisayar biliminin geçmişten günümüze nasıl evrildiğini anlamak, katılımcıların konuyu daha derinlemesine kavramalarına yardımcı olacaktır."
                ),
                (
                    1,
                    2,
                    "Yazılım ve Donanım İlişkisi",
                    "Bu bölümde, yazılım ve donanım arasındaki ilişki incelenecektir. Bilgisayarın iç ve dış donanım bileşenleri tanıtılacak ve yazılımın donanımla etkileşimi açıklanacaktır. Yazılım ve donanım arasındaki uyum ve etkileşim, katılımcıların bilgisayar sistemlerini daha iyi anlamalarına yardımcı olacaktır."
                ),
                (
                    1,
                    3,
                    "Ağ Temelleri ve Güvenlik İlkeleri",
                    "Bu bölümde, bilgisayar ağları ve iletişim protokolleri üzerine odaklanılacaktır. Ağ güvenliği konusunda temel kavramlar ve güvenlik ilkeleri ele alınarak, katılımcıların ağ güvenliği konusunda farkındalığı artırılacaktır. Bilgisayar ağlarının nasıl çalıştığı ve güvenlik önlemlerinin neden gerektiği hakkında detaylı bir anlayış, katılımcıların bilgisayar ağlarıyla etkili bir şekilde çalışmalarına olanak tanır."
                ),
                (
                    1,
                    4,
                    "Temel Bileşenlerin Çalışma Prensipleri",
                    "Bu bölümde, işlemci, bellek, depolama ve giriş/çıkış cihazları gibi temel bilgisayar bileşenlerinin çalışma prensipleri incelenecektir. Katılımcılar, bilgisayarın iç işleyişini daha iyi anlamak için bu konuları öğreneceklerdir. Her bir bileşenin nasıl çalıştığı ve birbiriyle nasıl etkileşime girdiği hakkında derinlemesine bir bilgi, katılımcıların bilgisayar donanımını daha etkin bir şekilde yönetmelerini sağlar."
                ),
                (
                    1,
                    5,
                    "Yazılım Geliştirme Temelleri",
                    "Bu bölümde, yazılım geliştirme temelleri üzerine odaklanılacaktır. Programlama dilleri, algoritmalar, veri yapıları ve yazılım geliştirme süreçleri ele alınarak, katılımcıların yazılım geliştirme becerileri geliştirilecektir. Temel programlama kavramlarına ve yazılım geliştirme prensiplerine hakim olmak, katılımcıların gelecekteki yazılım projelerinde daha başarılı olmalarına yardımcı olur."
                ),

                #
                (
                    2,
                    1,
                    "Bilgisayar Biliminin Temelleri",
                    "Bu dersin amacı, katılımcılara bilgisayar biliminin temel prensiplerini ve tarihçesini öğretmektir. Bilgisayarın temel yapı taşları, bilgisayar biliminin dalları ve gelişim süreci ele alınacaktır. Bilgisayar biliminin geçmişten günümüze nasıl evrildiğini anlamak, katılımcıların konuyu daha derinlemesine kavramalarına yardımcı olacaktır."
                ),
                (
                    2,
                    2,
                    "Yazılım ve Donanım İlişkisi",
                    "Bu bölümde, yazılım ve donanım arasındaki ilişki incelenecektir. Bilgisayarın iç ve dış donanım bileşenleri tanıtılacak ve yazılımın donanımla etkileşimi açıklanacaktır. Yazılım ve donanım arasındaki uyum ve etkileşim, katılımcıların bilgisayar sistemlerini daha iyi anlamalarına yardımcı olacaktır."
                ),
                (
                    2,
                    3,
                    "Ağ Temelleri ve Güvenlik İlkeleri",
                    "Bu bölümde, bilgisayar ağları ve iletişim protokolleri üzerine odaklanılacaktır. Ağ güvenliği konusunda temel kavramlar ve güvenlik ilkeleri ele alınarak, katılımcıların ağ güvenliği konusunda farkındalığı artırılacaktır. Bilgisayar ağlarının nasıl çalıştığı ve güvenlik önlemlerinin neden gerektiği hakkında detaylı bir anlayış, katılımcıların bilgisayar ağlarıyla etkili bir şekilde çalışmalarına olanak tanır."
                ),
                (
                    2,
                    4,
                    "Temel Bileşenlerin Çalışma Prensipleri",
                    "Bu bölümde, işlemci, bellek, depolama ve giriş/çıkış cihazları gibi temel bilgisayar bileşenlerinin çalışma prensipleri incelenecektir. Katılımcılar, bilgisayarın iç işleyişini daha iyi anlamak için bu konuları öğreneceklerdir. Her bir bileşenin nasıl çalıştığı ve birbiriyle nasıl etkileşime girdiği hakkında derinlemesine bir bilgi, katılımcıların bilgisayar donanımını daha etkin bir şekilde yönetmelerini sağlar."
                ),
                (
                    2,
                    5,
                    "Yazılım Geliştirme Temelleri",
                    "Bu bölümde, yazılım geliştirme temelleri üzerine odaklanılacaktır. Programlama dilleri, algoritmalar, veri yapıları ve yazılım geliştirme süreçleri ele alınarak, katılımcıların yazılım geliştirme becerileri geliştirilecektir. Temel programlama kavramlarına ve yazılım geliştirme prensiplerine hakim olmak, katılımcıların gelecekteki yazılım projelerinde daha başarılı olmalarına yardımcı olur."
                ),

                #

                (
                    3,
                    1,
                    "Bilgisayar Biliminin Temelleri",
                    "Bu dersin amacı, katılımcılara bilgisayar biliminin temel prensiplerini ve tarihçesini öğretmektir. Bilgisayarın temel yapı taşları, bilgisayar biliminin dalları ve gelişim süreci ele alınacaktır. Bilgisayar biliminin geçmişten günümüze nasıl evrildiğini anlamak, katılımcıların konuyu daha derinlemesine kavramalarına yardımcı olacaktır."
                ),
                (
                    3,
                    2,
                    "Yazılım ve Donanım İlişkisi",
                    "Bu bölümde, yazılım ve donanım arasındaki ilişki incelenecektir. Bilgisayarın iç ve dış donanım bileşenleri tanıtılacak ve yazılımın donanımla etkileşimi açıklanacaktır. Yazılım ve donanım arasındaki uyum ve etkileşim, katılımcıların bilgisayar sistemlerini daha iyi anlamalarına yardımcı olacaktır."
                ),
                (
                    3,
                    3,
                    "Ağ Temelleri ve Güvenlik İlkeleri",
                    "Bu bölümde, bilgisayar ağları ve iletişim protokolleri üzerine odaklanılacaktır. Ağ güvenliği konusunda temel kavramlar ve güvenlik ilkeleri ele alınarak, katılımcıların ağ güvenliği konusunda farkındalığı artırılacaktır. Bilgisayar ağlarının nasıl çalıştığı ve güvenlik önlemlerinin neden gerektiği hakkında detaylı bir anlayış, katılımcıların bilgisayar ağlarıyla etkili bir şekilde çalışmalarına olanak tanır."
                ),
                (
                    3,
                    4,
                    "Temel Bileşenlerin Çalışma Prensipleri",
                    "Bu bölümde, işlemci, bellek, depolama ve giriş/çıkış cihazları gibi temel bilgisayar bileşenlerinin çalışma prensipleri incelenecektir. Katılımcılar, bilgisayarın iç işleyişini daha iyi anlamak için bu konuları öğreneceklerdir. Her bir bileşenin nasıl çalıştığı ve birbiriyle nasıl etkileşime girdiği hakkında derinlemesine bir bilgi, katılımcıların bilgisayar donanımını daha etkin bir şekilde yönetmelerini sağlar."
                ),
                (
                    3,
                    5,
                    "Yazılım Geliştirme Temelleri",
                    "Bu bölümde, yazılım geliştirme temelleri üzerine odaklanılacaktır. Programlama dilleri, algoritmalar, veri yapıları ve yazılım geliştirme süreçleri ele alınarak, katılımcıların yazılım geliştirme becerileri geliştirilecektir. Temel programlama kavramlarına ve yazılım geliştirme prensiplerine hakim olmak, katılımcıların gelecekteki yazılım projelerinde daha başarılı olmalarına yardımcı olur."
                ),

                #

                (
                    4,
                    1,
                    "Bilgisayar Biliminin Temelleri",
                    "Bu dersin amacı, katılımcılara bilgisayar biliminin temel prensiplerini ve tarihçesini öğretmektir. Bilgisayarın temel yapı taşları, bilgisayar biliminin dalları ve gelişim süreci ele alınacaktır. Bilgisayar biliminin geçmişten günümüze nasıl evrildiğini anlamak, katılımcıların konuyu daha derinlemesine kavramalarına yardımcı olacaktır."
                ),
                (
                    4,
                    2,
                    "Yazılım ve Donanım İlişkisi",
                    "Bu bölümde, yazılım ve donanım arasındaki ilişki incelenecektir. Bilgisayarın iç ve dış donanım bileşenleri tanıtılacak ve yazılımın donanımla etkileşimi açıklanacaktır. Yazılım ve donanım arasındaki uyum ve etkileşim, katılımcıların bilgisayar sistemlerini daha iyi anlamalarına yardımcı olacaktır."
                ),
                (
                    4,
                    3,
                    "Ağ Temelleri ve Güvenlik İlkeleri",
                    "Bu bölümde, bilgisayar ağları ve iletişim protokolleri üzerine odaklanılacaktır. Ağ güvenliği konusunda temel kavramlar ve güvenlik ilkeleri ele alınarak, katılımcıların ağ güvenliği konusunda farkındalığı artırılacaktır. Bilgisayar ağlarının nasıl çalıştığı ve güvenlik önlemlerinin neden gerektiği hakkında detaylı bir anlayış, katılımcıların bilgisayar ağlarıyla etkili bir şekilde çalışmalarına olanak tanır."
                ),
                (
                    4,
                    4,
                    "Temel Bileşenlerin Çalışma Prensipleri",
                    "Bu bölümde, işlemci, bellek, depolama ve giriş/çıkış cihazları gibi temel bilgisayar bileşenlerinin çalışma prensipleri incelenecektir. Katılımcılar, bilgisayarın iç işleyişini daha iyi anlamak için bu konuları öğreneceklerdir. Her bir bileşenin nasıl çalıştığı ve birbiriyle nasıl etkileşime girdiği hakkında derinlemesine bir bilgi, katılımcıların bilgisayar donanımını daha etkin bir şekilde yönetmelerini sağlar."
                ),
                (
                    4,
                    5,
                    "Yazılım Geliştirme Temelleri",
                    "Bu bölümde, yazılım geliştirme temelleri üzerine odaklanılacaktır. Programlama dilleri, algoritmalar, veri yapıları ve yazılım geliştirme süreçleri ele alınarak, katılımcıların yazılım geliştirme becerileri geliştirilecektir. Temel programlama kavramlarına ve yazılım geliştirme prensiplerine hakim olmak, katılımcıların gelecekteki yazılım projelerinde daha başarılı olmalarına yardımcı olur."
                ),

                #

                (
                    5,
                    1,
                    "Bilgisayar Biliminin Temelleri",
                    "Bu dersin amacı, katılımcılara bilgisayar biliminin temel prensiplerini ve tarihçesini öğretmektir. Bilgisayarın temel yapı taşları, bilgisayar biliminin dalları ve gelişim süreci ele alınacaktır. Bilgisayar biliminin geçmişten günümüze nasıl evrildiğini anlamak, katılımcıların konuyu daha derinlemesine kavramalarına yardımcı olacaktır."
                ),
                (
                    5,
                    2,
                    "Yazılım ve Donanım İlişkisi",
                    "Bu bölümde, yazılım ve donanım arasındaki ilişki incelenecektir. Bilgisayarın iç ve dış donanım bileşenleri tanıtılacak ve yazılımın donanımla etkileşimi açıklanacaktır. Yazılım ve donanım arasındaki uyum ve etkileşim, katılımcıların bilgisayar sistemlerini daha iyi anlamalarına yardımcı olacaktır."
                ),
                (
                    5,
                    3,
                    "Ağ Temelleri ve Güvenlik İlkeleri",
                    "Bu bölümde, bilgisayar ağları ve iletişim protokolleri üzerine odaklanılacaktır. Ağ güvenliği konusunda temel kavramlar ve güvenlik ilkeleri ele alınarak, katılımcıların ağ güvenliği konusunda farkındalığı artırılacaktır. Bilgisayar ağlarının nasıl çalıştığı ve güvenlik önlemlerinin neden gerektiği hakkında detaylı bir anlayış, katılımcıların bilgisayar ağlarıyla etkili bir şekilde çalışmalarına olanak tanır."
                ),
                (
                    5,
                    4,
                    "Temel Bileşenlerin Çalışma Prensipleri",
                    "Bu bölümde, işlemci, bellek, depolama ve giriş/çıkış cihazları gibi temel bilgisayar bileşenlerinin çalışma prensipleri incelenecektir. Katılımcılar, bilgisayarın iç işleyişini daha iyi anlamak için bu konuları öğreneceklerdir. Her bir bileşenin nasıl çalıştığı ve birbiriyle nasıl etkileşime girdiği hakkında derinlemesine bir bilgi, katılımcıların bilgisayar donanımını daha etkin bir şekilde yönetmelerini sağlar."
                ),
                (
                    5,
                    5,
                    "Yazılım Geliştirme Temelleri",
                    "Bu bölümde, yazılım geliştirme temelleri üzerine odaklanılacaktır. Programlama dilleri, algoritmalar, veri yapıları ve yazılım geliştirme süreçleri ele alınarak, katılımcıların yazılım geliştirme becerileri geliştirilecektir. Temel programlama kavramlarına ve yazılım geliştirme prensiplerine hakim olmak, katılımcıların gelecekteki yazılım projelerinde daha başarılı olmalarına yardımcı olur."
                )
            ]




            egitmenler_data = [
                (
                    "Ahmet",
                    "Yıldırım",
                    "Bilişim Sistemleri"
                ),
                (
                    "Zeynep",
                    "Demir",
                    "Yazılım Sistemleri"
                ),
                (
                    "Ayşe",
                    "Kaya",
                    "Yazılım Sistemleri"
                )
            ]
            kurslar_data = [
                (
                    "Temel Bilişim Kavramları",
                    1,
                    "Bu kurs, yazılım, donanım ve bilişim dünyasına ait temel kavramları öğretir. Katılımcılar, bilgisayar bilimindeki temel prensipleri, yazılım ve donanım ilişkilerini anlamayı, ağ kavramlarını ve güvenlik ilkelerini öğrenirler.",
                    "Katılımcılar, bilgisayar sistemlerinin temel bileşenlerini ve çalışma prensiplerini kavrarlar. Ayrıca, ileri seviyedeki derslerde yazılım geliştirme becerilerini geliştirmeleri için sağlam bir temel oluştururlar.",
                    "bilgiteknoloji.png"
                ),
                (
                    "Yazılım Geliştirme Temelleri",
                    1,
                    "Bu kurs, katılımcıların yazılım yeteneklerini geliştirmeyi amaçlar. Temel programlama kavramları üzerine odaklanarak, katılımcılar ileri seviyedeki yazılım geliştirme derslerine hazırlanırlar.",
                    "Katılımcılar, programlama paradigmasını, veri yapılarını ve algoritmaları anlarlar. Ayrıca, bir yazılım projesini baştan sona yönetme becerilerini kazanırlar.",
                    "yazilim.png"
                ),
                (
                    "Yaygın Kullanılan Yazılım Dilleri",
                    2,
                    "Bu kurs, katılımcıların yaygın olarak kullanılan yazılım dilleri hakkında genel bir anlayış geliştirmesini sağlar. Python, Java, C++ gibi dillerin temel yapıları ve kullanım alanları incelenir.",
                    "Katılımcılar, farklı yazılım dillerinin sentaksını ve mantığını anlarlar. Bu bilgi, ileri seviyedeki derslerde çeşitli yazılım projeleri geliştirmelerine olanak tanır.",
                    "python.png"
                ),
                (
                    "Veri Tabanı Yönetimi",
                    2,
                    "Bu kurs, katılımcıların veri tabanı sistemlerini anlamalarını ve yönetmelerini sağlar. SQL dilinin temelleri öğretilir ve ilişkisel veri tabanı tasarımı üzerine odaklanılır.",
                    "Katılımcılar, karmaşık veri tabanı sorguları oluşturabilir ve veri tabanı yönetimi konusunda temel becerilere sahip olurlar.",
                    "siber.png"
                ),
                (
                    "Web Programlama Temelleri",
                    3,
                    "Bu kurs, katılımcıların web tabanlı uygulamalar geliştirmelerini sağlar. HTML, CSS ve JavaScript gibi web teknolojilerinin temel yapısı ve kullanımı öğretilir.",
                    "Katılımcılar, modern web uygulamalarını tasarlayabilir ve geliştirebilir hale gelirler.",
                    "web.png"
                )
                    ]

            self.cursor.executemany("INSERT INTO egitmenler (ad, soyad, uzmanlik) VALUES (?,?,?)",egitmenler_data)
            self.cursor.executemany('INSERT INTO kurslar (ad, egitmenid, aciklama, kazanimlar, fotograf) VALUES (?, ?, ?, ?, ?)', kurslar_data)
            self.cursor.execute("INSERT INTO kullanicilar (eposta, sifre, ad, soyad, telefon) VALUES ('enes', '123', 'Enes', 'Biçici', '5323184256')")
            self.cursor.executemany('INSERT INTO icerik (kursid, sayfa, baslik, aciklama) VALUES (?, ?, ?, ?)', ders_icerikleri)
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
