class MaxHeap:
    def __init__(self):
        self.heap = []

    def ebeveyn_indeks(self, i):
        return (i - 1) // 2

    def sol_cocuk_indeks(self, i):
        return 2 * i + 1

    def sag_cocuk_indeks(self, i):
        return 2 * i + 2

    def ekle(self, veri):
        self.heap.append(veri)
        
        su_anki_indeks = len(self.heap) - 1
        
        while su_anki_indeks > 0:
            baba_indeks = self.ebeveyn_indeks(su_anki_indeks)
            
            if self.heap[su_anki_indeks] > self.heap[baba_indeks]:
                self.heap[su_anki_indeks], self.heap[baba_indeks] = self.heap[baba_indeks], self.heap[su_anki_indeks]
                
                su_anki_indeks = baba_indeks
            else:
                break

    def en_buyugu_getir(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def en_buyugu_sil(self):
        if len(self.heap) == 0:
            return None
            
        max_deger = self.heap[0]
        
        son_eleman = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = son_eleman
            
            self._asagi_tasi(0)
            
        return max_deger

    def _asagi_tasi(self, indeks):
        
        en_buyuk_indeks = indeks
        sol = self.sol_cocuk_indeks(indeks)
        sag = self.sag_cocuk_indeks(indeks)
        
        if sol < len(self.heap) and self.heap[sol] > self.heap[en_buyuk_indeks]:
            en_buyuk_indeks = sol
            
        if sag < len(self.heap) and self.heap[sag] > self.heap[en_buyuk_indeks]:
            en_buyuk_indeks = sag
            
        if en_buyuk_indeks != indeks:
            self.heap[indeks], self.heap[en_buyuk_indeks] = self.heap[en_buyuk_indeks], self.heap[indeks]
            
            self._asagi_tasi(en_buyuk_indeks)

    def yazdir(self):
        print(f"Heap Listesi: {self.heap}")


mh = MaxHeap()
sayilar = [10, 30, 20, 5, 1, 50, 40]

print("--- EKLEME ADIMLARI ---")
for s in sayilar:
    mh.ekle(s)
    print(f"{s} eklendi -> {mh.heap}")

print("\n--- SİLME ADIMLARI (Büyükten Küçüğe) ---")
while len(mh.heap) > 0:
    print(f"Silinen (Max): {mh.en_buyugu_sil()}")
    print(f"Kalan Heap: {mh.heap}")