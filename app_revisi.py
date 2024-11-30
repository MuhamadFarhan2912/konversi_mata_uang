import streamlit as st
import locale
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Konversi Mata Uang", page_icon="💰", layout="wide")

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

st.markdown("""
    <style>
    .sidebar {
        width: 300px;
        background-color: blue;
        padding: 20px;
    }

    .sidebar h1 {
        text-align: left;
        font-weight: bold;
        font-size: 24px;
        color: #2a3d45;
    }

    .sidebar .stButton > button {
        background-color: #007bff;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        width: 100%;
    }

    .sidebar .stButton > button:hover {
        background-color: #0056b3;
    }
    
    .main {
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1>Konversi Mata Uang</h1>", unsafe_allow_html=True)
    st.markdown("Pilih menu untuk konversi mata uang.")
    
    select = option_menu('Pilih Menu', 
                         ['HOME', 'KONVERSI MATA UANG'],
                         icons=['house', 'currency-dollar'],  
                         default_index=0,
                         styles={"container": {"padding": "5px", "background-color": "#f8f9fa"},
                                 "icon": {"color": "black", "font-size": "20px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "10px"}})

if select == 'HOME':
    st.title('WELCOME TO FOURCODERS')
    st.text("Aplikasi Konversi Mata Uang Sederhana")
    st.markdown("""
    **FourCoders** menyajikan aplikasi konversi mata uang yang mudah digunakan.
    Pilih mata uang yang ingin dikonversi dan masukkan jumlah yang diinginkan.
    """)
    st.image("https://i.pinimg.com/736x/e7/5e/5f/e75e5fb7ab8de31ec5a8d8781e66a222.jpg", caption="Selamat datang di web fourcoders", use_container_width=True)

if select == 'KONVERSI MATA UANG':
    st.title('KONVERSI MATA UANG')

    col1, col2 = st.columns([1, 1])  

    with col1:
        mata_uang_asal = st.selectbox("Pilih Mata Uang Asal", ["USD", "MYR", "EUR", "YEN", "IDR"])
        if mata_uang_asal == "USD":
            bendera_asal = "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg"
        elif mata_uang_asal == "MYR":
            bendera_asal = "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg"
        elif mata_uang_asal == "EUR":
            bendera_asal = "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg"
        elif mata_uang_asal == "YEN":
            bendera_asal = "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg"
        elif mata_uang_asal == "IDR":
            bendera_asal = "IDR.png"  
        st.image(bendera_asal, width=50)

    with col2:
        mata_uang_tujuan = st.selectbox("Pilih Mata Uang Tujuan", ["USD", "MYR", "EUR", "YEN", "IDR"])
        if mata_uang_tujuan == "USD":
            bendera_tujuan = "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg"
        elif mata_uang_tujuan == "MYR":
            bendera_tujuan = "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg"
        elif mata_uang_tujuan == "EUR":
            bendera_tujuan = "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg"
        elif mata_uang_tujuan == "YEN":
            bendera_tujuan = "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg"
        elif mata_uang_tujuan == "IDR":
            bendera_tujuan = "IDR.png"  
        st.image(bendera_tujuan, width=50)


    jumlah = st.number_input(f"Masukkan jumlah {mata_uang_asal} yang ingin dikonversi:", min_value=1.00, help="Masukkan nilai lebih dari 0 untuk konversi")
    hitung = st.button('Hitung')

    if hitung:
        kurs = {
            "USD": {"MYR": 3.574, "EUR": 0.92, "YEN": 106.00, "IDR": 15854},
            "MYR": {"USD": 0.28, "EUR": 0.26, "YEN": 29.7, "IDR": 4600},
            "EUR": {"USD": 1.09, "MYR": 3.8, "YEN": 116.5, "IDR": 16800},
            "YEN": {"USD": 0.0094, "MYR": 0.034, "EUR": 0.0086, "IDR": 106},
            "IDR": {"USD": 0.000063, "MYR": 0.00022, "EUR": 0.000059, "YEN": 0.0094}
        }
        

        if mata_uang_asal != mata_uang_tujuan:
            hasil = jumlah * kurs[mata_uang_asal][mata_uang_tujuan]
            hasil = locale.currency(hasil, grouping=True, symbol=True)
            st.write(f"Hasil konversi dari {jumlah} {mata_uang_asal} ke {mata_uang_tujuan}: {hasil}")
            st.success(f'Hasil konversi adalah = {hasil}')
        else:
            st.error("Mata uang asal dan tujuan tidak bisa sama!")
