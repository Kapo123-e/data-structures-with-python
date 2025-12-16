class BSTDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None
        

    def ekle(self, yeni_veri):
        if self.veri == yeni_veri:
            return

        if yeni_veri < self.veri:
            if self.sol is None:
                self.sol = BSTDugumu(yeni_veri)
            else:
                self.sol.ekle(yeni_veri)
        
        elif yeni_veri > self.veri:
            if self.sag is None:
                self.sag = BSTDugumu(yeni_veri)
            else:
                self.sag.ekle(yeni_veri)


    def yazdir(self, seviye=0):
        if self.sag:
            self.sag.yazdir(seviye + 1)
        
        print("    " * seviye + str(self.veri))

        if self.sol:
            self.sol.yazdir(seviye + 1)


    def seviye_bul1(self, aranan_deger):
        seviye = 0
        if self.veri == aranan:
            return seviye
        if aranan_deger<self.veri:
            if self.sol is None:
                return seviye
            else:
                seviye+=1
                return seviye + self.sol.seviye_bul1(aranan_deger)
        elif aranan_deger>self.veri:
            if self.sag is None:
                return seviye
            else:
                seviye+=1
                return seviye + self.sag.seviye_bul1(aranan_deger)
        else:
            return seviye
        

    def seviye_bul2(self, aranan, suanki_seviye=0):
        if self.veri == aranan:
            return suanki_seviye
        
        if aranan < self.veri:
            if self.sol:
                return self.sol.seviye_bul2(aranan, suanki_seviye + 1)
            else:
                return -1
        
        elif aranan > self.veri:
            if self.sag:
                return self.sag.seviye_bul2(aranan, suanki_seviye + 1)
            else:
                return -1


    def ara1(self, aranan_deger):
        if aranan_deger<self.veri:
            if self.sol is None:
                return self.veri==aranan_deger
            else:
                return self.sol.ara1(aranan_deger)
        elif aranan_deger>self.veri:
            if self.sag is None:
                return self.veri==aranan_deger
            else:
                return self.sag.ara1(aranan_deger)
        else:
            return self.veri==aranan_deger
    
    
    def ara2(self, aranan):
        if self.veri == aranan:
            return True
        elif aranan < self.veri and self.sol:
            return self.sol.ara2(aranan)
        elif aranan > self.veri and self.sag:
            return self.sag.ara2(aranan)
        return False
    
    


root = BSTDugumu(50)

print("--- Ekleme İşlemleri Başlıyor ---")
liste = [30, 70, 20, 40, 60, 80]
for s in liste:
    root.ekle(s)

print("--- AĞAÇ YAPISI (Yan Yatmış) ---")
root.yazdir()
print("-" * 30)

aranan = int(input("Aramak istediğiniz değeri giriniz:"))
bulunan = root.ara(aranan)
sonuc_1 = f"{aranan} verisi BTS'de bulundu. BTS'nin {root.seviye_bul2(aranan)}. seviyesinde." if bulunan else "{aranan} verisi bulunamadı."
print(sonuc_1)