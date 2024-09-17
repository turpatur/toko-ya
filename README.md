# Tugas 2 PBP
## http://fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id
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

# Tugas 3 PBP
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan untuk memastikan bahwa data yang dikirimkan ke komponen, layanan, atau pengguna merupakan informasi yang benar, cepat, efisien, dan terproteksi dalam suatu platform. Tanpa adanya data delivery, sebuah platform tidak dapat berfungsi dengan benar karena komponen-komponen lain yang memerlukan data tidak dapat menerima informasi yang diperlukan sehingga memunculkan beberapa isu, seperti hilangnya komunikasi antarkomponen dan data yang tidak tersinkronisasi.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   - JSON sudah terintegrasi oleh Javascript sehingga implementasinya dalam pengembangan web menjadi lebih mudah.
   - JSON memiliki sintaks yang lebih mudah untuk dibaca, seperti dengan menggunakan pasangan key-value dan array untuk data.
   - Struktur data berupa key-value dan array juga sesuai dengan permodelan data di Javascript dan Python yang digunakan untuk pengembangan web.  
  
3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` berguna untuk memvalidasi isi form. Misal dalam form tersebut terdapat field yang memerlukan integer, tetapi diisi dengan String. Maka, `is_valid` akan mengembalikan nilai `False` sehingga memunculkan pesan error. Sebaliknya, apabila terdapat field integer yang diisi dengan integer, `is_valid()` akan mengembalikan nilai `True` dan data akan lanjut diproses. Hal ini dibutuhkan agar data yang masuk merupakan data dengan tipe data yang sesuai dan dibutuhkan.

4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` digunakan oleh Django untuk melindungi dari Cross-Site Request Forgery. CSRF sendiri adalah serangan di mana penyerang dapat melakukan hal-hal yang tidak diinginkan atau menipu user pada suatu website di mana user sedang terautentikasi. Apabila tidak dapat menambhakan `csrf_token` pada Django, penyerang dapat melakukan semacam action berupa request pada website yang user sudah terautentikasi sehingga website tersebut menerima request dan merespons pada request yang tidak dilakukan pada user itu sendiri. Apabila ada  `csrf_token`, website yang terautentikasi oleh user hanya dapat menerima request yang dibuat oleh user itu sendiri karena adanya token unik yang dibuat oleh django sehingga django hanya menerima token yang bernilai unik tersebut.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Membuat input form untuk menambahkan objek model pada app sebelumnya.
     - Pertama, saya membuat `forms.py` di project Django untuk  `ItemEntry`
       ```python
       from django.forms import ModelForm
       from main.models import ItemEntry
       
       class ItemEntryForm(ModelForm):
         class Meta:
            model = ItemEntry
            fields = ["name", "description", "price", "stock"]
       ```
     - Kemudian, membuat fungsi dalam `views.py` untuk menampilkan input pada form
       ```python
       def create_item_entry(request):
         form = ItemEntryForm(request.POST or None)
         if form.is_valid() and request.method == "POST":
           form.save()
           return redirect('main:show_main')
       
         context = {'form': form}
         return render(request, "create_item_entry.html", context)
       ```
     - Kemudian, membuat `create_item_entry.html` untuk mengisi input pada form
        ```python
        {% extends 'base.html' %} 
        {% block content %}
        <h1>Add New Mood Entry</h1>
        
        <form method="POST">
          {% csrf_token %}
          <table>
            {{ form.as_table }}
            <tr>
              <td></td>
              <td>
                <input type="submit" value="Add Item Entry" />
              </td>
            </tr>
          </table>
        </form>
        
        {% endblock %}
        ```
      - Kemudian, menambahkan kode pada block content di  `main.html`
        ```python
        ...
        {% if not item_entries %}
        <p>Belum ada data item pada Toko-ya.</p>
        {% else %}
        <table>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Price</th>
            <th>Stock</th>
          </tr>
        
          {% comment %} Berikut cara memperlihatkan data item di bawah baris ini 
          {% endcomment %} 
          {% for item_entry in item_entries %}
          <tr>
            <td>{{item_entry.name}}</td>
            <td>{{item_entry.description}}</td>
            <td>{{item_entry.price}}</td>
            <td>{{item_entry.stock}}</td>
          </tr>
          {% endfor %}
        </table>
        {% endif %}
        
        <br />
        
        <a href="{% url 'main:create_item_entry' %}">
          <button>Add New Item Entry</button>
        </a>
        ...
        ```
   - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
     - XML
       ```python
       def show_xml(request):
        data = ItemEntry.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
     - JSON
       ```python
        def show_json(request):
          data = ItemEntry.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
     - XML by id
       ```python
        def show_xml_by_id(request, id):
          data = ItemEntry.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
     - JSON by id
       ```python
        def show_json_by_id(request, id):
          data = ItemEntry.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
     - Hal ini bertujuan agar saya dapat mengambil data pada database dalam bentuk JSON atau XML. Untuk data yang spesifik dapat difilter menggunakan id. 
     
   - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
     - Untuk mengakses data, perlu routing URL yang dilakukan pada `urls.py`
       ```python
       from django.urls import path
       from main.views import show_main, create_item_entry, show_xml, show_json,show_xml_by_id, show_json_by_id
       app_name = 'main'
      
       urlpatterns = [
          path('', show_main, name='show_main'),
          path('create-item-entry', create_item_entry, name='create_item_entry'),
          path('xml/', show_xml, name='show_xml'),
          path('json/', show_json, name='show_json'),
          path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<str:id>/', show_json_by_id, name='show_json_by_id')
       ]
       ```
       - Routing dilakukan untuk mengakses data dari forms input via url dalam bentuk XML atau JSON dan bisa difilter berdasarkan id.
   - Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
     - XML
       ![image](https://github.com/user-attachments/assets/83d06960-7843-457e-8990-93306196392c)
     - JSON
       ![image](https://github.com/user-attachments/assets/ccad8de9-33d1-470f-980c-78ecb38e8499)
     - XML by id
       ![image](https://github.com/user-attachments/assets/417ae12d-014e-4398-8216-4195519f80fa)
     - JSON by id
       ![image](https://github.com/user-attachments/assets/cab3acf6-22f9-43f7-9c11-8dd456fd4e79)
