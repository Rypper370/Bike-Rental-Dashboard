# Bike Rental Dashboard 

## Deskripsi
Dashboard ini dikembangkan menggunakan Streamlit untuk menganalisis tren penyewaan sepeda berdasarkan dataset `day.csv`. Dashboard menyajikan berbagai visualisasi termasuk tren harian, tren berdasarkan musim, dan perbandingan penyewaan di hari kerja dan akhir pekan.

## Persyaratan
```
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal dependensi berikut:
- Python 3.7 atau lebih baru
- Streamlit
- Pandas
- Matplotlib
- Seaborn
```

##Instalasi
```
mkdir Bike Sharing Dashboard
cd Bike Sharing Dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Cara Menjalankan
```
1. Pastikan file `dashboard.py` dan dataset `day.csv` berada dalam satu direktori.
2. Buka terminal atau command prompt, lalu arahkan ke direktori yang berisi file tersebut.
3. Jalankan perintah berikut: streamlit run dashboard.py
4. Aplikasi akan berjalan di browser dengan alamat default `http://localhost:8501/`.
```

## Fitur Dashboard

1. **Filter Rentang Waktu**: Sidebar memungkinkan pengguna memilih rentang tanggal untuk analisis.
2. **Statistik Umum**:
   - Total penyewaan selama periode yang dipilih
   - Rata-rata penyewaan harian
   - Penyewaan maksimum dalam satu hari
   - Jumlah hari yang dianalisis
3. **Tren Penyewaan Harian**: Grafik garis yang menampilkan total penyewaan per hari.
4. **Penyewaan Berdasarkan Musim**: Grafik batang yang menunjukkan jumlah penyewaan di setiap musim.
5. **Perbandingan Penyewaan Hari Kerja dan Akhir Pekan**: Grafik batang yang membandingkan rata-rata penyewaan di hari kerja dan akhir pekan untuk setiap musim.



