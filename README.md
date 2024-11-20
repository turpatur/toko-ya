# PBP 
## [http://fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id](http://fathurrahman-kesuma-tokoya2.pbp.cs.ui.ac.id)

### Past Works:
1. [Tugas 2](https://github.com/turpatur/toko-ya/wiki/Tugas-2)
2. [Tugas 3](https://github.com/turpatur/toko-ya/wiki/Tugas-3)
3. [Tugas 4](https://github.com/turpatur/toko-ya/wiki/Tugas-4)
4. [Tugas 5](https://github.com/turpatur/toko-ya/wiki/Tugas-5)

### Tugas 6
1. **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**  
   - JavaScript dapat membuat konten web menjadi lebih interaktif.
   - JavaScript juga merespons lebih cepat karena eksekusinya melalui browser pengguna.
   - Pengalaman pengguna menjadi lebih baik karena dapat digunakan untuk berbagai fitur, seperti validasi form, drag and drop, dan dynamic content loading.

2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**  
   `await` digunakan untuk menunggu hasil `Promise` yang dikembalikan oleh `fetch()` sebelum melanjutkan ke kode berikutnya. Jika tidak menggunakan `await`, kode akan berjalan langsung tanpa menunggu hasil dari `fetch()`, yang bisa menyebabkan aplikasi menggunakan data yang belum selesai diambil oleh `fetch()`.

3. **Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?**  
   `csrf_exempt` membuat Django tidak melakukan pemeriksaan CSRF pada suatu fungsi view. Ini diperlukan dalam AJAX `POST` karena AJAX sering kali tidak membawa token CSRF, yang dapat menyebabkan kegagalan validasi CSRF. Namun, penggunaannya harus berhati-hati karena bisa menonaktifkan mekanisme keamanan Django.

4. **Mengapa pembersihan data input pengguna dilakukan di backend juga, bukan hanya di frontend?**  
   Pembersihan data di backend penting untuk alasan keamanan, misalnya mencegah data yang tidak aman dari pengiriman request secara langsung atau manipulasi form. Pembersihan di backend memastikan data yang diterima selalu sesuai format yang benar.

5. **Bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?**  
   - **Mengubah tugas 5 menjadi menggunakan AJAX.**
     - **AJAX `GET`**
       - Modifikasi kode untuk mendukung AJAX `GET`:
         - Buat fungsi `add_item_entry_ajax` pada `views.py`:
           ```python
           @csrf_exempt
           @require_POST
           def add_item_entry_ajax(request):
               name = strip_tags(request.POST.get("name"))
               description = strip_tags(request.POST.get("description"))
               price = request.POST.get("price")
               stock = request.POST.get("stock")
               user = request.user

               new_item = ItemEntry(
                   name=name, description=description,
                   price=price, stock=stock, 
                   user=user
               )
               new_item.save()

               return HttpResponse(b"CREATED", status=201)
           ```
         - Import fungsi di `urls.py`:
           ```python
           ...
           from main.views import add_item_entry_ajax
           ...
           ```
         - Routing URL:
           ```python
           ...
           path('create-item-entry-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
           ...
           ```
         - Tampilkan card dengan div ber-ID `"item_card"`:
           ```html
           <div id="item_card"></div>
           ```
         - Ambil data dengan AJAX `GET` hanya untuk pengguna yang sedang login:
           ```python
           user = request.user
           new_item = ItemEntry(
               name=name, description=description,
               price=price, stock=stock, 
               user=user
           )
           ```

     - **AJAX `POST`**
       - Buat tombol untuk membuka modal form untuk menambahkan item.
          - Tomol untuk membuka modal 
            ```html
               <button data-modal-target="crudModal" data-modal-toggle="crudModal" 
                  class="btn bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4" 
                  onclick="showModal();">
                  Add New Item Entry by AJAX
              </button>
            ```
          - Mmebuat function untuk menampilkan modal
            ```javascript
              const modal = document.getElementById('crudModal');
              const modalContent = document.getElementById('crudModalContent');
              function showModal() {
                  const modal = document.getElementById('crudModal');
                  const modalContent = document.getElementById('crudModalContent');
            
                  modal.classList.remove('hidden'); 
                  setTimeout(() => {
                    modalContent.classList.remove('opacity-0', 'scale-95');
                    modalContent.classList.add('opacity-100', 'scale-100');
                  }, 50); 
              }
            ```
       - Implementasikan view untuk menambahkan item baru ke basis data.
          -  Buat fungsi `add_item_entry_ajax` pada `views.py` yang sudah dijelaskan sebelumnya
          -  Membuat script js untuk add item entry 
          -  ```javascript
               function addItemEntry() {
                   fetch("{% url 'main:add_item_entry_ajax' %}", {
                     method: "POST",
                     body: new FormData(document.querySelector('#ItemEntryForm')),
                   })
                   .then(response => hideModal())
                   refreshItemEntries()
                   document.getElementById("ItemEntryForm").reset(); 
                   document.querySelector("[data-modal-toggle='crudModal']").click();
               
                   return false;
                 }
             ```
       - Buat path `/create-ajax/` yang mengarah ke view tersebut.
          - routing url `'create-item-entry-ajax'` seperti yangsudah dijelaskan sebelumnya 
       - Hubungkan form pada modal ke path `/create-ajax/`.
          - Form pada modal dihubungkan pada path melalui fetch() pada `addItemEntry()`
            ```javascript
            ...
                fetch("{% url 'main:add_item_entry_ajax' %}", {
               method: "POST",
               body: new FormData(document.querySelector('#ItemEntryForm')),
             })
            ...
            ``` 
       - Refresh halaman secara asinkron untuk menampilkan data terbaru tanpa reload seluruh halaman.
          - Refresh entry setiap kali menambahkan item:
           ```javascript
           async function refreshItemEntries() {
               document.getElementById("item_card").innerHTML = "";
               document.getElementById("item_card").className = "";
               const itemEntries = await getItemEntries();
               let htmlString = "";
               let classNameString = "";

               if (itemEntries.length === 0) {
                   classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                   htmlString = `
                       <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                           <img src="{% static 'image/sadge.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                           <p class="text-center text-gray-600 mt-4">Belum ada data item pada Toko-ya.</p>
                       </div>
                   `;
               } else {
                   classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6";
                   itemEntries.forEach((item) => {
                       const name = DOMPurify.sanitize(item.fields.name);
                       const description = DOMPurify.sanitize(item.fields.description);
                       htmlString += `
                           <div class="card border rounded-lg shadow-lg bg-white p-4">
                               <div class="card-body">
                                   <h2 class="card-title text-xl font-bold mb-2">${name}</h2>
                                   <p class="mb-2"><strong>Description:</strong> ${description}</p>
                                   <p class="mb-2"><strong>Price:</strong> Rp${item.fields.price}</p>
                                   <p class="mb-2"><strong>Stock:</strong> ${item.fields.stock}</p>
                                   <div class="card-actions flex space-x-2 mt-4">
                                       <a href="/edit-item/${item.pk}">
                                           <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-1 px-3 rounded">Edit</button>
                                       </a>
                                       <a href="/delete/${item.pk}">
                                           <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-3 rounded">Delete</button>
                                       </a>
                                   </div>
                               </div>
                           </div>
                       `;
                   });
               }
               document.getElementById("item_card").className = classNameString;
               document.getElementById("item_card").innerHTML = htmlString;
           }
           ```
