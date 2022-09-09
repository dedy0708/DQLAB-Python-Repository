#!/usr/bin/env python
# coding: utf-8

# # 1. What's Python?

# ## A. Pendahuluan tentang python
#    Python merupakan bahasa pemrograman yag diciptakan pada tahun 1991 oleh Guido van Russom, seorang matematikawan.
# 
# Python mulai beranjak naik dan populer. Pada beberapa survey terkait bahasa pemrograman yang sering dicari di google, Python berhasil melonjak tajam bahkan mengungguli Java. Bahkan dari insight developer survey dari stackoverflow pada tahun 2018, Python berhasil naik pada TOP 10 programming language yang paling dicari menggungguli seniornya, C, PHP, dan C#. Python merupakan programming language yang memiliki peningkatan pencarian yang sangat tajam dalam setahun terakhir. Python mengklaim dirinya adalah programming language dengan perkembangan tercepat. Selain dari perkembangan library yang semakin kuat, kontributor dari python juga sangat banyak yang akhirnya membuat python menjadi salah satu programming language yang solid dan berkembang pesat.
# 
# Python sendiri berguna dalam berbagai aspek :
# 
# Web Development (Server – Side)
# Software Development
# Mathematics
# Scripting
# Data Science
# Bisa mengelola Big Data dan Rumus matematika yang complex
# Cocok untuk riset dan rapid prototype suatu product dan launch hingga produksi
# CRUD sebuah file dan database
# Kepopuleran python sendiri sekarang ada pada track data science. Banyaknya library dan framework seperti scikit-learn dan tensorflow membuat para pecinta data mining, AI, dan Machine learning menyukai python dalam pengembangan riset dan penelitian mereka. Berkembangnya dunia data science didunia ini juga salah satu alasan kenapa python menjadi begitu populer sekarang.

# ## B. Mengapa Python Populer
# Selain aspek dari meningkatnya minat masyarakat dunia terhadap data science, ada banyak hal yang membuat Python populer. Python merupakan salah satu programming language yang cocok untuk scripting dan bisa bergerak dalam berbagai platform OS dan IoT. Python sangat mirip English language. Meskipun tergolong sebagai high level programming language, python sangat mudah dimengerti karena syntaxnya yang sederhana. Python bisa bergerak dalam dalam berbagai fungsional programming dan OOP.  Python berjalan pada intepreter system, artinya code yang sudah ditulis bisa dijalankan sesegera mungkin.
# 
# Beberapa hal yang mungkin kelebihan dari python:
# 
# Python dirancang untuk mudah dibaca, dan memiliki beberapa kesamaan dengan bahasa Inggris dengan pengaruh dari matematika.
# Python menggunakan baris baru untuk mengakhiri perintah, dibandingkan dengan bahasa pemrograman lain yang sering menggunakan titik koma atau tanda kurung.
# Python bergantung pada indentasi, menggunakan spasi, untuk mendefinisikan ruang lingkup; seperti lingkup loop, fungsi, dan kelas. Bahasa pemrograman lainnya sering menggunakan kurung kurawal untuk tujuan ini
# Jika kalian mencari di internet tentang programming python, biasanya akan ada 2 jenis python, python 2 dan python 3. versi utama Python yang paling baru adalah Python 3, yang akan kami gunakan dalam platform ini. Meskipun begitu, Python 2. Python 2 masih banyak digunakan karena versi python2 ini dianggap sudah stable dan masih bisa digunakan untuk production level. Berbeda dengan python3 yang masih berkembang terus menerus.

# ## C. Code Hello World
# Struktur code pada Python relatif sangat sederhana dan tidak terlalu rumit seperti pada Java ataupun C. Selain karena memang mudah dibaca, python juga termasuk pada high level programming language. Sebagai contoh, cobalah ketik coding pada Code Editor dengan perintah berikut untuk mengeluarkan kata-kata yang diperintahkan.

# In[1]:


print ("Hello World")
print(5+1)
### Note : setiap print akan mencetak baris baru.


# Memang terlihat sangat sederhana jika hanya untuk kasus sederhana yang kita pelajari pada section kali ini. Namun, python tidak sesederhana itu. Biasanya kita juga menggunakan import library khusus jika sudah menyangkut masalah yang lebih kompleks. Next section mungkin akan menjelaskan lebih lanjut.

# ## D. Melakukan comment pada code
# Pada suatu kegiatan membuat code, penting sekali bagi para penulis codenya untuk memberikan sebuah dokumentasi pada penulisan codenya. Mengapa hal itu sangat penting? Sederhana, jika codenya sudah lebih dari ribuan baris dan ada beberapa bagian yang perlu diperbaiki karena suatu perubahan, para penulis code cukup melihat dokumentasinya dan tidak perlu membaca dan memahami seluruh isi code dari awal. Nah, salah satu metode yang biasa digunakan adalah menggunakan comment. Sama dengan Bahasa R, python juga menggunakan tanda “#” untuk melakukan comment pada script.

# In[2]:


print(10*2+5) #fungsi matematika
print("Academy DQLab") #fungsi mencetak kalimat


# ## Variable, Basic Data Type and Print
# 
# Penggunaan variabel atau suatu objek yang bisa merepresentasikan sebuah nilai atau value sangat penting dalam bahasa pemrograman. Selain itu mempermudah dalam membaca source code, pemberian variable yang efisien juga akan membuat code berjalan optimal dan dinamis. Pada sesi kali ini kita akan belajar bagaimana cara inisialisasi variable dalam beberapa data type dan menampilkannya (print).
# 
# Tipe Data          Contoh                                                  Penjelasan
# 
# Boolean -->        True atau False             Menyatakan benar True yang bernilai 1, atau salah False yang bernilai 0
# 
# String -->     "Ayo belajar Python"       Menyatakan karakter/kalimat bisa berupa huruf angka, dll (diapit tanda " atau ')
# 
# Integer -->       25 atau 1209                                      Menyatakan bilangan bulat
#  
# Float -->        3.14 atau 0.99                              Menyatakan bilangan yang mempunyai koma
# 
# List -->         ['xyz', 786, 2.23]           Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah
# 
# Tuple -->       ('xyz', 768, 2.23)       Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah
# 
# Dictionary --> {'nama': 'adi','id':2}   Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai

# ## Printing data type

# In[42]:


#tipe data Boolean
print(True)

#tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah di DQLAB')

#tipe data Integer
print(20)

#tipe data Float
print(3.14)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Budi", 'umur':20})

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>


# In[43]:


#contoh lainnya
var_string="Belajar Python DQLAB"
var_int=10
var_float=3.14
var_list=[1,2,3,4]
var_tuple=("satu","dua","tiga")
var_dict={"nama":"Ali", 'umur':20}

print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))


# # 2. Struktur Kontrol: Percabangan Keputusan

# ## A. Pendahuluan
# Dalam membuat suatu keputusan biasanya pasti ada sebuah pilihan. Untuk mewujudkan suatu kerangka berpikir pada suatu pilihan pada bahasa pemrograman biasanya kita menggunakan konsep IF, ELSE. Pada python sebenarnya hampir sama dan tidak ada perbedaan yang terlalu signifikan. Perbedaanya mungkin ada pada
# 
# Pada praktek kali ini akan dibagi menjadi 3 bagian :
# 
# Menggunakan IF yang jika direpresentasikan dengan kata – kata, (Jika, sesuatu memenuhi suatu kondisi, maka lakukan A, jika tidak, tidak terjadi apa-apa)
# Menggunakan IF dan ELSE yang jika direpresentasikan dengan kata – kata, (Jika, sesuatu memenuhi suatu kondisi, maka lakukan A, jika tidak, lakukan B)
# Menggunakan IF, ELIF dan ELSE. ELIF sendiri sebenarnya sama persis dengan ELSE IF. Namun, pada python disingkat menjadi ELSE IF. (Jika, sesuatu memenuhi suatu kondisi, maka lakukan A, jika tidak, lakukan pengecekan pada kondisi berikutnya, jika memenuhi lakukan B, jika tidak maka lakukan C)

# ## B. IF Statment
# Penggunaan IF sebenarnya adalah sebuah statement untuk menentukan keputusan mana yang akan diambil berdasarkan suatu kondisi yang ditentukan oleh pembuat program.

# In[6]:


i = 10 #inisialisasi variable i yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini


# ## C. IF … ELSE …

# In[7]:


i = 10 #inisialisasi variable i yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10") #jika FALSE akan mencetak kalimat ini


# In[8]:


i = 5 #inisialisasi variable i yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10") #jika FALSE akan mencetak kalimat ini


# Penjelasan:
# Nilai variable adalah 5. Pada kondisi pertama variable i tidak memenuhi. Maka dari output yang diberikan adalah perintah pada else yang merupakan hasil apabila pengecekan pertama tidak sesuai

# ## D. IF … ELIF … ELSE ….

# In[44]:


i=3
if(i==5):
     print("ini adalah angka 5")
elif(i>5):
     print("lebih besar dari 5")
else:
     print("lebih kecil dari 5")


# Penjelasan :
# 
# Nilai variable i tidak memenuhi dari kondisi pertama dimana ditanyakan apakah nilai i sama dengan 5. Lalu masuk pada pengecekan kedua variable i juga tidak memenuhi. 
# 
# Maka dari itu langsung masuk pada perintah ketiga karena kedua pengecekan awal tidak memenuhi.

# ## E. NESTED IF

# In[55]:


# Python program to demonstrate 
# nested if statement 
i = 2
  
if (i == 2):  
    #  First if statement  
    if (i < 7):  
        print ("nilai i kurang dari 7")  
          
    # Nested - if statement  
    # Will only be executed if statement above  
    # it is true  
    if (i < 3):  
        print ("nilai kurang dari 7 dan kurang dari 3")  
    else:  
        print ("nilai kurang dari 7 tapi lebih dari 3")


# # 3. Operator Matematika dan Pembanding

# ## A. Pendahuluan
# 
# Data Science tidak akan terlepas dari matematika. Pada modul python ini kita juga belajar berbagai macam operator matematika dengan python yang tentu berguna untuk membantu menyelesaikan masalah dalam data science. Pada sesi kali ini, operator yang disajikan adalah operator dasar dan operator logika pada matematika. Pada dasarnya, setiap bahasa pemrograman akan memiliki operasi pengelolahan angka dan perbandingan.
# 
# Operator yang akan kita bahas kali ini adalah :
# 
# 1. Tambah (+)
# 
# 2. Kurang (-)
# 
# 3. Pembagi (/)
# 
# 4. Perkalian (*)
# 
# 5. Modulus (%)
# 
# 6. Kurang dari (<) 
# 
# 7. Lebih dari (>) 
# 
# 8. Kurang dari sama dengan (<=)
# 
# 9. Lebih dari sama dengan (>=)
# 
# 10. Sama dengan (=)

# ## B. Praktik Operasi Matematika
# Pada praktik ini kita akan mencoba seluruh operator matematika.
# 
# Fokus pada sesi ini dititikberatkan pada penggunaan operator matematika menggunakan dua variabel yang telah diinisialisasi masing-masingnya dengan bilangan bulat tertentu.

# In[2]:


a=10
b=5
selisih = a-b
jumlah = a+b
kali = a*b
bagi = a/b
print("Hasil penjumlahan a dan b adalah :", jumlah)
print("Selisih a dan b adalah           :",selisih)
print("Hasil perkalian a dan b adalah   :",kali)
print("Hasil pembagian a dan b adalah   :",bagi)


# ## C. Operasi modulus
# Modulus cukup jarang dipakai, akan tetapi untuk beberapa kasus modulus sangat berguna terutama dalam mempercepat proses perhitungan. Modulus merupakan fungsi yang akan menghitung sisa dari hasil pembagian.

# In[4]:


a=11
b=5

modulus=a%b
print("Hasil modulus",modulus)


# Kenapa bisa seperti itu? Prinsip modulus adalah dasarnya sebuah pembagian. Jika pembagi tidak bisa membagi habis angka yang dibagi maka akan dibagi hingga mendekati nilai terkecil yang tidak mampu dibagi lagi. Selisih antara angka yang mendekati dan angka yang dibagi nanti merupakan hasil modulus. Jika habis dibagi seperti kasus pertama 10/5 maka modulus akan mengembalikan nilai 0.

# ## D. Tugas Mid Praktek
# Buatlah sebuah program yang dapat menentukan suatu variabel apakah merupakan bilangan genap atau ganjil. Lakukan percobaan dengan langkah berikut:
# 
# Buat variabel dengan nama **“angka”** yang diisi dengan nilai 10
# Ganti bagian … dengan perhitungan untuk menentukan angka **modulus 2** bernilai 0.
# Jika **angka** bernilai genap maka keluarkan **"angka termasuk bilangan genap"**. Selanjutnya, ganti nilai variable **angka** dengan nilai **5** dan ceklah kembali apakah **angka** bernilai ganjil. Jika iya, keluarkan **"angka termasuk bilangan ganjil"**.
# 
# **Note**: Kamu bisa menggunakan materi-materi sebelumnya dengan menggabungkannya di tugas praktik ini untuk membantu kamu dalam mengerjakannya.

# In[6]:


angka=10

if(angka%2 == 0):
    print("angka termasuk bilangan genap")
else:
    print("angka termasuk bilangan ganjil")


# # 4. Perulangan

# ## A. Pendahuluan
# Perulangan atau looping merupakan salah satu elemen atau fungsi yang bisa dikatakan sangat menunjang untuk kebutuhan programming dan data science.
# 
# Ambil contoh, seandainya kita harus memproses 1000x eksekusi code. Tentu akan menghabiskan waktu bila kita harus menulis ulang kode tersebut sebanyak 1000x juga.
# 
# Selain tidak bersifat scalable, efisiensi akan mempengaruhi performa dari program yang kita buat. Seperti pada umumnya pada python juga memiliki fungsi for dan while untuk melakukan looping. Logikanya hampir sama, namun hanya berbeda dalam penulisannya jika kamu sudah terbiasa dengan C ataupun Java.

# ## B. Operator fungsi While
# Struktur while pada python tidak berbeda jauh dengan bahasa pemrograman lainnya. Lebih sederhananya, struktur penulisan python membuat dia mudah untuk dibaca.

# In[45]:


#nilai awal j =0
j = 0 

#ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
while j<3: 
    #lakukan perintah ini ketika perulangan
    print("Ini adalah perulangan ke -",j) 
    #setiap kali diakhir perulangan update nilai dengan ditambah 1.
    j=j+1 


# ## C. Fungsi Looping with for (1)
# Struktur looping for pada python berbeda dengan struktur for pada umumnya. Pastikan untuk memperhatikan hal ini dengan baik.

# In[46]:


for i in range (1,4): #perulangan for sebagai inisialisasi dari angka 1 hingga angka yang lebih kecil daripada 6.
    print("Ini adalah perulangan ke -", i) #perintah jika looping akan tetap berjalan


# Maksud dari fungsi **for i in range (1,6)** adalah, jika kita konversi pada JAVA atau C sama dengan **for(i=1;i<6i++)**. Jika dikonversi menjadi kalimat maka akan menjadi **“perulangan dimulai dari nilai i = 1 hingga nilai i kurang dari 6 dimana setiap kali perulangan nilai i akan selalu ditambah 1”**. Jika nilai i sudah mencapai 6 perulangan akan dihentikan.

# ## D. for (2) with access element
# Keunikan lain dari looping dengan python adalah selain bahasa yang mudah dimengerti, kita juga bisa mengakses elemen yang terdapat pada sebuah list. Berikut ini

# In[9]:


#contoh 
count=[1,2,3,4,5] #elemen list

for number in count: #looping untuk menampilkan semua elemen pada count
    print("Ini adalah element count : ", number) #menampilkan elemen list pada count


# #### Tugas Praktek
# Buatlah sebuah program yang mengeluarkan angka 1 sampai 10.
# Tampilan akan menunjukan "Angka ganjil 1" untuk angka ganjil dan "Angka genap 2" untuk angka genap. (Menggunakan looping for)
# Note: Kode dasar sudah disertakan, Anda cukup mengganti tanda # dengan nilai-nilai yang sesuai.

# In[71]:


for i in range (1,12):
    if(i%2 == 0):
        print("Angka {} adalah genap".format(i))
    else:
         print("Angka {} adalah ganjil".format(i))


# # 5. Function

# ## A. Pendahuluan
# Pada pembuatan program yang kompleks dan memiliki banyak fitur, kita diharuskan menggunakan fungsi. Hal ini bertujuan supaya kita tidak kesulitan untuk menulis kode programnya. Kesulitan ini bisa muncul karena banyak kode yang harus ditulis. Seiring berjalannya waktu, kode bisa menjadi sulit dibaca dan dirawat (maintenance).
# 
# Dalam hal ini, fungsi dapat dianalogikan sebagai sebuah perangkat untuk tujuan tertentu. Perangkat dengan tujuan tertentu ini merupakan fitur dari program kita yang dapat dipanggil kapanpun sesuai dengan kebutuhan. Untuk membuat sebuah fungsi perlu didasari pada tujuan tertentu apa yang akan dihasilkan oleh fitur program kita.
# 
# Dengan demikian, sebuah fungsi ini bersifat reusable atau dapat digunakan secara berulang. Di samping itu, penggunaan fungsi membuat program menjadi lebih terstruktur dan mudah dirawat.

# ## B. Membuat fungsi sendiri
# Fungsi pada Python, dibuat dengan kata kunci ***def***  kemudian diikuti dengan nama fungsinya.
# Sebagai contoh full code-nya, kamu bisa coba ketikkan kode di bawah ini :

# In[18]:


#Contoh
def nama_fungsi():
    print ("Hello ini Fungsi")

nama_fungsi()


# Sama seperti blok kode yang lain, kita juga harus memberikan indentasi (tab atau spasi 2x) untuk menuliskan isi fungsi.

# In[19]:


# Membuat Fungsi
def salam():
    print("Hello, Selamat Pagi")
## Pemanggilan Fungsi
salam()


# ## C. Parameter pada fungsi
# Sekarang, bagaimana kalau kita ingin memberikan input nilai ke dalam fungsi? Kita bisa menggunakan parameter. Parameter adalah variabel yang menampung nilai untuk diproses kedalam suatu fungsi.

# In[20]:


def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas);

# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6) 


# ## D. Fungsi dengan Return Value
# Fungsi yang tidak mengembalikan nilai biasanya disebut dengan prosedur. Namun, kadang kita butuh hasil proses dari fungsi untuk digunakan pada proses berikutnya. Maka fungsi harus mengembalikan nilai dari hasil pemrosesannya. Cara mengembalikan nilai adalah menggunakan kata kunci return lalu diikuti dengan nilai atau variabel yang akan dikembalikan.

# In[21]:


#alas dan tinggi merupakan parameter yang masuk
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas

# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga 
print("Luas segitiga: %d" % luas_segitiga(4, 6))


# # 6. Modul dan Package

# ## A. Pendahuluan
# Modul merupakan objek python yang telah tersedia dari pengembangnya atau dapat kamu kembangkan sendiri. Dalam bahasa yang cukup sederhana, modul adalah kumpulan kode Python yang distruktur ke dalam beberapa fungsi, kelas, dan variabel. Python sendiri telahmemiliki banyak library dan module yang bisa diakses oleh pengguna secara free.
# 
# Umumnya modul dikembangkan untuk tujuan umum yang luas penerapannya seperti:
# 
# - untuk pengolah data numerik seperti array 1D, 2D, 3D atau hingga nD dengan contohnya adalah **numpy****
# - untuk komputasi saintifik yang berbasis metode numerik dan statistik dengan contohnya adalah **scipy** dan **statsmodel**
# - untuk pengolah dan analisis data seperti Microsoft Excel atau Google Spreadsheets dengan contohnya adalah **pandas**, **pypolar**, dan **modin**
# - untuk visualisasi data dengan contohnya yaitu **matplotlib, seaborn, plotnine, altair, mayavi, bokeh, plotly**, dll.  
# - untuk pembelajaran mesin dengan contohnya yaitu **scikit-learn, xgboost, lightgbm, catboost, pycaret**, dll
# - untuk deep learning dengan contohnya adalah **keras, tensorflow, pytorch, cafe**, dll
# 
# Tentunya masih banyak lagi jika disebutkan. Library atau modul-modul yang telah disebutkan merupakan library yang umum digunakan oleh data scientist.

# ## B. Import Package dan Menggunakan modul
# Pada sesi praktik ini, kita akan menggunakan modul math yang merupakan module standar untuk berbagai fungsi matematika.
# Secara umum, module memiliki banyak fungsi. Cara pemrogram untuk mengakses fungsi-fungsi yang tersedia pada suatu modul juga berbeda-beda.

# In[22]:


import math
# math.pi merupakan sintak untuk memanggil fungsi pi
print("Nilai pi adalah:", math.pi)


# ## C. Import dengan Module Rename atau Alias
# Kita bisa mengimpor modul dengan mengganti namanya. Hal ini biasa dilakukan untuk menyingkat nama modul yang panjang.

# In[23]:


#menggunakan m sebagai module rename atau alias
import math as m

#m.pi merupakan sintak untuk memanggil fungsi
print("Nilai pi adalah:", m.pi)


# ## D. Import Sebagian Fungsi
# Sebuah module dapat memiliki puluhan atau ratusan fungsi. Terkadang kasus tertentu ketika memprogram, kita hanya membutuhkan satu, dua, atau beberapa buah fungsi saja. Untuk meminimalisir ketidakefisienan suatu program dalam me-load suatu module seperti yang telah dilakukan dalam format **import module_name**. Selanjutnya, kita dapat mengimport beberapa modul yang dibutuhkan saja menggunakan format **from module_name import function_name**

# In[24]:


from math import pi

print("Nilai pi adalah", pi)


# ## E. Import Semua isi Moduls
# Namun, jika memang yang dibutuhkan banyak, semisal lebih dari 10 atau bahkan ratusan fungsi, bisa dilakukan import semuanya dengan menggunakan format **from module_name import ***. Tanda * disini menunjukan semua fungsi diimport ke dalam code.

# In[27]:


from math import *

print("Nilai e adalah:", e)


# # 7. Membaca dari File

# ## A. Pendahuluan
# CSV atau comma separated value adalah salah satu tipe file yang digunakan secara luas di dunia programming. Tidak hanya itu CSV pun sering digunakan dalam pengolahan informasi yang dihasilkan spreadsheet untuk diproses lebih lanjut melalui mesin analitik. CSV pun dianggap sebagai file yang agnostik karena dapat digunakan oleh berbagai database untuk proses backup data. CSV dianggap sebagai salah satu tipe data yang sering dipakai untuk mengelola data pada proses lanjutan.

# ## B. Membaca Teks File (CSV)
# 
# Sekarang kita akan mencoba membaca sebuah file CSV yang telah dihasilkan aplikasi atau program lain. Di Python, hasil pembacaan setiap baris pada file CSV akan dikonversi menjadi list Python.
# 
# Berikut adalah contoh kode untuk membaca file CSV dengan kasus yang sangat sederhana.

# In[28]:


import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

# baca file csv secara streaming 
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = csv.reader(f, delimiter=',')
    
    # membaca baris per baris
    for row in reader:
        print(row)


# ## C. Membaca file CSV dengan menggunakan PANDAS
# Bagi yang belum familiar, PANDAS merupakan salah satu library yang sangat sering digunakan untuk aplikasi dan implementasi data science baik untuk data manipulation, data pre-processing, atau data wrangling. Pada sesi kali ini, kita akan menggunakan PANDAS untuk membaca file dari csv.

# In[69]:


import pandas as pd
pd.set_option("display.max_columns",40)

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)


# # 8. Grafik Dasar dengan Matplotlib

# ## A. Pendahuluan
# Grafik merupakan salah satu perangkat visualisasi. Visualisasi sendiri sudah menjadi salah satu challenge atau poin penting dalam data science. Selain bisa mempermudah seseorang untuk memahami data, visualisasi bisa meningkatkan analisa atau memunculkan knowledge yang tidak sempat terekspos ketika tidak menggunakan visualisasi.

# ## B. Bar Chart
# Sebelum masuk pada membuat grafik bar, kita akan membahas library yang akan gunakan. Python punya banyak library untuk visualisasi. Salah satu yang paling sering digunakan adalah matplotlib karena memang sudah ada sejak lama dan relatif stabil dalam perkembangannya. Maka dari itu, matplotlib dipilih untuk belajar visualisasi pada sesi kali ini.
# 
# Matplotlib sendiri menyediakan banyak jenis grafik mulai dari scatter/plot, line, bar, dan lain-lain. 
# 
# Pada praktik ini, akan ada tambahan library selain dengan menggunakan matplotlib dan pandas, yaitu menggunakan numpy. Numpy sendiri pada praktek kali ini digunakan untuk melakukan manipulasi data dari csv untuk memudahkan visualisasi.

# In[66]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()


plt.figure(figsize = (17,11))
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), 
        height=table['LAKI-LAKI WNI'], color = 'red')
plt.show()


# 
# 
# 
# ## C. Parameter dalam Grafik (Memberikan Nilai Axis dari data CSV)
# Jika ditelisik lebih dalam pada CSV, dari sana ada nama kelurahan yang merupakan variabel atau seharusnya menjadi nilai AXIS pada grafik ini. Di praktek kali ini, kita akan mencoba bagaimana menempatkan nama kelurahan pada grafik.

# In[65]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.figure(figsize = (17,10))
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'], color = 'green')
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
plt.show()


# ## D. Menambah Title dan Label pada Grafik
# Pada implementasi grafik, pemberian label pada AXIS dan Ordinat sangat penting untuk menjelaskan maksud grafik. Pada praktik kali ini, kita akan mencoba memberikan label dan title pada grafik yang telah dibuat sebelumnya.

# In[67]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.figure(figsize = (17,8))
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'], color = 'darkblue')
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat', size=15)
plt.ylabel('Jumlah Penduduk Laki - Laki', size=15)
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat', size=20)
plt.show()


# In[68]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.figure(figsize = (17,8))
plt.bar(x=np.arange(len(x_label)),height=table['PEREMPUAN WNI'], color = 'black')
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat', size=15)
plt.ylabel('Jumlah Penduduk PEREMPUAN', size=15)
plt.title('Persebaran Jumlah Penduduk PEREMPUAN di Jakarta Pusat', size=20)
plt.show()

