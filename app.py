import streamlit as st, locale
from streamlit_option_menu import option_menu
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

with st.sidebar:
    select = option_menu('Konversi Mata Uang', 
                         ['HOME', 
                          'USD TO IDR', 
                          'MYR TO IDR',
                          'EUR TO IDR',
                          'YEN TO IDR'],
                         default_index=0)

if select == 'HOME':
    st.title('WELCOME TO FOURCODERS')
    st.text("hai")
    st.write("hai")

if select == 'USD TO IDR':
    st.title('KONVERSI USD TO IDR')

    usdValue = st.number_input('Masukkan jumlah USD yang ingin di konversi: ', 0)
    hitung = st.button('Hitung')

    if hitung:  
        kurs = 15.854
        hasil = usdValue*kurs
        hasil = locale.currency(hasil, grouping=True, symbol=True)
        st.write("hasilnya", hasil)
        st.success(f'hasilnya adalah = {hasil}')

if select == 'MYR TO IDR':
    st.title('KONVERSI MYR TO IDR')

    myrValue = st.number_input('Masukkan jumlah MYR yang ingin di konversi: ', 0)
    hitung = st.button('Hitung')

    if hitung:  
        kurs = 3.574
        hasil = myrValue*kurs
        hasil = locale.currency(hasil, grouping=True, symbol=True)
        st.write("hasilnya", hasil)
        st.success(f'hasilnya adalah = {hasil}')

if select == 'EUR TO IDR':
    st.title('KONVERSI EUR TO IDR')

    eurValue = st.number_input('Masukkan jumlah EUR yang ingin di konversi: ', 0)
    hitung = st.button('Hitung')

    if hitung:  
        kurs = 16.800
        hasil = eurValue*kurs
        hasil = locale.currency(hasil, grouping=True, symbol=True)
        st.write("hasilnya", hasil)
        st.success(f'hasilnya adalah = {hasil}')

if select == 'YEN TO IDR':
    st.title('KONVERSI YEN TO IDR')

    yenValue = st.number_input('Masukkan jumlah YEN yang ingin di konversi: ', 0)
    hitung = st.button('Hitung')

    if hitung:  
        kurs = 106
        hasil = yenValue*kurs
        hasil = locale.currency(hasil, grouping=True, symbol=True)
        st.write("hasilnya", hasil)
        st.success(f'hasilnya adalah = {hasil}')