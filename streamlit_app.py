import streamlit as st
import math, time

st.markdown('''
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px;'>
    <h1>This is a header with background color</h1>
    <p>This is some text inside a div with background color.</p>
</div>
''', unsafe_allow_html=True)

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
