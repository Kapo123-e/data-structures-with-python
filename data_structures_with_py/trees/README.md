Bu klasör neden var?
- Bu klasör, ağaç (Tree) veri yapılarının farklı türlerini ve bu yapılar üzerinde gerçekleştirilen temel işlemleri içermektedir.

Ağaçlar;
- Hiyerarşik veri temsilinde
- Arama, sıralama ve indeksleme problemlerinde
- Dosya sistemleri ve veritabanlarında
* çok yaygın kullanılan temel veri yapılarındandır.


Klasör İçeriği:
trees/
├── recursion/ → Ağaçlarda kullanılan rekürsif yapıların temeli
├── avl_tree.py → Dengeli ikili arama ağacı (AVL)
├── binary_search_tree.py → Binary Search Tree (BST)
├── general_tree.py → Genel ağaç yapısı
├── max_heap.py → Max Heap veri yapısı
├── tree_traversals.py → Ağaç dolaşma (traversal) algoritmaları
└── README.md


Tasarım Kararı: Rekürsiyon neden ayrı klasör?
 - Rekürsiyon bir veri yapısı değildir. Ancak ağaçların:
  * Dolaşımı
  * Aranması
  * Dengelenmesi
 - neredeyse her zaman rekürsif düşünce gerektirir.
 - Bu yüzden recursion klasörü:
  * Ağaçlarla doğrudan ilişkili
  * Ama kavramsal olarak yardımcı bir yapı olarak konumlandırılmıştır
 - Bu yaklaşım, konular arasında anlamsal bağ kurmayı hedefler.


Dosyalar neyi temsil ediyor?
 - binary_search_tree.py → Temel BST ekleme ve arama mantığı
 - avl_tree.py → BST'nin dengesizliğini çözen AVL ağacı
 - max_heap.py → Öncelik bazlı veri erişimi (priority queue altyapısı)
 - tree_traversals.py → Preorder, Inorder, Postorder dolaşım algoritmaları
 - general_tree.py → İkili olmayan, çok çocuklu genel ağaç yapısı


Amaç
 - Ağaç veri yapılarının farklarını net görmek
 - Aynı problem için farklı ağaç türlerinin avantajlarını anlamak
 - Rekürsif düşünceyi doğal hale getirmek