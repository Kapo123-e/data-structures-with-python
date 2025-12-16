Bu klasör neden var?
 - Bu klasör, rekürsif düşünceyi izole şekilde anlamak için oluşturulmuştur.
 - Rekürsiyon;
  * Fonksiyonun kendisini çağırmasıdır
  * Matematiksel tanımlarla uyumludur
  * Ağaçlar ve grafikler için vazgeçilmezdir
 - Ancak çoğu zaman:
  * "Rekürsiyon ezberlenir ama anlaşılmaz"
 - Bu klasörün amacı bunu kırmaktır.


 İçerik:
 recursion/
├── recursive.py
└── README.md


recursive.py içinde ne var?
 - Bu dosyada:
  * Faktöriyel
  * Fibonacci
  * Geri sayım
  * Metin ters çevirme
  * Üs alma
 gibi temel rekürsif problemler yer alır.

Neden bu örnekler?
 - Küçük
 - Takip edilebilir
 - Çağrı yığını (call stack) net görülebilir

Amaç:
 - Ağaç koduna geçmeden önce rekürsiyon refleksi kazanmak


 Neden trees altında?
 - Çünkü:
  * Ağaçların doğal çalışma biçimi rekürsiftir
  * Traversal, arama ve ekleme işlemleri hep aynı mantığı kullanır
 - Bu klasör, ağaç kodları için zihinsel hazırlık alanıdır.


Hedef:
 - Rekürsiyon korkusunu ortadan kaldırmak
 - Ağaç algoritmalarını okurken "ne oluyor" sorusunu sormamak
 - Daha ileri algoritmalara (DFS, BFS, backtracking) zemin hazırlamak