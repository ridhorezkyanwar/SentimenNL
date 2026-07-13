from google_play_scraper import Sort, reviews
import pandas as pd
import time


def scrape_data():
    app_id = "com.shopee.id"  # ID Aplikasi Shopee di Play Store
    all_reviews = []
    continuation_token = None

    print("Memulai proses scraping ulasan Shopee...")

    # Kita butuh 10.000 data. API mengambil 200 data per request, jadi kita loop 50 kali.
    for i in range(50):
        result, continuation_token = reviews(
            app_id,
            lang="id",
            country="id",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token,
        )

        if not result:
            print("Tidak ada data lagi yang bisa diambil.")
            break

        all_reviews.extend(result)
        print(f"Batch {i+1} selesai. Total data terkumpul: {len(all_reviews)}")

        if len(all_reviews) >= 10000:
            print("Target 10.000 data tercapai!")
            break

        time.sleep(2)  # Delay 2 detik agar tidak diblokir oleh Google Play

    df = pd.DataFrame(all_reviews)
    # Ambil hanya kolom teks ulasan dan rating bintang
    df = df[["content", "score"]]
    df = df.dropna()

    # Simpan ke CSV
    df.to_csv("dataset_shopee.csv", index=False)
    print(f"Scraping selesai! Total data tersimpan: {len(df)}")


if __name__ == "__main__":
    scrape_data()
