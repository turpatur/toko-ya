# PBP 
## http://fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id
Past Works :
1. [Tugas 2](https://github.com/turpatur/toko-ya/wiki/Tugas-2)
2. [Tugas 3](https://github.com/turpatur/toko-ya/wiki/Tugas-3)
3. [Tugas 4](https://github.com/turpatur/toko-ya/wiki/Tugas-4)

### Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   Dari tertinggi ke terendah:
   - !important <br>
     Meningkatkan prioritas suatu style 
   - Inline Style <br>
     Menambahkan style langsung pada HTML
   - ID Selector <br>
     Menerapkan style pada element dengan suatu ID
   - Class Selector <br>
     Menerapkan style pada suatu class
   - Tag Selector <br>
     Menerapkan style pada suatu tag
   - Universal Selector <br>
     menerapkan style pada semua element
     
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
   Responsive design adalah design pada suatu website yang dapat diperbesar atau diperkecil tergantung ukuran layar pada suatu jenis perangkat. Responsive penting karena dapat mempermudah navigasi user pada suatu web pada semua perangkat. Aplikasi yang sudah menerapkan responsive design adalah `github.com` dan yang belum adalah `academic.ui.ac.id`
   
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
   - Margin <br>
     Margin adalah ruang transparan di luar border. 
   - Border <br>
     Border adalah garis yang menegelilingi padding dan konten.
   - Padding <br>
     Padding adalah ruang transparan yang mengelilingi konten.
   - Implementasi
     ```css
     div {
      border: 15px solid blue;
      padding: 20px;
      margin: 10px;
      }
     ```
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   - Flex Box <br>
     Flex Box adalah sistem layout satu dimensi dengan kemampuan untuk mendistribusikan ruang pada elemen-elemen pada suatu kontainer. Sesuai namanya, flex Box sangatlah fleksibel sehingga dapat berubah ukuran menyesuaikan ukuran layar. Kegunaan dari Flex Box adalah untuk mengatur elemen pada baris atau kolom dan memudahkan distribusi ruang antarelemen. 
   - Grid Layout <br>
     Grid Layout adalah sistem layout dua dimensi dengan baris dan kolom. Grid Layout memudahkan pengembang untuk mengatur elemen-elemen dalam susunan baris dan kolom. Kegunaannya adalah untuk mengatur elemendalam grid yang lebih komplek dan membuat tata letak yang berstruktur. 
   - Kegunaan <br>
     Kedua sistem layout memiliki kegunaan untuk membuat web yang responsif. 
    
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   - Implementasikan fungsi untuk menghapus dan mengedit product.
     - Buat function pada views
       ```python
       def edit_item(request, id):
            # Get mood entry berdasarkan id
            item = ItemEntry.objects.get(pk = id)
        
            # Set mood entry sebagai instance dari form
            form = ItemEntryForm(request.POST or None, instance=item)
        
            if form.is_valid() and request.method == "POST":
                # Simpan form dan kembali ke halaman awal
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))
        
            context = {'form': form}
            return render(request, "edit_item.html", context)
        
       def delete_item(request, id):
            # Get item berdasarkan id
            item = ItemEntry.objects.get(pk = id)
            # Hapus item
            item.delete()
            # Kembali ke halaman awal
            return HttpResponseRedirect(reverse('main:show_main'))
       ```
     - Routing url
       ```python
        from django.urls import path
        from main.views import show_main, create_item_entry, show_xml, show_json,show_xml_by_id, show_json_by_id
        from main.views import register
        from main.views import login_user
        from main.views import logout_user
        from main.views import edit_item
        from main.views import delete_item
        
        app_name = 'main'
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
            path('edit-item/<uuid:id>', edit_item, name='edit_item'),
            path('delete/<uuid:id>', delete_item, name='delete_item'),
        
        ]
       ```
   - Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut: 
     - Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
     - Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
     - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
     - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
     - Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
     - Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

       - tambahkan tailwind ke `base.html`
         ```html
          {% load static %}
          <!DOCTYPE html>
          <html lang="en">
            <head>
              <meta charset="UTF-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1.0" />
              {% block meta %} {% endblock meta %}
              <script src="https://cdn.tailwindcss.com"></script>
              <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
            </head>
            <body>
              {% block content %} {% endblock content %}
            </body>
          </html>
         ```
       - buat `global.css` untuk mendefinisikan styles pada `static/css/`
         ```css
          .form-style form input, 
          .form-style form textarea, 
          .form-style form select {
              width: 100%;
              padding: 0.5rem;
              border: 2px solid #bcbcbc;
              border-radius: 0.375rem; /* Tailwind's rounded-md equivalent */
              transition: border-color 0.3s, box-shadow 0.3s;
          }
          
          .form-style form input:focus, 
          .form-style form textarea:focus, 
          .form-style form select:focus {
              outline: none;
              border-color: #bcbcbc; /* Border color on focus */
              box-shadow: 0 0 0 3px #bcbcbc; /* Glow effect on focus */
          }
          
          .bg-offwhite {
              background-color: #f8f8f8; /* Adjust color to your liking */
          }

         ```
       - Modifikasi atau buat file html baru 
         - `login.html`
           ```html
            {% extends 'base.html' %}
            {% block meta %}
            <title>Login</title>
            {% endblock meta %}
            
            {% block content %}
            {% load static %}
            <link rel="stylesheet" href="{% static 'css/global.css' %}">
            
            <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
              <div class="max-w-md w-full space-y-8">
                <div>
                  <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
                    Login to your account
                  </h2>
                </div>
                <form class="mt-8 space-y-6" method="POST" action="">
                  {% csrf_token %}
                  <input type="hidden" name="remember" value="true">
                  <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                      <label for="username" class="sr-only">Username</label>
                      <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
                    </div>
                    <div>
                      <label for="password" class="sr-only">Password</label>
                      <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
                    </div>
                  </div>
            
                  <div>
                    <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                      Sign in
                    </button>
                  </div>
                </form>
            
                {% if messages %}
                <div class="mt-4">
                  {% for message in messages %}
                  {% if message.tags == "success" %}
                    <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                    </div>
                  {% elif message.tags == "error" %}
                    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                    </div>
                  {% else %}
                    <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                      <span class="block sm:inline">{{ message }}</span>
                    </div>
                  {% endif %}
                  {% endfor %}
                </div>
                {% endif %}
            
                <div class="text-center mt-4">
                  <p class="text-sm text-black">
                    Don't have an account yet?
                    <a href="{% url 'main:register' %}" class="font-medium text-gray-600 hover:text-green-700">
                      Register Now
                    </a>
                  </p>
                </div>
              </div>
            </div>
            {% endblock content %}
           ```
         - `register.html`
           ```html
            {% extends 'base.html' %} 
            {% block meta %}
            <title>Register</title>
            {% endblock meta %}
            
            {% block content %}
            {% load static %}
            <link rel="stylesheet" href="{% static 'css/global.css' %}">
            <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
              <div class="max-w-md w-full space-y-8 form-style">
                <div>
                  <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
                    Create your account
                  </h2>
                </div>
                <form class="mt-8 space-y-6" method="POST">
                  {% csrf_token %}
                  <input type="hidden" name="remember" value="true">
                  <div class="rounded-md shadow-sm -space-y-px">
                    {% for field in form %}
                      <div class="{% if not forloop.first %}mt-4{% endif %}">
                        <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                          {{ field.label }}
                        </label>
                        <div class="relative">
                          {{ field }}
                          <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                            {% if field.errors %}
                              <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                              </svg>
                            {% endif %}
                          </div>
                        </div>
                        {% if field.errors %}
                          {% for error in field.errors %}
                            <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                          {% endfor %}
                        {% endif %}
                      </div>
                    {% endfor %}
                  </div>
            
                  <div>
                    <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                      Register
                    </button>
                  </div>
                </form>
            
                {% if messages %}
                <div class="mt-4">
                  {% for message in messages %}
                  <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                  </div>
                  {% endfor %}
                </div>
                {% endif %}
            
                <div class="text-center mt-4">
                  <p class="text-sm text-black">
                    Already have an account?
                    <a href="{% url 'main:login' %}"  class="font-medium text-gray-600 hover:text-green-700">
                      Login here
                    </a>
                  </p>
                </div>
              </div>
            </div>
            {% endblock content %}
           ```
         - `item_card.html`
           ```html
               <div class="card border rounded-lg shadow-lg bg-white p-4">
                <div class="card-body">
                    <h2 class="card-title text-xl font-bold mb-2">{{ item_entry.name }}</h2>
                    <p class="mb-2"><strong>Description:</strong> {{ item_entry.description }}</p>
                    <p class="mb-2"><strong>Price:</strong> {{ item_entry.price }}</p>
                    <p class="mb-2"><strong>Stock:</strong> {{ item_entry.stock }}</p>
                    <div class="card-actions flex space-x-2 mt-4">
                        <a href="{% url 'main:edit_item' item_entry.pk %}">
                            <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-1 px-3 rounded">Edit</button>
                        </a>
                        <a href="{% url 'main:delete_item' item_entry.pk %}">
                            <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-3 rounded">Delete</button>
                        </a>
                    </div>
                </div>
            </div>
           ```
         - `main.html`
           ```html
            {% extends 'base.html' %}
            {% block content %}
            {% include 'navbar.html' %}
            {% load static %}
            
            <div class="container mx-auto p-4 mt-16">    
                {% if not item_entries %}
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/sadge.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data item pada Toko-ya.</p>
                </div>
                {% else %}
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                        {% for item_entry in item_entries %}
                            {% include 'item_card.html' %}
                        {% endfor %}
                    </div>
                {% endif %}
            
                <!-- Buttons for Add and Logout -->
                <div class="mt-4">
                    <a href="{% url 'main:create_item_entry' %}">
                        <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded">Add New Item Entry</button>
                    </a>
                    <a href="{% url 'main:logout' %}" class="ml-2">
                        <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">Logout</button>
                    </a>
                </div>
            
                <!-- User Information Section -->
                <div class="flex items-center mt-6">
                    <div class="mr-6">
                        <h5 class="text-sm text-gray-600 font-medium">Nama: {{ name }}</h5>
                    </div>
                    
                    <div class="mr-6">
                        <h5 class="text-sm text-gray-600 font-medium">Kelas: {{class}}</h5>
                    </div>
                    
                    <h5 class="text-sm text-gray-600 font-medium">Sesi terakhir login: {{ last_login }}</h5>
                </div>
            </div>
            {% endblock content %}
           ```
           - Masukkan `sadge.png` pada direktori `static/image/`
             ![image](https://github.com/user-attachments/assets/d10bf36b-19b4-4c74-9414-c84233f0af51)
         - create_item_entry
           ```html
            {% extends 'base.html' %} 
            {% load static %}  <!-- Load static files -->
            {% block content %}
            {% include 'navbar.html' %}
            
            <!-- Add top margin to avoid navbar overlay -->
            <div class="mt-20 max-w-xl mx-auto form-style">
              <h1 class="text-3xl font-bold text-center mb-6">Add New Item Entry</h1>
            
              <form method="POST" enctype="multipart/form-data" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                {% csrf_token %}
                
                <table class="w-full">
                  {{ form.as_p }}
                </table>
            
                <!-- Submit Button -->
                <div class="flex justify-center mt-6">
                  <input type="submit" value="Add Item Entry" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded cursor-pointer transition duration-300 animate-shine" />
                </div>
              </form>
            
            <!-- Link to the global.css file -->
            <link rel="stylesheet" href="{% static 'css/global.css' %}">
            
            {% endblock %}
           ```
       - buat `navbar.html` pada `root/templates/`
         ```html
          <!DOCTYPE html>
          <html lang="en">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <!-- Load static files -->
              {% load static %}
              <link rel="stylesheet" href="{% static 'css/styles.css' %}">
          </head>
          <body>
            <nav class="bg-green-800 shadow-lg fixed top-0 left-0 z-40 w-screen">
              <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-16">
                  
                  <!-- Logo section -->
                  <div class="flex-shrink-0">
                    <h1 class="text-2xl font-bold text-center text-white">Toko-ya</h1>
                  </div>
          
                  <!-- Menu section (Desktop) -->
                  <div class="hidden md:flex flex-grow justify-around">
                    <a href="{% url 'main:show_main' %}" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
                    <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
                    <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
                    <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
                  </div>
          
                  <!-- Mobile Menu Button -->
                  <div class="md:hidden flex items-center">
                    <button class="mobile-menu-button">
                      <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                      </svg>
                    </button>
                  </div>
          
                  <!-- Welcome message and logout/login -->
                  <div class="hidden md:flex items-center space-x-2">
                    {% if user.is_authenticated %}
                      <span class="text-gray-300">Welcome, {{ user.username }}</span>
                      <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                        Logout
                      </a>
                    {% else %}
                      <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                        Login
                      </a>
                      <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                        Register
                      </a>
                    {% endif %}
                  </div>
                </div>
              </div>
          
              <!-- Mobile Menu -->
              <div class="mobile-menu hidden md:hidden px-4 w-full">
                <div class="pt-2 pb-3 space-y-1 mx-auto">
                  <a href="{% url 'main:show_main' %}" class="block text-gray-300 px-3 py-2">Home</a>
                  <a href="#" class="block text-gray-300 px-3 py-2">Products</a>
                  <a href="#" class="block text-gray-300 px-3 py-2">Categories</a>
                  <a href="#" class="block text-gray-300 px-3 py-2">Cart</a>
          
                  {% if user.is_authenticated %}
                    <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                      Logout
                    </a>
                  {% else %}
                    <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                      Login
                    </a>
                    <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                      Register
                    </a>
                  {% endif %}
                </div>
              </div>
            </nav>
          
            <script>
              // Toggle mobile menu visibility
              const btn = document.querySelector("button.mobile-menu-button");
              const menu = document.querySelector(".mobile-menu");
          
              btn.addEventListener("click", () => {
                menu.classList.toggle("hidden");
              });
            </script>
          </body>
          </html>
         ```
