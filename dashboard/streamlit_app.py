import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/df.csv')
all_data = df.copy()  # Menjaga data tetap sama

# Pastikan kolom order_purchase_timestamp adalah datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')

# Title for dashboard
st.title('E-commerce Data Dashboard: Visualization & Explanatory Analysis')

# Sidebar for filtering data
st.sidebar.header("Filter Data")

# Filter for states
state_filter = st.sidebar.multiselect(
    'Pilih Negara Bagian',
    options=all_data['customer_state'].unique(),
    default=all_data['customer_state'].unique()
)

# Filter dataset based on sidebar inputs
filtered_data = all_data[all_data['customer_state'].isin(state_filter)]

# ---- Pertanyaan 1: Wilayah Mana yang Memiliki Pelanggan dengan Total Pengeluaran Tertinggi? ----
st.header("Total Pengeluaran Pelanggan per Negara Bagian")
state_payment = filtered_data.groupby(by="customer_state").agg({
    "order_id": "nunique",
    "payment_value": "sum"
}).sort_values(by="payment_value", ascending=False)

# Plot pie chart for total spending by state
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(state_payment['payment_value'], labels=state_payment.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('coolwarm', len(state_payment)))
ax1.axis('equal')  # Agar lingkaran tetap bulat
st.pyplot(fig1)

# ---- Pertanyaan 2: Bagaimana Performa Kategori Produk Berdasarkan Nilai Pesanan dan Skor Ulasan? ----
st.header("Performa Kategori Produk Berdasarkan Nilai Pesanan dan Skor Ulasan")
category_review = filtered_data.groupby(by="product_category_name_english").agg({
    "order_id": "nunique",
    "review_score": "mean"
}).sort_values(by="order_id", ascending=False)

# Plot scatter antara jumlah pesanan dan skor ulasan
plt.figure(figsize=(10, 6))
sns.scatterplot(x=category_review['order_id'], y=category_review['review_score'], hue=category_review.index, palette='Set2', s=100)
plt.title('Performa Kategori Produk Berdasarkan Pesanan dan Skor Ulasan')
plt.xlabel('Jumlah Pesanan')
plt.ylabel('Skor Ulasan Rata-rata')
plt.legend(title="Kategori Produk", bbox_to_anchor=(1, 1), loc="upper left")
st.pyplot(plt)

# ---- Pertanyaan 3: Apa Saja Kota dengan Penjual Terbanyak dan Bagaimana Kinerja Mereka? ----
st.header("Top 10 Kota dengan Penjual Terbanyak")
top_seller_cities = filtered_data.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).head(10)

# Plot jumlah penjual per kota sebagai diagram garis
plt.figure(figsize=(10, 6))
plt.plot(top_seller_cities.index, top_seller_cities.values, marker='o', linestyle='-', color='b')
plt.title('Top 10 Kota dengan Penjual Terbanyak')
plt.xlabel('Kota')
plt.ylabel('Jumlah Penjual')
plt.xticks(rotation=90)
plt.grid()  # Menambahkan grid untuk mempermudah pembacaan
st.pyplot(plt)

# ---- Pertanyaan 4: Bagaimana Kinerja Pengiriman Pesanan di Berbagai Wilayah? ----
st.header("Kinerja Pengiriman di Setiap Negara Bagian")
on_time_delivery = filtered_data.groupby(by=["customer_state", "delivered_on_time"]).agg({
    "order_id": "nunique"
}).unstack().fillna(0)

# Plot stacked bar untuk pengiriman tepat waktu vs terlambat
on_time_delivery.plot(kind="bar", stacked=True, figsize=(10, 6), color=['red', 'green'])
plt.title('Kinerja Pengiriman di Setiap Negara Bagian')
plt.xlabel('Negara Bagian')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=90)
plt.legend(title="Pengiriman Tepat Waktu", labels=['Terlambat', 'Tepat Waktu'])
st.pyplot(plt)
