def faktoriyel(n):
    if n==1:
        return n
    else:
        return n*faktoriyel(n-1)
print(faktoriyel(6))

#-------------------------------------

def geri_say(n):
    if n==-1:
        print("BİTTİ")
        return
    print(n)
    return geri_say(n-1)
geri_say(9)

#-------------------------------------

def topla(n):
    if n==0:
        return 0
    return n+topla(n-1)
print(topla(10))

#-------------------------------------

def ters_cevir(metin):
    if len(metin)==0:
        return ""
    ilk_harf = metin[0]
    kalan_metin = metin[1:]
    return ters_cevir(kalan_metin)+ilk_harf
print(ters_cevir("ters köşe"))

#-------------------------------------

def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    return fibonacci(n-1)+fibonacci(n-2)
import time
baslangic = time.time()
print(fibonacci(35))
bitis = time.time()
print(f"geçen süre: {bitis-baslangic} saniye")

#-------------------------------------

def us_alma(taban,us):
    if us==0: return 1
    return us_alma(taban,us-1)*taban
print(us_alma(2,10))

#-------------------------------------

hafiza = {}
def fib_zeki(n):
    if n in hafiza:
        return hafiza[n]
    if n<=1:
        return n
    sonuc = fib_zeki(n-1)+fib_zeki(n-2)
    hafiza[n] = sonuc
    return sonuc
import time
baslangic = time.time()
print(f"sonuç: {fib_zeki(35)}")
bitis = time.time()
print(f"geçen süre: {bitis-baslangic} saniye")
