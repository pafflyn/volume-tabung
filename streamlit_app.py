import streamlit as st
import math, time

st.title("Menghitung volume tabung ")

r = number = st.number_input('Masukkan Jari-Jari (cm):', 0)
t = number = st.number_input('Masukkan Tinggi(cm):', 0)

if st.button("Hitung volume", type='primary'):
    loading = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        loading.progress(i+1)
   
   
    v = math.pi*(r**2)*t
    st.success(f'Volume tabung adalah {v:2f}')
