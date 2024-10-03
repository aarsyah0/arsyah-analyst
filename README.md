# E-commerce Data Dashboard: Visualization & Explanatory Analysis

Dashboard ini merupakan aplikasi visualisasi data untuk menganalisis performa E-commerce berdasarkan beberapa metrik seperti pengeluaran pelanggan, performa kategori produk, dan kinerja pengiriman di berbagai wilayah.

## Live Demo

Anda dapat mengakses dashboard ini secara langsung melalui tautan berikut:

[https://arsyah-analyst-dashboard.streamlit.app/#e-commerce-data-dashboard](https://arsyah-analyst-dashboard.streamlit.app/#e-commerce-data-dashboard)

## Fitur Utama

- **Total Pengeluaran Pelanggan per Negara Bagian**: Pie chart yang menunjukkan distribusi total pengeluaran per negara bagian.
- **Performa Kategori Produk**: Scatter plot untuk menganalisis hubungan antara jumlah pesanan dan skor ulasan rata-rata per kategori produk.
- **Top Kota dengan Penjual Terbanyak**: Diagram garis yang menampilkan jumlah penjual di setiap kota.
- **Kinerja Pengiriman Pesanan**: Bar chart bertumpuk untuk membandingkan jumlah pesanan yang dikirim tepat waktu atau terlambat.

## Persyaratan

Untuk menjalankan aplikasi ini secara lokal, Anda memerlukan beberapa dependensi berikut:

- Python 3.7 atau lebih baru
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Cara Menjalankan Aplikasi Secara Lokal

1. **Clone Repository**

   Clone repository ini dari GitHub:

   ```bash
   git clone https://github.com/aarsyah0/arsyah-analyst.git
   ```

2. **Install Dependencies**
   cd arsyah-analyst
   pip install -r requirements.txt

3. **Jalankan Aplikasi Streamlit**
   cd dashboard
   streamlit run streamlit_app.py
4. **Buka Aplikasi di Browser**
   http://localhost:8501
   **Struktur Proyek**  
   arsyah-analyst/
   │
   ├── dashboard/ # Folder tempat aplikasi Streamlit berada
   │ └── streamlit_app.py # Script utama aplikasi Streamlit
   │
   ├── data/ # Folder tempat menyimpan dataset CSV
   ├── requirements.txt # Daftar dependensi untuk aplikasi
   └── README.md # Dokumentasi proyek ini

**Kontribusi**
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau ajukan issue di repository GitHub.

Dibuat oleh: Sutan Arsyah Nugraha
Email: arsasaja2@gmail.com
ID Dicoding: aarsyah0

### Instruksi

- **Menjalankan aplikasi**: Langkah-langkah untuk menjalankan aplikasi secara lokal sudah disesuaikan dengan path `dashboard/streamlit_app.py`.
- **Git clone**: Langkah untuk meng-clone repository.
- **Live demo**: Tautan langsung ke versi live di Streamlit Cloud.

Dengan README ini, pengguna dapat dengan mudah menjalankan aplikasi baik secara lokal maupun melihat versi live.
