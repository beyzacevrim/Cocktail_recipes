# Cocktail_recipes

# 🥂 Cocktail Tarifi Öneri Sistemi

Bu Python projesi, kullanıcının elinde bulunan malzemelere göre en uygun kokteyl tariflerini öneren içerik tabanlı bir öneri sistemidir. Word2Vec algoritması ile malzeme benzerlikleri hesaplanır ve kullanıcıya en uygun tarifler sıralanarak sunulur.

## 📌 Proje Hakkında

Kullanıcıdan aldığı malzeme bilgisine göre kokteyl tariflerini analiz eder ve en uygun 3-5 tarifi önerir. Tarifler, `cocktail_recipes.json` dosyasından çekilir. Girdi malzemeleri ile tarif malzemeleri arasındaki benzerlik, Gensim kütüphanesinin Word2Vec modeliyle hesaplanır.

## 🛠️ Kullanılan Teknolojiler

- Python 3
- Gensim (Word2Vec)
- NumPy
- JSON veri formatı

## 🚀 Nasıl Kullanılır?

1. Gerekli kütüphaneleri yükleyin:
pip install gensim numpy


2. `cocktail.py` dosyasını çalıştırın:
python cocktail.py


3. Elinizde bulunan malzemeleri virgülle ayırarak girin:
beyaz rom, lime, buz


4. Eşleşen tarifler benzerlik sırasına göre ekranda listelenir.

## 📂 Dosyalar

- `cocktail.py`: Ana uygulama dosyası.
- `cocktail_recipes.json`: Kokteyl tariflerinin bulunduğu veri dosyası.

## 🔍 Örnek Tarif Çıktısı

Malzemelerinize göre en iyi 3 kokteyl tarifi:

Mojito (Benzerlik: 91.35)
Malzemeler: 50 ml beyaz rom, 1 lime, 2 çay kaşığı şeker, Nane yaprakları, Soda, Buz
Talimatlar: Nane yapraklarını ve şekeri bir bardakta ezin. Lime suyu ve beyaz rom ekleyin. Bardağı buzla doldurun ve soda ile tamamlayın. Nazikçe karıştırın ve servis edin.
Süre: 5 dakika
Zorluk: Kolay


## 👩‍💻 Geliştirici

**Beyza Çevrim**  
Zonguldak Bülent Ecevit Üniversitesi — Bilgisayar Mühendisliği  
2025


