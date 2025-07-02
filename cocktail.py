import json
import gensim
from gensim.models import Word2Vec
import numpy as np

# JSON dosyasından kokteyl tariflerini yükle
try:
    with open("cocktail_recipes.json", "r", encoding="utf-8") as f:
        tarifler = json.load(f)
except FileNotFoundError:
    print("cocktail_recipes.json dosyası bulunamadı. Lütfen tarifleri ekleyin.")
    exit()

# Tüm tariflerden tüm malzemeleri topla
tüm_malzemeler = []
for tarif in tarifler:
    tüm_malzemeler.extend([malzeme.lower() for malzeme in tarif["ingredients"]])

# Word2Vec modeli eğit
model = Word2Vec([tüm_malzemeler], min_count=1, vector_size=100, window=5, sg=1)

# Benzerlik hesaplama fonksiyonu
def benzerlik_hesapla(kullanıcı_malzemeleri, tarif_malzemeleri):
    if not kullanıcı_malzemeleri or not tarif_malzemeleri:
        return 0
    benzerlikler = []
    for malzeme in kullanıcı_malzemeleri:
        malzeme_benzerlikleri = []
        for hedef in tarif_malzemeleri:
            try:
                malzeme_benzerlikleri.append(model.wv.similarity(malzeme, hedef))
            except KeyError:
                pass  # Modelde olmayan malzemeleri yoksay
        if malzeme_benzerlikleri:
            benzerlikler.append(max(malzeme_benzerlikleri))  # En yüksek benzerliği al
    return np.mean(benzerlikler) if benzerlikler else 0

# Kullanıcıdan mevcut malzemeleri al
kullanıcı_malzemeleri = input("Malzemelerinizi virgülle ayırarak girin: ").split(",")
kullanıcı_malzemeleri = [malzeme.strip().lower() for malzeme in kullanıcı_malzemeleri]

# Benzerliğe dayalı olarak eşleşen tarifleri bul
eşleşen_tarifler = []
for tarif in tarifler:
    tarif_malzemeleri = [malzeme.lower() for malzeme in tarif["ingredients"]]
    benzerlik = benzerlik_hesapla(kullanıcı_malzemeleri, tarif_malzemeleri)
    if benzerlik > 0:  # Sadece pozitif benzerliğe sahip tarifleri ekle
        eşleşen_tarifler.append((tarif, benzerlik))

# Tarifleri benzerliğe göre sırala
eşleşen_tarifler.sort(key=lambda x: x[1], reverse=True)

# En iyi 3 tarifi göster
if eşleşen_tarifler:
    print("Malzemelerinize göre en iyi 3 kokteyl tarifi:")
    for i, (tarif, benzerlik) in enumerate(eşleşen_tarifler[:5]):
        benzerlik_yuzde=benzerlik*100
        print(f"\n{i + 1}. {tarif['name']} (Benzerlik: {benzerlik_yuzde:.2f})")
        print(f"  Malzemeler: {', '.join(tarif['ingredients'])}")
        print(f"  Talimatlar: {' '.join(tarif['instructions'])}")
        print(f"  Süre: {tarif['duration']}")
        print(f"  Zorluk: {tarif['difficulty']}")
else:
    print("Malzemeleriniz için eşleşen tarif bulunamadı.")
