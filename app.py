import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# Data contoh
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([3000, 3500, 4000, 5000, 6000, 6500, 7000, 8500, 9000, 10000])

# Membuat model regresi linear
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Judul aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

# Input tahun pengalaman kerja
years_experience = st.number_input("Masukkan jumlah tahun bekerja:", min_value=0.0, step=0.1)

# Prediksi gaji
if st.button("Prediksi Gaji"):
    gaji = lin_reg.predict([[years_experience]])
    st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah ${gaji[0]:,.2f}")