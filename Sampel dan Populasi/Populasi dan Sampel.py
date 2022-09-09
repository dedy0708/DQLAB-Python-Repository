#!/usr/bin/env python
# coding: utf-8

# #### Name: Dedy Kurnianto
# 
# #### Source Course    : **DQLAB ACADEMY**
# #### Website                 : https://academy.dqlab.id/
# #### Course Name       : Populasi dan Sampel

# ## 1. Pendahuluan
# Populasi dan sampel adalah salah satu hal yang panting dalam pada awal sebuah penelitian, karena dengan menentukan jenis objek penelitian, seorang peneliti mampu memilih metode mana yang nantinya lebih sesuai dengan kebutuhan penelitian.  

# ### A. Populasi dan Sampel
# - Populasi dapat diartikan sebagai jumlah keseluruhan objek-objek yang akan diteliti. Contoh Populasi 1000 gajah di Indonesia
# 
# - Sampel dapat diartikan sebagai bagian dari populasi itu sendiri. Contoh dari 1000 populasi Gajah diIndonesia akan diambil sampel sebanyak 300 Gajah untuk diteliti. Sampel ini diharapkan dapat mewakili keseluruhan Populasi tersebut.

# ### B. Penarikan Sampel
# Teknik penarikan sampling bisa dilakukan bila populasi bersifat homogen atau memiliki karakteristik yang sama atau setidak-tidaknya hampir sama. Dan apabila keadaan populasi bersifat heterogen, maka sampel yang dihasilkannya dapat bersifat tidak representatif atau tidak dapat menggambarkan karakteristik populasi. dibawah ini terdapat perbedaan dari sampling probabilitas dan non probabilitas.

# In[11]:


#perbedaan probability sampling dan nonprobability sampling
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(10, 7))
img = mpimg.imread('tabel sample.png')
imgplot = plt.imshow(img)
plt.show()


# Dari perbedaan itu terdapat beberapa contoh penarikan sampling yaitu dapat dilihat pada gambar dibawah ini

# In[12]:


#macam sampling
plt.figure(figsize=(10, 7))
img = mpimg.imread('macam sampling.png')
imgplot = plt.imshow(img)
plt.show()


# Penarikan bisa bias karena penarikan sampel non-probability sampling tidak **representatif**. **Maksudnya yaitu ketika penarikan sampel dilakukan akan menghasilkan data yang secara akurat tidak mencerminkan populasi yang sedang dikaji**. Untuk itu penarikan sampel dengan menggunakan non-probability sampling sedapat mungkin dihindari

# ## 2. Probability Sampling
# Pada kesempatan ini, akan dijelaskan tentang ***probability sampling***.
# Probability Sampling menurut gambar diatas terdiri dari:
# 1. Simple Random Sampling
# 2. Stratified Sampling
# 3. CLuster Sampling
# 4. Systematic Random Sampling

# ### A. Simple Random Sampling
# Simple random sampling atau disebut random sampling, dapat mengambil secara acak setiap anggota populasi berdasarkan nilai probabilitas tertentu. Dalam hal ini setiap anggota populasi akan memiliki kesempatan yang sama untuk dipilih yaitu berdasarkan nilai probabilitas yang telah ditentukan.
# 
# Metode penarikan sampel dengan simple random sampling memiliki **kelebihan** yaitu
# 
#   - mudah digunakan jika populasi diketahui atau populasi dengan jumlah yang relatif kecil
#   - mudah digunakan jika keberagaman atau tingkatan (stratifikasi) dalam populasi tidak diperhitungkan 
# 
# dan **kekurangannya** yaitu
# 
#   - sulit digunakan jika populasinya relatif besar (karena akan memakan biaya dan usaha yang besar) serta populasinya beragam atau memiliki tingkatan (stratifikasi) yang perlu diperhitungkan
#   - adanya galat peyampelan (sampling error) karena sampel yang diambil tidak secara akurat mewakili populasi yang akan disampel
#  
# 
# Penarikan sampel dapat dilakukan dengan memanfaatkan random number generator yang tersedia melalui beberapa aplikasi pengolah data di komputer. Sebagai contoh, dari sebuah populasi dengan 120 butir data (butir data 1 s/d butir data 120) akan ditarik sampel sebesar 10% dengan menggunakan simple random sampling. Maka dengan memanfaatkan random number generator akan diperoleh sampel seperti yang ditunjukkan oleh kotak berwarna kuning.

# In[13]:


#macam sampling
plt.figure(figsize=(10, 7))
img = mpimg.imread('cnth samp.png')
imgplot = plt.imshow(img)
plt.show()


# In[5]:


##Simple Random Sampling Menggunakan Python
# Import modul random
import random

# Set seed sebagai bilangan bulat 0, dan dapat diganti
# dengan bilangan bulat lainnya, sesuai dengan instruksi Senja
random.seed(2345)

# Ambil sampel dalam rentang butir data, yaitu 1 s/d 200
# Inisialisasi sampel
sampel = []
# Looping sebanyak sampel yang ingin ditarik yaitu 10% (12 butir data)
for i in range(20): 
    sampel.append(random.randint(1, 200))
# Cetaklah sampel
print("Sampel:", sampel)


# In[6]:


##Simple Random Sampling Menggunakan Numpy
# Import numpy sebagai aliasnya np
import numpy as np

# Set seed sebagai bilangan bulat 0, dan dapat diganti
# dengan bilangan bulat lainnya
np.random.seed(0)

# Ambil sampel dalam rentang butir data, yaitu 1 s/d 200,
# sebanyak 10% (20 butir data)
sampel = np.random.randint(1, 200, size=20)
# Cetaklah sampel
print("sampel:", sampel)


# ### B. Stratified Sampling
# Suatu populasi dapat memiliki beberapa strata atau tingkatan. Pengelompokan ke dalam strata atau tingkatan ini dapat dilakukan dengan menentukan karakteristik yang sama dimiliki oleh individu di dalam populasi itu, misalnya jenis kelamin; golongan darah; atau tingkat pendidikan. 
# 
# Penarikan sampel pada populasi yang memiliki strata ini disebut dengan stratified sampling. Besar sampel yang ditarik juga mengacu pada proporsi atau probabilitas dari setiap strata yang dimiliki populasi tersebut. Jika ditarik secara acak maka disebut dengan stratified random sampling.
# 
# Stratified sampling tentu memiliki kelebihan berupa  kemampuan metode ini dalam mendapatkan karakteristik populasi di dalam sampel yang ditarik yang menyebabkan galat penyampelan (sampling error) lebih kecil dibandingkan dengan simple random sampling.
# 
# Sementara itu, kekurangan stratified sampling terletak pada kondisi jika strata yang dimiliki oleh populasi tidak dapat didefinisikan dengan jelas karakteristiknya. Ini bermakna, adanya karakteristik yang bertindihan antra strata ketika pengelompokkan dilakukan. Hal ini tentu akan memperumit penarikan sampel dan metode ini tidak cocok digunakan.
# 
#  
# 
# Berikut penggambarannya, aku akan menggunakan kembali populasi yang berisi bilangan bulat 1 s/d 120, yang disusun ke dalam kotak berukuran 10 baris x 12 kolom. Populasi ini akan dipartisi ke dalam 4 strata.
# 
# Strata #1 merupakan 3 kolom data pada bagian kiri,
# 
# Strata #2 menyatakan 3 kolom data bagian tengah kiri, dan seterusnya hingga 
# 
# Strata #4.
# 
# Di sini setiap strata akan memiliki 30 butir data. Dengan mengambil 10% sampel untuk masing-masing strata maka akan diperoleh 3 butir data yang merupakan sampel yang ditarik dari setiap strata. Kembali, pengambilan sampel yang dilakukan adalah representatif.

# In[14]:


#Stratified sampling
plt.figure(figsize=(10, 7))
img = mpimg.imread('randstra.png')
imgplot = plt.imshow(img)
plt.show()


# ### C. Cluster sampling 
# Cluster Sampling akan mempartisi populasi ke dalam sejumlah kluster/grup tertentu. Antar kluster akan bersifat homogen mutual namun dalam satu kluster akan berisi individu yang heterogen secara karakteristik. Berbeda dengan stratified sampling, setiap strata populasi memiliki individu homogen secara karakteristik. Selanjutnya sampel dapat ditarik dengan pemilihan secara acak kluster/grup tersebut. Dengan demikian seluruh anggota pada seluruh kluster/grup terpilih akan menjadi sampel yang ditarik. 
# 
# Metode cluster sampling ini memiliki kelebihan yaitu sebagai metode yang cukup mudah jika dibandingkan dengan metode lainnya karena pengambilan sampel berdasarkan grup atau kluster.
# 
# Sementara itu kekurangannya yaitu galat penyampelan (sampling error) yang cukup tinggi.
# 
# Penggunaannya secara umum ditemui dalam penyampelan berdasarkan kondisi geografis.
# 
#  
# 
# Untuk populasi 120 butir data bilangan bulat yang akan dipartisi menjadi 20 kluster/grup. Penarikan 10% sampel pada populasi dengan 20 kluster/grup akan menghasilkan 2 kluster/grup yang terpilih seperti yang ditunjukkan berikut ini.

# In[15]:


#Cluster sampling
plt.figure(figsize=(10, 7))
img = mpimg.imread('clussamp.png')
imgplot = plt.imshow(img)
plt.show()


# ### D. Systematic Random Sampling
# Systematic random sampling diterapkan dengan mengurutkan seluruh anggota populasi, kemudian penarikan sampel dilakukan menentukan butir data awal terlebih dahulu dan butir data berikutnya dipilih sampel sebesar k interval antar data tertentu. Dengan kata lain antar sampel yang ditarik dalam populasi memiliki perioda sebesar k interval.
# 
# Metode ini memiliki kelebihan yaitu mudah dilakukan karena perlu diurutkan saja dan penyampelan dilakukan secara berulang untuk nilai interval tertentu yang sama.
# 
# Sementara itu, kelemahan metode ini terletak pada ketidakakuratan penyampelan jika populasi memiliki perioda.  Terutama perioda populasi sama atau mendekati dengan perioda penyampelan data. 
# 
#  
# 
# Misalkan memiliki populasi 16 buah bilangan bulat yang telah diurutkan dari nilai terkecil hingga nilai terbesar. Butir data kedua dijadikan sebagai butir data awal untuk penarikan sampel. Untuk butir data selanjutnya dipilih setiap 4 interval antar data seperti yang ditunjukkan berikut.

# In[16]:


#Systematic Random sampling
plt.figure(figsize=(10, 7))
img = mpimg.imread('rand3.png')
imgplot = plt.imshow(img)
plt.show()


# ## 3. Representative Sampling
# 
# Suatu sampel dikatakan representatif jika memenuhi kriteria:
# 
# 1. menggunakan metode penarikan sampel yang sesuai yaitu metode probability sampling diantaranya simple random sampling, stratified sampling, cluster sampling, dan systematic random sampling.
# 2. sampel yang ditarik dari populasi haruslah cukup besar sehingga data yang terkumpul dapat menggambarkan populasi yang sedang dikaji.
# 
# Kriteria kedua ini dipengaruhi oleh tiga faktor:
# 
# 1. **ukuran populasi**: semakin besar ukuran populasi maka semakin besar ukuran sampel yang dibutuhkan
# 2. **selang kepercayaan** (confidence level): seberapa percayanya kamu terhadap nilai populasi yang dikaji. Nilai yang biasa digunakan adalah 90%, 95%, atau 99%. Dalam hal ini semakin tinggi selang kepercayaan semakin besar ukuran sampel yang diperlukan dan secara langsung berkorelasi dengan semakin representatifnya sampel ditarik dari populasi.
# 3. **margin galat (margin of error)**: seberapa besarkah galat atau error penarikan sampel yang dapat ditoleransi (dalam persen). Margin galat yang rendah akan menghasilkan jumlah sampel yang besar, dan sebaliknya.
#  
# untuk menggabungkan kedua kriteria tersebut harus memilih salah satu metode penarikan sampel pada kriteria 1 dan kemudian menerapkan kriteria 2. Untuk simple random sampling saja kamu dapat mengambil jumlah sampel n dari populasi berukuran N menggunakan persamaan matematis berikut

# In[25]:


#rumus ukuran
plt.figure(figsize=(3, 2))
img = mpimg.imread('rumus1.png')
imgplot = plt.imshow(img)
plt.show()


# In[28]:


#rumus
plt.figure(figsize=(3, 2))
img = mpimg.imread('rumus2.png')
imgplot = plt.imshow(img)
plt.show()


# dan z merupakan nilai z (z-score) berdasarkan selang kepercayaan (lihat tabel), p adalah proporsi sampel dan e merupakan besar margin galat.

# In[9]:


#tabel z-score
plt.figure(figsize=(7, 5))
img = mpimg.imread('tabelconf.png')
imgplot = plt.imshow(img)
plt.show()


# Jika kamu memperoleh hasil ukuran sampelnya tidak dalam bilangan bulat maka kamu harus membulatkannya ke arah kanan garis bilangan atau dengan kata lain kamu bulatkan ke atas. Untuk pembulatan ini kamu dapat menggunakan ceil dari modul math di python. Jika kamu menggunakan pustaka numpy kamu dapat menggunakan numpy.ceil(). 
# 
# Serta jika ukuran populasi yang akan ditarik sampelnya adalah tidak berhingga (N → ∞), maka jumlah sampelnya n = n’,

# In[34]:


#Menentukan Jumlah sample
# Import math
import math
# Jumlah anggota populasi
N = 8963
# Proporsi
p = 0.25
# z-score
z = 1.96
# Margin of error
e = 0.05
# Perhitungan ukuran sampel, n
n_aksen = z**2 * p * (1 - p) / e**2
n = n_aksen / (1 + (n_aksen / N))
# Cetak jumlah sampel
print("Jumlah sampel:", math.ceil(n))


# ## Mini Project
# ### Problem I: Mencari Jumlah Sampel dengan Selang Kepercayaan

# In[11]:


# Import numpy sebagai aliasnya np
import numpy as np
# Jumlah anggota populasi
N = 8963
# Proporsi
p = 0.25
# Selang kepercayaan (confidence interval)
ci = [0.70, 0.75, 0.80, 0.85, 0.92, 0.95, 0.96, 0.98, 0.99, 0.999]
# z-score
z = [1.04, 1.15, 1.28, 1.44, 1.75, 1.96, 2.05, 2.33, 2.58, 3.29]
z = np.array(z)
# Margin of error
e = 0.05
# Perhitungan ukuran sampel, n
n_aksen = z**2 * p * (1 - p) / e**2
n = np.ceil(n_aksen / (1 + (n_aksen / N)))
# Cetak ukuran sampel untuk setiap variasi selang kepercayaan
print("Ukuran sampel untuk setiap variasi selang kepercayaan")
print("+--------------------+---------------+")
print("| Selang kepercayaan | Jumlah sampel |")
print("+--------------------+---------------+")
for ci_, n_ in zip(ci, n):
    print("| %17.3f  | %13d |" % (ci_, n_))
print("+--------------------+---------------+")


# ### Problem II: Mencari Varian Margin Galat

# In[12]:


# Import numpy sebagai aliasnya
import numpy as np
# Jumlah anggota populasi
N = 8963
# Proporsi
p = 0.25
# Selang kepercayaan (confidence interval) ci = 0.95
# dengan z-score sebesar
z =  1.96
# Margin of error
e = np.array([0.01, 0.02, 0.05, 0.10, 0.20, 0.25, 0.33, 0.50])
# Perhitungan ukuran sampel, n
n_aksen = z**2 * p * (1 - p) / e**2
n = np.ceil(n_aksen / (1 + (n_aksen / N)))
# Cetak ukuran sampel untuk setiap variasi margin galat
print("Ukuran sampel untuk setiap variasi margin galat")
print("+--------------+---------------+")
print("| Margin galat | Jumlah sampel |")
print("+--------------+---------------+")
for e_, n_ in zip(e, n):
    print("| %12.2f | %13d |" % (e_, n_))
print("+--------------+---------------+")


# ## 4. Kesimpulan
# Berdasarkan mini project diatas dapat disimpulkan bahwa:
# 
# - Semakin tinggi nilai **selang kepercayaan** (semakin mendekati 100%) maka **jumlah sampel** yang perlu ditarik dari suatu populasi akan semakin banyak atau sebaliknya.
# - Semakin tinggi nilai **margin galat** yang digunakan maka jumlah sampel yang ditarik akan menjadi lebih sedikit atau sebaliknya.
