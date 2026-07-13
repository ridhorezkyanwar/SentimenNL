# SentimenNLP

Analisis Sentimen Review Shopee Bahasa Indonesia dengan NLP dan Machine Learning.

## Deskripsi

Project ini membangun pipeline end-to-end untuk analisis sentimen review Shopee dalam Bahasa Indonesia. Mulai dari muat dataset, pembersihan teks, normalisasi slang, ekstraksi fitur TF-IDF, pelatihan model klasifikasi, hingga evaluasi dan prediksi real-time.

## Judul Project

SentimenNLP

## Fitur Utama

- Pembersihan dan normalisasi teks bahasa Indonesia
- Penanganan kata slang Shopee dan stopword sederhana
- Pembagian data training / testing secara stratified
- Ekstraksi fitur menggunakan TF-IDF
- Pelatihan beberapa model: Logistic Regression, Random Forest, dan Deep Neural Network
- Evaluasi dengan akurasi, precision, recall, F1-score, dan confusion matrix
- Contoh inferensi real-time dengan teks review baru

## Struktur Folder

- `dataset_shopee.csv`  : dataset review Shopee
- `pelatihan_dan_inferensi.ipynb`  : notebook end-to-end untuk training, evaluasi, dan inference
- `scraping.py`  : script scraping data review (jika ingin mengumpulkan data tambahan)
- `requirements.txt`  : dependensi Python untuk menjalankan project
- `model_sentimen_terbaik.h5`  : model hasil pelatihan yang disimpan dari notebook

## Teknologi

- Python 3
- pandas
- numpy
- scikit-learn
- tensorflow
- matplotlib
- seaborn
- google-play-scraper

## Langkah Persiapan dan Instalasi

1. Buka terminal di folder project.
2. Buat virtual environment (opsional tetapi direkomendasikan):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. Install dependensi:

   ```powershell
   pip install -r requirements.txt
   ```

4. Jalankan notebook untuk melihat seluruh proses:

   ```powershell
   jupyter notebook pelatihan_dan_inferensi.ipynb
   ```

## Cara Menjalankan

- Buka `pelatihan_dan_inferensi.ipynb` dan jalankan sel secara berurutan.
- Notebook memuat dataset, membersihkan teks, melatih model, mengevaluasi performa, lalu melakukan inferensi pada kalimat contoh.
- Jika ingin menjalankan model secara manual, Anda dapat memuat `model_sentimen_terbaik.h5` di dalam Python dan menerapkan `vectorizer` yang tersimpan.

## Hasil Utama

Notebook menampilkan hasil berikut (perkiraan berdasarkan output latihan):

- Akurasi testing model utama: sekitar 88%
- Precision dan recall yang baik terutama untuk kelas positif
- Confusion matrix yang memvisualisasikan performa model
- Contoh prediksi:
  - "Aplikasi Shopee jelek sekali, loadingnya lemot dan sering keluar sendiri!" → Negatif
  - "Sangat puas belanja di sini, barang cepat sampai dan banyak diskon gratis ongkir!" → Positif

## Proses Upload ke GitHub

1. Buat repository baru di GitHub dengan nama misalnya `sentimen-nlp`.
2. Tambahkan deskripsi singkat: `Analisis sentimen review Shopee Bahasa Indonesia menggunakan NLP dan machine learning.`
3. Di folder project lokal, jalankan:

   ```powershell
   git init
   git add .
   git commit -m "Initial commit: add SentimenNLP project"
   git branch -M main
   git remote add origin https://github.com/<username>/sentimen-nlp.git
   git push -u origin main
   ```

4. Pastikan file `README.md`, `requirements.txt`, `pelatihan_dan_inferensi.ipynb`, dan `dataset_shopee.csv` ada di repo.
5. Buka halaman GitHub repository, dan verifikasi README sudah tampil dengan baik.

## Saran untuk Portfolio

- Gunakan judul repository `sentimen-nlp` atau `analisis-sentimen-shopee`.
- Tambahkan deskripsi repository yang jelas.
- Sertakan screenshot atau ringkasan hasil evaluasi di README jika memungkinkan.
- Tambahkan bagian "Apa yang saya pelajari" untuk menjelaskan pengalaman Anda dengan NLP, preprocessing, dan evaluasi model.

## Kontak

Jika ingin menambahkan informasi personal, tambahkan di README:

- Nama: [Nama Anda]
- Email: [email@example.com]
- LinkedIn: [link LinkedIn]

---

README ini dibuat sebagai dokumentasi portfolio untuk project SentimenNLP.
