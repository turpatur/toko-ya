# Tugas 1 PBP
## 
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
- Membuat sebuah proyek Django baru. \
  Saya membuat project baru dengan membuat directory baru `toko-ya`, di dalam direktorinya saya buat virtual environment dengan `python -m venv env`, lalu menjalankan virtual environment dengan `env\Scripts\activate`. Setelah itu, saya menginstall dependencies yang terdapat pada `requirements.txt` dengan `pip install -r requirements.txt`. Kemudian, saya menjalankan perintah `djangoadmin startproject toko_ya .` untuk inisiasi project django
- Membuat aplikasi dengan nama main pada proyek tersebut. \
  Saya menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi main. Kemudian, saya menambahkan `'main` pada variabel `INSTALLED_APPPS` di file `settings.py` pada direktory `tokoy_ya`.
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main. \
  Saya membuat routing request ke aplikasi main dengan menambahkan `path('', include('main.urls'))` di variabel `urlpatterns` pada file `urls.py` dalam direktori `toko_ya`. Hal ini bertujuan untuk mengimpor rute url dari aplikasi `main` ke `urls.py`.
- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. \
&ensp; * `name`\
&ensp; * `price`\
&ensp; * `description`\
Saya membuat class `ItemEntry` dalam `models.py` dalam direktori `main` yang memiliki atribut-atribut seperti yang sudah disebutkan dengan atribut `name` berupa `CharField`, `price` berupa `IntegerField`, description berupa `TextField`, dan saya tambahkan `stock` berupa `IntegerField`.
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  pada  `views.py` saya membuat fungsi `show_main` untuk merender tampilan HTML. Tampilan HTML yang dirender berisi nama aplikasi, nama, dan NPM.
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
  karena fungsi `show_main` sudah dibuat, saya menambahkan `path('', show_main, name='show_main'),` pada variabel `urlpatterns` di `urls.py` dalam direktori `toko_ya` untuk memetakan fungsi `show_main` pada HTML yang sudah dibuat
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  saya membuat project tokoya2 pada PWS dan menambahkan `"fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id"` pada `ALLOWED HOSTS` di `settings.py` pada direktori `toko_ya`, lalu menjalankan perintah `git add remote pws fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id` untuk push project saya ke pws.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html. <br>
![Bagan](https://github.com/user-attachments/assets/72c07ff8-52d2-4d6f-bd9e-a15d8835d82c)

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak! <br>
Git berfungsi sebagai _version control_ untuk pengembangan perangkat lunak yang bisa melacak adanya perubahan-perubahan dalam kode yang kita telah buat. Untuk membuat fitur baru, kita dapat melakukan `branch` agar fitur tersebut tidak mempengaruhi version live pada suatu project, apabila sudah aman, dapat melakukan merge pada pada project live. Apabila ada kesalahan dapat melakukan rollback ke versi sebelumnya. Hal ini membuat git sangat berguna untuk pengembangan perangkat lunak.
 
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? <br>
Django menerapkan arsitektur MVT (Model View Template) untuk memisahkan tugas-tugas pada masing masing komponen sehingga kode dapat mudah dikelola. Hal ini membuat django cocok untuk permulaan pembelajaran pengembangan perangkat lunak karena MVT membuat mahasiswa dapat mengerti pengembangan web secara terstruktur. Selain itu, Django juga memiliki dokuemntasi yang lengkap dan komunitas yang aktif sehingga dapat memudahkan untuk mencari solusi.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django memungkinkan pengembang perangkat lunak untuk berinteraksi dengan database relasional yang merupakan berupa tabel berisi baris dan kolom dengan object python dan tanpa menulis query SQL secara langsung untuk memudahkan pengelolaan database.
