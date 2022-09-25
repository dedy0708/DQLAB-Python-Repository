#!/usr/bin/env python
# coding: utf-8

# #### Source Course    : **DQLAB ACADEMY**
# #### Website                 : https://academy.dqlab.id/
# #### Course Name       : Ukuran Data: Variasi
# #### Name              : Dedy Kurnianto

# ## 1. Variasi Data - Part 1

# ### A. Membaca Dataset
# 
# Membaca data dalam bentuk teks dapat menggunakan method .loadtxt() dari numpy. Melalui .loadtxt() dapat digunakan parameter nama file yaitu pada data string "https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", dan baris pertama harus dilewati (skip) dengan menggunakan parameter skiprows=1. Hasil pembacaan data teks ini akan ditempatkan ke dalam variabel tinggi_badan yang bertipe numpy.ndarray.

# In[2]:


# Import numpy sebagai aliasnya np
import numpy as np

# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

# Cetak ukuran dataset dan isinya
print("Ukuran data tinggi_badan:", tinggi_badan.shape)
print("Data tinggi_badan (cm):\n", tinggi_badan)


# ### B. Rentang Data (Range)
# Melalui hasil yang telah didapatkan sebelumnya bahwa variabel tinggi_badan memiliki bentuk array baris dengan jumlah data sebanyak 250 butir data.
# 
# Selanjutnya dapat mengukur variasi data pada variabel tinggi_badan, variasi data ini diukur dengan menggunakan range yang merupakan **jangkauan data**, yaitu beda nilai maksimum dan minimum.
# 
# Kembali, array baris tinggi_badan ini memiliki tipe numpy.ndarray. Untuk array yang sudah bertipe data numpy.ndarray dapat diterapkan method **.min() dan .max()** setelah nama variabelnya, yaitu variabel tinggi_badan. 
# 
#  

# In[3]:


# rentang data
print("Range data:")
print("  min:", tinggi_badan.min())
print("  max:", tinggi_badan.max())


# ### C. Visualisasi Data dengan Swarmplot
# Menampilkan visualisasi butir-butir data variabel tinggi_badan ini sebelum menentukan variasi data dengan menggunakan kuartil data, box plot data, ataupun persentil data [ini](https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt).
# 
# Sebelumnya import terlebih dahulu library seaborn sebagai aliasnya (sns) dan berikut dengan library matplotlib. Selanjutnya dapat menggunakan seaborn.swarmplot(x=nama_variabel, size=ukuran_marker_butir_data). Parameter size ini merupakan ukuran dari marker plot butir data, ini bertipe int.

# In[6]:


#import library
import matplotlib.pyplot as plt
import seaborn as sns

# Visualisasikan dengan swarmplot variabel tinggi_badan dengan ukuran marker 8
fig, ax = plt.subplots(figsize=(10,4)) 
sns.swarmplot(x=tinggi_badan, size=8, color="darkcyan", edgecolor=None, ax=ax)
ax.grid(axis="x")
plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()


# ### D. Kuartil Data dengan numpy.percentile
# Untuk mengukur varaisi data adalah dengan menggunakan kuartil yang membadi data menjadi empat bagian sama besar. Kemudian, aku akan menentukan kuartil 1, 2, dan 3 dari data tinggi_badan, namun aku tidak menemukan method .quartile() di numpy. 
# 
# - Method .percentile() yang aku temukan seperti ini : 
# 
# ***numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, interpolation="linear", keepdims=False)***
# 
# dengan parameter
# 
# - a : array (numpy.ndarray) atau list yang akan dihitung persentilnya
# 
# - q : persentil ke- yang harus dinyatakan dalam rentang bilangan ril antara 0 dan 100. q ini dapat digunakan berupa nilai tunggal atau dapat juga digunakan beberapa nilai persentil ke-nya sekaligus seperti persentil ke-10, 50, dan 90 yang dituliskan dalam python list [10, 50, 90].
# 
# - axis : untuk array 2D atau lebih ini berguna bahwa terhadap baris atau kolom kah persentil akan dihitung. axis ini dapat menerima None, int, atau tuple of int. None adalah nilai default-nya yang akan menentukan persentil untuk array a yang telah diubah menjadi array 1D.
# 
# - out : nama alternatif untuk output array untuk menampung hasil.
# 
# - overwrite_input : default adalah False untuk tidak menimpa array input.
# 
# - interpolation : jenis interpolasi yang digunakan jika persentil yang diinginkan berada di antara dua butir data berdekatan. Pilihan yang dapat digunakan adalah "linear", "lower", "higher", "midpoint", "nearest". Nilai default-nya adalah "linear".
# 
# - keepdims : ketika diset True maka akan mempertahankan dimensi array a. Default adalah False.
# 
# Penggunaan method .percentile() akan menghasilkan skalar (nilai tunggal) atau list beberapa nilai sesuai dengan nilai q yang diberikan apakah skalar atau list beberapa nilai juga.

# In[7]:


# Perhitungan Q1, Q2, dan Q3 satu persatu
print("Perhitungan Q1, Q2, dan Q3 satu persatu")
Q1 = np.percentile(tinggi_badan, 25)
Q2 = np.percentile(tinggi_badan, 50)
Q3 = np.percentile(tinggi_badan, 75)
print("Kuartil 1 (Q1):", Q1)
print("Kuartil 2 (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)

# Perhitungan Q1, Q2, dan Q3 sekaligus
print("\nPerhitungan Q1, Q2, dan Q3 sekaligus")
Q123 = np.percentile(tinggi_badan, [25, 50, 75])
print("[Q1, Q2, Q3]:", Q123)


# ### E. Kuartil Data dengan numpy.quantile
# 
# Untuk method .quantile() sendiri  seperti ini :
# 
# ***numpy.quantile(a, q, axis=None, out=None, overwrite_input=False, interpolation="linear", keepdims=False)***
# 
# Parameternya (dan keterangannya juga) dengan .percentile() hanya saja yang menjadi sorotan  adalah parameter q-nya yang harus dinyatakan dalam bilangan ril antara 0 dan 1. Artinya, ketika mau menentukan kuartil 1, maka mengisikan parameter q dengan 0.25.

# In[8]:


# Perhitungan Q1, Q2, dan Q3 satu persatu
print("Perhitungan Q1, Q2, dan Q3 satu persatu")
Q1 = np.quantile(tinggi_badan, 0.25)
Q2 = np.quantile(tinggi_badan, 0.5)
Q3 = np.quantile(tinggi_badan, 0.75)
print("Kuartil 1 (Q1):", Q1)
print("Kuartil 2 (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)

# Perhitungan Q1, Q2, dan Q3 sekaligus
print("\nPerhitungan Q1, Q2, dan Q3 sekaligus")
Q123 = np.quantile(tinggi_badan, [0.25, 0.5, 0.75])
print("[Q1, Q2, Q3]:", Q123)


# ### F. Nilai Upper dan Lower Whisker
# 
# Untuk itu, selanjutnya dapat menghitung terlebih dahulu jarak antar kuartile (inter-quartile range) IQR yang merupakan beda nilai antara kuartil 3 Q3 dan nilai kuartil 1 Q1. Lower whisker dapat aku hitung dengan
# 
# - Q1 - 1.5*IQR
# 
# dan upper whisker dihituung dengan
# 
# - Q3 + 1.5*IQR
# 
# Seperti penjelasan Senja tadi lower dan upper whisker merupakan batas yang menentukan apakah butir data merupakan inlier atau outlier (pencilan).

# In[9]:


# Jarak antar kuartil (inter quartile range, IQR)
IQR = Q3 - Q1
print("Jarak antar kuartil (IQR):", IQR)
print("\nlower whisker:", Q1 - 1.5*IQR)
print("           Q1:", Q1)
print("           Q2:", Q2)
print("           Q3:", Q3)
print("upper whisker:", Q3 + 1.5*IQR)


# ### G. Visualisasi Data dengan Box Plot
# Sekarang akan menampilkan visualisasi box plot ini berikut dengan swarmplot untuk data tinggi_badan. 
#  
# Visualisasi ini menggunakan library dari seaborn.boxlot(x=nama_variabel, whis=pengali_IQR). Parameter whis ini merupakan besarnya pengali IQR untuk menentukan dimanakah posisi lower dan upper whiskernya nanti, whis ini tentu bertipe float.

# In[10]:


ig, ax = plt.subplots(figsize=(10,4))
# Plotkanlah boxplot pada data tinggi_badan dengan nilai whis 1.5
sns.boxplot(x=tinggi_badan, whis=1.5, color="greenyellow", ax=ax)
# Plotkan kembali swarmplot
sns.swarmplot(x=tinggi_badan, size=8, color="darkcyan", edgecolor=None, ax=ax)
ax.grid(axis="x")
plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()


# #### Penjelasan
# Visualisasi diatas adalah implementasi dari hasil perhitungan nilai upper dan lowernya dan juga nilai Q1,Q2,Q3. 
# 
# Library visualisasi baik seaborn atau matplotlib biasanya menempatkan lower dan upper whisker ke butir data terdekatnya yang masih inliers. Untuk kasusku ini, lower whisker 143.5 cm ditempatkan pada butir data 144 cm. Begitu juga dengan upper whisker yang bernilai 179.5 cm yang diletakkan pada butir data 177 cm sebagai nilai maksimum data tinggi_badan.
# 
# Hasil perhitunganmu untuk lower dan upper whisker dibanding dengan yang ditampilkan oleh library visualisasi sama-sama mau menunjukkan apakah ada data pencilan. Perhitunganmu menghasilkan satu pencilan dan hal yang sama juga ditunjukkan oleh box plot yang kamu hasilkan dengan seaborn

# ### H. Menentukan Persentil
# Persentil merupakan ukuran sebaran dengan cara membagi data 100 bagian sama besar. Selanjutnya, adalah ingin menentukan persentil ke-5 dan ke-95 dari data tinggi_badan ini. Untuk itu dapat menggunakan dua method dari numpy yaitu .percentile() dan .quantile(). Penggunaan kedua method ini tentunya sama dengan yangg telah dilakukan dalam perhitungan kuantil sebelumnya.

# In[11]:


# Persentil ke-5 dan ke-95
print("Menggunakan np.percentile")
P5, P95 = np.percentile(tinggi_badan, [5, 95])
print("  Persentil ke-5  (P5) :", P5)
print("  Persentil ke-95 (P95):", P95)

print("\nMenggunakan np.quantile")
P5, P95 = np.quantile(tinggi_badan, [0.05, 0.95])
print("  Persentil ke-5  (P5) :", P5)
print("  Persentil ke-95 (P95):", P95)


# ## 2. Variasi Data - Part 2

# ### A. Dua Cara Pengerjaan
# Selanjutnya adalah menghitung varians dan standar deviasi secara python’s way dan numpy’s way dengan membuatkan sub program atau fungsi.
# 
# Untuk python’s way kita dapat menggunakan perulangan (looping) ataupun list comprehension dalam mengkonstruksi perhitungan varians dan standar deviasi.
# 
# Sementara itu, dengan numpy’s way kita bisa memanfaatkan kekuatan komputasi secara vektorisasi dengan numpy array. Fungsi bawaan numpy numpy.var() untuk perhitungan varians dan numpy.std() untuk perhitungan standar deviasi dapat digunakan untuk mengecek hasil perhitungan kalian secara python’s way dan numpy’s way.
#  
# 
# Membaca dokumentasi materi [numpy.var()](https://numpy.org/doc/stable/reference/generated/numpy.var.html?highlight=numpy%20var#numpy.var) dan [numpy.std()](https://numpy.org/doc/stable/reference/generated/numpy.std.html?highlight=numpy%20std#numpy.std). Kedua method ini memiliki parameter yang sama. Untuk itu, aku akan lihat numpy.var() saja saat ini. 
# 
# ***numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=, *, where=)***
# 
# Parameter yang umum diset, yaitu :
# 
# - a : array (numpy.ndarray) atau list yang akan dihitung variansnya
# 
# - axis : Untuk array 2D atau lebih ini berguna bahwa terhadap baris atau kolom kah persentil akan dihitung. axis ini dapat menerima None, int, atau tuple of int. None adalah nilai default-nya yang akan menentukan persentil untuk array a yang telah diubah menjadi array 1D.
# 
# - dtype : tipe data untuk mengkomputasi varians. Jika a adalah array integer makan akan otomatis dikonversi ke numpy.float64, tetapi jika array a sudah float maka tidak akan dikonversi.
# 
# - out : nama alternatif untuk output array untuk menampung hasil.
# 
# - ddof : Berupa bilangan bulat yang merupakan delta derajat kebebasan atau faktor koreksi. Nilai default-nya adalah 0 yaitu untuk perhitungan biased variance. Kita dapat mengentrikan nilainya sebesar 1 untuk perhitungan unbiased variance.
# 
# - keepdims : ketika di set True maka akan mempertahankan dimensi array a. Default adalah True.
# 
# - where : elemen-elemen array yang akan dilibatkan dalam perhitungan varians
# 
# 

# ### B. Varians dan Standar Deviasi dengan Python
# Untuk array tinggi_badan dapat menggunakan parameter ddof saja, seperti yang disebutkan dalam sebelumnya.
# 
# Dengan membuat fungsi untuk perhitungan varians dan standar deviasi sehingga dengan mudah dapat dipanggil nantinya untuk data yang diberikan. Untuk rata-rata, sebenarnya, dapat menggunakan secara langsung fungsi numpy.mean(). 

# In[4]:


def py_rata_rata(data):
    return sum(data) / len(data)

def py_varians(data, k=1):
    rerata, var = py_rata_rata(data), 0
    for d in data:
        var += (d - rerata) ** 2
    return var / (len(data) - k)

def py_standar_deviasi(data, k=1):
    return py_varians(data, k=k) ** 0.5

print("Menggunakan user-defined function pada array tinggi_badan")
print("  unbiased varians        :", py_varians(tinggi_badan))
print("  biased varians          :", py_varians(tinggi_badan, k=0))
print("  unbiased standar deviasi:", py_standar_deviasi(tinggi_badan))
print("  biased standar deviasi  :", py_standar_deviasi(tinggi_badan, k=0))

print("\nMenggunakan method .var() dan .std() pada array tinggi_badan")
print("  unbiased varians        :", tinggi_badan.var(ddof=1))
print("  biased varians          :", tinggi_badan.var())
print("  unbiased standar deviasi:", tinggi_badan.std(ddof=1))
print("  biased standar deviasi  :", tinggi_badan.std())


# In[15]:


#penjelasan rumus
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(12, 7))
img = mpimg.imread('penjelasanrumus.png')
imgplot = plt.imshow(img)
plt.show()


# ### C. Varians dan Standar Deviasi dengan Numpy
# Selain menggunakan rumus umum, pada library numpy bisa langsung mencarinya dengan menggunakan method .var() dan .std() pada array data tinggi_badan. 

# In[5]:


def np_rata_rata(data):
    return data.sum() / len(data)

def np_varians(data, k=1):
    rerata = np_rata_rata(data)
    return ((data - rerata) ** 2).sum() / (len(data) - k)

def np_standar_deviasi(data, k=1):
    return np_varians(data, k=k) ** 0.5

print("Menggunakan user-defined function pada array tinggi_badan")
print("  unbiased varians        :", np_varians(tinggi_badan))
print("  biased varians          :", np_varians(tinggi_badan, k=0))
print("  unbiased standar deviasi:", np_standar_deviasi(tinggi_badan))
print("  biased standar deviasi  :", np_standar_deviasi(tinggi_badan, k=0))

print("\nMenggunakan method .var() dan .std() pada array tinggi_badan")
print("  unbiased varians        :", tinggi_badan.var(ddof=1))
print("  biased varians          :", tinggi_badan.var())
print("  unbiased standar deviasi:", tinggi_badan.std(ddof=1))
print("  biased standar deviasi  :", tinggi_badan.std())


# ## Mini Project

# ### A. Problem #1
# Problem yang harus diselesaikan:
# 
# - mengimport pandas sebagai aliasnya pd
# - membaca dataset melalui url ("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt") dengan menggunakan pandas.read_csv yang kemudian ditampung oleh variabel tinggi_badan.
# - mencek tipe data tinggi_badan apakah bertipe pandas.DataFrame atau bukan.
# - mencetak 5 data teratas dengan method .head() dan 5 data terbawah dengan method .tail() pada data frame tinggi_badan.
# - menentukan statistik deskriptif data frame tinggi_badan menggunakan method .describe() yang ditampung ke dalam variabel statistik_deskriptif, dan kemudian cetaklah statistik_deskriptif ini untuk mengetahui hasilnya.
# - menentukan kuartil Q1 dan Q3 dapat dilakukan berdasarkan hasil pada variabel statistik_deskriptif ini dengan mengakses kolom "tinggi_badan (cm)" dan kemudian akses kembali kolom yang menunjukkan hasil penghitungan kuartil.
# - menghitung IQR seperti yang pernah ku kerjakan sebelumnya dan mencetak hasilnya.
# - menghitung persentil pada data frame tinggi_badan untuk kolom "tinggi_badan (cm)" menggunakan method .quantile dengan hanya memasukkan parameter q seperti yang telah ku kerjakan padanumpy.quantile()

# In[17]:


# Import pandas sebagai aliasnya yaitu pd
import pandas as pd

# Baca dataset
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# Cetak type(tinggi_badan) dan data frame tinggi_badan sendiri
print("type(tinggi_badan):", type(tinggi_badan))
print(tinggi_badan)

# Hitung statistik deskriptif tinggi_badan
statistik_deskriptif = tinggi_badan.describe()
# Cetak statistik deskriptif tinggi_badan
print("\nStatistik deskriptif:\n", statistik_deskriptif)

# Tentukan IQR
Q1 = statistik_deskriptif["tinggi badan (cm)"]["25%"]
Q3 = statistik_deskriptif["tinggi badan (cm)"]["75%"]
IQR = Q3 - Q1
#Cetak IQR
print("\nIQR:", IQR)

# Persentil ke-5 dan ke-95
percentile = tinggi_badan.quantile(q=[0.05, 0.95])
print("\nPersentil ke-5 dan ke-95:\n", percentile)


# ### B. Problem #2
# Untuk menjawab rasa penasaranku terkait representasi lower dan upper whisker pada box plot di seaborn atau matplotlib. Aku akan merubah data maksimum tinggi badan saja nih. Upper whisker sebelumnya berada di 179.5 cm. Aku akan rubah butir data 177 cm menjadi 186 cm. Dengan demikian akan ada 2 pencilan tentunya.
# 
#  
# 
# Untuk mengerjakan ini aku akan melakukan langkah-langkah berikut
# 
# - mencetak statistik deskriptif pada dataframe tinggi_badan sebelum dan setelah dimodifikasi nilai maksimumnya seperti yang diinginkan oleh Sunyi.
# - mengimpor kedua pustaka visualisasi yaitu matplotlib.pyplot dan seaborn ke dalam aliasnya.
# - memplotkan data awal dan data yang telah dimodifikasi menggunakan .boxplot dan .swarmplot dari seaborn. Parameter data pada kedua plot ini dapat aku gunakan karena aku sudah punya variabel bertipe data frame, yaitu data tinggi badan yang awal dan yang telah dimodifikasi. Untuk box plot set parameter whiskernya sesuai dengan yang telah dipelajari.

# In[18]:


# Import pandas sebagai aliasnya yaitu
import pandas as pd

# Baca dataset
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
print("Statistik deskriptif data awal:\n", tinggi_badan.describe().T)

# Modifikasi data maksimum tinggi badan menjadi 186 cm
tinggi_badan_mod = tinggi_badan.replace(tinggi_badan.max(), 186)
print("\nStatistik deskriptif data modifikasi:\n", tinggi_badan_mod.describe().T)

# Import matplotlib.pyplot dan seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(2, 1, figsize=(12,8), sharex=True)
# Plot data awal
sns.boxplot(data=tinggi_badan, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[0])
sns.swarmplot(data=tinggi_badan, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[0])
axs[0].grid(axis="x")
axs[0].set_xlabel(None)
axs[0].set_title("Data awal", color="darkcyan", fontsize=16)

# Plot data modifikasi
sns.boxplot(data=tinggi_badan_mod, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[1])
sns.swarmplot(data=tinggi_badan_mod, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[1])
axs[1].grid(axis="x")
axs[1].set_xlabel(None)
axs[1].set_title("Data modifikasi", color="darkcyan", fontsize=16)

plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()

