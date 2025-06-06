# -*- coding: utf-8 -*-
"""DATAMining

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JK6RhIxMBRHTTk7J5JTFfLMluvsUA60J
"""



import pandas as pd
from IPython.display import display # Import the display function

# Mengatur opsi tampilan pandas untuk menampilkan tabel secara utuh
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Pastikan Google Drive Anda sudah terpasang (uncomment jika belum)
# from google.colab import drive
# drive.mount('/content/drive')

# Ganti 'jalur_file_anda.xlsx' dengan jalur sebenarnya ke file XLSX Anda di Google Drive
file_path = '/content/drive/My Drive/Data ulasan Shopee tentang COD.xlsx'

# Baca file Excel ke dalam Pandas DataFrame (ini adalah struktur tabel)
df = pd.read_excel(file_path)

# Menampilkan DataFrame, yang akan dirender sebagai tabel di notebook
# Menggunakan Styler untuk mengatur perataan teks ke kiri
display(df.style.set_properties(**{'text-align': 'left'}))

uat