class AVLDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None
        self.yukseklik = 1

class AVLAgaci:
    
    def yukseklik_al(self, dugum):
        if not dugum: return 0
        return dugum.yukseklik

    def denge_getir(self, dugum):
        if not dugum: return 0
        return self.yukseklik_al(dugum.sol) - self.yukseklik_al(dugum.sag)

    def saga_dondur(self, z):
        y = z.sol
        T3 = y.sag
        y.sag = z
        z.sol = T3
        z.yukseklik = 1 + max(self.yukseklik_al(z.sol), self.yukseklik_al(z.sag))
        y.yukseklik = 1 + max(self.yukseklik_al(y.sol), self.yukseklik_al(y.sag))
        return y

    def sola_dondur(self, z):
        y = z.sag
        T2 = y.sol
        y.sol = z
        z.sag = T2
        z.yukseklik = 1 + max(self.yukseklik_al(z.sol), self.yukseklik_al(z.sag))
        y.yukseklik = 1 + max(self.yukseklik_al(y.sol), self.yukseklik_al(y.sag))
        return y

    def ekle(self, dugum, veri):
        
        if not dugum:
            return AVLDugumu(veri)
        
        if veri < dugum.veri:
            dugum.sol = self.ekle(dugum.sol, veri)
        elif veri > dugum.veri:
            dugum.sag = self.ekle(dugum.sag, veri)
        else:
            return dugum

        
        dugum.yukseklik = 1 + max(self.yukseklik_al(dugum.sol), self.yukseklik_al(dugum.sag))

        denge = self.denge_getir(dugum)

        
        if denge > 1 and veri < dugum.sol.veri:
            return self.saga_dondur(dugum)

        if denge < -1 and veri > dugum.sag.veri:
            return self.sola_dondur(dugum)

        if denge > 1 and veri > dugum.sol.veri:
            dugum.sol = self.sola_dondur(dugum.sol)
            return self.saga_dondur(dugum)

        if denge < -1 and veri < dugum.sag.veri:
            dugum.sag = self.saga_dondur(dugum.sag)
            return self.sola_dondur(dugum)

        return dugum

    def ara(self, dugum, aranan):
        if not dugum: return False
        if dugum.veri == aranan: return True
        if aranan < dugum.veri: return self.ara(dugum.sol, aranan)
        return self.ara(dugum.sag, aranan)

    def yazdir(self, dugum, seviye=0):
        if not dugum: return
        self.yazdir(dugum.sag, seviye + 1)
        print("    " * seviye + str(dugum.veri))
        self.yazdir(dugum.sol, seviye + 1)

avl = AVLAgaci()
root = None

sayilar = [50, 20, 60, 10, 40, 45]

print("--- EKLEME ADIMLARI ---")
for s in sayilar:
    print(f"\nEkleniyor: {s}")
    root = avl.ekle(root, s)
    avl.yazdir(root)
    print("-" * 20)