#!/usr/bin/env python
# coding: utf-8

# #### Source Course    : **DQLAB ACADEMY**
# #### Website                 : https://academy.dqlab.id/
# #### Course Name       : Ukuran Data: Pemusatan
# #### Name              : Dedy Kurnianto

# ## Pendahuluan

# Ukuran pemusatan data *(measures of central tendency)* adalah nilai yang digunakan untuk menggambarkan sekumpulan data dengan mengidentifikasikan pusat dari kumpulan data tersebut. Ukuran pemusatan data yang paling sering digunakan adalah rata-rata (mean), median, dan modus (mode)

# ### A. Rata-Rata (Mean)
# Rata-rata (mean) adalah jumlah dari seluruh nilai pada suatu set data yang dibagi dengan banyaknya data    
# 
# Rata-rata juga merupakan pengukuran pemusatan data yang paling terkenal. Apabila kita memiliki data sejumlah  dan data tersebut memiliki nilai x1, x2, x3,..... xn maka rata-rata dari data tersebut dapat dihitung dengan rumus berikut

# In[3]:


#rumus mean
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(12, 7))
img = mpimg.imread('mean.png')
imgplot = plt.imshow(img)
plt.show()


# ### B. Median (Nilai Tengah)
# Median atau nilai tengah dari kumpulan data yang telah diurutkan dari nilai terkecil sampai terbesar atau sebaliknya,

# ### C. Modus (Mode)
# Modus (mode) yang merupakan ukuran pemusatan dengan menggunakan data yang paling sering muncul pada kumpulan data

# ### D. Membaca Data Survei
# Pada tahap ini, aku akan mencoba menggunakan dataset tinggi badan yang telah tersedia melalui url: https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt untuk mempelajari mean, median, dan modus.

# In[4]:


# Import library pandas sebagai aliasnya pd
import pandas as pd

# Membaca file survei_tinggi_badan.txt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")

# Mencetak 5 data teratas
print(df.head(5))


# ### E. Mengubah Nama Kolom
# Aku dapat melihat dataset ini sangat sederhana karena hanya terdiri dari satu kolom, yaitu kolom tinggi badan dalam satuan cm.
# Kemudian untuk mempermudah penulisan nama kolom, aku mengubah kolom “tinggi badan (cm)” menjadi “tinggi”.

# In[5]:


# melakukan rename terhadap kolom "tinggi badan (cm)" menjadi "tinggi"
df.rename({'tinggi badan (cm)' : 'tinggi'}, axis=1, inplace=True)
print(df.head(5))


# ### F. Nilai Mean
# Kemudian, aku memeriksa apakah ada data yang bernilai null. Hal ini penting karena data kosong dapat mempengaruhi perhitungan pemusatan data.

# In[6]:


# Mengecek apakah ada data yang bernilai null
print("Mengecek apakah ada data yang bernilai null")
print(df.isnull().any().any())

# Mengecek jumlah data
print("\nMengecek jumlah data")
print(df.shape)

# Mendapatkan nilai mean menggunakan fungsi mean yang disediakan pandas
print("\nMean:", df["tinggi"].mean())


# ### G. Nilai Median dan Modus
# Dari proses sebelumnya, aku mendapatkan nilai mean 161.352 yang berarti merupakan rata-rata tertinggi dari dataset ini. Kemudian aku mencari nilai median (nilai tengah) dari data. Untungnya, pandas juga sudah menyediakan fungsi median():

# In[7]:


# Mendapatkan nilai median menggunakan fungsi median yang disediakan pandas
print("Median data")
print(">> Median: ", df["tinggi"].median())

# Mendapatkan nilai modus menggunakan fungsi mode yang disediakan pandas
print("\nModus data")
print(">> Modus: ", df["tinggi"].mode())


# ## 2. Anscombe’s Quartet

# ## A. Membaca Dataset
# Kali ini, aku tidak meminta bantuan Antara karena aku dapat mencari informasi melalui DQLab. Berdasarkan sumber yang kudapatkan, aku merangkum catatan mengenai Anscombe’s Quartet berikut ini:    
# 
# *Anscombe’s Quartet pertama kali diperkenalkan oleh Francis John “Frank” Anscombe pada tahun 1973. Anscombe’s Quartet berisi 4 dataset yang memiliki nilai statistik yang hampir sama, tetapi sangat berbeda ketika digambarkan dalam bentuk grafik. Setiap dataset memiliki 11 data poin yang merepresentasikan nilai x dan y.&

# In[2]:


# import library pandas
import pandas as pd

#load dataset ke dataframe anscombe
anscombe = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/anscombe.csv")

# menampilkan seluruh baris data yang ada
print("Anscombe's Quartet")
print(anscombe)

# menampilkan mean dataset anscombe
print("\nMean dari Anscombe's Quartet")
print(anscombe.mean())


# ### B. Visualisasi Scatter
# Selanjutnya, memvisualisasikan setiap pasang (x1, y1), (x2, y2), (x3, y3), dan (x4, y4) menggunakan fungsi scatter(). 

# In[3]:


# import matplotlib untuk plotting
import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8,8))
# scatter plot (x1, y1), (x2, y2), (x3, y3), dan (x4, y4)
ax[0][0].scatter(anscombe.x1, anscombe.y1)
ax[0][1].scatter(anscombe.x2, anscombe.y2)
ax[1][0].scatter(anscombe.x3, anscombe.y3)
ax[1][1].scatter(anscombe.x4, anscombe.y4)

k = 1
for i in range(2):
    for j in range(2):
        ax[i][j].set_xlabel("x" + str(k), fontsize=12)
        ax[i][j].set_ylabel("y" + str(k), fontsize=12)
        ax[i][j].grid()
        k += 1

plt.tight_layout()
plt.show()


# In[17]:


# mendapatkan nilai mean menggunakan fungsi mean yang disediakan pandas
print("Nilai rata-ratanya adalah {} ".format(df["tinggi"].mean()))

# mendapatkan nilai median menggunakan fungsi median yang disediakan pandas
print("Nilai mediannya adalah {} ".format(df["tinggi"].median()))

# mendapatkan nilai modus menggunakan fungsi mode yang disediakan pandas
print("Nilai modusnya adalah {} ".format(df["tinggi"].mode()))

