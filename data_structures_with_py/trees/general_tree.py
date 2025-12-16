class AgacDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.cocuklar = []
        self.ebeveyn = None

    def cocuk_ekle(self, cocuk_dugumu):
        self.cocuklar.append(cocuk_dugumu)
        cocuk_dugumu.ebeveyn = self

    def agaci_yazdir(self):
        seviye = self.seviye_bul()
        
        bosluk = "  " * seviye * 2
        prefix = bosluk + "|__ " if self.ebeveyn else ""
        
        print(prefix + self.veri)
        
        if self.cocuklar:
            for cocuk in self.cocuklar:
                cocuk.agaci_yazdir()

    def seviye_bul(self):
        seviye = 0
        p = self.ebeveyn
        while p:
            seviye += 1
            p = p.ebeveyn
        return seviye
    
    def ara(self, aranan_deger):
        if self.veri == aranan_deger:
            return self
        
        for cocuk in self.cocuklar:
            sonuc = cocuk.ara(aranan_deger)
            if sonuc is not None:
                return sonuc
        
        return None


root = AgacDugumu("Elektronik")

laptop = AgacDugumu("Laptop")
telefon = AgacDugumu("Telefon")
tv = AgacDugumu("Televizyon")

root.cocuk_ekle(laptop)
root.cocuk_ekle(telefon)
root.cocuk_ekle(tv)

macbook = AgacDugumu("MacBook")
oyun_pc = AgacDugumu("Gaming Laptop")
is_pc = AgacDugumu("İş Bilgisayarı")

laptop.cocuk_ekle(macbook)
laptop.cocuk_ekle(oyun_pc)
laptop.cocuk_ekle(is_pc)

iphone = AgacDugumu("iPhone")
samsung = AgacDugumu("Samsung")

telefon.cocuk_ekle(iphone)
telefon.cocuk_ekle(samsung)

msi = AgacDugumu("MSI Raider")
asus = AgacDugumu("Asus ROG")

oyun_pc.cocuk_ekle(msi)
oyun_pc.cocuk_ekle(asus)

print("--- MAĞAZA KATEGORİ AĞACI ---")
root.agaci_yazdir()

bulunan = root.ara("Samsung")
sonuc_1 = f"Test 1 (Var Olan): {bulunan.veri}, Seviye: {bulunan.seviye_bul()}" if bulunan else "Test 1: Bulunamadı"


bulunan_yok = root.ara("Buzdolabı")
sonuc_2 = f"Test 2 (Olmayan): {bulunan_yok.veri}" if bulunan_yok else "Test 2 (Olmayan): Başarıyla None döndü."

print(sonuc_1)
print(sonuc_2)