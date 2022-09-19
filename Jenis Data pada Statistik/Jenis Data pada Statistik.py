#!/usr/bin/env python
# coding: utf-8

# #### Source Course    : **DQLAB ACADEMY**
# #### Website                 : https://academy.dqlab.id/
# #### Course Name       : Jenis Data pada Statistik
# #### Name                    : Dedy Kurnianto

# ## 1. Skala Pengukuran Data

# Skala pengukuran data terdiri atas empat jenis, yaitu :
# 
# 1. Nominal/Kategorikal, contoh: warna mata yang terdiri atas kategori – misalnya –coklat, biru, hijau.
# 
#    Data dengan skala pengukuran nominal/kategorikal memiliki sifat:
# 
#   - tidak memiliki urutan
#   - setiap butir data hanya memiliki satu nilai pada kategorinya
#   - hanya dapat dihitung berapa banyak jumlah setiap kategori
#   - ukuran pemusatan data dengan skala ini adalah modus (kategori yang paling banyak muncul)
#  
# 
# 2. Ordinal, contoh: tingkat kepuasan suatu layanan – misalnya – tidak puas < kurang puas < puas < sangat puas.
# 
#    Data dengan skala pengukuran ordinal memiliki sifat:
# 
#   - memiliki urutan atau tingkatan, tidak puas tingkat/levelnya lebih rendah dibandingkan dengan kurang puas, dst.
#   - setiap butir data hanya memiliki satu nilai pada kategorinya
#   - antar tingkatan kategori tidak dapat dilakukan operasi matematis
#   - hanya dapat dihitung berapa banyak jumlah setiap kategori
#   - ukuran pemusatan data dengan skala ini adalah modus dan median (kategori yang paling banyak muncul dan nilai tengah karena dapat diurutkan)
#  
# 
# 3. Interval, contoh: suhu/temperatur dalam skala Celcius atau Fahrenheit; dan skor SAT (dalam rentang 400 – 1600).
# 
#    Data dengan skala pengukuran interval memiliki sifat:
# 
#   - memiliki urutan nilai.
#   - antar butir data dapat dilakukan operasi matematis
#   - dapat dilakukan perhitungan statistik berupa ukuran pemusatan data (modus, median, mean atau nilai rata-rata) dan ukuran penyebaran data (varians dan standar deviasi atau simpangan baku)
#   - tidak memiliki nilai 0 sesungguhnya, maksudnya skala terendah data ini adalah nol – misal – suhu dalam Celcius dapat benilai negatif yang berarti skala terendah bukan 0; score SAT terendah adalah 400 dan tidak mungkin peserta tes memperoleh lebih rendah dari 400 ini.
#  
# 
# 4. Rasio, contoh: panjang suatu objek, berat suatu objek, dan tinggi suatu objek.
# 
#    Data dengan skala pengukuran rasio memiliki sifat:
# 
#   - memiliki urutan nilai.
#   - antar butir data dapat dilakukan operasi matematis
#   - dapat dilakukan perhitungan statistik berupa ukuran pemusatan data (modus, median, mean atau nilai rata-rata) dan ukuran penyebaran data (varians dan standar deviasi atau simpangan baku)
#   - memiliki nilai 0 sesungguhnya (skala terendah data adalah nol); panjang; berat; atau tinggi suatu objek tidak akan mungkin memiliki nilai negatif.
#   - antar butir data dapat dibandingkan (dapat dihitung rasionnya) karena memiliki nilai 0 sesungguhnya.

# ## 2. Data Nominal dan Ordinal di Pandas
# 
# Di python untuk skala interval dan rasio kita bisa menggunakan tipe data int, float, numpy.intXX, numpy.floatXX, pandas.IntXXDtype, atau pandas.FloatXXDtype contohnya 8, 16, 32, atau 64 untuk integer dan 32, atau 64 untuk float
# 
# Setiap kategori untuk skala nominal dan ordinal dapat ditulis dengan menggunakan string.
# 
# Dalam python kita dapat menggunakan pandas.DataFrame, kolom dengan isi butir data berupa string akan bertipe object. Untuk itu kamu perlu mengubahnya menggunakan pandas.CategoricalDtype.
# 
#  
# 
# ***pandas.CategoricalDtype(categories=None, ordered=False)***
# 
# dengan parameternya
# 
# *categories* : list kategori, opsional
# 
# *ordered* : ***bool***, kategorinya terurut atau tidak, default adalah ***False*** (tidak terurut). Jika bernilai ***True*** kategorinya memiliki tingkatan/level sehingga dapat digunakan untuk skala ordinal.
# 
# 
# Method CategoricalDtype akan menghasilkan skala data kategori atau ordinal yang dapat digunakan untuk merubah tipe data pada kolom DataFrame. Jika pandas.CategoricalDtype dinyatakan ke dalam variabel cat dan DataFrame sebagai nama_dataframe, maka suatu kolom DataFrame nama_kolom dapat diubah tipe datanya dari object ke category dengan
# 
# ***nama_dataframe = nama_dataframe.astype({nama_kolom: cat})***

# ### a. Data Nominal pada Pandas

# In[1]:


import pandas as pd # Importlah pandas sebagai aliasnya pd

gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita", "Wanita", "Wanita", "Pria", "Pria", "Wanita"] # Data jenis_kelamin
df = pd.DataFrame({"jenis_kelamin": gender})

print("Cek tipe data awal:\n ", df.dtypes) # Cek tipe data
cat = pd.CategoricalDtype(["Pria", "Wanita"]) # Buat kategori untuk kolom jenis_kelamin
df = df.astype({"jenis_kelamin": cat}) # Ubahlah tipe data kolom jenis_kelamin
print("\nCek tipe data setelah diubah:\n ", df.dtypes) # Cek kembali tipe data


# ### b. Data Ordinal pada Pandas

# In[2]:


# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data jenis_kelamin
gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita",
          "Wanita", "Wanita", "Pria", "Pria", "Wanita"]
# Data cek medis
mcu = ["tidak pernah", "rutin (1 tahun sekali)",
       "tidak tentu waktunya", "tidak pernah", 
       "rutin (1 tahun sekali)", "lebih dari 2 tahun sekali",
       "tidak pernah", "tidak pernah", 
       "rutin (1 tahun sekali)", "2 tahun sekali"]
# Data frame
df = pd.DataFrame({"jenis_kelamin": gender,
                   "cek_medis": mcu})
# Cek tipe data
print("Cek tipe data awal:\n", df.dtypes)

# Buat kategori untuk kolom jenis_kelamin
cat = pd.CategoricalDtype(["Pria", "Wanita"])
# Buat kategori berurut untuk kolom cek_medis
ordl = pd.CategoricalDtype(["tidak pernah", 
                            "tidak tentu waktunya",
                            "lebih dari 2 tahun sekali",
                            "2 tahun sekali",
                            "rutin (1 tahun sekali)"], ordered=True)
# Ubahlah tipe data kolom jenis_kelamin dan cek_medis
df = df.astype({"jenis_kelamin": cat,
                "cek_medis": ordl})
# Cek kembali tipe data
print("\nCek tipe data setelah diubah:\n", df.dtypes)

# Cetaklah tiga baris teratas sesuai dengan yang ditunjukkan pada bagian Theory, ketikkan di baris 33
print("\n", df["cek_medis"].head(3))


# ### c. Data Berkelompok
# Di python biasanya digunakan kombinasi kurung siku dan/atau kurung biasa untuk merepresentasikan interval suatu nilai. Kurung siku digunakan jika nilai batas bawah atau batas atas interval termasuk ke dalam nilai interval, atau disebut inklusif. Sementara itu, kurung biasa digunakan ketika batas bawah atau batas atas interval tidak termasuk ke dalam nilai interval atau disebut dengan ekslusif.

# In[9]:


get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(7, 5))
img = mpimg.imread('databerkelompok.png')
imgplot = plt.imshow(img)
plt.show()


# Coba perhatikan penulisan yang dimaksudkan ini, a dan b merupakan batas bawah dan batas atas interval nilai.

# ### d. pandas.cut untuk Data Berkelompok
# Untuk membuat data berkelompok dapat menggunakan method .cut dari pandas,
# 
# ***pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates=”raise”, ordered=True)***
# 
# dengan parameter
# 
# - x : array 1D yang dapat berupa 1D list, 1D **numpy.ndarray**, atau **pandas.series** yang akan dihitung persentilnya
# 
# - bins : pengelompokkan data dapat dilakukan dengan menggunakan
#   - **int**, yang berupa jumlah bin sehingga menghasilkan rentang data dengan lebar yang sama.
#   - urutan bilangan, (**list**, numpy 1D array) yang merupakan batas untuk setiap interval, misal **bins=[1, 2, 4]** adalah untuk 2 bin dalam interval 1 s/d 2, dan 2 s/d 4. Inclusif atau ekslusif ditentukan oleh parameter right dan include_lowest yang diterapkan untuk setiap bin (rentang/interval) yang dinyatakan.
#   - IntervalIndex menyatakan secara tepat batas bawah dan batas atas setiap bin yang akan dibuat. Untuk penggunaannya dapat melihat **pandas.IntervalIndex!**
# 
# - right : **bool**, default adalah **True** (inklusif); menentukan batas atas setiap bin bersifat inklusif atau eklusif dan hanya berefek untuk bins berupa **int** atau urutan bilangan.
# 
# - labels : array atau **False**, default adalah **None**; digunakan untuk menspesifikasi label untuk setiap bin yang panjangnya harus sama dengan jumlah bin. Labels diabaikan jika bins adalah IntervalIndex.
# 
# - retbins: default adalah **False** untuk tidak menimpa array input.
# 
# - precision: kepresisian nilai interval yang dihasilkan, default adalah 3 digit dibelakang koma.
# 
# - include_lowest: **bool**, default adalah **False** (eklusif); menentukan batas bawah setiap bin bersifat inklusif atau eklusif.
# 
# - duplicates: Jika batas setiap bin tidak unik maka keluarkan **ValueError** atau buang nilai yang tidak unik.
# 
# - ordered: **bool**, default adalah **True**; apakah label yang dihasilkan berurut atau tidak.
# 
# Langkah ini hanya menghasilkan bin untuk data. Jika data bertipe **pandas.DataFrame** maka dapat menerapkan method **.groupby** pada data ini dan kemudian menggunakan aggregasi **.count()**. Aggregasi count digunakan untuk menghitung seberapa banyak data di dalam binnya.
# 
# Jika keluaran **pandas.cut** disebut dengan sebuah variabel dengan nama, misalnya, **grup** maka
# 
#                   data.groupby(grup).count()
# 
# yang akan menghasilkan frekuensi seperti yang ditunjukkan oleh tabel pengelompokkan data.

# #### Mempraktekan pandas.cut pada Data Berkelompok

# In[4]:


# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data berat badan 120 orang 
bb120 = [71.2, 66.8, 66.9, 65.9, 69.7, 63.4, 71.5, 66.5, 68.6, 67.5, 
         70.9, 63.9, 67.4, 67.2, 70.3, 65.8, 67.7, 66.2, 68.1, 69.2, 
         65.8, 70.3, 69.8, 69.0, 69.8, 66.6, 67.8, 66.1, 67.5, 69.1, 
         66.6, 67.2, 66.6, 66.3, 66.7, 68.0, 65.8, 68.5, 71.3, 69.5, 
         67.6, 66.2, 66.5, 71.4, 68.1, 66.7, 68.4, 72.2, 68.2, 69.2, 
         68.6, 67.3, 65.7, 67.3, 67.6, 69.2, 69.7, 69.9, 68.6, 69.8, 
         66.5, 70.5, 69.0, 67.4, 69.0, 67.8, 70.3, 71.0, 72.4, 65.2, 
         65.1, 67.0, 68.3, 69.8, 68.6, 64.0, 67.4, 69.7, 68.5, 69.5, 
         67.6, 67.6, 68.4, 68.8, 68.4, 68.2, 66.7, 68.8, 68.2, 70.3, 
         70.4, 68.4, 67.2, 66.7, 68.8, 68.2, 67.3, 68.1, 66.8, 69.4, 
         67.1, 70.4, 68.8, 69.2, 65.8, 68.3, 69.5, 66.1, 67.5, 68.1, 
         65.3, 68.6, 69.7, 66.3, 68.7, 65.4, 67.9, 64.8, 70.2, 68.8]
# Bin dengan menggunakan urutan bilangan (menggunakan list)
# yang sesuai dengan tabel yang dicontohkan
bin_list = list(range(63, 74))
print("bin berat badan dalam urutan bilangan:\n", bin_list)
# Buatlah kelompok data seperti tabel yang ditunjukkan
bin_bb = pd.cut(bb120, bin_list, right=False, include_lowest=True)
# Ubah bb120 ke dalam pandas.DataFrame
df_bb120 = pd.DataFrame(bb120)
# Kelompokkanlah df_bb120 ke dalam bin yang telah disediakan
tabel_bb = df_bb120.groupby(bin_bb).count()
# Untuk menset header dari tabel_bb
tabel_bb.rename(columns={0: "frekuensi"}, inplace=True)
tabel_bb.index.rename("rentang berat badan [kg]", inplace=True)
print("\nData berkelompok berat badan 120 orang:\n", tabel_bb)


# ### Mini Project
# #### Menghitung Kondisi Kesehatan 120 Orang Berdasarkan Nilai BMI-nya
# 
# **BMI atau Body Mass Index** adalah ukuran yang digunakan untuk mengukur proporsionalitas antara tinggi dan berat badan seseorang. BMI merupakan cara yang mudah untuk menilai apakah seseorang mengalami obesitas atau tidak. Untuk menghitung Body Mask Index dapat menggunakan rumus dibawah ini:

# In[10]:


#rumus BMI
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(7, 5))
img = mpimg.imread('rumusbmi.png')
imgplot = plt.imshow(img)
plt.show()


# Setelah nilai BMI diperoleh dengan persamaan di atas dapat ditentukan kategori orangnya apakah obesitas, kegemukan, normal, atau kurus berdasarkan kriteria berikut

# In[12]:


#kriteria BMI
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(10, 7))
img = mpimg.imread('kriteriabmi.png')
imgplot = plt.imshow(img)
plt.show()


# In[13]:


# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data berat badan 120 orang (kg)
bb120 = [71.2, 66.8, 66.9, 65.9, 69.7, 63.4, 71.5, 66.5, 68.6, 67.5, 
         70.9, 63.9, 67.4, 67.2, 70.3, 65.8, 67.7, 66.2, 68.1, 69.2, 
         65.8, 70.3, 69.8, 69.0, 69.8, 66.6, 67.8, 66.1, 67.5, 69.1, 
         66.6, 67.2, 66.6, 66.3, 66.7, 68.0, 65.8, 68.5, 71.3, 69.5, 
         67.6, 66.2, 66.5, 71.4, 68.1, 66.7, 68.4, 72.2, 68.2, 69.2, 
         68.6, 67.3, 65.7, 67.3, 67.6, 69.2, 69.7, 69.9, 68.6, 69.8, 
         66.5, 70.5, 69.0, 67.4, 69.0, 67.8, 70.3, 71.0, 72.4, 65.2, 
         65.1, 67.0, 68.3, 69.8, 68.6, 64.0, 67.4, 69.7, 68.5, 69.5, 
         67.6, 67.6, 68.4, 68.8, 68.4, 68.2, 66.7, 68.8, 68.2, 70.3, 
         70.4, 68.4, 67.2, 66.7, 68.8, 68.2, 67.3, 68.1, 66.8, 69.4, 
         67.1, 70.4, 68.8, 69.2, 65.8, 68.3, 69.5, 66.1, 67.5, 68.1, 
         65.3, 68.6, 69.7, 66.3, 68.7, 65.4, 67.9, 64.8, 70.2, 68.8]
# Data tinggi badan 120 orang (cm)
tb120 = [157., 163., 156., 166., 162., 165., 155., 160., 164., 161., 
         172., 149., 166., 162., 167., 161., 144., 164., 160., 155., 
         157., 162., 177., 163., 155., 173., 159., 156., 154., 157., 
         174., 167., 166., 162., 163., 165., 163., 162., 168., 160., 
         163., 156., 171., 170., 150., 160., 165., 165., 166., 159., 
         136., 163., 152., 166., 166., 149., 167., 160., 157., 164., 
         170., 171., 154., 159., 162., 162., 159., 147., 160., 154., 
         162., 156., 161., 157., 159., 159., 170., 166., 160., 154., 
         168., 152., 154., 157., 155., 156., 170., 161., 157., 166., 
         163., 154., 158., 165., 174., 171., 167., 161., 151., 157., 
         160., 165., 162., 162., 173., 164., 160., 159., 162., 156.,
         170., 160., 158., 156., 167., 153., 159., 163., 161., 163.]


# In[7]:


# DataFrame yang berisi bb120 dan tb120
df = pd.DataFrame({"berat_badan_kg": bb120,
                   "tinggi_badan_cm": tb120})
# Hitunglah BMI-nya sesuai dengan persamaan yang diberikan
df["BMI"]= df["berat_badan_kg"] / (df["tinggi_badan_cm"]/100)**2
# Cetak lima data teratas data frame df
print("Lima data teratas:", df.head(), sep="\n")

# Buat urutan bilangan yang merupakan batas dari kategori BMI
bin_list = [0, 18.5, 25, 30, 1000]
# Kategorikan nilai BMI melalui kolom BMI yang telah dihitung
bin_cut = pd.cut(df["BMI"], bin_list, right=False, include_lowest=True)
# Kelompokkanlah kolom BMI sesuai dengan kategorinya dan hitung jumlah orang disetiap kategorinya
kondisi = df[["BMI"]].groupby(bin_cut).count()
kondisi.rename(columns={"BMI": "Jumlah"}, inplace=True)
# Kondisi kesehatan 120 penduduk di suatu kelurahan
print("\nKondisi kesehatan 120 penduduk di suatu kelurahan:")
print(kondisi)


# ### Kesimpulan

# Dari hasil analisis mini project diatas, terlihat bahwa ada 5 orang penduduk dari 120 responden merupakan orang dengan kondisi obesitas, 83 orang berkondisi gemuk dan 32 orang responden normal  
