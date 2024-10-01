------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 2
------------------------------------------------------------------------------------------------------------------------------------------

1. Tautan menuju aplikasi PWS yang sudah di-deploy
    Link PWS: https://pbp.cs.ui.ac.id/web/project/raysha.reifika/tinychefmart

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah proyek Django baru.
        - Membuat folder baru bernama TinyChefMart yang merupakan nama project dan menghubungkannya dengan git.
        - Membuat akun pws dan project baru
        - Membuat dan mengaktifkan virtual environment  
        - Menyiapkan dependencies dengan nama requirements.txt yang nantinya akan di-install. 
        - Membuat sebuah proyek Django baru dengan nama tiny_chef_mart
        - Menambahkan allowed host didalam settings berupa local host, ip, dan url pws
        - Membuat file bernama .gitignore. .gitignore diperlukan untuk menentukan file dan direktori yang harus diabaikan oleh git
        - Melakukan add, commit, push setiap diperlukan perubahan ke git

    - Membuat aplikasi dengan nama main pada proyek tersebut.
        - Membuat aplikasi baru bernama main
        - Menambahkan main ke dalam installed_apps di settings.py
        - Membuat direktori baru bernama templates di dalam direktori main
        - Di dalam templates buat file main.html yang akan berfungsi sebagai templates langsung denagn struktur kode django yang sesuai untuk menampilkan data
    
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Buka urls.py pada tiny_chef_mart
        - Tambahkan rute path('', include('main.urls'))
        - '' akan mengarahkan ke file urls.py pada main

    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
        - Membuat class product sebagai model yang akan didefinisikan
        - Di dalam class product, ditambahkan atribut app_name, price, desc, dan quantity dengan tipe data yang sesuai.
        - Model nantinya akan berisi data-data
        - Melakukan migrasi setiap melakukan perubahan pada model agar perubahan model database dapat dilacak

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Mengubah dictionary context pada file views.py di main dengan data yang akan dirender ke html
        
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Membuat file urls.py di dalam folder main untuk mengatur rute url

    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - Melakukan add, commit, push setiap diperlukan perubahan ke git sebelum melakukan deployment
        - Melakukan perintah di project command untuk project baru
        - Melakukan push ke pws master setiap ada perubahan tanpa melakukan perintah di project command

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    [Client/Browser] 
        |
        | (Request: Mengirim/Mengetik URL)
        v
    [Internet] ------------------> [Web Server] ------------------------------------------> [urls.py]
                                                            (URL Routing)                       |
                                                                                                |
                                                                                                | (Melakukan request)
                                                                                                v
                                                    [Templates Folder]  <--------------------[views.py]
                                                            |                                    ^
                                                (Rendered)  |                                    | (Query Data)
                                                            v                                    v
                                                    [Client/Browser]                       [models.py] <----> [Database]
                                                                                                        
                            
                
    Client melalui browser mengetik sebuah url, dimana url akan mengirimkan request ke web server. Server akan memproses request dan melakukan url routing. dari url akan diekstrak argumen dari request tersebut. Dengan menggunakan database di models dan html template,  client akan menerima informasi kembali sebagai sebuah response

    urls.py:
    - Urls akan mengirim request ke views
    - Django memetakan argumen request atau url ke view
    - Url yang dikirim akan menentukan akan aplikasi yang dijalankan 

    views.py: 
    - Setelah urls dipetakan, views akan mengambil data  dari models dan mengolah data. Kemudian, data akan dikirimkan ke template html untuk dirender

    models.py:
    - Models akan mendefinisikan data dan mengelola interaksi dengan database.

    template html:
    - views akan merender template html dengan data dari models. Kemudian, akan mengirim response kepada client berupa web berdasarkan url yang diakses.

Referensi:
https://scele.cs.ui.ac.id/pluginfile.php/237029/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    Git adalah alat software development yang berfungsi sebagai sistem kontrol versi untuk menyimpan, mengatur, dan dokumentasi hasil kerja dalam hal ini adalah kode. Kemudian, git juga dapat men-track perubahan kode yang dilakukan sehingga jika terdapat kesalahan pada kode dapat dilihat dan dibandingkan dengan versi sebelumnya. Git juga dapat membantu dalam kerja tim dengan adanya branching dan merging. Meskipun bekerja sendiri, suatu tim dapat menggambungkan pekerjaannya (merging) dan memastikan setiap bagian tidak ada yang bentrok (branching).

Referensi:
https://dcloud.co.id/blog/apa-itu-git.html#:~:text=Git%20adalah%20alat%20software%20development,code)%20secara%20efisien%20dan%20kolaboratif.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Django terorganisir dengan baik dan mudah untuk  diinstal. Desainer Django membuat kerangka kerja untuk  menerapkan arsitektur web dalam kode.
    - Django bekerja dengan baik dengan data karena memiliki model ORM. 
    - Django memisahkan antar kode dengan konsep MVT atau  Model-View-Template.  Oleh karena konsep tersebut, dapat mempermudah pengelolaan dan pengembangan serta memisahkan logika aplikasi dari tampilan.
    - Hemat biaya karena django adalah proyek Python gratis, tetapi menyediakan banyak komponen bawaan, seperti autentikasi, admin panel, dan ORM. Dengan komponen bawaan ini, pemula dapat lebih mudah memahami.
    - Django merupakan platform yang populer sehingga memiliki banyak dokumentasi.

    Dengan beberapa poin diatas, alasan dari seringnya framework django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah django mudah dipelajari bagi pemula. 

Referensi:
https://aws.amazon.com/id/what-is/django/
https://cheesecakelabs.com/blog/django-framework-app-development/

6. Mengapa model pada Django disebut sebagai ORM?
    Model dalam konsep MVT django merupakan cara dari suatu data disimpan, diatur, dan dikelola. Model menghubungkan aplikasi dengan database dan membuat interaksi. ORM adalah Object Relational Mapping. Model pada django disebut sebagai ORM karena kerangka kerja django menggunakan lapisan pemetaan objek relasional yang dapat digunakan untuk berinteraksi dengan data. Oleh karena itu, dengan ORM pada django, developer dapat berinteraksi dengan database, seperti memodifikasi database,  menggunakan objek python tanpa menuliskan SQL nya secara manual.

Referensi:
https://www.scaler.com/topics/django/relationships-in-django-models/
https://pbp-fasilkom-ui.github.io/ganjil-2025/docs/tutorial-1


------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 3
------------------------------------------------------------------------------------------------------------------------------------------

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    - Dengan data delivery, memungkinkan komunikasi yang efisien dan efektif antara client dan server melalui request HTTP.
    - Data delivery memungkinkan client mendapatkan informasi secara real time.
    - Data delivery memastikan layanan yang saling berinteraksi dan berbagi data mendapatkan data yang diperlukan untuk berfungsi dengan baik.
    - Data delivery memastikan sinkronisassi data antar sistem
    - Data delivery mendukung penggunakan API yang memungkinkan integrasi antar sistem

    In conclusion, Data delivery sangat penting untuk pengimplementasian  sebuah platform karena data delivery memastikan platform dapat mengirmkan dan menerima data dengan baik, cepat, dan efisien sehingga memastikan pengalaman client yang optimal.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, JSON lebih baik daripada XML karena JSON memiliki sintaks yang identik dengan kode untuk membuat javascript objects 
    sehingga mudah untuk meng-convert JSON data kedalam native Javascript objects. Kemudian, kode untuk membaca dan menghasilkan JSON data dapat ditulis dalam bahasa pemograman apapun. Selain itu, untuk AJAX Applications, JSON lebih cepat dan lebih mudah dari pada XML. 

    Alasan JSON lebih populer:
    - Sintaksnya JSON yang sederhana dan memiliki struktur yang mirip dengan Javascript. Sedangkan XML menggunakan tag yang lebih kompleks. Oleh karena itu, sintaks JSON lebih efisien dalam penulisan dan pembacaan data serta memudahkan dalam parsing. 
    - Dalam AJAX Applications, pengiriman data lebih cepat saat menggunakan JSON karena tidak diperlukan tag penutup yang berlebihan sehingga ukuran data yang dikirimkan lebih kecil.
    - Struktur data JSON juga lebih sederhana daripada XML karena JSON menggunakan kurung kurawal untuk objek dan kurung siku untuk array 
    sehingga lebih mudah saat bekerja dengan struktur data yang kompleks. Sedangkan, XML menggunakan tag yang lebih rumit untuk dibaca dan diolah.

    In conclusion, JSON lebih populer daripada XML karena lebih sederhana, performanya lebih cepat, lebih mudah untuk digunakan dan diproses.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() memiliki fungsi untuk memeriksa apakah data yang diinput pengguna valid sesuai dengan aturan. Jika sudah valid, data akan disimpan ke dalam database. Namun, jika tidak valid, tidak akan disimpan dalam database dan akan terdapat pesan error.
    Method is_valid() juga dapat membersihkan data input dan menyimpannya ke dalam atribut cleaned_data dengan melakukan seperti ini 
    name = form.cleaned_data['name']

    Mengapa method is_valid() dibutuhkan:
    - Method is_valid() memastikan bahwa hanya data yang sesuai aturan (valid) saja yang diproses/disimpan. Dengan hal ini dapat mencegah data yang salah atau berbahaya masuk ke dalam sistem yang dapat menyebabkan data corrupt dan kesalahan fatal lainnya. Kemudian, method is_valid() dapat memberikan respon ketika terdapat pengguna yang memberikan input yang salah sehingga pengguna dapat mengetahui apa yang harus diperbaiki. 
    
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    CSRF (Cross-Site Request Forgery) adalah sistem keamanan yang melindungi aplikasi web dari serangan yang dinamakan Cross-Site Request Forgery (CSRF). Saat membuat form django, csrf_token dibutuhkan untuk memastikan setiap dilakukan POST yang dikirim ke server berasal dari sumber resmi. 

    Jika kita tidak menambahkan csrf_token, aplikasi akan sangat rentan terhadap serangan CSRF karena aplikasi tidak dapat membedakan antara permintaan resmi dan permintaan yang dimanipulasi sehingga hacker dapat memanipulasi pengguna untuk melakukan tindakan tidak sah di aplikasi web tanpa sepengetahuan pengguna. Jika serangan tersebut berhasil, hacker dapat mengakses data sensitif, seperti akun bank, dan melakukan tindakan berbahaya lainnya.

    Hacker dapat memanfaatkan hal tersebut dengan membuat web berbahaya yang dapat memberikan request ke aplikasi django yang rentan. Kemudian, ketika pengguna sudah login ke web tersebut, akan terdapat request berbahaya yang dikirimkan ke server tanpa csrf_token. Tanpa csrf_token, server tidak bisa mendeteksi request tersebut resmi atau tidak sehingga server memproses request tersebut.
    
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat input form untuk menambahkan objek model pada app sebelumnya
        - Di dalam main membuat file forms.py untuk menerima input data
        - Membuat base.html didalam folder templates di direktori utama sebagai kerangka umum, lalu ubah settings pada bagian templates dengan menambahkan 'DIRS': [BASE_DIR / 'templates'],
        - Pada folder templates di direktori main, tambahkan block content
        - Pada views.py di main, tambahkan import redirect. Lalu, buat fungsi create_product_entry dengan parameter request untuk dilakukan method is_valid. Kemudian, tambahkan product_entries didalam show_main.
        - Tambahkan path url di urls.py
        - Buat file bernama create_product_entry.html pada direktori main/templates.
        - Didalam main.html, tambahkan kode untuk menampilkan product dan tombol add product entry untuk menerima input data.

    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        - Menambahkan id dan primary key didalam file models.py, lalu lakukan migrasi melalui cmd.
        - Pada views.py, tambahkan import HttpResponse dan serializers
        - Membuat fungsi dengan nama show_xml, show_json dengan parameter request.
        - Membuat fungsi dengan nama show_xml_by_id, show_json_by_id dengan parameter request dan id

    - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - Pada urls.py, tambahkan import show_xml, show_json dan tambahkan path urlnya sehingga linknya dapat dibuka dengan format xml atau json.
        - Pada urls.py, tambahkan import show_xml_by_id, show_json_by_id dan tambahkan path urlnya sehingga linknya dapat dibuka dengan format xml atau json berdasarkan idnya.

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![Screenshot 2024-09-16 191618](https://github.com/user-attachments/assets/0eb78173-1c67-4320-9ecd-d16651b071bf)
![Screenshot 2024-09-16 191640](https://github.com/user-attachments/assets/2a5af1f7-c395-48a4-8159-83528be39d82)
![Screenshot 2024-09-16 191655](https://github.com/user-attachments/assets/754cb741-b318-47aa-a446-a990c61f69ec)
![Screenshot 2024-09-16 191559](https://github.com/user-attachments/assets/b2dae56b-22b4-45d1-9f07-951efd1c566a)



Referensi:
https://scele.cs.ui.ac.id/pluginfile.php/238122/mod_resource/content/1/04%20-%20Data%20Delivery.pdf
https://www.thedevspace.io/community/django-forms


------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 4
------------------------------------------------------------------------------------------------------------------------------------------

1. Apa perbedaan antara HttpResponseRedirect() dan redirect():
    - Pengertian:
        - HttpResponseRedirect(): Kelas bawaan dari Django untuk membuat respon HTTP. Terdapat berbagai status kode, seperti 302 yang menandakan redirect.
        - redirect(): Fungsi dari Django yang lebih sederhana dan fleksibel.
    - Argumen:
        - HttpResponseRedirect(): Menerima url sebagai argumen. 
        - redirect(): Menerima url, nama url, atau objek sebagai argumen.
    - Pengubahan ke url:
        - HttpResponseRedirect(): Tidak secara langsung sehingga dibutuhkan fungsi reverse(). 
        - redirect(): Secara langsung mengarahkan ke url.
    - Contoh: 
        - HttpResponseRedirect():
            response = HttpResponseRedirect(reverse('main:login'))
        - redirect():
            return redirect('main:login')

2. Jelaskan cara kerja penghubungan model MoodEntry dengan User!
    Untuk menghubungkan model dengan user, pada model ditambahkan foreignKey. Dengan foreignKey, satu pengguna akan memiliki banyak entry mood (Relasi one to many). ForeignKey dilakukan dengan kode seperti ini:
    user = models.ForeignKey(User, on_delete=models.CASCADE). Namun, sebleumnya perlu dilakuakn import 
    from django.contrib.auth.models import User

    Kemudian, user yang diidentifikasi hanya user yang sedang login dengan menggunakan request.user. Dengan cara ini, entry mood pada saat itu hanya berlaku untuk user yang sedang login. Jika kita logout, dan login dengan user berbeda, data sebelumnya tidak akan ada, tetapi, jika logout dan login dengan user yang sama, data akan tetap ada.
    product_entries = ProductTinyChef.objects.filter(user=request.user)
 
3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    - Perbedaan:
        - Definisi:
            - Authentication: Proses untuk memverifikasi identitas pengguna yang login.
            - Authorization: Proses untuk memverifikasi seorang pengguna dapat mengakses sesuatu.
        - Proses saat login:
            - Authentication: 
                - Pengguna menginput nama dan password
                - Django mengecek apakah sesuai dengan data di database
                - Jika sesuai, akan dibuat sebuah session agar pengguna yang sudah login sehingga tidak perlu login berulang kali
            - Authorization: 
                - Setelah login dan diotentikasi, sistem memeriksa hak akses. 
                - Lalu, authorization menentukan halaman tertentu saja yang dapat diakses pengguna tersebut berdasarkan peran hak aksesnya.
        - Cara django mengimplementasikan:
            - Authentication: 
                - Terdapat fungsi authenticate() untuk memverifikasi identitas pengguna
                - Terdapat fungsi login() untuk menyimpan pengguna di session tersebut. Dengan session, django dapat melacak status login server.
            - Authorization:
                - Dengan decorator @login_required, django memastikan bahwa pengguna harus login sebelum mengakses halaman tertentu
    
4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
    Django mengingat pengguna yang telah login dengan session dan cookies. Session adalah cara Django untuk menyimpan data pengguna. Session disimpan didalam server bukan browser. Namun, selain session terdapat cookies yang menyimpan session di browser, kemudian dikirim ke server. Session ID akan disimpan didalam cookies. Django menggabungkan session dan cookie untuk melacak status login pengguna saat menggunakan web tersebut. 

    Kegunaan cookies:
    - Melakukan pelacakan aktivitas pengguna
    - Jika sudah login, lalu pengguna menutup browser, cookies dapat mengingat pengguna
    - Menyimpan preferensi pengguna, seperti tema dan bahasa browser

    Apakah semua cookies aman?
    - Tidak semua cookies aman. Cookies harus terdapat "Secure" atau "HttpOnly" untuk menghindari ancaman keamanan. Selain itu, dapat juga digunakan CSRF token dan dikirimkan melalui HTTPS untuk memastikan kemanan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
        - Mengaktifkan env
        - Pada views, tambahkan import untuk membuat form, authenticate, login, dan logout. Lalu, menambahkan fungsi register, login, dan logout dan membuat file HTML baru dengan nama register.html dan login.html pada main/templates. 
        - Pada urls.py, menambahkan import dan path url register, login, dan logout.
        - Lalu, menambahkan decorator login_required agar sebelum mengakses halaman belanja harus login terlebih dahulu

    - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
        - Mengaktifkan env
        - Menjalankan python manage.py runserver
        - Membuka http://localhost:8000/ 
        - Registrasi dan login dengan 2 akun berbeda
        - Untuk masing-masing akun, buat 3 data

    - Menghubungkan model Product dengan User.
        - Pada models.py, menambahkan import user
        - Lalu, tambahkan foreignkey pada ProductEntry
            user = models.ForeignKey(User, on_delete=models.CASCADE)
        - Lalu, input namanya diubah menjadi request.user
        - Lalu, untuk menyaring product berdasarkan user dilakukan 
        product_entries = ProductTinyChef.objects.filter(user=request.user)
        - Lalu, lakukan migrate

    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
        - Tambahkan cookie berupa last_login pada views.py
        - Pada fungsi login, tambahkan sebagai berikut
            response.set_cookie('last_login', str(datetime.datetime.now()))
        - Pada show_main, dimasukkan context last_login
        - Pada logout(), juga tambahkan response.delete_cookie('last_login') agar ketika logout, data loginnya dihapus
        - Menambahkan last_login pada main.html


------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 5
------------------------------------------------------------------------------------------------------------------------------------------

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    - Inline styles : Selector yang diterapkan langsung pada elemen HTML
    contoh:
    <p style="color: red;">Teks ini merah</p>

    - ID selectors : Selector yang menggunakan ID elemen dan memiliki # didepannya
    contoh:
    <p id="intro">Teks ini menggunakan ID</p>

    #intro {
    color: blue;
    }   

    - Classes selector : Selektor ini digunakan ketika ingin mengatur gaya berdasarkan kelas elemen, yang dapat diterapkan pada beberapa elemen HTML. Ditandai dengan . diawal
    contoh:
    <p class="highlight">Teks ini menggunakan kelas</p>

    .highlight {
    color: green;
    }

    - Element selector : Elemen dipilih berdasarkan tag HTMLnya
    contoh:
    <p>Teks ini menggunakan selektor elemen</p>

    p {
    color: black;
    }

    CSS Selector memiliki prioritas, yaitu yang pertama inline styles, lalu id selector, lalu class selector,dan yang terakhir element selectors. Jika ada lebih dari satu gaya yang diterapkan ke elemen yang sama, aturan dengan prioritas lebih tinggi akan digunakan. Namun, jika terdapat gaya dengan prioritas yang sama, akan digunakan yang ditulis terakhir,

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
    Responsive design adalah cara menyusun web agar secara otomatis dapat menyesuaikan skala dan elemen sesuai dengan ukuran layar.

    - Bagi developer, responsive design dapat menghemat biaya dan lebih efisien untuk pengelolaan karena developer hanya perlu membuat 1 situs web yang dapat menyesuaikan dengan berbagai versi dengan berbagai skala untuk mobile ataupun desktop.
    - Dengan responsive design, Google melalui Search Engine Optimization (SEO) memberikan website tersebut boost yang lebih banyak sehingga lebih sering ditampilkan sebagai hasil pencarian.
    -  Sebagai pengguna, dengan responsive design, dapat membantu meningkatkan user experience karena dapat dipastikan konten dapat dilihat lebih cepat dan pandangan pengguna akan lebih positif.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    - Margin: 
        - Area di luar border yang memberi jarak antar elemen. 
        - Dibagian paling luar elemen 
        - Tidak mempengaruhi ukuran elemen.
        - Cara: margin: 20px;
    - Border: 
        - Garis yang mengelilingi elemen. 
        - Terletak diantara margin dan padding. 
        - Mempengaruhi ukuran elemen.
        - Cara: border: 3px solid blue;
    - Padding:
        - Area didalam border yang memberi jarak antara elemen dan border
        - Terletak diantara elemen dan border
        - Mempengaruhi ukuran elemen
        - Cara: padding: 30px;

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   - Flexbox:
     - Flexbox adalah sistem layout di css yang digunakan untuk mengatur elemen dalam satu dimensi.
     - Elemen diatur berdasarkan container sehingga dapat mengatur posisi, ukuran, dan jarak antar elemen dengan mudah.
     - Cocok untuk design yang simple, seperti navigasi, form, dan daftar, yang elemennya disusun dalam 1 baris atau 1 kolom.
   - Grid:
     - Grid adalah sistem layout di css yang digunakan untuk mengatur elemen dalam dua dimensi.
     - Elemen diatur berdasarkan grid sehingga memungkinan untuk menentukan posisi tepat elemen yang diinginkan
     -  Cocok untuk design yang kompleks, seperti layout halaman, yang elemennya disusun dalam struktur yang lebih terkoordinasi.
       
6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  - Menambahkan script tailwind ke dalam base.html
    <script src="https://cdn.tailwindcss.com">
  - Di dalam views.py, tambahkan fungsi edit dan delete
  - Buat file html baru untuk fungsi edit
  - Tambahkan path url untuk edit dan delete
  - Di dalam main.html tambahkan tombol edit dan delete
  - Membuat navbar.html untuk memiliki navbar
  - Menambahkan navbar ke dalam main.html, create product, dan edit.
  - Menambahkan konfigurasi static di settings agar dapat menambahkan gambar dan styling pada page
  - Buat folder dengan root static/css, lalu didalamnya tambahkan folder global.css untuk styling semua halaman dan image untuk kumplan gambar yang nantinya akan ditampilkan di page
  - Melakukan styling untuk login, register, main, edit, dan product page. Kemudian, pada card productnya juga

  
Referensi:
https://scele.cs.ui.ac.id/pluginfile.php/239159/mod_resource/content/1/06%20-%20Web%20Design%20Using%20HTML5%20and%20CSS3.pdf
https://www.webfx.com/web-design/learn/why-responsive-design-important/
https://www.exabytes.co.id/blog/perbedaan-margin-dan-padding/
