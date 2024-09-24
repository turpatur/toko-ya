# PBP 
## http://fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id
Past Works :
1. [Tugas 2](https://github.com/turpatur/toko-ya/wiki/Tugas-2)
2. [Tugas 3](https://github.com/turpatur/toko-ya/wiki/Tugas-3)
### Tugas 4
1.  Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
  - `HttpResponseRedirect()`
    - return HTTP response dengan status code 302
    - Hanya menerima argumen URL 
  
  - `redirect()`
    - return `HttpResponseRedirect()` 
    - Dapat menerima argumen selain URL, seperti model dan view. 
    - Lebih singkat secara sintaks 

2. Jelaskan cara kerja penghubungan model `Product` dengan `User`! <br>
  `Product` dapat dihubungkan dengan `user` dengan menggunakan `ForeignKey`. Hal tersebut menghubungkan `Product` dengan `User` dengan relasi many-to-one sehingga banyak `Product` dapat dimiliki oleh satu `User`, tetapi satu `Product` hanya dimiliki oleh satu `User`.

4.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
  - Authentication
    - Proses verifikasi identitas User agar website dapat diakses oleh User yang diverifikasi.
  - Authorization 
    - Proses pemberian hak izin untuk User yang telah terautentikasi untuk mengakses suatu resource atau melakukan suatu action <br>
    
  - Saat pengguna login, Django melakukan Authentication untuk memverifikasi User. Apabila sesuai Django melakukan Authorization untuk memberi hak akses yang sesuai kepada User. Django dapat mengimplementasikan authentication dengan AuthenticationForm(), lalu mengecek apakah form diisi dengan informasi yang valid terhadap suatu User dengan is_valid(). Apabila valid, Django dapat membuat session dengan login(). Django dapat mengimplementasikan Authorization dengan permissions dan groups yang dapat diatur pada model atau view. 

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
  - Django mengigat pengguna yang telah login dengan menggunakan session dan cookies. Django menyimpan session ID berupa cookie pada browser user. Setiap kali user mengirimkan request, cookie juga ikut dikirim. Jika session ID yang dikirim cocok dengan session ID yang disimpan, maka Django menganggap bahwa User yang melakukan request adalah sama dengan yang login. 
  - Kegunaan lain dari cookies adalah untuk menyimpan preferensi pengguna, missal dark mode atau light mode pada suatu website dan personaliasi iklan yang dimunculkan pada suatu website. 
  - Tidak semya cookies aman untuk digunakan karena dapat digunakan untuk XSS (Cross-Site Scripting) dan Session Hijacking. Untuk membuat Cookies menjadi lebih aman, dapat menambahkan atribut pada cookies, seperti HttpOnly agar cookies tidak dapat diakses JavaScript, Secure agar cookies hanya dapat diakses pada HTTPS, atau SamSite untuk mencegah mengirm cookies ke situs lain.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   -  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
     - Register
       - buat function `register` pada views.py
         ```python
         def register(request):
          form = UserCreationForm()
          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
          context = {'form':form}
          return render(request, 'register.html', context)
         ```
       - buat file `register.html` pada `main/templates`
         ```html
          {% extends 'base.html' %}
          {% block meta %}
          <title>Register</title>
          {% endblock meta %}
          
          {% block content %}
          
          <div class="login">
            <h1>Register</h1>
          
            <form method="POST">
              {% csrf_token %}
              <table>
                {{ form.as_table }}
                <tr>
                  <td></td>
                  <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
              </table>
            </form>
          
            {% if messages %}
            <ul>
              {% for message in messages %}
              <li>{{ message }}</li>
              {% endfor %}
            </ul>
            {% endif %}
          </div>
          
          {% endblock content %}
         ```
     - Login
       - buat function `login_user` pada views.py
           ```python
           def login_user(request):
             if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
          
                if form.is_valid():
                      user = form.get_user()
                      login(request, user)
                      return redirect('main:show_main')
          
             else:
                form = AuthenticationForm(request)
             context = {'form': form}
             return render(request, 'login.html', context)
           ```
       - buat file `login.html` pada `main/templates`
         ```html
          {% extends 'base.html' %}
          {% block meta %}
          <title>Login</title>
          {% endblock meta %}
          
          {% block content %}
          <div class="login">
            <h1>Login</h1>
          
            <form method="POST" action="">
              {% csrf_token %}
              <table>
                {{ form.as_table }}
                <tr>
                  <td></td>
                  <td><input class="btn login_btn" type="submit" value="Login" /></td>
                </tr>
              </table>
            </form>
          
            {% if messages %}
            <ul>
              {% for message in messages %}
              <li>{{ message }}</li>
              {% endfor %}
            </ul>
            {% endif %} Don't have an account yet?
            <a href="{% url 'main:register' %}">Register Now</a>
          </div>
          
          {% endblock content %}
         ```
     - Logout
        - buat function `logout_user` pada views.py
          ```python
             def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response
           ```
       - Tambahkan tombol logout pada `main.html` di `main/templates`
           ```python
               ...
                <a href="{% url 'main:logout' %}">
                  <button>Logout</button>
                </a>
                ...
           ```
     - Tambahkan path ke `urlpatterns` pada `urls.py`
       ```python
       urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-item-entry', create_item_entry, name='create_item_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        ]
       ``` 

   - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
     - Buat 2 akun, kemudian buat 3 item entri di masing-masing akun tersebut
       - ![image](https://github.com/user-attachments/assets/32d48c9d-aa03-4d58-99a6-0b1e8c28111d)
       - ![image](https://github.com/user-attachments/assets/fbb3d868-81b0-4c5f-98bd-f9c821050a23)
   - Menghubungkan model Product dengan User.
     - Modifikasi model agar `ItemEntry` memiliki atribut user dengan `ForeignKey` untuk menghubungkan model dengan `User`
       ```python
        from django.db import models
        import uuid  
        from django.contrib.auth.models import User
        # Create your models here.
        
        class ItemEntry(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            name = models.CharField(max_length=255)
            description = models.TextField()
            price = models.IntegerField()
            stock = models.IntegerField()
       ```
     - Migrate model dengan menjalankan perintah berikut <br>
       - `python manage.py makemigrations`
       - `python manage.py migrate`
   - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
     - Set cookies pada `login_user`
       ```python
       def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  response = HttpResponseRedirect(reverse("main:show_main"))
                  response.set_cookie('last_login', str(datetime.datetime.now()))
                  return response
      
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
       ```
     - Menambahkan informasi cookie `last_login` pada `show_main`
       ```python
        @login_required(login_url='/login')
        def show_main(request):
            item_entries = ItemEntry.objects.filter(user=request.user)
            context = {
                'title': 'Toko-ya',
                'name': request.user.username,
                'class': 'PBP E',
                'item_entries' : item_entries,
                'last_login': request.COOKIES['last_login'],
            }
            return render(request, "main.html", context)
       ```
     - Tampilkan sesi terakhir login pada  `main.html`
       ```html
        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
       ```
