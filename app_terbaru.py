import streamlit as st
import locale
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Konversi Mata Uang", page_icon="💰", layout="wide")

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

st.markdown("""
    <style>
    .sidebar {
        width: 250px;  /* Mengurangi lebar sidebar */
        background-color: #f8f9fa;
        padding: 10px;  /* Mengurangi padding */
        margin: 0;
    }

    .sidebar h1 {
        text-align: left;
        font-weight: bold;
        font-size: 20px;
        color: #2a3d45;
    }

    .sidebar .stButton > button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
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
                         ['HOME', 'KONVERSI MATA UANG', 'ANGGARAN PERJALANAN', 'PERBANDINGAN HARGA BARANG', 'TENTANG APLIKASI'],
                         icons=['house', 'currency-dollar', 'airplane', 'tags','info-circle'],  
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

elif select == 'KONVERSI MATA UANG':
    st.title('KONVERSI MATA UANG')

    col1, col2 = st.columns([1, 1])  

    with col1:
        mata_uang_asal = st.selectbox("Pilih Mata Uang Asal", ["USD", "MYR", "EUR", "YEN", "IDR"])
        bendera_asal = {
            "USD": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "EUR": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
            "YEN": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
            "IDR": "https://pluspng.com/img-png/flag-logo-vector-png-republic-of-indonesia-flag-logo-vector-1600.png"
        }[mata_uang_asal]
        st.image(bendera_asal, width=50)

    with col2:
        mata_uang_tujuan = st.selectbox("Pilih Mata Uang Tujuan", ["USD", "MYR", "EUR", "YEN", "IDR"])
        bendera_tujuan = {
            "USD": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "EUR": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
            "YEN": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
            "IDR": "https://pluspng.com/img-png/flag-logo-vector-png-republic-of-indonesia-flag-logo-vector-1600.png"
        }[mata_uang_tujuan]
        st.image(bendera_tujuan, width=50)

    jumlah = st.number_input(f"Masukkan jumlah {mata_uang_asal} yang ingin dikonversi:", min_value=1.00)
    if st.button('Hitung'):
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
            st.success(f'Hasil konversi: {hasil}')
        else:
            st.error("Mata uang asal dan tujuan tidak boleh sama!")

elif select == 'ANGGARAN PERJALANAN':
    st.title("ANGGARAN PERJALANAN")

    # Pilih Mata Uang Asal dan Tujuan
    col1, col2 = st.columns([1, 1])  

    with col1:
        mata_uang_asal = st.selectbox("Pilih Mata Uang Asal", ["USD", "MYR", "EUR", "YEN", "IDR"])
        bendera_asal = {
            "USD": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "EUR": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
            "YEN": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
            "IDR": "https://pluspng.com/img-png/flag-logo-vector-png-republic-of-indonesia-flag-logo-vector-1600.png"
        }[mata_uang_asal]
        st.image(bendera_asal, width=50)

    with col2:
        mata_uang_tujuan = st.selectbox("Pilih Mata Uang Tujuan", ["USD", "MYR", "EUR", "YEN", "IDR"])
        bendera_tujuan = {
            "USD": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "EUR": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
            "YEN": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
            "IDR": "https://pluspng.com/img-png/flag-logo-vector-png-republic-of-indonesia-flag-logo-vector-1600.png"
        }[mata_uang_tujuan]
        st.image(bendera_tujuan, width=50)

    # Input biaya transportasi, akomodasi, dan makanan
    biaya_transportasi = st.number_input("Masukkan biaya transportasi (per hari):", min_value=0.0)
    biaya_akomodasi = st.number_input("Masukkan biaya akomodasi (per hari):", min_value=0.0)
    biaya_makanan = st.number_input("Masukkan biaya makanan (per hari):", min_value=0.0)
    
    # Input durasi perjalanan
    durasi_perjalanan = st.number_input("Masukkan durasi perjalanan (hari):", min_value=1)

    if st.button("Hitung Anggaran"):
        # Hitung total anggaran perjalanan per hari
        total_biaya_harian = biaya_transportasi + biaya_akomodasi + biaya_makanan

        # Hitung total anggaran perjalanan berdasarkan durasi
        total_anggaran = total_biaya_harian * durasi_perjalanan

        # Menggunakan kurs konversi mata uang yang sudah ada
        kurs = {
            "USD": {"MYR": 3.574, "EUR": 0.92, "YEN": 106.00, "IDR": 15854},
            "MYR": {"USD": 0.28, "EUR": 0.26, "YEN": 29.7, "IDR": 4600},
            "EUR": {"USD": 1.09, "MYR": 3.8, "YEN": 116.5, "IDR": 16800},
            "YEN": {"USD": 0.0094, "MYR": 0.034, "EUR": 0.0086, "IDR": 106},
            "IDR": {"USD": 0.000063, "MYR": 0.00022, "EUR": 0.000059, "YEN": 0.0094}
        }

        if mata_uang_asal != mata_uang_tujuan:
            hasil_anggaran = total_anggaran * kurs[mata_uang_asal][mata_uang_tujuan]
            st.success(f'Anggaran Perjalanan Anda dalam {mata_uang_tujuan}: {locale.currency(hasil_anggaran, grouping=True)}')
        else:
            st.error("Mata uang asal dan tujuan tidak boleh sama!")

elif select == 'PERBANDINGAN HARGA BARANG':

    st.title("PERBANDINGAN HARGA BARANG")

    # Pilih Barang yang Ingin Dibandingkan
    barang = st.selectbox("Pilih Barang untuk Perbandingan Harga", ["Makanan", "Pakaian", "Elektronik", "Souvenir"])
    
    # Pilih Lokasi untuk Membandingkan Harga
    lokasi = st.multiselect("Pilih Lokasi (Negara atau Kota)", ["USA", "Malaysia", "Indonesia", "Japan", "Germany"])
    
    # Harga Barang di Setiap Lokasi dalam USD
    harga_barang_usd = {
        "Makanan": {"USA": 5, "Malaysia": 3, "Indonesia": 2, "Japan": 4, "Germany": 6},
        "Pakaian": {"USA": 50, "Malaysia": 30, "Indonesia": 20, "Japan": 40, "Germany": 55},
        "Elektronik": {"USA": 200, "Malaysia": 180, "Indonesia": 150, "Japan": 190, "Germany": 220},
        "Souvenir": {"USA": 10, "Malaysia": 5, "Indonesia": 3, "Japan": 8, "Germany": 12},
    }

    # Kurs Mata Uang
    kurs = {
        "USD": {"MYR": 4.6, "EUR": 0.92, "YEN": 106, "IDR": 15854},  # USD ke mata uang lain
        "MYR": {"USD": 0.22, "EUR": 0.20, "YEN": 23.04, "IDR": 3500}, # MYR ke mata uang lain
        "EUR": {"USD": 1.09, "MYR": 5.0, "YEN": 116.5, "IDR": 16800},
        "YEN": {"USD": 0.0094, "MYR": 0.034, "EUR": 0.0086, "IDR": 106},
        "IDR": {"USD": 0.000063, "MYR": 0.00022, "EUR": 0.000059, "YEN": 0.0094},
    }

    if lokasi:  # Jika ada lokasi yang dipilih
        st.write(f"Harga {barang} di Beberapa Lokasi:")
        for loc in lokasi:
            if loc in harga_barang_usd[barang]:  # Memastikan negara ada dalam data harga
                harga_in_usd = harga_barang_usd[barang][loc]  # Harga dalam USD
                # Menampilkan harga dalam mata uang asal
                st.write(f"{loc} (USD): {harga_in_usd} USD")
                # Mengonversi harga ke mata uang lain
                for mata_uang in kurs["USD"]:
                    harga_dalam_mata_uang = harga_in_usd * kurs["USD"][mata_uang]
                    st.write(f"{mata_uang}: {harga_dalam_mata_uang:.2f}")
            else:
                st.write(f"{loc}: Data tidak tersedia")
    else:
        st.warning("Pilih lokasi untuk melihat perbandingan harga.")

elif select == 'TENTANG APLIKASI':
    st.title('Tentang Aplikasi')
    st.markdown("""
    Aplikasi ini adalah platform konversi mata uang yang dirancang untuk memudahkan pengguna dalam menghitung konversi mata uang antarnegara. 
    Aplikasi ini mendukung beberapa mata uang populer dan memungkinkan pengguna untuk menghitung anggaran perjalanan berdasarkan mata uang yang dipilih.
    
    ### Fitur:
    - **Konversi Mata Uang:** Menghitung nilai tukar antar mata uang.
    - **Anggaran Perjalanan:** Menghitung estimasi anggaran perjalanan berdasarkan biaya per hari dan durasi perjalanan.
    - **Perbandingan Harga Barang:** Membandingkan harga barang tertentu di berbagai lokasi.
    
    **Pengembang:** FourCoders Team
    """)




